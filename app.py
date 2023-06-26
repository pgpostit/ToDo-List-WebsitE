from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

task_list = []  # Lista de tarefas

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form["task"].strip() != "":
            task_list.append(request.form["task"])
        return redirect(url_for("tasks"))
    task_list.clear()
    return render_template("index.html")

@app.route("/tasklist")
def tasks():
    return render_template("index.html", tasklist = task_list)

if __name__ == "__main__":
    app.run()
