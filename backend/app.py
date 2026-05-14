from flask import Flask, request, jsonify

app = Flask(__name__)

# 🌐 Homepage (fixes 404)
@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Hex Specter</title>
        </head>
        <body style="background:black;color:lime;font-family:monospace;text-align:center;padding-top:50px;">
            <h1>💀 HEX SPECTER ACTIVE</h1>
            <p>Cyber Security Tool is Running</p>
            <p>Endpoint: /analyze</p>
        </body>
    </html>
    """

# 🔍 File scan endpoint
@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({
            "error": "No file uploaded"
        }), 400

    file = request.files["file"]

    return jsonify({
        "filename": file.filename,
        "status": "scanned successfully",
        "result": "safe (demo response)"
    })


# 🚀 run server (needed for Render)
if __name__ == "__main__":
    app.run()