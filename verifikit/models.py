from django.db import models

class ProcessedData(models.Model):
    keywords = models.TextField()  # Almacena las palabras clave como texto
    processDate = models.DateTimeField(auto_now_add=True)  # Fecha y hora de procesamiento
