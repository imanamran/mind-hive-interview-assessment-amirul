# Mindhive Interview Assessment by Amirul Iman bin Amran

LinkedIn: [Amirul Iman](https://www.linkedin.com/in/amirul-iman-a-905061179/)
GitHub: [Mind Hive Interview Assessment - Amirul](https://github.com/imanamran/mind-hive-interview-assessment-amirul/tree/main)

## Description
This assessment showcases an application combining web scraping, geospatial analysis, and AI-driven search functionalities.

It involves constructing a full-stack solution with a Django-powered backend and a React.js frontend, focusing on the efficient gathering, storage, and visualization of geospatial data from Subway outlets in Kuala Lumpur.

The project leverages technologies including MongoDB for data storage and leaflet.js for geospatial analysis and mapping, and OpenAI's gpt-4-turbo-preview model to enhance search capabilities.

## Installation & Setup

### Backend Setup

#### Prerequisites
- Python 3
- MongoDB
- OpenAI API Key

#### Steps
1. **Create a Python Virtual Environment (Optional but Recommended)**
- python3 -m venv mindhive_venv
- source mindhive_venv/bin/activate

2. **Install Required Libraries**
- Navigate to `mindhive/requirements.txt`.
- Run `pip install -r requirements.txt`.

3. **Start the Django Application**
- Export MongoDB URI and OpenAI API key as environment variables.
- Change directory to `mindhive/api` and run:
  ```
  export MONGO_CONNECTION_STRING="<MongoDB_URI>"
  export OPENAI_API_KEY="<OpenAI_API_Key>"
  python3 manage.py runserver
  ```

### Frontend Setup

#### Prerequisites
- Node.js and npm

#### Steps
1. **Install Node Modules**
- In the project root directory, run `npm install`.

2. **Start the Frontend Application**
- Run `npm start`.

## Methodology

### Part 1 & 2: Web Scraping, Database Storage & Geocoding
- **Target URL for Scraping**: `https://subway.com.my/find-a-subway`
- view-source:https://subway.com.my/find-a-subway to better understand the structure
- Example
```html
<div
    class="fp_listitem fp_list_marker2"
    data-latitude="3.128099"
    data-longitude="101.678678"
>
    <div class="location_left">
        <h4>Subway Menara UOA Bangsar</h4>
        <div class="infoboxcontent">
            <p>Jalan Bangsar Utama 1, Unit 1-2-G, Menara UOA Bangsar, Kuala Lumpur, 59000</p>
            <p></p>
            <p>Monday - Sunday, 8:00 AM - 8:00 PM</p>
            <p></p>
            <p class="infoboxlink">    
                <a href="/find-a-subway" title="Subway Menara UOA Bangsar">Find out more...</a>
            </p>                
        </div>        
        <div class="infopointer"></div>
    </div>
    <div class="location_right">    
        <div class="directionButton">
            <a target="_blank" href="https://goo.gl/maps/8n6W5Syy3vUAGeQV8">
                <i class="fa-solid fa-location-dot"></i>
            </a>
            <a target="_blank" href="https://www.waze.com/en/live-map/directions/my/federal-territory-of-kuala-lumpur/kuala-lumpur/subway-@-menara-uoa-bangsar?place=ChIJPWFRH5RJzDERvHvlO1uTQpY">
                <i class="fa-brands fa-waze"></i>
            </a>
        </div>
    </div>
</div>
```


- Scrape details such as name, address, operating hours, Waze link and geographical coordinates, in Kuala Lumpur ensuring pagination handling.
- Store the data in MongoDB with an appropriate schema.

### Part 3: API Development
- Develop a backend API using Django to serve outlet data.
- Establish MongoDB connection

### Part 4: Frontend Development and Visualization
- Create a React.js web application for visualizing outlets on a map.
- Implement a 5KM radius catchment visualization for each outlet and highlight intersections.
- Frameworks and Libraries
    - **leaflet.js**: For interactive mapping.
    - **web-vitals**: For measuring web vitals.

### Part 5: Enhanced Search Functionality
- Add a search box for queries.
- Use OpenAI's gpt-4-turbo-preview model