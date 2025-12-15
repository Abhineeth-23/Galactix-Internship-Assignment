from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return jsonify({
        "message": "Welcome to HITAM!!!"
    }), 200

if __name__ == "__main__":
    app.run()
