from application import app, db, login_manager
from flask import redirect, render_template, request, url_for
from application.memos.models import Memo
from application.memos.forms import MemoForm
from application.categories.models import Category
from flask_login import login_required, current_user

@app.route("/memos", methods=["GET"])
def memos_index():
    return render_template("memos/list.html", memos = Memo.query.all())

@app.route("/memos/<memo_id>/", methods=["GET"])
@login_required
def memos_show_one(memo_id):
    return render_template("memos/list.html", memos = Memo.query.get(memo_id))   

@app.route("/memos/delete/<memo_id>/", methods=["POST"])
@login_required
def memos_delete_one(memo_id):
    if current_user.role_id != 0:
        return login_manager.unauthorized()
    Memo.delete_memo(memo_id)
    return render_template("memos/list.html", memos = Memo.query.all())

@app.route("/memos/new/")
@login_required
def memos_form():
    return render_template("/memos/new.html", form = MemoForm())

@app.route("/memos/<memo_id>/", methods=["POST"])
@login_required
def memos_add_importance(memo_id):

    m = Memo.query.get(memo_id)
    m.importance = m.importance + 1
    db.session().commit()
  
    return redirect(url_for("memos_index"))

@app.route("/memos/", methods=["POST"])
@login_required
def memos_create():
    form = MemoForm(request.form)
    if not form.validate():
        return render_template("memos/new.html", form = form)

    m = Memo(form.name.data)
    m.account_id = current_user.id

    db.session().add(m)
    db.session().commit()
  
    return redirect(url_for("memos_index"))