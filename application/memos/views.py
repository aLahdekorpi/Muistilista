from application import app, db
from flask import redirect, render_template, request, url_for
from application.memos.models import Memo

@app.route("/memos", methods=["GET"])
def memos_index():
    return render_template("memos/list.html", memos = Memo.query.all())

@app.route("/memos/new/")
def memos_form():
    return render_template("/memos/new.html")

@app.route("/memos/<memo_id>/", methods=["POST"])
def memos_add_importance(memo_id):

    m = Memo.query.get(memo_id)
    m.importance = m.importance + 1
    db.session().commit()
  
    return redirect(url_for("memos_index"))

@app.route("/memos/", methods=["POST"])
def memos_create():
    m = Memo(request.form.get("name"))

    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("memos_index"))