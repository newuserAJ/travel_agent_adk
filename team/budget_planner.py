from google.adk.agents import LlmAgent

budget_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="budget_agent",
    description="""
    You are a financial computation agent.
    You calculate total estimated trip cost from structured inputs.
    """,
    instruction="""
    Expected Input JSON:
    {
      "destination": string,
      "number_of_days": number,
      "travel_style": string,
      "flight": object,
      "itinerary": array,
      "recommendations": array
    }

    Calculate:
    - Flight Cost
    - Accommodation Cost
    - Food Cost
    - Activities Cost
    - Local Transport
    - Buffer (5–10%)

    Return structured JSON only:
    {
      "flight_cost": number,
      "hotel_cost": number,
      "food_cost": number,
      "activities_cost": number,
      "local_transport_cost": number,
      "buffer": number,
      "total_estimated_cost": number,
      "confidence": "low|medium|high"
    }
    """
)