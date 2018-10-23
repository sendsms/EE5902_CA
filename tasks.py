import math

tasks = {
    1: {
        "Duration": 7,
        "Deadline": 18,
        "Current": 650
    },
    2: {
        "Duration": 5,
        "Deadline": 10,
        "Current": 800
    },
    3: {
        "Duration": 8,
        "Deadline": 26,
        "Current": 400
    },
    4: {
        "Duration": 10,
        "Deadline": 38,
        "Current": 380
    }
}

def CalDuration(Vdd, Vdd_new, I, Duration):
    voltage_sets = set([3.3, 3.0, 2.7, 2.5, 2.0])

    assert Vdd in voltage_sets
    assert Vdd_new in voltage_sets

    Vth = 0.4
    s = Vdd / Vdd_new
    I_new = I / math.pow(s, 3)
    Duration_new = Duration * s * (1 + 2 * (s - 1) * Vth / (Vdd - Vth))

    return I_new, Duration_new