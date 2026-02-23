from livekit import api
import jwt

# 🔐 Replace with your LiveKit Cloud credentials
api_key = "APIM3u3ABkCYfNk"
api_secret = "ROk68aI3vSp5EZZLd9ZvjrLWi40IUbghRcvLItrxhbE"

room_name = "99900yyanannahdiijjinhking"  # Must match the room name used in AgentSession

# Build token
token = (
    api.AccessToken(api_key, api_secret)
    .with_identity("user1")
    .with_name("User One")
    .with_grants(
        api.VideoGrants(
            room_join=True,
            room=room_name,
        )
    )
    .with_room_config(
        api.RoomConfiguration(
            agents=[
                api.RoomAgentDispatch(
                    agent_name="pitchsense-agent"
                )
            ]
        )
    )
)

jwt_token = token.to_jwt()

print("\n========== LIVEKIT TOKEN ==========\n")
print(jwt_token)
print("\n===================================\n")

decoded = jwt.decode(jwt_token, options={"verify_signature": False})
print("Decoded payload:\n")
print(decoded)