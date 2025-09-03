from flask import Blueprint, render_template
from ..models import Product

shop = Blueprint("shop", __name__)


@shop.route("/")
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)
