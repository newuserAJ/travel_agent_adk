from google.adk.agents import Agent

parser_agent=Agent(
    model="gemini-2.5-flash",
    name="parser_agent",
    description="""
    Extracts structured travel request from user message.
    """,
    instruction="""
    You receive a user's travel query in natural language.

    Extract structured JSON in this format:
    {
      "origin": string,
      "destination": string,
      "number_of_days": number,
      "travel_style": "budget" | "mid_range" | "luxury",
      "departure_date": string,
      "return_date": string | null,
      "interests": [string],
      "pace": "slow" | "moderate" | "fast"
    }
    
    If any field is missing, infer reasonably.
    Return JSON only.
    No explanations.
    """
)