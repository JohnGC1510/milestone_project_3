import os
import pygal
from pygal.style import Style
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)


@app.route("/profile/<user>")
def profile(user):
    user = mongo.db.users.find_one(
            {"username": session["user"]})

    questions = mongo.db.questions.find()
    if user["user_type"] == "student":
        student = mongo.db.students.find_one({"userId": user["_id"]})
        return render_template("profile.html", user=user, questions=questions,
                               student=student)

    return render_template("profile.html", user=user, questions=questions)


@app.route("/all_questions")
def all_questions():
    questions = list(mongo.db.questions.find())
    user = mongo.db.users.find_one(
            {"username": session["user"]})
    return render_template(
        "all_questions.html", questions=questions, user=user)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    questions = list(mongo.db.questions.find(
        {"$text": {"$search": query}}
    ))
    user = mongo.db.users.find_one(
            {"username": session["user"]})
    return render_template(
        "all_questions.html", questions=questions, user=user)


@app.route("/answer/<question_id>", methods=["GET", "POST"])
def answer(question_id):
    userId = mongo.db.users.find_one(
        {"username": session["user"]}
        )["_id"]
    student = mongo.db.students.find_one({"userId": userId})
    student_answer = request.form.get("answer")
    question_answer = mongo.db.questions.find_one(
        {"_id": ObjectId(question_id)})["answer"]
    if student_answer == question_answer:
        flash("correct")
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$inc": {"questions_correct": +1}}
        )
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$inc": {"questions_answered": +1}}
        )
    else:
        flash("incorrect")
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$inc": {"questions_answered": +1}}
        )

    return redirect(url_for('all_questions'))


@app.route("/make_graph")
def make_graph():
    userId = mongo.db.users.find_one(
        {"username": session["user"]}
        )["_id"]
    student = mongo.db.students.find_one({"userId": userId})
    correct = float(student["questions_correct"])
    total = float(student["questions_answered"])
    custom = Style(
        background="transparent",
        colors=("#0D31C5", "#B4B5B7"),
        opacity="0.6",
        opacity_hover="0.9"
    )
    # avoid division by zero error
    if total != 0:
        incorrect = total - correct
        correct_value = (correct/total)*100
        incorrect_value = (incorrect/total)*100
        pie_chart = pygal.Pie(
            show_legend=False, margin=0, style=custom)
        pie_chart.add("Correct", correct_value)
        pie_chart.add("Incorrect", incorrect_value)
        pie_chart.render()
    else:
        pie_chart = pygal.Pie(
            show_legend=False, margin=0, style=custom)
        pie_chart.add("Correct (example)", 65)
        pie_chart.add("Incorrect (example)", 35)
        pie_chart.render()

    return pie_chart.render_response()


@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    modules = mongo.db.modules.find()
    if request.method == "POST":
        question = {
            "module_name": request.form.get("module_name").lower(),
            "grade": request.form.get("grade"),
            "question_name": request.form.get("question_name"),
            "question": request.form.get("question"),
            "method": request.form.get("method"),
            "answer": request.form.get("answer"),
            "author": session["user"]
        }
        for module in modules:
            if module["module_name"] == question.get("module_name"):
                mongo.db.modules.update_one(
                    {"module_name": module["module_name"]},
                    {"$inc": {"total_questions": +1}}
                )
        mongo.db.questions.insert_one(question)
        flash("question successfully added")
        return redirect(url_for("profile", user=session["user"]))

    return render_template("add_question.html", modules=modules)


