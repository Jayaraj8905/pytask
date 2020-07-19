from flask import Flask
from flask import send_file
from flask import make_response
import requests
import io, csv
import json

app = Flask(__name__)

@app.route("/")
def default():
    return "Server 1!"

@app.route("/download")
def download():
    # Initialize the csv
    dest = io.StringIO()
    writer = csv.writer(dest)

    # Request the data from server
    r = requests.get("http://localhost:5002/parse")
    parsedData = json.loads(r.text)

    # Iterate and construct the data
    for data in parsedData:  
        writer.writerow([data[0], str(data[1]), data[2], data[3], data[4]])
    
    # Respond the data
    output = make_response(dest.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)