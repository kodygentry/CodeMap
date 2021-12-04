from flask import Flask
import json
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
GoogleMaps(app, key="my-key")


@app.route('/', methods=["GET"])
def my_map():
    mymap = Map(
                identifier="view-side",
                varname="mymap",
                style="height:720px;width:1100px;margin:0;", # hardcoded!
                lat=37.4419, # hardcoded!
                lng=-122.1419, # hardcoded!
                zoom=15,
                markers=[(37.4419, -122.1419)] # hardcoded!
            )

    return render_template('index.html', mymap=mymap)


def search():
    # Absolute path to the static directory within your Pycharm Flask app. Be sure to put 'all_locations_all_jobtypes.json' in the static folder 
    f = open('/Users/riemannhypothesis/PycharmProjects/CodeMap_FlaskApp/static/all_locations_all_jobtypes.json')
    jobs_lst = json.loads(f.read())

    for dictionary in jobs_lst:
        for key, value in dictionary.items():
            print(key + ": " + value)
        print()
search()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
