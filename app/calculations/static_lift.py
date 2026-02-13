import math

def sling_tension(load_t: float, sling_angle_deg: float, number_of_legs: int) -> float:
    """
    Calculate sling tension per leg for a symmetric lift.

    load_t: Total load in tonnes
    sling_angle_deg: Sling angle from horizontal (degrees)
    number_of_legs: Number of sling legs
    """
    if load_t <= 0:
        raise ValueError("Load must be greater than zero")

    if sling_angle_deg <= 0 or sling_angle_deg >= 90:
        raise ValueError("Sling angle must be between 0 and 90 degrees")

    if number_of_legs <= 0:
        raise ValueError("Number of sling legs must be greater than zero")

    angle_rad = math.radians(sling_angle_deg)
    tension = load_t / (number_of_legs * math.sin(angle_rad))

    return round(tension, 3)
