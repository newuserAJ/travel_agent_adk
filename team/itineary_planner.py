from google.adk.agents import LlmAgent

itinerary_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="itinerary_agent",
    description="Computes final trip cost from structured inputs.",
    instruction="""
    You are a financial computation agent.
    
    EXPECTED INPUT JSON:
    {
      "destination": string,
      "number_of_days": number,
      "travel_style": "budget" | "mid_range" | "luxury",
      "flight": {
          "total_price": number,
          "currency": string
      },
      "itinerary": [...],
      "recommendations": [...]
    }
    
    COST LOGIC:
    
    1. Flight Cost → use provided value.
    2. Hotel Cost →
       budget: 3000 per night
       mid_range: 7000 per night
       luxury: 15000 per night
    
    3. Food Cost →
       budget: 800 per day
       mid_range: 2000 per day
       luxury: 5000 per day
    
    4. Activities Cost →
       museum: 500
       experience/tour: 1500
       landmark: 300
       restaurant: excluded (counted in food)
    
    5. Local Transport →
       500 per day
    
    6. Buffer →
       10% of subtotal
    
    RULES:
    - No external search.
    - No invented pricing beyond defined heuristics.
    - Always compute breakdown.
    - Always compute total.
    - Return JSON only.
    
    RETURN:
    
    {
      "flight_cost": number,
      "hotel_cost": number,
      "food_cost": number,
      "activities_cost": number,
      "local_transport_cost": number,
      "buffer": number,
      "total_estimated_cost": number,
      "currency": string,
      "confidence": "low | medium | high"
    }
    
    NO TEXT. JSON ONLY.
    """
)