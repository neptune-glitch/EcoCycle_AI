from google.adk.agents import Agent
from skills.identify import identify
from skills.retrieve import retrieve
from skills.security import security_check

root_agent = Agent(
    name="ecocycle_agent",
    model="gemini-2.5-flash",
    description="EcoCycle AI Recycling Assistant",
    instruction="""
You are EcoCycle AI.

Workflow:

1. If the user uploads an image,
   call identify().

2. Call retrieve().

3. Reply with:

Material
Recyclable
Reuse Ideas
Compostable
Eco Tip

Always use the tools.
""",
    tools=[
        security_check,
        identify,
        retrieve,
    ],
)