from flask import (Flask,
    render_template, request,
    redirect, url_for, send_from_directory
     )
from bs4 import BeautifulSoup
import requests
import pandas as pd
from htmldocx import HtmlToDocx
import os
UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        ID = request.form['specialIDInput']
        docType = request.form['docType']
        if docType == "sheets":
            url = f"https://docs.google.com/spreadsheets/u/0/d/{ID}/htmlview"
            try:
                websiteContent = requests.get(url)
                soup = BeautifulSoup(websiteContent.text, "html.parser")
                docName = soup.title.string.replace(".", "").replace("/", "").replace(" ", "")
                tab = pd.read_html(websiteContent.text)
                tab[0].to_csv(f"uploads/sheets/{docName}.csv")
                return render_template("index.html", doc_type="sheets", name=f"{docName}.csv")
            except Exception:
                return redirect(url_for("index"))
        elif docType == "docx":
            url = f"https://docs.google.com/document/d/{ID}/mobilebasic"
            try:
                new_parser = HtmlToDocx()
                websiteContent = requests.get(url)
                soup = BeautifulSoup(websiteContent.text, "html.parser")
                docName = soup.title.string.replace(".", "").replace("/", "")
                div = soup.find("div", {"class": "doc"})
                d = div.find("div")
                docx = new_parser.parse_html_string(d.prettify())
                docx.save(f"uploads/docx/{docName}.docx")
                return render_template("index.html", doc_type="docx", name=f"{docName}.docx")

            except Exception:
                return redirect(url_for("index"))
        
        return redirect(url_for("index"))
    else:
        return render_template("index.html")

@app.route('/uploads/<doc_type>/<name>')
def download_file(doc_type, name):
    print("redirect successful")
    return send_from_directory(app.config["UPLOAD_FOLDER"] + f"/{doc_type}/",  name)