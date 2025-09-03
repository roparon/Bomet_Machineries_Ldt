from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Product
from ..extensions import db

admin = Blueprint("admin", __name__)

@admin.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    if current_user.role != "admin":
        flash("Unauthorized!", "danger")
        return redirect(url_for("shop.home"))

    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        product = Product(
            name=name,
            description="Default description",
            price=price,
            category="General",
            stock=10
        )
        db.session.add(product)
        db.session.commit()
        flash("Product added successfully!", "success")
        return redirect(url_for("shop.home"))

    return render_template("add_product.html")
