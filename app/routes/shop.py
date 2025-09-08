from flask import Blueprint, render_template
from app.models import Product 

shop = Blueprint("shop", __name__)

@shop.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)
