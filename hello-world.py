from flask import Flask, render_template

app = Flask(__name__)

# Initialize a visitor counter
visitor_count = 0

@app.route('/')
def index():
    global visitor_count
    visitor_count += 1
    return render_template('index.html', count=visitor_count)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
