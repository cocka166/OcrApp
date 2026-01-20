# OCR Uploader – Cloud-Based Extraction Tool

Webová aplikace pro automatizované rozpoznávání a evidenci šestimístných kódů z fotografií štítků. Projekt demonstruje integraci cloudových služeb do firemních procesů a důraz na bezpečné nakládání s credentials.

## Funkcionalita
* **AI Recognition:** Automatické rozpoznávání textu pomocí Google Cloud Vision API.
* **Manual Correction:** Rozhraní pro ověření a ruční korekci rozpoznaných dat uživatelem.
* **Evidence dat:** Ukládání zpracovaných údajů do CSV formátu pro další analýzu.
* **Moderní Web UI:** Responzivní rozhraní postavené na Flask a HTML/CSS/JS.

## Technologie
* **Backend:** Python (Flask)
* **Cloud AI:** Google Cloud Vision API
* **Zabezpečení:** Správa Service Account klíčů přes environmentální proměnné / .gitignore

## Instalace a konfigurace
1. **Prerekvizity:** Python 3.7+
2. **Instalace závislostí:**
   ```bash
   pip install flask google-cloud-vision werkzeug

