from flask import Flask
from flask import send_file
from flask import make_response
import io, csv

app = Flask(__name__)

@app.route("/")
def default():
    return "Server 1!"

@app.route("/download")
def download():
    dest = io.StringIO()
    writer = csv.writer(dest)

    writer.writerow(['Name', 'Profession'])
    writer.writerow(['Derek', 'Software Developer'])
    writer.writerow(['Steve', 'Software Developer'])
    writer.writerow(['Paul', 'Manager'])
    output = make_response(dest.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)