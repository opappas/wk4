import requests
from datetime import datetime

# NASA APOD API settings
api_key = ""

# Get today's month and day
today = datetime.today()
month_day = today.strftime("%m-%d")

# Collect HTML for all years
apod_entries = []

for year_offset in range(1, 11):  # past 10 years
    year = today.year - year_offset
    date = f"{year}-{month_day}"

    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
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
            media_tag = f'<iframe src="{media_url}" width="100%" height="500" allowfullscreen></iframe>'

        # Single entry block
        entry_html = f"""
        <div class="apod-entry">
            <h2>{title}</h2>
            <p class="meta">&#x1F5D3; Date: {apod_date}<br>
            <br>
               <span class="material-symbols-outlined"> attribution </span>

            Author: {author}</p>{media_tag}
            <p>{explanation}</p>
        </div>
        """
        apod_entries.append(entry_html)
    else:
        print(f"Failed to fetch APOD for {date}")

# Combine into full HTML page
html = f"""
 <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>NASA API - Past 10 years</title>
    
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet"> 
        <link href="css/nasa.css" rel="stylesheet"> 

  </head>
<body>
    <main>
    <h1>NASA Astronomy Pictures of the Day - Past 10 Years ({month_day})</h1>
     <div class="apod-grid">
        {''.join(apod_entries)}
    </div>
    </main>
</body>
</html>
"""

# Write the HTML file
with open("nasa_apod3.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Webpage created: nasa_apod3.html")
