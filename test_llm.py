from llm_parser import extract_preferences


query = """
I need a hotel room for one night.
My budget is 5000 rupees.
I want a quiet room with a good view
and a large room.
"""


preferences = extract_preferences(query)


print("Extracted Hotel Preferences")
print("---------------------------")

for key, value in preferences.items():
    print(f"{key}: {value}")