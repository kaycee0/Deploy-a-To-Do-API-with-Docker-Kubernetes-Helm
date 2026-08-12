from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = {}
next_id = 1

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values()))

@app.route("/task", methods=["POST"])
def add_task():
    global next_id
    data = request.get_json()
    task = {"id": next_id, "title": data["title"], "done": False}
    tasks[next_id] = task
    next_id += 1
    return jsonify(task), 201

@app.route("/task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "not found"}), 404
    del tasks[task_id]
    return "", 204

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)