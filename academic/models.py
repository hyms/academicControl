from django.db import models

# Create your models here.

class user(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=15)
    segundo = models.CharField(max_length=15 , blank=True)
    apPaterno = models.CharField('Apellido Paterno' , max_length=15)
    apMaterno = models.CharField('Apellido Paterno' , max_length=15)
    fechaNacimiento = models.DateField('Fecha de Naciomiento')
    ci = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    tipo = models.CharField(max_length=15)
#    idRelacion = models.ForeignKey(user, blank=True)

class carrera(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField('Fecha de Creacion')
    cantSemestres = models.IntegerField('Cantidad de Semestres' , blank=True)
    cantAnios = models.IntegerField('Cantidad de Anios')
    descripcion = models.CharField(max_length=500)

class materia(models.Model):
    codigoMateria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField('Fecha de Creacion')
    idCarrera = models.ForeignKey(carrera)
    semestre = models.IntegerField('Cantidad de Semestres' , blank=True)
    anio = models.IntegerField('Anio')
#    idPresedente = models.ForeignKey(materia , blank=True)

class horario(models.Model):
    turno = models.IntegerField('Turno')
    periodo = models.IntegerField('Periodo')
    duracion = models.IntegerField('Duracion (mins)')
    idMateria = models.ForeignKey(materia)
    
class asignar(models.Model):
    idUser = models.ForeignKey(user)
    idHorario = models.ForeignKey(horario)
    fecha = models.DateField('Fecha de asignacion')

class notas(models.Model):
    nota = models.IntegerField('Nota')
    fecha = models.DateField()
    idAlumno = models.ForeignKey(user)
    idMateria = models.ForeignKey(materia)
    obs = models.CharField(max_length=100, blank=True)

class transaccion(models.Model):
    monto = models.FloatField('Monto')
    tipo = models.IntegerField('Tipo')
    idUser = models.ForeignKey(user)
    obs = models.CharField(max_length=100, blank=True)