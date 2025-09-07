from flask import Flask, request, jsonify

from pymongo import MongoClient

# Create Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

# -------------------------------
# Option 1: Home Route
# -------------------------------
@app.route("/")
def home():
    return """
    <h1>Welcome to the To-Do App</h1>
    <p>Go to <a href='/todo'>/todo</a> to submit items.</p>
    """

# -------------------------------
# Option 2: To-Do Form Page
# -------------------------------
@app.route("/todo")
def todo_page():
    return """
    <h2>Submit a To-Do Item</h2>
    <form id="todoForm">
      <label>Item Name:</label><br>
      <input type="text" id="itemName" name="itemName" required><br><br>
      <label>Item Description:</label><br>
      <textarea id="itemDescription" name="itemDescription" required></textarea><br><br>
      <button type="submit">Submit</button>
    </form>

    <script>
    document.getElementById("todoForm").addEventListener("submit", async function(e) {
        e.preventDefault();
        const itemName = document.getElementById("itemName").value;
        const itemDescription = document.getElementById("itemDescription").value;

        const response = await fetch("/submittodoitem", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({itemName, itemDescription})
        });

        const result = await response.json();
        alert(result.message);
    });
    </script>
    """

# -------------------------------
# Backend API Route
# -------------------------------
@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get("itemName", "").strip()
    item_description = data.get("itemDescription", "").strip()

    if not item_name or not item_description:
        return jsonify({"status": "error", "message": "Missing fields"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"status": "success", "message": "Item added successfully!"}), 201

# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
