from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://Well2025:Don2025W@cluster0.5z1lm5k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Cluster0"]           # Database name
collection = db["Well2025"]         # Collection name

# Route for form page
@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        try:
            # Get data from form
            name = request.form.get("name")
            email = request.form.get("email")

            # Validate input
            if not name or not email:
                error = "Please fill out all fields!"
                return render_template("form.html", error=error)

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            # Redirect to success page
            return redirect(url_for("success"))

        except Exception as e:
            error = f"Error: {str(e)}"
            return render_template("form.html", error=error)

    return render_template("form.html", error=error)

# Route for success page
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
