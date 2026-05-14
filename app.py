from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hex_Specter backend online 💀"

@app.route("/scan", methods=["POST"])
def scan_file():
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filename = file.filename

    # fake forensic logic (we’ll upgrade later)
    return jsonify({
        "file": filename,
        "status": "ANALYZED",
        "risk_level": "LOW",
        "findings": [
            "File received successfully",
            "No suspicious structure detected",
            "Scan completed (demo mode)"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)