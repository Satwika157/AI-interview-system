from flask import Flask, render_template, request
from questions import questions
from score import calculate_score

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/interview", methods=["POST"])
def interview():

    level = request.form["level"]

    q = questions[level]

    return render_template("interview.html", questions=q, level=level)


@app.route("/result", methods=["POST"])
def result():

    level = request.form["level"]

    q = questions[level]

    user_answers = []

    for i in range(len(q)):
        user_answers.append(request.form.get(f"q{i}"))

    score = calculate_score(user_answers, q)

    return render_template("result.html", score=score,total=len(q))


if __name__ == "__main__":
    app.run(debug=True)