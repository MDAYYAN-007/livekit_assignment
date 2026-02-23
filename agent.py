from livekit.agents import (
    AgentSession,
    Agent,
    JobContext,
    WorkerOptions,
    cli,
    AutoSubscribe,
)

from core.engine import PitchEngine

engine = PitchEngine()

class PitchSenseAgent(Agent):
    def __init__(self):
        super().__init__(
            instructions="You are PitchSense, an AI startup pitch mentor."
        )

    async def on_message(self, message, context):
        result = engine.evaluate_pitch(message)
        return result["mentor_response"]


async def entrypoint(ctx: JobContext):

    await ctx.connect(auto_subscribe=AutoSubscribe.NONE)

    session = AgentSession()

    await session.start(
        agent=PitchSenseAgent(),
        room=ctx.room,
    )


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            agent_name="pitchsense-agent",
            num_idle_processes=1
        )
    )