from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form["task"].strip() != "":
            task_list.append(request.form["task"])
        print(task_list)
        return redirect(url_for("index", tasklist = task_list))
    return render_template("index.html", tasklist = task_list)




if __name__ == "__main__":
    task_list = []
    app.run(debug=True, port=4000)