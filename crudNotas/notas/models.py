from django.db import models

# Create your models here.
class nota(models.Model):
    identificador_unico = models.IntegerField('ID',
    blank= False,
    null= False,
     )
    nombre_nota = models.CharField ('Nombre Nota',
    max_length= 50,
    blank= False,
    null= False
    )
    descripcion_nota = models.CharField ('Descripción Nota',
    max_length= 50,
    blank= False,
    null= False
    )
    fecha_creacion = models.DateTimeField('Fecha de Creación',
    auto_now= True
    )
    fecha_finalizacion = models.DateTimeField('Fecha de Finalización',
    auto_now= True
    )
    # estado_nota = models.CharField ('Estado de Nota',
    # (Falta completar información por eso esta comentado ))
