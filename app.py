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

""" DEBUG = if ("DEVELOPMENT" in os.environ) True else False """

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


def calc_working_grade(score):
    """
    Calculates the current students working grade from their percentage of questions answered correctly
    """
    if score >= 90:
        current_grade = 9
    elif score >= 80:
        current_grade = 8
    elif score >= 70:
        current_grade = 7
    elif score >= 60:
        current_grade = 6
    elif score >= 50:
        current_grade = 5
    elif score >= 40:
        current_grade = 4
    elif score >= 30:
        current_grade = 3
    elif score >= 20:
        current_grade = 2
    elif score >= 10:
        current_grade = 1
    else:
        current_grade = "U"

    return current_grade


# Error Handling Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/profile/<user>")
def profile(user):
    """
    This function generates the profile page for users. For student users
    it specifically takes the data from mongodb to create tuples that
    allow the progess bars to be dynamically updated.
    """
    if "user" not in session:
        return render_template("not_user.html")

    user = mongo.db.users.find_one(
            {"username": session["user"]})

    questions = mongo.db.questions.find()
    if user["user_type"] == "student":
        energy_correct = 0
        particles_correct = 0
        electricity_correct = 0
        radioactivity_correct = 0
        modules = mongo.db.modules.find()
        student = mongo.db.students.find_one({"userId": user["_id"]})
        student_correct = student["questions_correct_id"]
        modules_array = []
        if student["questions_answered"] > 0:
            percentage_correct = (float(
                student["questions_correct"])/float(
                    student["questions_answered"]))*100
            working_grade = calc_working_grade(percentage_correct)
        else:
            working_grade = 4
        mongo.db.students.update_one(
             {"userId": user["_id"]},
             {"$set": {"current_grade": working_grade}}
         )
        """
         Code below creates an array of tuples that couples the name of
         the module with the percentage of code that the student has answered
         correctly in that  module to allow for automatically updating progress
         bars. Issue with current code is that you will manually need to add
         additional modules.
        """
        for question in questions:
            for correct in student_correct:
                if question["_id"] == correct:
                    if question["module_name"] == "energy":
                        energy_correct += 1
                    if question["module_name"] == "electricity":
                        electricity_correct += 1
                    if question["module_name"] == "particles":
                        particles_correct += 1
                    if question["module_name"] == "radioactivity":
                        radioactivity_correct += 1
        for module in modules:
            if (module["module_name"] == "energy" and module[
                    "total_questions"] > 0):
                energy_percent = (
                    float(energy_correct)/float(module["total_questions"]))*100
                if energy_percent > 100:
                    energy_percent == 100
                modules_array.append(
                    (module["module_name"], round(energy_percent, 2)))

            if (module["module_name"] == "electricity" and
                    module["total_questions"] > 0):
                electric_percent = (
                    float(electricity_correct)/float(
                        module["total_questions"]))*100
                modules_array.append(
                    (module["module_name"], round(electric_percent, 2)))

            if (module["module_name"] == "particles" and
                    module["total_questions"] > 0):
                particle_percent = (
                    float(particles_correct)/float(
                        module["total_questions"]))*100
                modules_array.append(
                    (module["module_name"], round(particle_percent, 2)))

            if (module["module_name"] == "radioactivity" and
                    module["total_questions"] > 0):
                radioactivity_percent = (
                    float(radioactivity_correct)/float(
                        module["total_questions"]))*100
                modules_array.append(
                    (module["module_name"], round(radioactivity_percent, 2)))

        return render_template("profile.html", user=user, questions=questions,
                               student=student, modules=modules_array)

    return render_template("profile.html", user=user, questions=questions)


