from fuzzy_logic import hotel_control_system
from skfuzzy import control as ctrl
from rooms import rooms


def convert_view(value):
    value = str(value).lower()

    if "low" in value:
        return 30
    elif "high" in value:
        return 90
    else:
        return 60


def convert_quietness(value):
    value = str(value).lower()

    if "quiet" in value:
        return 90
    elif "noisy" in value:
        return 30
    else:
        return 60


def convert_space(value):
    value = str(value).lower()

    if "small" in value:
        return 30
    elif "large" in value:
        return 90
    else:
        return 60


def calculate_room_score(room, preferences):

    budget = int(preferences["budget_per_night"])

    # If room is over the user's budget,
    # it should receive a lower suitability.
    if room["price"] <= budget:
        budget_value = budget
    else:
        budget_value = max(0, budget - (room["price"] - budget))

    view_value = room["view"]
    quietness_value = room["quietness"]
    space_value = room["space"]

    simulation = ctrl.ControlSystemSimulation(
        hotel_control_system
    )

    simulation.input["budget"] = budget_value
    simulation.input["view"] = view_value
    simulation.input["quietness"] = quietness_value
    simulation.input["space"] = space_value

    simulation.compute()

    return simulation.output["suitability"]


def recommend_rooms(preferences):

    results = []

    for room in rooms:

        score = calculate_room_score(
            room,
            preferences
        )

        results.append({
            "name": room["name"],
            "price": room["price"],
            "rating": room["rating"],
            "score": score
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results