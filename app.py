from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
courses = {}
enrolled_list = {}

@app.route("/student", methods=["POST"])
def add_student():
    data = request.json

    student_id = data.get("student_id")
    student_age = data.get("student_age")
    student_mail = data.get("student_mail")
    student_name = data.get("student_name")

    for student in students.values():
        if student["student_mail"] == student_mail:
            return jsonify({"error":"email already register"}), 400
    
    if student_age < 16:
        return jsonify({"error":"student must be greater than 16"}), 400
    
    students[student_id] = {
        "student_name": student_name,
        "student_age": student_age,
        "student_mail": student_mail
    }

    return jsonify({"status":"student added sucessfully"}), 201

@app.route("/student", methods=["GET"])
def get_students():
    response = {}
    for student_id, data in students.items():
        response[student_id] = {
            "student_name": data["student_name"],
            "student_age": data["student_age"],
            "student_mail": data["student_mail"]
        }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)