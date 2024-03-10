import numpy as np
from utils.convert import convert_mpers_2_kmperh

BEAUFORE_WIND_SCALE = {
    "Calm": [0, 0.99],
    "Light Air": [1, 5],
    "Light Breeze": [6, 11],
    "Gentle Breeze": [12, 19],
    "Moderate Breeze": [20, 28],
    "Fresh Breeze": [29, 38],
    "Strong Breeze": [38, 49],
    "Near Gale": [50, 61],
    "Gale": [62, 74],
    "Strong Gale": [75, 88],
    "Storm": [89, 102],
    "Violent Storm": [103, 117],
    "Hurricane": [118]
}


def compute_general_evolution(temp: list, pres: list, pop: list) -> str:
    # We set an item time which is integer value from 0 to len(temp)
    tendance_temp = compute_tendance(temp)
    tendance_pres = compute_tendance(pres)
    tendance_pop = compute_tendance(pop)

    if tendance_temp == "En hausse" and tendance_pres == "En hausse" and tendance_pop == "En baisse":
        return "En amelioration"
    elif tendance_temp == tendance_pres == tendance_pop == "Stable":
        return "Stable"
    else:
        return "En dégradation"


def compute_tendance(val: list) -> str:
    """
    Function to compute the tendance of a specific variable using a linear regression
    """
    # We set an item time which is integer value from 0 to len(val)
    time = np.arange(0, len(val))
    val = np.array(val)

    # We make a linear regression in order to estimate the tendance using the pente
    pente, intercept = np.polyfit(time, val, 1)

    # pente < -0.2 -> En baisse | -0.2 < pente < 0.2 -> Stable | pente > 0.2 -> En hausse
    if pente < -0.2:
        return "En baisse"
    elif -0.2 <= pente <= 0.2:
        return "Stable"
    else:
        return "En hausse"


def compute_mean_wind(wind_speed: list) -> str:
    mean = round(convert_mpers_2_kmperh(np.mean(wind_speed)), 2)
    for key, value in BEAUFORE_WIND_SCALE.items():
        if len(value) == 2:
            if value[0] <= mean <= value[1]:
                return key
        else:
            if mean >= value[0]:
                return key
    return "Value not detected in the Beaufore wind Scale"
