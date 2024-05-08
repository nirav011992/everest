# app.py
from flask import Flask, request, jsonify
from outcome_chart import BOWLING_CARDS, SHOT_CARDS, TIMINGS, predict_outcome, get_commentary
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to CricSummit 2021!"

@app.route('/predict_outcome', methods=['POST'])
def predict_outcome_route():
    data = request.get_json()
    bowl_card = data.get('bowl_card')
    shot_card = data.get('shot_card')
    timing = data.get('timing')
    if bowl_card and shot_card and timing:
        outcome = predict_outcome(bowl_card, shot_card, timing)
        commentary = get_commentary(outcome)
        return jsonify({
            "commentary": f"{commentary} - {outcome}",
            "outcome": outcome
        })
    return jsonify({"error": "Invalid input"}), 400

@app.route('/super_over', methods=['POST'])
def super_over():
    data = request.get_json()
    team1_name = data.get("team1_name", "India")
    team2_name = data.get("team2_name", "Australia")
    team1_score = data.get("team1_score", 20)
    target = team1_score + 1

    wickets = 2
    balls = 6
    score = 0
    commentary_list = []

    for ball in range(1, balls + 1):
        if wickets == 0:
            break
        bowl_card = random.choice(BOWLING_CARDS)
        shot_card = random.choice(SHOT_CARDS)
        timing = random.choice(TIMINGS)
        outcome = predict_outcome(bowl_card, shot_card, timing)
        if outcome == "wicket":
            wickets -= 1
        else:
            score += int(outcome[0])

        commentary = get_commentary(outcome)
        commentary_list.append(
            f"{team1_name} bowled {bowl_card} ball, {team2_name} played {timing} {shot_card} shot. {commentary} - {outcome}"
        )

    result = f"{team2_name} {'won' if score >= target else 'lost'} by {'wickets' if score >= target else 'runs'}"
    commentary_list.append(f"{team2_name} scored: {score} runs")
    commentary_list.append(result)

    return jsonify(commentary_list)

if __name__ == '__main__':
    app.run(debug=True)
