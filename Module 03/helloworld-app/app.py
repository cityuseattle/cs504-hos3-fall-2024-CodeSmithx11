from flask import Flask
from flask import request
import json

database = {}
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/students', methods=['POST'])
def post_students_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))  # Although redundant, keeping as-is
        if "name" not in dict_json or "age" not in dict_json:
            return 'Invalid input', 400
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object:", e)
        return 'Failed', 400

@app.route('/students', methods=['PUT'])
def put_students_details():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))  # Although redundant, keeping as-is
        if "name" not in dict_json or "age" not in dict_json:
            return 'Invalid input', 400
        database[dict_json["name"]] = dict_json["age"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object:", e)
        return 'Failed', 400

@app.route('/students/<Student_name>', methods=['GET'])
def get_students_details(Student_name):
    try:
        if Student_name not in database:
            return 'Record Not Found', 404
        name = database[Student_name]
        return 'Record Found: ' + Student_name + ' age is ' + str(name), 200
    except Exception as e:
        print("Error during fetching record:", e)
        return 'Failed to fetch record', 400

@app.route('/students/<Student_name>', methods=['DELETE'])
def delete_students_details(Student_name):
    try:
        if Student_name not in database:
            return 'Record Not Found', 404
        database.pop(Student_name)
        return 'Record deleted successfully', 200
    except Exception as e:
        print("Error while removing record:", e)
        return 'Error while removing record', 400
