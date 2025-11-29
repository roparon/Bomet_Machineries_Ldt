from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models import Product
from datetime import datetime


shop = Blueprint("shop", __name__)

products = [
    {"id": 1, "name": "Electric Motor 5HP", "category": "motors", "price": 15000, "image": "/static/images/motor1.jpg"},
    {"id": 2, "name": "Honda Generator 3kVA", "category": "generators", "price": 45000, "image": "/static/images/generator1.jpg"},
    {"id": 3, "name": "Posho Mill Grade 1", "category": "posho_mills", "price": 80000, "image": "/static/images/posho1.jpg"},
    {"id": 4, "name": "Water Pump 2HP", "category": "water_pumps", "price": 12000, "image": "/static/images/pump1.jpg"},
]
@shop.route("/")
def home():
    categorized_products = {}
    for product in products:
        category = product["category"]
        if category not in categorized_products:
            categorized_products[category] = []
        categorized_products[category].append(product)

    return render_template(
        "index.html",
        categorized_products=categorized_products,
        current_year=datetime.now().year,
        cart_count=len(session.get("cart", []))
    )


@shop.route("/search")
def search():
    query = request.args.get("query", "").lower()
    search_results = [p for p in Product if query in p["name"].lower()]
    return render_template(
        "index.html",
        categorized_products={"Search Results": search_results},
        current_year=datetime.now().year,
        cart_count=len(session.get("cart", []))
    )

@shop.route("/category/<category>")
def category(category):
    filtered_products = [p for p in products if p["category"] == category]

    return render_template(
        "index.html",
        categorized_products={category: filtered_products},
        current_year=datetime.now().year,
        cart_count=len(session.get("cart", []))
    )
@shop.route("/product/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return render_template("404.html"), 404  
    return render_template(
        "product_detail.html",
        product=product,
        current_year=datetime.now().year,
        cart_count=len(session.get("cart", []))
    )
@shop.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get("cart", [])
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    cart.append(product)
    session["cart"] = cart
    return redirect(url_for("shop.view_cart")) 
@shop.route("/cart")
def view_cart():
    cart = session.get("cart", [])
    total_price = sum(item["price"] for item in cart)
    return render_template(
        "cart.html",
        cart=cart,
        total_price=total_price,
        current_year=datetime.now().year,
        cart_count=len(cart)
    )