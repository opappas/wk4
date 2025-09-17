import requests

# NASA APOD API settings
# TODO 1: Get your key at: https://api.nasa.gov/
api_key = ""

date = "2006-12-14"

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
# print(url) # Uncomment for API request check

# Request data from NASA
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    title = data.get("title", "NASA Astronomy Picture of the Day")
    explanation = data.get("explanation", "No description provided.")
    media_url = data.get("url")
    media_type = data.get("media_type", "image")  # could be "video"
    copyright = data.get("copyright", "Public Domain")
    print(title)
    print(explanation)
    print(media_url)
    print(media_type)
    print(copyright)
else:
    print("Fail")