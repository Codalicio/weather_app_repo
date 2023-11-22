from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def show_home_page():
    return render_template('index.html')

@app.route("/weather_app", methods=['POST', 'GET'])
def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q' : request.form.get('city'),
        'appid' : '6b0c76cc3196d0e2c8ed090eb2ccaa1c',
        'units' : 'metric'
    }
    response = requests.get(url, params=param)
    data = response.json()
    city = data['name']
    return f"Data : {data}, city : {city}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)