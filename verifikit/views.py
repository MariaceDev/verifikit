from django.shortcuts import render
from django.http import HttpResponse
import requests
from.utils import extract_web_text, extract_bold_words, recognize_keywords

def process_url(request):
   
    if request.method == 'POST':
        url = request.POST['url']
        web_text = extract_web_text(url)
        bold_words = extract_bold_words(url)

        if not web_text:  # Check if web text extraction failed
            return HttpResponse("Failed to extract text from the URL.", status=400)
        
        keywords = recognize_keywords(web_text)
        if not keywords:  # Check if keyword recognition failed
            return HttpResponse("Failed to recognize keywords.", status=400)
        
        keywords_str = keywords

        context = {
            'keywords': keywords_str,
            'bold_words': bold_words,
            'url': url
        }

        return render(request, 'index.html', context)
    else:
         return render(request, 'index.html')
    
def process_api(request):
    context = {}
    if request.method == 'POST' and 'area_actividad' in request.POST:
        area_actividad = request.POST['area_actividad']
        # Consultar la API del Corpus del Español del Instituto Cervantes
        api_url = f'https://corpus.cervantes.es/corpus/search?query={area_actividad}'
        headers = {'Accept': 'application/json'}
        
        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                # Obtener las primeras 20 palabras clave (o menos si no hay suficientes)
                palabras_clave = [resultado['palabra'] for resultado in data['resultados']][:20]
                context['area_actividad'] = area_actividad
                context['recomendaciones'] = palabras_clave
            else:
                context['error'] = 'Error al obtener las palabras clave'
        except Exception as e:
            context['error'] = str(e)
    
    return render(request, 'index.html', context)

