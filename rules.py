def evaluate(m):
    flags = []

    if 150 <= m["knee"] <= 165:
        flags.append("good_knee_position")
    else:
        flags.append("knee_upright")

    if m["head"] > 0.03:
        flags.append("unstable_head")

    if m["trunk"] > 0.12:
        flags.append("excessive_lean")

    return flags
