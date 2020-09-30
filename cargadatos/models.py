from django.db import models

# Create your models here.

class Profesor(models.Model):
    UsuarioUnab=models.EmailField(primary_key=True)
    rut=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=20)
    Coordinador=models.BooleanField()

class Ramo(models.Model):
    CodigoRamo=models.CharField(max_length=20,primary_key=True)
    NombreRamo=models.CharField(max_length=20)

class Seccion(models.Model):
    nrc=models.CharField(max_length=20,primary_key=True)
    semestre=models.CharField(max_length=20)
    CodigoRamo=models.ForeignKey(Ramo,on_delete=models.CASCADE)
    UsuarioUnab=models.ForeignKey(Profesor,on_delete=models.PROTECT)

class Lista(models.Model):
    nrc=models.ForeignKey(Seccion,on_delete=models.CASCADE)
    UsuarioUnab=models.EmailField()
    notas=models.DecimalField(decimal_places=3, max_digits=20)
    estado=models.CharField(max_length=20)


class Estudiante (models.Model):
    UsuarioUnab=models.EmailField(primary_key=True)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=20)
    rut=models.CharField(max_length=20)
    nrc=models.ForeignKey(Lista,on_delete=models.PROTECT)
    sede=models.CharField(max_length=20)
    carrera=models.CharField(max_length=50)
    jornada=models.CharField(max_length=20)

class Ejercicios(models.Model):
    IdEjercicio=models.CharField(max_length=20,primary_key=True)
    NombreProblema=models.CharField(max_length=50)
    skill1=models.BooleanField()
    skill2=models.BooleanField()
    skill3=models.BooleanField()
    skill4=models.BooleanField()
    knowledge1=models.BooleanField()
    knowledge2=models.BooleanField()
    knowledge3=models.BooleanField()
    knowledge4=models.BooleanField()
    complejidad=models.CharField(max_length=20)
    hito=models.IntegerField()


class TablonEjercicios(models.Model):
    UsuarioUnab=models.ForeignKey(Estudiante,null=True,on_delete=models.PROTECT)
    dia=models.CharField(max_length=20)
    mes=models.CharField(max_length=20)
    año=models.CharField(max_length=20)
    IdEjercicio=models.ForeignKey(Ejercicios,on_delete=models.PROTECT)
    Puntaje=models.DecimalField(decimal_places=3, max_digits=20)

