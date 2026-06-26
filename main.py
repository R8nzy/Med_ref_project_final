from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def search_disease(query):
    headers = {
        "User-Agent": "MedRef/1.0 (educational project; nuradil@example.com)"
    }
    
    # Шаг 1 — ищем страницу
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 1
    }
    search_response = requests.get(search_url, params=search_params, headers=headers)
    search_data = search_response.json()
    
    results = search_data.get("query", {}).get("search", [])
    if not results:
        return None
    
    page_title = results[0]["title"]
    
    # Шаг 2 — получаем содержимое страницы
    content_params = {
        "action": "query",
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "titles": page_title,
        "format": "json"
    }
    content_response = requests.get(search_url, params=content_params, headers=headers)
    content_data = content_response.json()
    
    pages = content_data.get("query", {}).get("pages", {})
    page = list(pages.values())[0]
    
    description = page.get("extract", "")
    if len(description) > 500:
        description = description[:500] + "..."
    
    # Шаг 3 — получаем секции
    sections_params = {
        "action": "parse",
        "page": page_title,
        "prop": "sections",
        "format": "json"
    }
    sections_response = requests.get(search_url, params=sections_params, headers=headers)
    sections_data = sections_response.json()
    sections = sections_data.get("parse", {}).get("sections", [])
    
    symptoms = []
    treatment = []
    
    for section in sections:
        title = section.get("line", "").lower()
        index = section.get("index", "")
        
        if "symptom" in title or "sign" in title or "clinical" in title:
            section_params = {
                "action": "parse",
                "page": page_title,
                "prop": "wikitext",
                "section": index,
                "format": "json"
            }
            r = requests.get(search_url, params=section_params, headers=headers)
            wikitext = r.json().get("parse", {}).get("wikitext", {}).get("*", "")
            lines = [l.strip("*# ").strip() for l in wikitext.split("\n") if l.strip().startswith("*")]
            symptoms = lines[:8]
            
        elif "treatment" in title or "management" in title or "therapy" in title:
            section_params = {
                "action": "parse",
                "page": page_title,
                "prop": "wikitext",
                "section": index,
                "format": "json"
            }
            r = requests.get(search_url, params=section_params, headers=headers)
            wikitext = r.json().get("parse", {}).get("wikitext", {}).get("*", "")
            lines = [l.strip("*# ").strip() for l in wikitext.split("\n") if l.strip().startswith("*")]
            treatment = lines[:8]
    
    return {
        "name": page_title,
        "description": description,
        "symptoms": symptoms,
        "treatment": treatment
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    mode = 'disease'
    query = ""
    
    if request.method == 'POST':
        query = request.form['query']
        mode = request.form['mode']
        result = search_disease(query)
        if result is None:
            error = "Not found. Please try another query."
    
    return render_template('index.html', result=result, error=error, mode=mode, query=query)

if __name__ == '__main__':
    app.run(debug=True)