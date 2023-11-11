
resource "aws_ecs_cluster" "ecs_cluster" {
  name = "minmatar-fleet-cluster"
}

resource "aws_ecs_capacity_provider" "ecs_capacity_provider" {
  name = "test1"
  auto_scaling_group_provider {
    auto_scaling_group_arn = aws_autoscaling_group.ecs_asg.arn
    managed_scaling {
      maximum_scaling_step_size = 1000
      minimum_scaling_step_size = 1
      status                    = "ENABLED"
      target_capacity           = 3
    }
  }
}



resource "aws_ecs_cluster_capacity_providers" "example" {
  cluster_name       = aws_ecs_cluster.ecs_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.ecs_capacity_provider.name]
  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = aws_ecs_capacity_provider.ecs_capacity_provider.name
  }
}

resource "aws_ecs_task_definition" "hermes_ecs_task_definition" {
  family       = "hermes-ecs-task"
  network_mode = "awsvpc"
  cpu          = 256
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }
  container_definitions = jsonencode([
    {
      name      = "hermes"
      image     = aws_ecr_repository.hermes.repository_url
      cpu       = 256
      memory    = 512
      essential = true
      portMappings = [
        {
          containerPort = 8000
          hostPort      = 8000
          protocol      = "tcp"
        }
      ]
    }
  ])
}

resource "aws_ecs_service" "hermes_ecs_service" {
  name            = "hermes-ecs-service"
  cluster         = aws_ecs_cluster.ecs_cluster.id
  task_definition = aws_ecs_task_definition.hermes_ecs_task_definition.arn
  desired_count   = 2

  network_configuration {
    subnets         = [aws_subnet.subnet.id, aws_subnet.subnet2.id]
    security_groups = [aws_security_group.security_group.id]
  }

  force_new_deployment = true
  placement_constraints {
    type = "distinctInstance"
  }

  triggers = {
    redeployment = timestamp()
  }

  capacity_provider_strategy {
    capacity_provider = aws_ecs_capacity_provider.ecs_capacity_provider.name
    weight            = 100
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.ecs_tg.arn
    container_name   = "hermes"
    container_port   = 8000
  }
  depends_on = [aws_autoscaling_group.ecs_asg]
}