@app.route("/edit_question/<question_id>", methods=["GET", "POST"])
def edit_question(question_id):
    question = mongo.db.questions.find_one({"_id": ObjectId(question_id)})
    modules = mongo.db.modules.find()
    question_module = question.get("module_name")

    if request.method == "POST":
        question_update = {
            "module_name": request.form.get("module_name").lower(),
            "grade": request.form.get("grade"),
            "question_name": request.form.get("question_name"),
            "question": request.form.get("question"),
            "method": request.form.get("method"),
            "answer": request.form.get("answer"),
            "author": session["user"]
        }
        for module in modules:
            module_name = module.get("module_name")
            updated_name = question_update.get("module_name")
            # if module is unchanged by edit
            if (updated_name == module_name and
                    question_module == module_name):
                break

            # if module name equal to last questions module total_questions -=1
            elif (module_name == question_module and
                    module_name != updated_name):
                mongo.db.modules.update_one(
                    {"module_name": module["module_name"]},
                    {"$inc": {"total_questions": -1}}
                )
            # if module name has changed on edit module total_questions +=1
            elif (module_name == updated_name and
                    module_name != question_module):
                mongo.db.modules.update_one(
                    {"module_name": module["module_name"]},
                    {"$inc": {"total_questions": +1}}
                )
        mongo.db.questions.update(
            {"_id": ObjectId(question_id)}, question_update)
        flash("question successfully edited")
        return redirect(url_for("profile", user=session["user"]))

    return render_template("edit_question.html",
                           modules=modules, question=question)


@app.route("/delete_question/<question_id>")
def delete_question(question_id):
    question = mongo.db.questions.find_one({"_id": ObjectId(question_id)})
    mongo.db.modules.update_one(
            {"module_name": question["module_name"]},
            {"$inc": {"total_questions": -1}}
        )
    mongo.db.questions.remove({"_id": ObjectId(question_id)})
    flash("Question has been deleted")
    return redirect(url_for("profile", user=session["user"]))


@app.route("/manage_modules")
def manage_modules():
    modules = mongo.db.modules.find()
    return render_template("manage_modules.html", modules=modules)


@app.route("/add_module", methods=["GET", "POST"])
def add_module():
    if request.method == "POST":
        module = {
            "module_name": request.form.get("module_name").lower(),
            "total_questions": 0
        }
        mongo.db.modules.insert_one(module)
        return redirect(url_for("manage_modules"))

    return render_template("add_module.html")


@app.route("/edit_module/<module_id>", methods=["GET", "POST"])
def edit_module(module_id):
    if request.method == "POST":
        module_edit = {
            "module_name": request.form.get("module_name").lower()
        }
        mongo.db.modules.update(
            {"_id": ObjectId(module_id)},
            module_edit
        )
        flash("Module has been updated")
        return redirect(url_for("manage_modules"))

    module = mongo.db.modules.find_one({"_id": ObjectId(module_id)})
    return render_template("edit_module.html", module=module)


@app.route("/delete_module/<module_id>")
def delete_module(module_id):
    mongo.db.modules.remove({"_id": ObjectId(module_id)})
    flash("Module deleted successfully")
    return redirect(url_for("manage_modules"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("login"))

        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "title": request.form.get("title"),
            "first_name": request.form.get("first_name").lower(),
            "surname": request.form.get("surname").lower(),
            "user_type": request.form.get("user_type"),
            "class": request.form.get("class")
        }
        mongo.db.users.insert_one(new_user)

        if new_user["user_type"] == "student":
            student = {
                "userId": new_user["_id"],
                "class": request.form.get("class"),
                "questions_answered": 0,
                "questions_correct": 0,
                "percentage_correct": 0.0,
                "current_grade": 4
            }
            mongo.db.students.insert_one(student)

        if new_user["user_type"] == "teacher":
            teacher = {
                "userId": new_user["_id"],
                "class": request.form.get("class")
            }
            mongo.db.teachers.insert_one(teacher)

        # put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", user=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        input_name = request.form.get("username").lower()
        existing_user = mongo.db.users.find_one({"username": input_name})

        if existing_user:
            # ensure hahsed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password").lower()):
                session["user"] = input_name
                flash("welcome, {}".format(input_name))
                return redirect(url_for("profile", user=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        else:
            # invalid username
            flash("incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
