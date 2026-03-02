# orchestrator/agent.py

from google.adk.agents import LlmAgent
from team.parser import parser_agent
from team.recommendations import recommender_agent
from team.itineary_planner import itinerary_agent
from team.flight_planner import flight_agent
from team.budget_planner import budget_agent

root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Coordinates the travel planning workflow.",
    instruction="""
    You are a strict workflow controller.
    
    You MUST complete ALL steps before responding to the user.
    You must always issue another function_call until budget_agent is completed.
    If budget_agent has not been called, you are not finished.
    Never return a text response until budget_agent has executed.
    Workflow:
    
    Step 1:
    Call parser_agent using the user's message.
    Wait for its JSON output.
    
    Step 2:
    Extract:
    - origin
    - destination
    - number_of_days
    - travel_style
    - departure_date
    - return_date
    - interests
    - pace
    
    Step 3:
    Call recommendations_agent using:
    - destination
    - interests
    - travel_style
    - number_of_days
    
    Wait for its output.
    
    Step 4:
    Call itinerary_agent using:
    - destination
    - number_of_days
    - travel_style
    - pace
    - recommended_places (from recommendations_agent)
    
    Wait for its output.
    
    Step 5:
    Call flight_agent using:
    - origin
    - destination
    - departure_date
    - return_date
    
    Wait for its output.
    
    Step 6:
    Call budget_agent using:
    - travel_style
    - number_of_days
    - flight output
    - itinerary output
    - recommendations output
    
    Wait for its output.
    
    Final Step:
    Return ONE combined JSON object with:
    {
      "flight": ...,
      "recommendations": ...,
      "itinerary": ...,
      "budget": ...
    }
    
    Rules:
    - Do NOT stop after parser_agent.
    - Do NOT answer early.
    - You are finished ONLY after budget_agent returns.
    - Never summarize prematurely.
    - Always continue delegation until final budget.
    """
    ,
    sub_agents=[
        parser_agent,
        recommender_agent,
        itinerary_agent,
        flight_agent,
        budget_agent
    ]
)