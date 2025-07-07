OCR Uploader

Webová aplikace pro nahrávání fotek štítků a automatické rozpoznávání 6místných čísel pomocí Google Cloud Vision API. Umožňuje ruční korekci rozpoznaného čísla, ukládá data do CSV a zobrazuje seznam uložených čísel.

Technologie: Python (Flask), Google Cloud Vision API, HTML/CSS/JS

Požadavky: Python 3.7+, Flask, google-cloud-vision, Google Service Account klíč

Instalace:
pip install flask google-cloud-vision werkzeug
Přidejte credentials.json (Google Service Account key) do projektu a .gitignore (nikdy nepushujte citlivá data).

Spuštění:
python app.py — pak otevřít http://localhost:5000

Poznámky:
Produktivní nasazení doporučeno přes WSGI server (Gunicorn, Nginx). API klíče chraňte a omezujte oprávnění. CSV lze nahradit databází pro lepší škálovatelnost.

************************************************************************************************************************************************************************************************************************************************

OCR Uploader

A web application for uploading label photos and automatically recognizing 6-digit numbers using the Google Cloud Vision API. It allows manual correction of the recognized number, saves data to a CSV file, and displays the saved numbers list.

Technologies: Python (Flask), Google Cloud Vision API, HTML/CSS/JS

Requirements: Python 3.7+, Flask, google-cloud-vision, Google Service Account key

Installation:
pip install flask google-cloud-vision werkzeug
Add your credentials.json (Google Service Account key) to the project and include it in .gitignore to avoid pushing sensitive data.

Running:
python app.py — then open http://localhost:5000

Notes:
For production, use a WSGI server like Gunicorn or Nginx. Protect API keys and restrict permissions. Consider replacing the CSV with a database for better scalability.
