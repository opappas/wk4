import requests
import os

import requests

# NASA APOD API settings
# TODO 1: Get your key at: https://api.nasa.gov/
api_key = ""

date = "2006-12-14"
date = "2019-01-20"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"

# Request data
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    title = data.get("title", "NASA Astronomy Picture of the Day")
    explanation = data.get("explanation", "No description provided.")
    media_url = data.get("url")
    media_type = data.get("media_type", "image")
    author = data.get("copyright", "Public Domain")
    apod_date = data.get("date", date)

    # Image or video
    if media_type == "image":
        media_tag = f'<a href="{media_url}" target="_blank"><img src="{media_url}" alt="{title}" class="nasa-image"></a>'
    else:
        media_tag = f'<iframe src="{media_url}" height="200" allowfullscreen></iframe>'

    # HTML content with external CSS
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
    
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet"> 
        <link href="css/nasa.css" rel="stylesheet"> 

  </head>
    <body>
        <main>
        <div class="content">
            <h1>{title}</h1>
            <p class="meta">&#x1F5D3; Date: {apod_date}<br>
            <br>
               <span class="material-symbols-outlined"> attribution </span>

            Author: {author}</p>{media_tag}
            <p>{explanation}</p>
        </div>
        </main>
    </body>
    </html>
    """

    # Write the HTML file
    with open("nasa_apod2.html", "w", encoding="utf-8") as file:
        file.write(html)

    print("Webpage created: nasa_apod2.html")

else:
    print("Failed to fetch APOD. Check your API key or date.")
