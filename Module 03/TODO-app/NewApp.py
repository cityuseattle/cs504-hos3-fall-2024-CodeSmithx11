from flask import Flask, request, jsonify, Response
import json  # Importing JSON for advanced JSON handling

app = Flask(__name__)

# In-memory to-do list storage
to_do_list = {}

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Create a new task.
    """
    data = request.get_json()
    task_name = data.get("name")
    task_status = data.get("status", "TO DO")
    
    if task_name in to_do_list:
        # Custom error response using json.dumps
        error_response = {"error": "Task already exists"}
        return Response(json.dumps(error_response), status=400, mimetype='application/json')

    to_do_list[task_name] = task_status
    # Returning a success message using jsonify
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Retrieve all tasks.
    """
    print("Data being returned:", json.dumps(to_do_list, indent=2))  # Logging tasks as JSON to the console
    return jsonify(to_do_list), 200

@app.route('/tasks/<task_name>', methods=['PUT'])
def update_task(task_name):
    """
    Update a task's status.
    """
    if task_name not in to_do_list:
        # Custom error response using json.dumps
        error_response = {"error": "Task not found"}
        return Response(json.dumps(error_response), status=404, mimetype='application/json')

    data = request.get_json()
    new_status = data.get("status", "TO DO")
    to_do_list[task_name] = new_status
    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/tasks/<task_name>', methods=['DELETE'])
def delete_task(task_name):
    """
    Delete a task.
    """
    if task_name not in to_do_list:
        # Custom error response using json.dumps
        error_response = {"error": "Task not found"}
        return Response(json.dumps(error_response), status=404, mimetype='application/json')

    del to_do_list[task_name]
    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/debug', methods=['GET'])
def debug_tasks():
    """
    Debug route to view tasks in JSON format.
    """
    # Pretty-print the tasks with json.dumps
    return Response(json.dumps(to_do_list, indent=2), mimetype='application/json')

