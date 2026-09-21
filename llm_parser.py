from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()


class HotelPreferences(BaseModel):

    budget_per_night: int = Field(
        description="Maximum budget per night in Indian rupees"
    )

    room_noise_preference: str = Field(
        description="Preferred room noise level: quiet, medium, or noisy"
    )

    view_preference: str = Field(
        description="Preferred view: low, medium, or high"
    )

    room_size_preference: str = Field(
        description="Preferred room size: small, medium, or large"
    )


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


structured_llm = llm.with_structured_output(
    HotelPreferences
)


def extract_preferences(user_query):

    prompt = f"""
    You are a hotel room preference assistant.

    Read the user's natural-language request and extract the hotel
    room preferences.

    User request:
    {user_query}

    Rules:

    1. Extract the maximum budget per night as an integer.
    2. Convert the view preference:
       - poor/no view = low
       - normal/city view = medium
       - good/beautiful/sea view = high

    3. Convert the noise preference:
       - noisy/busy = noisy
       - normal = medium
       - quiet/peaceful/silent = quiet

    4. Convert room size:
       - small/compact = small
       - normal/standard = medium
       - large/spacious/big = large

    5. If a preference is not mentioned, use a reasonable medium value.

    Return the information in the required structured format.
    """

    result = structured_llm.invoke(prompt)

    return result.model_dump()