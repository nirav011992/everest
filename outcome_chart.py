# outcome_chart.py
import random

# Define the shot and ball combinations
BOWLING_CARDS = [
    "Bouncer", "Outswinger", "Yorker", "Off Break",
    "Inswinger", "Leg Cutter", "Slower Ball", "Pace",
    "Off Cutter", "Doosra"
]

SHOT_CARDS = [
    "Straight", "Flick", "Long On", "SquareCut", "Sweep",
    "CoverDrive", "Pull", "Scoop", "LegLance", "UpperCut"
]

TIMINGS = ["Early", "Good", "Late", "Perfect"]
OUTCOMES = ["1 run", "2 runs", "3 runs", "4 runs", "5 runs", "6 runs", "wicket", "0 runs"]

# Outcome chart mapping
OUTCOME_CHART = {
    ("Bouncer", "Pull", "Perfect"): "6 runs",
    ("Bouncer", "Pull", "Late"): "wicket",
    ("Yorker", "Straight", "Early"): "2 runs",
    ("Pace", "Straight", "Good"): "1 run",
    ("Inswinger", "Sweep", "Perfect"): "4 runs",
    ("Outswinger", "CoverDrive", "Good"): "3 runs",
    ("Off Break", "Flick", "Late"): "wicket",
    # Additional outcomes can be added here...
}

# Predict outcome based on given shot and bowl type
def predict_outcome(bowl_card, shot_card, timing):
    return OUTCOME_CHART.get((bowl_card, shot_card, timing), random.choice(OUTCOMES))

# Generate random commentary
COMMENTARY = {
    "wicket": "It's a wicket. Excellent line and length.",
    "6 runs": "That's massive and out of the ground.",
    "4 runs": "Just over the fielder.",
    "1 run": "Excellent running between the wickets.",
    "2 runs": "Convert ones into twos.",
    "0 runs": "Edged and taken."
}

def get_commentary(outcome):
    return COMMENTARY.get(outcome, "Excellent shot.")
