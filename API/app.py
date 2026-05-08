from flask import render_template
from flask import Flask

# 1. Initialize the app
app = Flask(__name__)

# 2. Define a route (The URL)
@app.route("/")
def home():
    # 3. Define the response (The content)
    return "<h1>Hello, Class!</h1><p>Welcome to your first Flask app.</p>"
@app.route("/greet/<name>")
def greet_user(name):
    return f"Hello, {name}! You are looking at a dynamic route."

@app.route("/report-card")
def report():
    student_data = {
        "name": "Alex",
        "subject": "Computer Science",
        "grade": "A+"
    }
    return render_template("index.html", student=student_data)

if __name__ == "__main__":
    app.run()

