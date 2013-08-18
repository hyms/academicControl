#encoding:utf-8
from django.db import models

# Create your models here.

class user(models.Model):
    TIPO_CHOICE =(
                  #(0,'admin'),
                  ('1','Administrativo'),
                  ('2','Docente'),
                  ('3','Estudiante'),
                  ('4','Familiar')
                  )
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=15)
    segundo = models.CharField(max_length=15 , blank=True, null=True)
    apPaterno = models.CharField('Apellido Paterno' , max_length=15)
    apMaterno = models.CharField('Apellido Paterno' , max_length=15)
    fechaNacimiento = models.DateField('Fecha de Naciomiento', auto_now=True)
    ci = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICE)
    idRelacion = models.ForeignKey('self', blank=True, null=True)

class carrera(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField('Fecha de Creación', auto_now=True)
    cantSemestres = models.PositiveSmallIntegerField('Cantidad de Semestres' , blank=True, null=True)
    cantAnios = models.IntegerField('Cantidad de Años')
    descripcion = models.CharField(max_length=500)

class materia(models.Model):
    codigoMateria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField('Fecha de Creación', auto_now=True)
    semestre = models.PositiveSmallIntegerField('Cantidad de Semestres' , blank=True, null=True)
    anio = models.PositiveSmallIntegerField('Año')
    idCarrera = models.ForeignKey(carrera)
    idPresedente = models.ForeignKey('self' , blank=True, null=True)

class horario(models.Model):
    turno = models.PositiveSmallIntegerField('Turno')
    periodo = models.PositiveSmallIntegerField('Periodo')
    duracion = models.IntegerField('Duración (mins)')
    idMateria = models.ForeignKey(materia)
    
class asignar(models.Model):
    idUser = models.ForeignKey(user)
    idHorario = models.ForeignKey(horario)
    fecha = models.DateField('Fecha de asignación')

class notas(models.Model):
    nota = models.PositiveSmallIntegerField('Nota')
    fecha = models.DateField(auto_now=True)
    idAlumno = models.ForeignKey(user)
    idMateria = models.ForeignKey(materia)
    obs = models.CharField(max_length=100, blank=True, null=True)

class transaccion(models.Model):
    TIPO_MONEY_CHOICE =(
                  #(0,'admin'),
                  (1,'Mensualidad'),
                  (2,'Sueldo'),
                  (3,'Tramite'),
                  (4,'Otros')
                  )
    monto = models.FloatField('Monto')
    tipo = models.IntegerField('Tipo',choices=TIPO_MONEY_CHOICE)
    idUser = models.ForeignKey(user)
    obs = models.CharField(max_length=100, blank=True, null=True)