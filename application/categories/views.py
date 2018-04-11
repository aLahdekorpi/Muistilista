from flask import render_template, request, redirect, url_for

from application import app, db
from application.categories.models import Category

@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all())