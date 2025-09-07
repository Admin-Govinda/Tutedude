from flask import jsonify

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    try:
        data = request.get_json()

        item_name = data.get("itemName")
        item_description = data.get("itemDescription")

        if not item_name or not item_description:
            return jsonify({"status": "error", "message": "Missing fields"}), 400

        # Insert into MongoDB
        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })

        return jsonify({"status": "success", "message": "Item added successfully!"}), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
