### DESCRIPCIÓN DEL ESCENARIO

Para que una empresa se beneficie del kit digital ofrecido por el gobierno, debe cumplir una serie de requisitos específicos relacionados con los módulos "Sitio Web y Presencia básica en Internet" y "Presencia Avanzada en Internet". Verifikit se ha diseñado como una herramienta para verificar estos requisitos, facilitando el trabajo tanto a las empresas como a los agentes digitalizadores. Ofrece las siguientes funcionalidades:

- **Detección y selección de palabras clave dentro del texto de tu web:** Verifikit analiza el texto de la URL proporcionada por el usuario, extrae palabras clave para mejorar el posicionamiento SEO y propone alternativas más eficaces.

En una segunda fase del proyecto se implementarán los siguientes puntos:

- **SEO On-Page:** Verifikit detectará la optimización de la estructura del HTML de la web, señalando fallos o necesidades.
  
- **Metadatos estructurados:** Verifikit verificará si se han incluido suficientes etiquetas para los metadatos a través del HTML.

### Tecnologías y tareas

El proyecto se desarrolla como una aplicación web utilizando las siguientes tecnologías:

- **Backend:** Framework Python Django con las siguientes librerías:
  - Extracción de texto de URLs mediante web scraping utilizando Beautiful Soup.
  - Selección de palabras clave y reconocimiento de entidades relevantes para SEO con SpaCy.

- **Frontend:** Construido con HTML, CSS y JavaScript.

### NOMBRE DE LA TAREA

El objetivo de esta tarea es seleccionar las palabras clave más relevantes del texto extraído para mejorar el posicionamiento SEO. Se utilizará la librería SpaCy para identificar entidades nombradas y palabras significativas, empleando el modelo preentrenado "es_core_news_sm" para el reconocimiento de entidades nombradas en español.

    import spacy
    from collections import Counter

    nlp = spacy.load('es_core_news_sm')

    def recognize_keywords(text, num_keywords=10):

      doc = nlp(text)

      # Contador de palabras clave
      keyword_counter = Counter()

      # Identificar y agregar entidades nombradas relevantes para SEO
      for ent in doc.ents:
        if ent.label_ in ['PER', 'ORG', 'LOC']:  # Filtrar entidades relevantes para SEO
            keyword_counter[ent.text.lower()] += 1

      # Contar sustantivos y adjetivos relevantes
      for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ'] and not token.is_stop:
            keyword_counter[token.lemma_.lower()] += 1

      # Obtener las palabras clave más frecuentes
      keywords = [keyword for keyword, count in keyword_counter.most_common(num_keywords)]
      return keywords



La función utilizará etiquetas como `PER` (Personas), `ORG` (Organizaciones), `LOC` (Lugares), así como categorías gramaticales como `NOUN`, `PROPN` y `ADJ`. Se gestionarán las Stop Words y se normalizará el texto para trabajar con los lemas.

Para llevar a cabo este proyecto, es crucial contar con tres perfiles profesionales especializados:

- Profesionales en SEO y Marketing Digital para definir y validar criterios de relevancia de palabras clave.
- Desarrolladores de Software para la implementación y mantenimiento de la infraestructura técnica.
- Especialistas en Procesamiento del Lenguaje Natural para optimizar modelos y ajustar algoritmos de reconocimiento de palabras clave.

### CORPUS DE EVALUACIÓN

El corpus de evaluación consiste en los textos extraídos de la URL proporcionada por el usuario. Se compararán las palabras destacadas en la web con las identificadas como significativas por nuestro modelo y filtros, requiriendo colaboración entre lingüistas y expertos en SEO para garantizar la funcionalidad del proyecto.

Se muestra a continuación un ejemplo del prototipo utilizando la dirección de Cálamo&Cran (https://www.calamoycran.com/):

### Captura de pantalla del resultado

### CONCLUSIONES

Uno de los principales desafíos encontrados ha sido la necesidad de abordar temáticas diversas para incluir instrucciones especializadas, lo cual podría resolverse dividiendo el proyecto en áreas profesionales para una especialización más profunda con respecto al corpus. Además, se debe considerar la importancia de las llamadas Long Tail en SEO.

