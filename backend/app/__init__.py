from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.getenv("DATABASE_PATH", "livestock.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tag TEXT UNIQUE NOT NULL,
            species TEXT NOT NULL,
            breed TEXT,
            age INTEGER
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_id INTEGER,
            temperature REAL,
            notes TEXT,
            observed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_id INTEGER,
            message TEXT,
            status TEXT DEFAULT 'New'
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS vaccinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_id INTEGER,
            vaccine_name TEXT,
            vaccination_date TEXT
        )
    """)

    conn.commit()
    conn.close()


create_tables()


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/api/animals", methods=["GET", "POST"])
def animals():
    conn = get_db()

    if request.method == "GET":
        data = conn.execute("SELECT * FROM animals").fetchall()
        conn.close()
        return jsonify([dict(row) for row in data])

    data = request.get_json() or {}

    if not data.get("tag") or not data.get("species"):
        conn.close()
        return jsonify({"error": "Tag and species are required"}), 400

    try:
        conn.execute(
            "INSERT INTO animals (tag, species, breed, age) VALUES (?, ?, ?, ?)",
            (data["tag"], data["species"], data.get("breed"), data.get("age"))
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Animal registered successfully"}), 201

    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Animal tag already exists"}), 409


@app.route("/api/animals/<int:animal_id>/observations", methods=["GET", "POST"])
def observations(animal_id):
    conn = get_db()

    if request.method == "GET":
        data = conn.execute(
            "SELECT * FROM observations WHERE animal_id = ?", (animal_id,)
        ).fetchall()
        conn.close()
        return jsonify([dict(row) for row in data])

    data = request.get_json() or {}
    temperature = data.get("temperature")
    notes = data.get("notes", "")

    animal = conn.execute(
        "SELECT id FROM animals WHERE id = ?", (animal_id,)
    ).fetchone()

    if animal is None:
        conn.close()
        return jsonify({"error": "Animal not found"}), 404

    conn.execute(
        "INSERT INTO observations (animal_id, temperature, notes) VALUES (?, ?, ?)",
        (animal_id, temperature, notes)
    )

    if temperature is not None and float(temperature) > 39.5:
        conn.execute(
            "INSERT INTO alerts (animal_id, message) VALUES (?, ?)",
            (animal_id, "High temperature - fever risk")
        )

    conn.commit()
    conn.close()
    return jsonify({"message": "Observation recorded successfully"}), 201


@app.route("/api/alerts", methods=["GET"])
def get_alerts():
    conn = get_db()
    data = conn.execute("SELECT * FROM alerts").fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])


@app.route("/api/alerts/<int:alert_id>/acknowledge", methods=["POST"])
def acknowledge_alert(alert_id):
    conn = get_db()
    result = conn.execute(
        "UPDATE alerts SET status = 'Acknowledged' WHERE id = ?",
        (alert_id,)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({"error": "Alert not found"}), 404

    return jsonify({"message": "Alert acknowledged"})


@app.route("/api/animals/<int:animal_id>/vaccinations", methods=["GET", "POST"])
def vaccinations(animal_id):
    conn = get_db()

    if request.method == "GET":
        data = conn.execute(
            "SELECT * FROM vaccinations WHERE animal_id = ?", (animal_id,)
        ).fetchall()
        conn.close()
        return jsonify([dict(row) for row in data])

    data = request.get_json() or {}

    if not data.get("vaccine_name") or not data.get("vaccination_date"):
        conn.close()
        return jsonify({"error": "Vaccine name and date are required"}), 400

    conn.execute(
        """INSERT INTO vaccinations
        (animal_id, vaccine_name, vaccination_date)
        VALUES (?, ?, ?)""",
        (animal_id, data["vaccine_name"], data["vaccination_date"])
    )

    conn.commit()
    conn.close()
    return jsonify({"message": "Vaccination recorded successfully"}), 201


@app.route("/api/dashboard")
def dashboard():
    conn = get_db()

    animal_count = conn.execute(
        "SELECT COUNT(*) FROM animals"
    ).fetchone()[0]

    alert_count = conn.execute(
        "SELECT COUNT(*) FROM alerts WHERE status = 'New'"
    ).fetchone()[0]

    vaccination_count = conn.execute(
        "SELECT COUNT(*) FROM vaccinations"
    ).fetchone()[0]

    conn.close()

    return jsonify({
        "total_animals": animal_count,
        "new_alerts": alert_count,
        "total_vaccinations": vaccination_count
    })


if __name__ == "__main__":
    app.run(debug=True)