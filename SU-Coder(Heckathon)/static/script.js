function getWeather() {
    const form = document.getElementById('weather-form');
    const formData = new FormData(form);

    fetch('/weather', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => displayWeather(data))
    .catch(error => console.error('Error:', error));
}

function displayWeather(weather) {
    const weatherInfo = document.getElementById('weather-info');
    
    if (weather.error) {
        weatherInfo.innerHTML = `<p>Error: ${weather.error}</p>`;
    } else {
        weatherInfo.innerHTML = `
            <p>Temperature: ${weather.temperature}°C</p>
            <p>Feels Like: ${weather.feels_like}°C</p>
            <p>Max Temperature: ${weather.max_temp}°C</p>
            <p>Min Temperature: ${weather.min_temp}°C</p>
            <p>Humidity: ${weather.humidity}%</p>
            <p>Visibility: ${weather.visibility} km</p>
            <p>Wind Speed: ${weather.wind_speed} m/s</p>
            <p>Sunrise: ${new Date(weather.sunrise * 1000).toLocaleTimeString()}</p>
            <p>Sunset: ${new Date(weather.sunset * 1000).toLocaleTimeString()}</p>
            <p>Main Weather: ${weather.weather_main}</p>
            <p>Weather Description: ${weather.weather_description}</p>
            <img src="http://openweathermap.org/img/w/${weather.weather_icon}.png" alt="Weather Icon">
        `;
    }
}
