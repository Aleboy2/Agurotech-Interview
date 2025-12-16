from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

# In-memory storage for tasks
tasks = {}

def validate_task_data(data, is_update=False):
    """Validate task data"""
    errors = []
    
    if not is_update:
        if not data.get('title'):
            errors.append('Title is required')
        if not data.get('description'):
            errors.append('Description is required')
    
    if 'status' in data:
        if data['status'] not in ['todo', 'in_progress', 'done']:
            errors.append('Status must be todo, in_progress, or done')
    
    if 'priority' in data:
        if data['priority'] not in ['low', 'medium', 'high']:
            errors.append('Priority must be low, medium, or high')
    
    return errors

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks with optional status filter"""
    status_filter = request.args.get('status')
    
    if status_filter:
        filtered_tasks = {k: v for k, v in tasks.items() if v['status'] == status_filter}
        return jsonify(list(filtered_tasks.values())), 200
    
    return jsonify(list(tasks.values())), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    errors = validate_task_data(data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    task_id = str(uuid.uuid4())
    task = {
        'id': task_id,
        'title': data['title'],
        'description': data['description'],
        'status': data.get('status', 'todo'),
        'priority': data.get('priority', 'medium'),
        'created_at': datetime.utcnow().isoformat()
    }
    
    tasks[task_id] = task
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task"""
    task = tasks.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify(task), 200

@app.route('/tasks/<task_id>', methods=['PATCH'])
def update_task(task_id):
    """Update task status or other fields"""
    task = tasks.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    errors = validate_task_data(data, is_update=True)
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Update allowed fields
    if 'title' in data:
        task['title'] = data['title']
    if 'description' in data:
        task['description'] = data['description']
    if 'status' in data:
        task['status'] = data['status']
    if 'priority' in data:
        task['priority'] = data['priority']
    
    tasks[task_id] = task
    return jsonify(task), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    del tasks[task_id]
    return jsonify({'message': 'Task deleted successfully'}), 200

@app.route('/')
def home():
    """Serve the frontend"""
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
