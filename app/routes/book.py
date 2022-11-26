from flask import Blueprint, render_template, flash, redirect, url_for
from app.forms import BookForm
from app.models.book import Book
from app.db import db


book_router = Blueprint("book_router", __name__)


@book_router.route("/crear", methods=['GET','POST'])
def create():
    book_form = BookForm()

    if book_form.validate_on_submit():
        new_book = Book(
        book_form.title.data,
        book_form.author.data,
        book_form.pages.data,
        book_form.publish_date.data,
        book_form.description.data,
        book_form.isbn.data
        )

        #insertar en la collection books
        db.books.insert_one(new_book.to_json())
        flash("Book created successfully","success")
        return redirect(url_for('book_router.index'))
    return render_template("create.html", book_form=book_form)