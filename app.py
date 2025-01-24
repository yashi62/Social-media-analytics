from flask import Flask, render_template, jsonify, request
from analytics import Analytics

app = Flask(__name__)
analytics = Analytics()

@app.route('/')
def dashboard():
    metrics = analytics.get_summary_metrics()
    return render_template('dashboard.html', metrics=metrics)

@app.route('/engagement', methods=['GET'])
def engagement():
    engagement_data = analytics.get_engagement_metrics()
    return jsonify(engagement_data)

@app.route('/content_performance', methods=['GET'])
def content_performance():
    performance_data = analytics.get_content_performance()
    return jsonify(performance_data)

@app.route('/user_activity', methods=['GET'])
def user_activity():
    activity_data = analytics.get_user_activity()
    return jsonify(activity_data)

if __name__ == "__main__":
    app.run(debug=True)
