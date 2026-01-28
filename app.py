from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ.get("mysql.railway.internal"),
    user=os.environ.get("root"),
    password=os.environ.get("ZiJhZcWdzikRmvpOOFDysxPNYNClVUFW"),
    database=os.environ.get("railway"),
    port=os.environ.get("3306")
)

cursor = db.cursor()

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json

    sql = """INSERT INTO contact_messages
             (fullname, email, message)
             VALUES (%s, %s, %s)"""

    cursor.execute(sql, (
        data["fullname"],
        data["email"],
        data["message"]
    ))
    db.commit()

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run()
