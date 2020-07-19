from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "Server 2!"

@app.route("/parse")
def parse():
    return "Parsing"
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)