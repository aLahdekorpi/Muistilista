from application import app, db, login_manager
from flask import redirect, render_template, request, url_for
from application.memos.models import Memo
from application.memos.forms import MemoForm
from application.categories.models import Category
from flask_login import login_required, current_user

@app.route("/memos", methods=["GET"])
def memos_index():
    memos = Memo.query.all()
    memos.sort(key=lambda Memo: Memo.importance, reverse = True)
    return render_template("memos/list.html", memos = memos, categories = Category.query.all())

@app.route("/memos/<memo_id>/", methods=["GET"])
@login_required
def memos_show_one(memo_id):
    return render_template("memos/one.html", memo = Memo.query.get(memo_id))   

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

@app.route("/memos/<memo_id>/add", methods=["POST"])
@login_required
def memos_add_importance(memo_id):

    m = Memo.query.get(memo_id)
    m.importance = m.importance + 1
    db.session().commit()
  
    return redirect(url_for("memos_index"))

@app.route("/memos/<memo_id>/sub", methods=["POST"])
@login_required
def memos_subtract_importance(memo_id):

    m = Memo.query.get(memo_id)
    if(m.importance > 0):
        m.importance = m.importance - 1
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

@app.route("/memos/edit/<memo_id>/", methods=["GET" ,"POST"])
@login_required
def memos_edit_one(memo_id):
    memoToEdit = Memo.query.filter_by(id=memo_id).first()  

    if request.method == "GET":
        return render_template("memos/edit.html", memo_id = memo_id, memoToEdit = memoToEdit, form = MemoForm())

    form = MemoForm(request.form)
    memoToEdit.name = form.name.data

    db.session.commit()

    return redirect(url_for("memos_index"))    