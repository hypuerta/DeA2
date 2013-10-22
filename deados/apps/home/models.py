from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Institucion_nombre(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Institucion(models.Model):
	user = models.ForeignKey(User,related_name='perfil',unique=True)
	def __unicode__(self):
		return self.user.username

class Jugador(models.Model):
	idJugador			= models.AutoField(primary_key=True,blank=False,null=False)
	nombre				= models.CharField(max_length=90)
	idInstitucion		= models.ForeignKey(Institucion)
	puntos_totales		= models.IntegerField()
	puntos_negativos	= models.IntegerField()
	puntos_positivos	= models.IntegerField()
	fechaRegistro 		= models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre
		
class Pregunta(models.Model):
	OPCIONES_GRADO		= ((1,'primaria'),(2,'sexto_septimo'),(3,'octavo_noveno'))
	OPCIONES_CATEGORIA	= ((1,'teoria'),(2,'agilidad_mental'))
	OPCIONES_RESPUESTA	= ((1,'unica_respuesta'),(2,'multiple_repuesta'),(3,'booleana'),(4,'secuencial'))
	idPregunta			= models.AutoField(primary_key=True,blank=False,null=False)
	idInstitucion		= models.ForeignKey(Institucion)
	contenido			= models.CharField(max_length=61)
	grado				= models.IntegerField(choices=OPCIONES_GRADO, default=1)
	categoria			= models.IntegerField(choices=OPCIONES_CATEGORIA,default=1)
	tipoRespuesta		= models.IntegerField(choices=OPCIONES_RESPUESTA,default=1)

	def __unicode__(self):
		return self.contenido

class Respuesta(models.Model):
	idRespuesta		= models.AutoField(primary_key=True,blank=False,null=False)
	idPregunta		= models.ForeignKey(Pregunta)
	contenido		= models.CharField(max_length=41)

	class Meta:
		abstract = True

class Respuesta_Unica(Respuesta):
	determinacion		= models.BooleanField(default=False)

	def __unicode__(self):
		return self.contenido

class Respuesta_Multiple(Respuesta):
	determinacion			= models.BooleanField(default=False)

	def __unicode__(self):
		return self.contenido

class Respuesta_Secuencial(Respuesta):
	secuencia 				= models.IntegerField()

	def __unicode__(self):
		return self.contenido

class Respuesta_Booleana(Respuesta):
	determinacion			= models.BooleanField(default=False)

	def __unicode__(self):
		return self.contenido