from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
courses = {
    101: {
        "course_name": "Python Basics",
        "max_students": 3,
        "enrolled_students": []
    },
    201: {
        "course_name": "Data Structures",
        "max_students": 5,
        "enrolled_students": []
    },
    301: {
        "course_name": "Web Development",
        "max_students": 7,
        "enrolled_students": []
    }
}
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

@app.route("/courses", methods=["GET"])
def get_courses():
    response = {}
    for course_id, data in courses.items():
        response[course_id]={
            "course_name": data["course_name"],
            "max_students": data["max_students"],
            "enrolled_students": data["enrolled_students"]
        }
    return (response)


if __name__ == '__main__':
    app.run(debug=True)