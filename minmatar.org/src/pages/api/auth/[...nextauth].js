import NextAuth from "next-auth"
import EVEOnlineProvider from "next-auth/providers/eveonline";

export const authOptions = {
  // Configure one or more authentication providers
  providers: [
    {
        id: "eveonline",
        name: "EVE Online",
        clientId: process.env.EVE_CLIENT_ID,
        clientSecret: process.env.EVE_CLIENT_SECRET,
        type: "oauth",
        authorization: "https://login.eveonline.com/v2/oauth/authorize?scope=",
        token: "https://login.eveonline.com/v2/oauth/token",
        userinfo: "https://login.eveonline.com/oauth/verify",
        profile(profile) {
            return {
            id: String(profile.CharacterID),
            name: profile.CharacterName,
            email: null,
            image: `https://image.eveonline.com/Character/${profile.CharacterID}_128.jpg`,
            }
        },
        callbacks: {
            session: async ({ session, token }) => {
            session.user.id = token.id;
            return session;
            }
        }
    }
  ],
}

export default NextAuth(authOptions)