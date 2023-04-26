from flask import render_template, redirect

from flask import Blueprint


import repositories.book_repository as book_repo

tasks_blueprint = Blueprint("books", __name__)

@tasks_blueprint.route("/books")
def books ():
    books = book_repo.select_all()
    return render_template("books.jinja", books_to_display = books)

@tasks_blueprint.route('/books/delete/<id>', methods=['POST'])
def delete_book(id):
    book_repo.delete_by_id(int(id))
    return redirect('/books')

