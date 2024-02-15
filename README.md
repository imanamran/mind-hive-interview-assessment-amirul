# DESCRIPTION


# INSTALLATION & SETUP

BACKEND: Django, MongoDB, OpenAI
1. Create a python virtual environment (Optional)
    - `python3 -m venv mindhive` 
    - `source mindhive/bin/activate`

2. Install libraries mindhive/requirements.txt
    - `pip install -r requirements.txt`

3.  Start Django mindhive/api
    - Export MongoDB and OpenAI KEY
    - `python3 manage.py runserver`

FRONTEND: React.js
1. Install node module 
    - Root directory
    - `npm install` 

2. Start frontend
    - `npm start`

# METHODOLOGY

A. Scrapping
1. view-source:https://subway.com.my/find-a-subway
    
2. Fields:
    - Filter by “Kuala Lumpur” and get;
    - Name
    - Address
    - Operating Hours
    - Waze link
    - Geocoding
    
3. Save as JSON
    - In mindhive/scraper/scraper/spiders directory
    - `scrapy runspider ietf.py -o output.json`

4. Store to MongoDB

B. Build API using Django

C. Develop frontend using React.js
- Framework
-- turf.js
-- leaflet.js
-- web-vitals