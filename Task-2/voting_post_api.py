from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/voting", methods=["POST"])
def voting_check():

    data = request.get_json()

    if data is None or "name" not in data or "age" not in data:
        return jsonify({
            "error": "Please provide name and age"
        }), 400

    name = data["name"]
    age = data["age"]

    if not isinstance(age, int):
        return jsonify({
            "error": "Age must be an integer"
        }), 400

    if age >= 18:
        status = "eligible to vote"
    else:
        status = "not eligible to vote"

    return jsonify({
        "name": name,
        "age": age,
        "voting_status": status
    }), 200


if __name__ == "__main__":
    app.run()
