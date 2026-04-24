from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return f"{self.nombre} <{self.email}>"
