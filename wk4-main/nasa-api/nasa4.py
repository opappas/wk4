import requests
from datetime import datetime

# NASA APOD API settings
api_key = ""

# Get today's month and day
today = datetime.today()
month_day = today.strftime("%m-%d")

entries = []

for offset in range(1, 11):  # last 10 years
    year = today.year - offset
    date = f"{year}-{month_day}"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        title = data.get("title", "NASA Astronomy Picture of the Day")
        explanation = data.get("explanation", "No description provided.")
        media_url = data.get("url")
        media_type = data.get("media_type", "image")
        apod_date = data.get("date", date)

        heading_id = f"title-{year}"

        # Only images work well for front of a flip-card
        if media_type == "image":
            entry_html = f"""
      <div class="apod-entry">
        <div class="apod-card">
          <div class="apod-front">
            <h2 id="{heading_id}">{title}</h2>
            <img src="{media_url}" alt="{title}">
          </div>
          <div class="apod-back">
            <p><strong>Date:</strong> {apod_date}</p>
            <p>{explanation}</p>
          </div>
        </div>
      </div>
            """
            entries.append(entry_html)
        else:
            # For video, just show title + iframe on front
            entry_html = f"""
      <div class="apod-entry">
        <div class="apod-card">
          <div class="apod-front">
            <h2 id="{heading_id}">{title}</h2>
            <iframe src="{media_url}" width="100%" height="200"
                    allowfullscreen "></iframe>
          </div>
          <div class="apod-back">
            <p><strong>Date:</strong> {apod_date}</p>
            <p>{explanation}</p>
          </div>
        </div>
      </div>
            """
            entries.append(entry_html)
    else:
        print(f"Failed to fetch APOD for {date}")

# Build full HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>NASA APOD Flip Cards</title>
  <link rel="stylesheet" href="css/nasa.css">
  <link rel="stylesheet" href="css/flipcards.css">
</head>
<body>
  <main>
    <h1>NASA Astronomy Picture of the Day - Flip Cards ({month_day})</h1>
    <div class="apod-grid">
      {''.join(entries)}
    </div>
  </main>
</body>
</html>
"""

with open("nasa4.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Webpage created: nasa4.html")
