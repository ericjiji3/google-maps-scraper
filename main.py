from src import Gmaps
from flask import Flask, render_template, Response, request, redirect, url_for, send_file
import os, shutil

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def json():
    if request.method == 'GET':
        query = []
        query = [request.values.get('query')]
        print(query)
        result = Gmaps.places(query)
        if os.path.isdir("output/" + query[0]):
            shutil.rmtree("output/" + query[0])
        return result
    return render_template('main.html')

@app.route("/background_process", methods=['GET', 'POST'])
def background_process():
    # print(request.values.get('searchQuery'))
    # query = [request.values.get('searchQuery')]
    # print(query)
    # Gmaps.places(query)
    # return send_file("output/all/csv/places-of-all.csv", as_attachment=True)
    query = request.args.get('query', None)
    Gmaps.places(query)
    return render_template()

# queries = [
#    "web developers in bangalore"
# ]

# Gmaps.places(queries, max=5)

