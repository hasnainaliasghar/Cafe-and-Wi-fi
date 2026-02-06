# Cafe & Wifi Finder

A simple web application built with **Flask** and **SQLAlchemy** that helps users find cafes with WiFi, sockets, and other amenities. Users can view details about each cafe, including location, coffee prices, and whether calls can be taken there.

---

## Features

- Display a list of cafes with images and basic info.
- Click on a cafe to view detailed information in a modal.
- Filter cafes based on amenities like WiFi, sockets, toilet, and seating.
- Mobile-friendly and responsive design.
- SQLite database for storing cafe information.

---

## Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLAlchemy ORM
- SQLite
- HTML, CSS, JavaScript (Vanilla)

---

## Installation

1. **Clone the repository**

#bash
git clone https://github.com/yourusername/cafe-wifi-finder.git
cd cafe-wifi-finder
#Create a virtual environment

python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
Install dependencies

pip install -r requirements.txt
Run the application

python app.py
Open your browser and visit http://127.0.0.1:5000/

##Database
The application uses SQLite as the database. The Cafes table has the following schema:

Column	        Type	    Description
id	            Integer	  Primary Key
name	          String	  Name of the cafe (unique)
map_url	        String	  Google Maps URL of the cafe
img_url	        String	  Image URL of the cafe
location	      String	  General location or area
has_sockets	    Integer	  1 if sockets available, else 0
has_toilet	    Integer	  1 if toilet available, else 0
has_wifi	      Integer	  1 if WiFi available, else 0
can_take_calls	String	  Yes/No
seats	          String	  Number of seats or description
coffee_price	  String	  Average coffee price

#Project Structure
cafe-wifi-finder/
│
├─ app.py               # Flask application
├─ cafes.db             # SQLite database
├─ templates/
│   └─ index.html       # Main template
├─ static/
│   ├─ assets/
│   │   └─ style.css    # CSS styles
├─ requirements.txt     # Python dependencies
└─ README.md
Future Improvements
Add search and filter functionality.

Add user authentication for submitting new cafes.

Use a more robust database like PostgreSQL for production.

Add interactive maps integration.

##Author

Hasnain Ali Asghar
GitHub: hasnainaliasghar
Email: hasnainaliasghar@outlook.com
