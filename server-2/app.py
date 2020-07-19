from flask import Flask
import json
import time

app = Flask(__name__)

# dictionary with integer keys
pary_dict = {
    'Democratic-Republican': 'DR', 
    'Democrat': 'DEM', 'Whig': 'WH', 'Republican': 'REP', 
    'National Union': 'NU'
}

@app.route("/")
def default():
    return "Server 2!"

@app.route("/parse")
def parse():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return json.dumps(executeData(data));


def executeData(data):
    newData = [['Name', 'Party', 'Presendial Term', 'President Number', 'Ingestion Time']];
    # Iterate the data
    for unit in data:
        # Ignore the fedaralist party
        if (unit['pp'].find('Federalist') != -1):
            continue

        # Convert the first name backwards
        split = unit['nm'].split(" ")
        split[0] = split[0][::-1]
        name = " ".join(split);

        # Create the ingestion time
        ingestionTime = time.time()
        newData.append([
            name,
            # Set the acronym of the party name
            pary_dict[unit['pp']] if pary_dict[unit['pp']] != None else unit['pp'],
            unit['tm'],
            unit['president'],
            ingestionTime
        ])

    # TODO: Arrange alphabatically

    return newData

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)