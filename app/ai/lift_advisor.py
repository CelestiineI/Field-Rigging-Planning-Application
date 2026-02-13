def lift_advisory(utilization_ratio: float):
    advice = []

    if utilization_ratio > 1.0:
        advice.append("Utilization exceeds 1.0 — increase sling capacity or reduce load.")
    elif utilization_ratio > 0.9:
        advice.append("Utilization is high — consider increasing sling angle or adding sling legs.")
    else:
        advice.append("Utilization is within acceptable limits.")

    return advice