@app.route("/all_questions")
def all_questions():
    """
    Function takes information from mongodb that allows students
    to be able to see and answer all questions
    """
    if "user" not in session:
        return render_template("not_user.html")

    questions = list(mongo.db.questions.find())
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    student = mongo.db.students.find_one(
        {"userId": user["_id"]}
    )
    return render_template(
        "all_questions.html", questions=questions, user=user,
        student=student
        )


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Function to allow users to able to search through all questions
    """
    query = request.form.get("query")
    questions = list(mongo.db.questions.find(
        {"$text": {"$search": query}}
    ))
    user = mongo.db.users.find_one(
            {"username": session["user"]})
    student = mongo.db.students.find_one(
        {"userId": user["_id"]}
    )
    return render_template(
        "all_questions.html", questions=questions, user=user,
        student=student
        )


@app.route("/answer/<question_id>", methods=["GET", "POST"])
def answer(question_id):
    """
    Function takes the answer submitted by the student and
    updates relevant parts of the database to provide student
    with some statistics on performance
    """
    userId = mongo.db.users.find_one(
        {"username": session["user"]}
        )["_id"]
    student = mongo.db.students.find_one({"userId": userId})
    student_answer = request.form.get("answer").lower()
    question_answer = mongo.db.questions.find_one(
        {"_id": ObjectId(question_id)})["answer"]
    if student_answer == question_answer:
        flash("correct")
        mongo.db.students.update(
            {"_id": student["_id"]},
            {"$inc": {"questions_correct": +1,
             "questions_answered": +1}}
        )
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$addToSet": {"questions_correct_id": ObjectId(question_id)}}
        )
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$pull": {"questions_unanswered": ObjectId(question_id)}}
        )
        questions_incorrect = mongo.db.students.find_one(
            {"_id": student["_id"]}
        )["questions_incorrect_id"]
        for incorrect_id in questions_incorrect:
            if incorrect_id == ObjectId(question_id):
                mongo.db.students.update_one(
                    {"_id": student["_id"]},
                    {"$pull":
                     {"questions_incorrect_id": ObjectId(question_id)}}
                )
    else:
        flash("incorrect")
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$inc": {"questions_answered": +1}}
        )
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$addToSet": {"questions_incorrect_id": ObjectId(question_id)}}
        )
        mongo.db.students.update_one(
            {"_id": student["_id"]},
            {"$pull": {"questions_unanswered": ObjectId(question_id)}}
        )
    return redirect(url_for('all_questions'))


@app.route("/make_graph")
def make_graph():
    """
    Function uses pygal libary and data from student to generate
    a pie chart
    """
    userId = mongo.db.users.find_one(
        {"username": session["user"]}
        )["_id"]
    student = mongo.db.students.find_one({"userId": userId})
    correct = float(student["questions_correct"])
    total = float(student["questions_answered"])
    custom = Style(
        background="transparent",
        colors=("#1EAC1E", "#EE0404"),
        opacity="0.6",
        opacity_hover="0.9"
    )
    # avoid division by zero error
    if total != 0:
        incorrect = total - correct
        correct_value = (correct/total)*100
        incorrect_value = (incorrect/total)*100
        percentage = round(correct_value, 1)

        mongo.db.students.update_one(
            {"userId": userId},
            {"$set": {"percentage_correct": percentage}}
        )
        pie_chart = pygal.Pie(
            show_legend=False, margin=0, style=custom)
        pie_chart.add("Correct", correct_value)
        pie_chart.add("Incorrect", incorrect_value)
        pie_chart.render()
    else:
        pie_chart = pygal.Pie(
            show_legend=False, margin=0, style=custom)
        pie_chart.add("Correct (example)", 100)
        pie_chart.render()

    return pie_chart.render_response()


@app.route("/classes")
def classes():
    """
    function orders student data numerically to allow a top ten table
    to be displayed for student's comparison as well as being
    ordered alphabetically for ease of teacher
    """
    if "user" not in session:
        return render_template("not_user.html")

    user = mongo.db.users.find_one(
        {"username": session["user"]}
    )
    students = list(mongo.db.students.find(
        {"class": user["class"]}
    ).sort([("surname", 1)]))

    questions_answered = []
    questions_correct = []
    top_ten = 0
    for student in students:
        if top_ten <= 9:
            answered = (student["questions_answered"], student["username"])
            correct = (student["questions_correct"], student["username"])
            questions_answered.append(answered)
            questions_correct.append(correct)
            top_ten += 1

    questions_answered.sort(key=lambda x: x[0], reverse=True)
    questions_correct.sort(key=lambda x: x[0], reverse=True)

    return render_template(
        "class.html",
        user=user,
        questions_answered=questions_answered,
        questions_correct=questions_correct,
        students=students
        )


@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    """
    function takes information from the user submitted form
    and updates database with the question added by the user
    """
    if "user" not in session:
        return render_template("not_user.html")

    user_type = mongo.db.users.find_one(
        {"username": session["user"]}
    )["user_type"]
    if user_type == "admin" or user_type == "teacher":
        modules = mongo.db.modules.find()
        if request.method == "POST":
            question = {
                "module_name": request.form.get("module_name").lower(),
                "grade": request.form.get("grade"),
                "question_name": request.form.get("question_name"),
                "question": request.form.get("question"),
                "method": request.form.get("method"),
                "answer": request.form.get("answer").lower(),
                "author": session["user"]
            }
            mongo.db.questions.insert_one(question)
            for module in modules:
                if module["module_name"] == question.get("module_name"):
                    mongo.db.modules.update_one(
                        {"module_name": module["module_name"]},
                        {"$inc": {"total_questions": +1}}
                    )

            students = mongo.db.students.find()
            for student in students:
                mongo.db.students.update_one(
                    {"userId": student["userId"]},
                    {"$addToSet": {"questions_unanswered": question["_id"]}}
                )

            flash("question successfully added")
            return redirect(url_for("profile", user=session["user"]))

        return render_template("add_question.html", modules=modules)
    else:
        return render_template("no_premission.html")


@app.route("/edit_question/<question_id>", methods=["GET", "POST"])
def edit_question(question_id):
    """
    Function that edits the database based on how the user wishes
    to edit the question
    """
    if "user" not in session:
        return render_template("not_user.html")
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
    """
    Function that deletes question and removes the corresponding
    values form the database
    """
    question = mongo.db.questions.find_one({"_id": ObjectId(question_id)})
    mongo.db.modules.update_one(
            {"module_name": question["module_name"]},
            {"$inc": {"total_questions": -1}}
        )
    students = mongo.db.students.find()
    for student in students:
        mongo.db.students.update_one(
            {"userId": student["userId"]},
            {"$pull": {"questions_unanswered": question["_id"]}}
        )
    mongo.db.questions.remove({"_id": ObjectId(question_id)})
    flash("Question has been deleted")
    return redirect(url_for("profile", user=session["user"]))


@app.route("/module/<module_name>")
def module(module_name):
    """
    Function that allows the users an additonal option to filter
    the questions by module rather than search for a specific
    question
    """
    if "user" not in session:
        return render_template("not_user.html")
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    student = mongo.db.students.find_one(
        {"userId": user["_id"]}
    )
    questions = list(mongo.db.questions.find(
        {"module_name": module_name}
    ))
    modules = mongo.db.modules.find()
    return render_template(
        "module.html",
        user=user,
        questions=questions,
        student=student,
        modules=modules,
        mod_name=module_name
        )


@app.route("/manage_modules")
def manage_modules():
    """
    Function that creates a page that allows an
    admin user to add or remove modules
    """
    if "user" not in session:
        return render_template("not_user.html")
    user_type = mongo.db.users.find_one(
        {"username": session["user"]}
    )["user_type"]
    if user_type == "admin":
        modules = mongo.db.modules.find()
        return render_template("manage_modules.html", modules=modules)
    else:
        return render_template("no_premission.html")


@app.route("/add_module", methods=["GET", "POST"])
def add_module():
    """
    Function that adds a module to the database"
    """
    if "user" not in session:
        return render_template("not_user.html")
    user_type = mongo.db.users.find_one(
        {"username": session["user"]}
    )["user_type"]
    if user_type == "admin":
        if request.method == "POST":
            module = {
                "module_name": request.form.get("module_name").lower(),
                "total_questions": 0
            }
            mongo.db.modules.insert_one(module)
            return redirect(url_for("manage_modules"))

        return render_template("add_module.html")
    else:
        return render_template("no_premission.html")


@app.route("/edit_module/<module_id>", methods=["GET", "POST"])
def edit_module(module_id):
    """
    Function that edits a module and it's values in the database
    """
    if "user" not in session:
        return render_template("not_user.html")
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
    """
    Function that deletes a module from the database. This function
    needs updating so all the questions assocciated with a module
    are transferred to a different module when a module is deleted.
    However the physics cirriculuum rarely changes so a moudle will
    very rarely need deleting
    """
    mongo.db.modules.remove({"_id": ObjectId(module_id)})
    flash("Module deleted successfully")
    return redirect(url_for("manage_modules"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Function that add's a new user to the database and directs them
    to thier profile page
    """
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
        mongo.db.classes.update_one(
                {"class_name": new_user["class"]},
                {"$addToSet": {"member_names": new_user["username"]}}
            )

        if new_user["user_type"] == "student":
            questions = mongo.db.questions.find()
            question_ids = []
            for question in questions:
                question_ids.append(question["_id"])

            student = {
                "userId": new_user["_id"],
                "username": new_user["username"],
                "first_name": request.form.get("first_name").lower(),
                "surname": request.form.get("surname").lower(),
                "class": request.form.get("class"),
                "questions_answered": 0,
                "questions_correct": 0,
                "percentage_correct": 0.0,
                "current_grade": 4,
                "questions_unanswered": question_ids,
                "questions_correct_id": [],
                "questions_incorrect_id": []
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
        return redirect(url_for("profile", user=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Function that allows user to log in
    """
    if request.method == "POST":
        input_name = request.form.get("username").lower()
        existing_user = mongo.db.users.find_one({"username": input_name})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = input_name
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
    """
    function that allows user to logout
    """
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
