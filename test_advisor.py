from llm_parser import extract_preferences
from hotel_advisor import recommend_rooms


query = """
I need a hotel room for one night.
My budget is 5000 rupees.
I want a quiet room with a good view
and a large room.
"""


# -----------------------------
# AI COMPONENT
# -----------------------------

preferences = extract_preferences(query)

print("AI EXTRACTED PREFERENCES")
print("-------------------------")

for key, value in preferences.items():
    print(f"{key}: {value}")


# -----------------------------
# FUZZY LOGIC + ROOM SELECTION
# -----------------------------

results = recommend_rooms(preferences)


print("\nROOM RECOMMENDATIONS")
print("--------------------")

for room in results:

    print(
        f"{room['name']} | "
        f"₹{room['price']} | "
        f"Rating: {room['rating']} | "
        f"Score: {room['score']:.2f}"
    )


# -----------------------------
# BEST ROOM
# -----------------------------

best_room = results[0]

print("\nRECOMMENDED ROOM")
print("----------------")

print(f"Room: {best_room['name']}")
print(f"Price: ₹{best_room['price']} per night")
print(f"Rating: {best_room['rating']}")
print(f"Suitability Score: {best_room['score']:.2f}/100")