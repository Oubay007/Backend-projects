from flask import Flask, request, jsonify
import requests
from pypdf import PdfReader
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PDF_URLS = [
    "https://www.fmpc.ac.ma/wp-content/uploads/2025/07/liste-admis-medecine.pdf",
    "https://www.fmpc.ac.ma/wp-content/uploads/2025/07/liste-admis-pharmacie.pdf"
]

PDF_FILENAMES = [
    "pdf_file_1.pdf",
    "pdf_file_2.pdf"
]

def download_pdfs():
    for url, filename in zip(PDF_URLS, PDF_FILENAMES):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
        else:
            return False  # Fail if any PDF fails to download
    return True  # All PDFs downloaded successfully

def search_pdfs(massar_id):
    for filename in PDF_FILENAMES:
        reader = PdfReader(filename)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        if massar_id in text:
            return True
    return False

@app.route("/api/check", methods=["POST"])
def check():
    data = request.get_json()
    massar_id = data.get("massar_id", "").strip()
    if not massar_id:
        return jsonify({"error": "No Massar ID provided"}), 400

    if not download_pdfs():
        return jsonify({"error": "Failed to download PDFs"}), 500

    found = search_pdfs(massar_id)
    if found:
        return jsonify({"result": "You have been accepted"})
    else:
        return jsonify({"result": "You haven't been accepted"})

if __name__ == "__main__":
    app.run(debug=True)
