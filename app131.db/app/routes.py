from app import myapp_obj
from flask import render_template
from flask import redirect,request
from app.forms import LoginForm
from app.forms import RecipeForm
from app.models import User
from app.models import RecipeTable
from app import db
# from <X> import <Y>

@myapp_obj.route("/")
def main():
    name = "Maria"
    return render_template("hello.html", name = name)

@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)
    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))

@myapp_obj.route("/recipe")
def recipe():
    recipes = RecipeTable.query.all()
    return render_template("recipelist.html", recipes=recipes)

@myapp_obj.route("/recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    recipe = RecipeTable.query.get_or_404(recipe_id)
    return render_template("viewrecipe.html", recipe=recipe)

@myapp_obj.route("/recipe/<int:recipe_id>/delete", methods=['POST'])
def delete_recipe(recipe_id):
    recipe = RecipeTable.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect("/recipe")
