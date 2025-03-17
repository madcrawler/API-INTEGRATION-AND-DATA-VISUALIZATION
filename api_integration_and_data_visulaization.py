import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "15509831c2590d405f247b6b8bda5ff6"
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    print("Weather data fetched successfully!")
except requests.exceptions.RequestException as e:
    print("API Request Error:", e)
    exit()

timestamps = [entry["dt_txt"] for entry in data["list"]]
temperatures = [entry["main"]["temp"] for entry in data["list"]]
humidity = [entry["main"]["humidity"] for entry in data["list"]]
wind_speed = [entry["wind"]["speed"] for entry in data["list"]]

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
sns.lineplot(x=timestamps, y=temperatures, marker="o", color="red")
plt.xticks(rotation=45)
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast for {CITY} - Temperature")
plt.grid()

plt.subplot(3, 1, 2)
sns.lineplot(x=timestamps, y=humidity, marker="o", color="blue")
plt.xticks(rotation=45)
plt.ylabel("Humidity (%)")
plt.title(f"Weather Forecast for {CITY} - Humidity")
plt.grid()

plt.subplot(3, 1, 3)
sns.lineplot(x=timestamps, y=wind_speed, marker="o", color="green")
plt.xticks(rotation=45)
plt.ylabel("Wind Speed (m/s)")
plt.title(f"Weather Forecast for {CITY} - Wind Speed")
plt.grid()

plt.tight_layout()
plt.show()
