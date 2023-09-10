from flask import Flask
import datadog

app = Flask(__name__)
#datadog.initialize(api_key=d4111343-89c5-440a-baa0-a054430b909a)
@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
