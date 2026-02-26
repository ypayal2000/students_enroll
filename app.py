from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}
courses = {
    "C1": {
        "course_name": "Python Basics",
        "max_students": 3,
        "enrolled_count": 0,
        "course_count": 0
    },
    "C2": {
        "course_name": "Data Structures",
        "max_students": 5,
        "enrolled_count": 0,
        "course_count": 0
    },
    "C3": {
        "course_name": "Web Development",
        "max_students": 7,
        "enrolled_count": 0,
        "course_count": 0
    }
}
enrolled_list = {}
enrolled_id = 100

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
            "enrolled_count": data["enrolled_count"]
        }
    return (response)

@app.route("/enroll", methods = ["POST"])
def enroll():
    global enrolled_id
    data = request.json
    course_id = data.get("course_id")
    student_id = data.get("student_id")

    if student_id not in students:
            return jsonify({"error":"student does not exist"}), 400

    if course_id not in courses:
        return jsonify({"error": "course not exist"}), 400

    for enrollment in enrolled_list.values():
        if enrollment["student_id"] == student_id and enrollment["course_id"] == course_id:
            return jsonify({"error": "student not enroll in same course twice"}), 400

    course = courses[course_id]
    if course["course_count"] >= course["max_students"]:
        return jsonify({"error": "course is full"}), 400

    enrolled_list[enrolled_id] = {
        "student_id": student_id,
        "course_id": course_id,
        "course_name": data["course_name"]
    }
    course["course_count"] += 1
    course["enrolled_count"] +=1
    enrolled_id +=1

    return jsonify({"status":"enrolled successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)