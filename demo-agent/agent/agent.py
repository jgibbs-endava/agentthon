from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from .tools import calculator, get_weather
from .sub_agent import researcher_agent

root_agent = Agent(
    name="root_agent",
    model=Gemini(model="gemini-2.5-flash"),
    instruction="""You are the Root Agent of the ADK Hackathon Demo.
You have a researcher sub-agent that you can use for finding random facts
You also have direct access to a calculator, and get weather tools.

Delegate looking up interesting facts to the researcher_agent.
Use the calculator for any math.
Use the get weather tool for any weather queries.
""",
    sub_agents=[researcher_agent],
    tools=[get_weather,calculator],
)

app = App(
    root_agent=root_agent,
    name="agent",
)
