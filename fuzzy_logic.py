import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# -----------------------------
# INPUT VARIABLES
# -----------------------------

budget = ctrl.Antecedent(
    np.arange(0, 10001, 1),
    'budget'
)

view = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'view'
)

quietness = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'quietness'
)

space = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'space'
)


# -----------------------------
# OUTPUT VARIABLE
# -----------------------------

suitability = ctrl.Consequent(
    np.arange(0, 101, 1),
    'suitability'
)


# -----------------------------
# BUDGET MEMBERSHIP FUNCTIONS
# -----------------------------

budget['low'] = fuzz.trimf(
    budget.universe,
    [0, 0, 3500]
)

budget['medium'] = fuzz.trimf(
    budget.universe,
    [2500, 5000, 7000]
)

budget['high'] = fuzz.trimf(
    budget.universe,
    [5500, 10000, 10000]
)


# -----------------------------
# VIEW MEMBERSHIP FUNCTIONS
# -----------------------------

view['low'] = fuzz.trimf(
    view.universe,
    [0, 0, 50]
)

view['medium'] = fuzz.trimf(
    view.universe,
    [30, 50, 75]
)

view['high'] = fuzz.trimf(
    view.universe,
    [60, 100, 100]
)


# -----------------------------
# QUIETNESS MEMBERSHIP FUNCTIONS
# -----------------------------

quietness['low'] = fuzz.trimf(
    quietness.universe,
    [0, 0, 50]
)

quietness['medium'] = fuzz.trimf(
    quietness.universe,
    [30, 55, 80]
)

quietness['high'] = fuzz.trimf(
    quietness.universe,
    [60, 100, 100]
)


# -----------------------------
# SPACE MEMBERSHIP FUNCTIONS
# -----------------------------

space['small'] = fuzz.trimf(
    space.universe,
    [0, 0, 50]
)

space['medium'] = fuzz.trimf(
    space.universe,
    [30, 55, 80]
)

space['large'] = fuzz.trimf(
    space.universe,
    [60, 100, 100]
)


# -----------------------------
# SUITABILITY MEMBERSHIP
# -----------------------------

suitability['poor'] = fuzz.trimf(
    suitability.universe,
    [0, 0, 30]
)

suitability['average'] = fuzz.trimf(
    suitability.universe,
    [20, 45, 65]
)

suitability['good'] = fuzz.trimf(
    suitability.universe,
    [55, 70, 85]
)

suitability['excellent'] = fuzz.trimf(
    suitability.universe,
    [75, 100, 100]
)

# -----------------------------
# FUZZY RULES
# -----------------------------

rule1 = ctrl.Rule(
    budget['high'] &
    view['high'] &
    quietness['high'],
    suitability['excellent']
)

rule2 = ctrl.Rule(
    budget['medium'] &
    view['high'] &
    quietness['high'],
    suitability['good']
)

rule3 = ctrl.Rule(
    budget['low'] &
    view['low'] &
    quietness['low'],
    suitability['poor']
)

rule4 = ctrl.Rule(
    space['large'] &
    quietness['high'],
    suitability['excellent']
)

rule5 = ctrl.Rule(
    budget['medium'] &
    space['medium'],
    suitability['good']
)

rule6 = ctrl.Rule(
    view['medium'] &
    quietness['medium'],
    suitability['average']
)

# -----------------------------
# CONTROL SYSTEM
# -----------------------------

hotel_control_system = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6
])