"""app.py - the IN-CODE COMPONENT.

The route handlers live here, inside the main file. Each one imports
and calls a function from the outside module crypto_service.py.
"""
from flask import Flask, jsonify, render_template, request

from crypto_service import generate_hybrid_session_key, sha256_hash

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hash")
def hash_route():
    # In-code route handler calling the outside function
    text = request.args.get("text", "")
    if not text:
        return jsonify(error="Provide ?text=..."), 400
    return jsonify(text=text, algorithm="SHA-256", hash=sha256_hash(text))


@app.route("/generate-key")
def key_route():
    # In-code route handler calling the outside function
    return jsonify(generate_hybrid_session_key())


if __name__ == "__main__":
    app.run(debug=True)
