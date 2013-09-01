from django.contrib import admin

from academic.models import user
from academic.models import carrera
from academic.models import materia
from academic.models import horario
from academic.models import asignar
from academic.models import notas
from academic.models import transaccion

admin.site.register(user)
admin.site.register(carrera)
admin.site.register(materia)
admin.site.register(horario)
admin.site.register(asignar)
admin.site.register(notas)
admin.site.register(transaccion)