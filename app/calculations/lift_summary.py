import math

def lift_summary(
    load_t: float,
    sling_angle_deg: float,
    number_of_legs: int,
    daf: float = 1.3,
    sling_wll_t: float = 50.0
):
    if load_t <= 0:
        raise ValueError("Load must be greater than zero")

    if sling_angle_deg <= 0 or sling_angle_deg >= 90:
        raise ValueError("Sling angle must be between 0 and 90 degrees")

    if number_of_legs <= 0:
        raise ValueError("Number of sling legs must be greater than zero")

    if daf < 1.0:
        raise ValueError("DAF must be >= 1.0")

    angle_rad = math.radians(sling_angle_deg)

    factored_load = load_t * daf
    hook_load = factored_load
    tension_per_leg = factored_load / (number_of_legs * math.sin(angle_rad))
    utilization = tension_per_leg / sling_wll_t

    return {
        "daf": round(daf, 2),
        "factored_load_t": round(factored_load, 3),
        "hook_load_t": round(hook_load, 3),
        "tension_per_leg_t": round(tension_per_leg, 3),
        "utilization_ratio": round(utilization, 3)
    }
