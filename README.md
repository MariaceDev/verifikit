Para que una empresa se beneficie del kit digital que ofrece el gobierno, debe pasar por una serie de justificaciones que exigen que se cumplan unos objetivos. Atendiendo a los requisitos de los módulos: “Sitio Web y Presencia básica en Internet” y “Presencia Avanzada en Internet”; Verifikit ha sido pensado como una herramienta de verificación de dichos requisitos para facilitar el trabajo, tanto a las propias empresas como a los agentes digitalizadores, ofreciendo diversas funcionalidades: 

Detección y selección de palabras clave dentro del texto de tu web: Verifikit analiza el texto de la URL que proporcione el usuario, extrae las palabras que están marcadas para resaltar el posicionamiento SEO de la página y propone alternativas más sensibles. 

Los siguientes puntos serán implementados en una segunda fase del proyecto: 

Dentro del SEO On-Page: detección del optimizado de la estructura. Verifikit detecta las etiquetas del HTML de la web y expone fallos o necesidades. 

Metadatos estructurados: a través del HTML, verifikit detecta si se han introducido las etiquetas suficientes para incorporar los metadatos. 

Tecnologías y tareas 

El proyecto se expone a través de una aplicación web creada con las siguientes tecnologías: 

Para la parte backend se utilizará el framework de python Django junto con las siguientes librerías: 

La extracción de los textos de la URL dada se realizará mediante la técnica web scraping con la librería Beautiful Soup. 

La selección de las palabras clave, teniendo en cuenta el reconocimiento de entidades relevantes para el posicionamiento SEO, se desarrollará con la librería SpaCy. 

La parte front será construida con HTML, CSS y JS. 

 

NOMBRE DE LA TAREA 
El objetivo de la tarea que se va a desarrollar es seleccionar las palabras clave más relevantes del texto extraído para mejorar el posicionamiento SEO.  

Se realizará utilizando la librería SpaCy, con la que se identificarán las entidades nombradas y palabras significativas. Para ello, se utilizará a siguiente función: 

 nlp = spacy.load('es_core_news_sm')

def recognize_keywords(text, num_keywords=10):
   
    doc = nlp(text)

    #keywords counter
    keyword_counter = Counter()

    # Identify and add relevant named entities

    for ent in doc.ents:
        if ent.label_ in ['PER', 'ORG', 'LOC']:  # Filter SEO-relevant entities
            keyword_counter[ent.text.lower()] += 1

    # Count relevant nouns and adjectives

    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ'] and not token.is_stop:
            keyword_counter[token.lemma_.lower()] += 1
    

    #Get the most frequent keywords

    keywords = [keyword for keyword, count in keyword_counter.most_common(num_keywords)]
    return keywords
    
El objetivo de la tarea que se va a desarrollar es seleccionar las palabras clave más relevantes del texto extraído para mejorar el posicionamiento SEO.  
Para la selección de las palabras claves se ha decidido utilizar las siguientes etiquetas: 

Personas (`PER`): el nombre de personas relevantes puede ser importante para el posicionamiento. 

Organizaciones (`ORG`): igualmente hay que resaltar las instituciones. 

Lugares (`LOC`): los lugares pueden ser importantes para el SEO local, ayudando a geolocalizar el contenido y hacerlo relevante para búsquedas específicas de ubicaciones. 

Debido a la naturaleza dinámica de los textos y a que la temática de las páginas que se van a analizar es muy amplia, se han considerado etiquetas de carácter universal, pero relevantes para SEO. 

Además, hacemos uso del estándar POS (Part of Speech tagging) de SpaCy, al seleccionar las categorías gramaticales estimadas como importantes: (`NOUN`), nombres propios (`PROPN`) y adjetivos (`ADJ`). También, se han gestionado las Stop Words o palabras vacías y se ha normalizado el texto para trabajar con los lemas. 

Hay que resaltar que, para realizar este proyecto, es muy importarte contar con tres perfiles profesionales especializados:  

Profesionales en SEO y Marketing Digital: Para colaborar con los lingüistas en la definición y validación de criterios de relevancia de palabras clave. 

Desarrolladores de Software: Para implementar y mantener la infraestructura técnica del proyecto. 

Especialistas en Procesamiento del Lenguaje Natural: Para optimizar los modelos y ajustar los algoritmos de reconocimiento de palabras clave. 

 

CORPUS DE EVALUACIÓN 

El corpus de evaluación se corresponde con los textos extraídos de la URL proporcionada por el usuario. Será relativamente sencillo realizar una comparación pues, primero, se obtendrán las palabras que ya están resaltadas como importantes en la web y, después, se obtendrán las que se han considerado más significativas según nuestro modelo y los filtros utilizados en la función anteriormente definida. 

En este momento será necesario un trabajo conjunto entre lingüistas y expertos en SEO para comprobar la correcta funcionalidad del proyecto. 

Un ejemplo de cómo se ejecutaría el proyecto sería el siguiente, utilizando como ejemplo la dirección de Cálamo&Cran (https://www.calamoycran.com/): 


Captura de pantalla del resultado 

CONCLUSIONES 

Considero que la aplicación puede ser muy útil para profesionales pues, según mi experiencia, cuando llegas a un proyecto que había comenzado otro compañero, comprobar que todos los pasos se han realizado de manera correcta puede llevar mucho tiempo y Verifikit puede ayudar en estas tareas. Supone un apoyo perfecto que pueden desarrollar los perfiles ya nombrados, entre ellos el lingüista. 

El problema más importante con el que me he encontrado ha sido la dificultad de abarcar las temáticas para poder incluir instrucciones más especializadas. Podría solucionarse dividiendo el proyecto en áreas profesionales para poder especializar más el trabajo con el corpus. Y, también, cómo tener en cuenta las llamadas Long Tail, tan importantes para el SEO. 
 
 
