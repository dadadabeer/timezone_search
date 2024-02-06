from flask import Flask, render_template, Response, request
from database import find_timezones

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/searchresults', methods=['GET'])
def search_results():
    city_query = request.args.get('city', '')
    if city_query:
        cities = find_timezones(city_query)  
        html = ''.join(f'<tr onclick="setTimezone(\'{city}\', \'{timezone}\')"><td>{city}</td><td>{country}</td>' for city, country, timezone in cities)  #just remove html for timezone in cp4
        return Response(html, mimetype='text/html')
    return Response('', mimetype='text/html')

if __name__ == '__main__':
    app.run()
