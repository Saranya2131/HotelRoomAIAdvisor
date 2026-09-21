import skfuzzy.control as ctrl

from fuzzy_logic import hotel_control_system


def calculate_suitability(
    budget_value,
    view_value,
    quietness_value,
    space_value
):

    simulation = ctrl.ControlSystemSimulation(
        hotel_control_system
    )

    simulation.input['budget'] = budget_value
    simulation.input['view'] = view_value
    simulation.input['quietness'] = quietness_value
    simulation.input['space'] = space_value

    simulation.compute()

    return simulation.output['suitability']


# Test the fuzzy system
score = calculate_suitability(
    4500,
    80,
    85,
    75
)

print("Suitability Score:", round(score, 2))