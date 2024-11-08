# Weather App API

A simple weather app that fetches real-time weather data for a user-specified city using the OpenWeather API. The app displays current temperature, "feels like" temperature, wind speed and direction, and a brief weather description.

## Features
- **Real-time weather data**: Retrieves the latest weather data for any city entered by the user.
- **Detailed weather info**: Shows temperature, feels-like temperature, wind speed (in m/s), wind direction, and weather conditions.
- **Error handling**: Provides clear error messages when the city is not found or data cannot be fetched.

## Technologies Used
- **Python**: Main programming language for the app.
- **OpenWeather API**: Data source for the current weather conditions.

## Clone This GitHub and Run

1. **Install Required Library**:

  - This app requires the `requests` library. Install it using:
      ```bash
      pip install requests
      ```

3. **Clone the repository**:
    ```bash
    git clone https://github.com/sushan64/Weather-app-api.git
    cd Weather-app-api
    python main.py
    ```

## You can also run

1. **Install Required Library**:
 - This app requires the `requests` library. Install it using:
      ```bash
      pip install requests
      ```

3. **Get an OpenWeather API Key**:
    - Sign up on [OpenWeather](https://openweathermap.org/api) to obtain a free API key.

4. **Replace API Key**:
    - Open the code file and replace the `appid` parameter in the URL with your own API key:
      ```python
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid=YOUR_API_KEY"
      ```

5. **Run the App**:
    - Run the app using:
      ```bash
      python app.py
      ```
6. **Enter Your Open Weather API**

5. **Enter a City**:
    - When prompted, enter the name of the city you want the weather information for.

## Usage Example

After entering a city name, you’ll receive a detailed weather report:

```plaintext
Enter City Name: Kathmandu
City: Kathmandu
Temperature: 24°C
Feel Like: 26°C
Wind Speed: 10.8 m/s
Wind Degree: 120°
Weather: clear sky
```

## Error Handling
If there’s an error (e.g., city not found), the app will display a message like:

```plaintext
Error: city not found
```

## License
This project is licensed under the MIT License.
