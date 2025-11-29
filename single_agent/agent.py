# Example prompt: What is AI and how can it benefit me?

from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

retry_config=types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1, # Initial delay before first retry (in seconds)
    http_status_codes=[429, 500, 503, 504] # Retry on these HTTP errors
)

root_agent = Agent(
    name='root_agent',
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),  
    description='A helpful assistant that can answer user questions using Google Search',
    instruction='Use Google Search to answer the user\'s questions accurately and concisely.',
    tools=[google_search]
)