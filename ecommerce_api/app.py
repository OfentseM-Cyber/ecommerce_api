# --- SAMPLE USER DATA ---
users = []
{
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "password": "hashed_password_here"
}

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# --- SAMPLE PRODUCT DATA ---
products = []

# --- HOME ROUTE ---
@app.route('/')
def home():
    return {"message": "E-commerce API is running!"}

# --- PRODUCT RESOURCE ---
class ProductList(Resource):
    def get(self):
        return {"products": products}

    def post(self):
        data = request.get_json()
        product = {
            "id": len(products) + 1,
            "name": data.get("name"),
            "price": data.get("price")
        }
        products.append(product)
        return product, 201
    
    from flask import jsonify

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Check if user already exists
        if any(user["email"] == email for user in users):
            return {"message": "User already exists"}, 400

        user = {
            "id": len(users) + 1,
            "username": username,
            "email": email,
            "password": generate_password_hash(password)
        }
        users.append(user)
        return {"message": "User registered successfully"}, 201

# Register route
api.add_resource(Register, "/api/auth/register")


# Register route
api.add_resource(ProductList, "/api/products")

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = next((u for u in users if u["email"] == email), None)
        if user and check_password_hash(user["password"], password):
            return {"message": "Login successful", "user": {"id": user["id"], "username": user["username"], "email": user["email"]}}, 200
        return {"message": "Invalid email or password"}, 401

# Register route
api.add_resource(Login, "/api/auth/login")

if __name__ == "__main__":
    app.run(debug=True)
