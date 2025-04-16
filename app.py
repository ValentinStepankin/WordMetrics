"""Основной модуль для анализа текстовых файлов.
Позволяет загружать текстовые файлы и отображать результаты с постраничной навигацией."""

import math

from flask import Flask, request, render_template, session
from utils.text_processing import process_text
from utils.tfidf_calculator import calculate_tfidf

app = Flask(__name__)
PER_PAGE = 10


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["text_file"]

        text = file.read().decode("utf-8")
        words = process_text(text)
        tfidf_data = calculate_tfidf(words)

        session['tfidf_data'] = tfidf_data

        return render_template(
            "result.html",
            data=tfidf_data[:PER_PAGE],
            page=1,
            total_pages=math.ceil(len(tfidf_data) / PER_PAGE)
        )

    return render_template("upload.html")


@app.route("/results/<int:page>")
def show_results(page):
    tfidf_data = session.get('tfidf_data', [])

    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginated_data = tfidf_data[start:end]

    return render_template(
        "result.html",
        data=paginated_data,
        page=page,
        total_pages=math.ceil(len(tfidf_data) / PER_PAGE)
    )


if __name__ == "__main__":
    app.secret_key = "secret_key"
    app.run(debug=True)
