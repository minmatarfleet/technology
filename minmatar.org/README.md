This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

- [Next.js Page Router](https://nextjs.org/docs/pages/building-your-application/routing)
- [NextAuth.js with EVE Online Provider](https://next-auth.js.org/providers/eveonline#options)
- [Tailwind CSS](https://tailwindcss.com/docs/guides/nextjs) with [Stacked Layout](https://tailwindui.com/components/application-ui/application-shells/stacked)

# Getting Started
- `cp .env.example .env`
- Fill out with information from https://developers.eveonline.com (set callback URL to `http://localhost:3000/api/auth/callback/eveonline`)
- `npm i`
- `npm run dev`


You should be able to navigate and log in.