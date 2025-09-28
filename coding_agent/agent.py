from google.adk.agents import Agent
#agent development kit, API keys gonna be all ove the place lol 
# this is where the schematics for agent is
root_agent = Agent(
 name = "coding_assistant", 
 model= "gemini-2.0-flash",
 instruction="""you are a coding agent that helps the user achieve their coding goals, keep all responses as simple as possible. ensure security protocols and proper data structure organization""",
)
