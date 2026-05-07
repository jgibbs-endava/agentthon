from google.adk.agents import Agent
from google.adk.models import Gemini
from .tools import get_weather, get_random_fact

researcher_agent = Agent(
    name="researcher_agent",
    model=Gemini(model="gemini-2.5-flash"),
    instruction="""You are a Researcher Agent. 
Your job is to find interesting information and weather details.
Be thorough and present your findings clearly.""",
    tools=[get_weather, get_random_fact],
)
