from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

meetings = [
    
]

@app.route('/')
def index():
    return render_template('index.html', meetings=meetings)

@app.route('/add_meeting', methods=['POST'])
def add_meeting():
    new_meeting = {
        "id": len(meetings) + 1,
        "topic": request.form.get('topic'),
        "date": request.form.get('date'),
        "start_time": request.form.get('start_time'),
        "end_time": request.form.get('end_time'),
        "participants": request.form.get('participants').split(',')
    }
    meetings.append(new_meeting)
    return jsonify({"status": "success"})

@app.route('/update_meeting/<int:meeting_id>', methods=['PUT'])
def update_meeting(meeting_id):
    meeting = next((m for m in meetings if m['id'] == meeting_id), None)
    if meeting:
        meeting.update(request.json)
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "error", "message": "Meeting not found"})

@app.route('/delete_meeting/<int:meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    global meetings
    meetings = [m for m in meetings if m['id'] != meeting_id]
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
