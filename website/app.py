from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    first_name = None
    food = None
    if request.method == "POST":
        first_name = request.form.get("first_name")
        food = request.form.get("food")
    return render_template("index.html", first_name=first_name, food=food)

if __name__ == "__main__":
    app.run(debug=True)