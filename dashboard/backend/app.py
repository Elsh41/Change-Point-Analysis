import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_json(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "service": "Brent Oil Analytics API"}), 200

@app.route("/api/prices", methods=["GET"])
def get_prices():
    prices = load_json("brent_prices.json")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    
    if start_date:
        prices = [p for p in prices if p["date"] >= start_date]
    if end_date:
        prices = [p for p in prices if p["date"] <= end_date]
        
    return jsonify({"count": len(prices), "data": prices})

@app.route("/api/events", methods=["GET"])
def get_events():
    events = load_json("oil_events.json")
    category = request.args.get("category")
    if category:
        events = [e for e in events if e.get("Category") == category]
    return jsonify({"count": len(events), "data": events})

@app.route("/api/changepoints", methods=["GET"])
def get_change_points():
    changepoints = load_json("change_points.json")
    return jsonify({"count": len(changepoints), "data": changepoints})

@app.route("/api/metrics", methods=["GET"])
def get_summary_metrics():
    prices = load_json("brent_prices.json")
    if not prices:
        return jsonify({})
    
    price_vals = [p["price"] for p in prices if p.get("price") is not None]
    return jsonify({
        "total_records": len(prices),
        "min_price": round(min(price_vals), 2) if price_vals else 0,
        "max_price": round(max(price_vals), 2) if price_vals else 0,
        "avg_price": round(sum(price_vals) / len(price_vals), 2) if price_vals else 0,
        "latest_price": price_vals[-1] if price_vals else 0
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)