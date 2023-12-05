from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    if request.method == 'POST':
        try:
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']

            if not city or not country:
                return jsonify({'error': 'Please enter both city and country.'})

            api_key = 'e5dccfe743f53b0389cd37b16b9b07ad'  
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}')
            data = response.json()

            if response.ok:
                temperature_celsius = round(data['main']['temp'] - 273.15)
                weather_details = {
                    'temperature': temperature_celsius,
                    'feels_like': round(data['main']['feels_like'] - 273.15),
                    'max_temp': round(data['main']['temp_max'] - 273.15),
                    'min_temp': round(data['main']['temp_min'] - 273.15),
                    'humidity': data['main']['humidity'],
                    'visibility': round(data['visibility'] / 1000, 2),
                    'wind_speed': data['wind']['speed'],
                    'sunrise': data['sys']['sunrise'],
                    'sunset': data['sys']['sunset'],
                    'weather_main': data['weather'][0]['main'],
                    'weather_description': data['weather'][0]['description'],
                    'weather_icon': data['weather'][0]['icon']
                }
                print(weather_details)
                return render_template('weather.html', **weather_details)
            else:
                return render_template('home.html', error=data['message'])

        except Exception as e:
            return jsonify({'error': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
