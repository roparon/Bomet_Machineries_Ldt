from app.extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), default="customer")  # "customer", "admin"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship("Order", back_populates="user", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(200))  # can store static path
    category = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order_items = db.relationship("OrderItem", back_populates="product", lazy=True)

    def __repr__(self):
        return f"<Product {self.name} - {self.price}>"




class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Pending")  # Pending, Paid, Shipped, Delivered
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship("User", back_populates="orders")
    order_items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order {self.id} by User {self.user_id}>"



class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)  # store snapshot of product price at order time
    order = db.relationship("Order", back_populates="order_items")
    product = db.relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem {self.quantity} x {self.product_id}>"
