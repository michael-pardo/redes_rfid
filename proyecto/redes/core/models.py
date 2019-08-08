from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Auditoria(models.Model):
    """
    Modelo de Auditoria donde se va a guardar de forma automatica la fecha de
    creación de un objeto, quien lo creó, la fecha de la última actualización y
     quien fue el que lo actualizó, este modelo no tendrá vista en la parte
    administrativa de la plataforma ya que se usa como herencia en todos los
    modelos para recrear este registro automático sobre todos los datos que
    se trabajan en la misma.
    """
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
        help_text="Fecha en la que se hizo la acción."
    )
    """Fecha Creacion - tipo: DateTimeField"""
    creado_por = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_creado_por',
        null=True, blank=True,
        verbose_name='Usuario de creación',
        help_text="Usuario que realizó la acción"
    )
    """Creado Por - tipo: ForeignKey"""
    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización',
        help_text="Fecha en la que se hizo una actualización."
    )
    """Fecha Actualizacion - tipo: DateTimeField"""
    actualizado_por = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='%(class)s_modificado_por',
        null=True, blank=True,
        verbose_name='Usuario última actualización',
        help_text="Usuario que realizó la actualización."

    )
    """Actualizado Por - tipo: ForeignKey"""

    class Meta:
        abstract = True

    def traer_usuario(self):
        return get_current_user()

    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.creado_por = self.traer_usuario()
            self.actualizado_por = self.traer_usuario()
        else:
            self.actualizado_por = self.traer_usuario()

        super(Auditoria, self).save(*args, **kwargs)


class Usuario(Auditoria):
    user = models.OneToOneField(
        User, models.CASCADE,
        help_text="Identificador del usuario asignado."
    )
    documento = models.CharField(
        max_length=20,
        help_text="Número del documento de identidad del usuario."
    )
    rol = models.CharField(
        max_length=20,
        help_text="Tipo de rol."
    )
    facultad = models.CharField(
        max_length=20,
        help_text="Facultad a la que pertenece."
    )

    def __str__(self):
        return '{}'.format(self.user.get_full_name())

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Tarjeta(Auditoria):
    TARJETA = 'TARJETA'
    LLAVERO = 'LLAVERO'

    TIPOS = (
        (TARJETA, TARJETA),
        (LLAVERO, LLAVERO)
    )

    codigo = models.CharField(
        max_length=100,
        help_text='Código de la tarjeta',
        unique=True
    )
    tipo = models.CharField(
        max_length=50, choices=TIPOS,
        default='tipo de tarjeta'
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE,
        help_text='Usuario que tiene asiganado la tarjeta'
    )

    def __str__(self):
        return 'Tarjeta: {}'.format(self.codigo)

    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"


class Lector(Auditoria):
    codigo = models.CharField(
        max_length=100,
        help_text='Código del lector',
        unique=True
    )
    ubicacion = models.CharField(
        max_length=100,
        help_text='Lugar en el cual está ubicado el lector'
    )

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        return 'Lector: {} ubicado en {}'.format(self.codigo, self.ubicacion)


class Registro(models.Model):
    tarjeta = models.ForeignKey(
        Tarjeta, on_delete=models.CASCADE,
        help_text='Tarjeta asociada al registro'
    )
    lector = models.ForeignKey(
        Lector, on_delete=models.CASCADE,
        help_text='Lector asociado al registro'
    )
    fecha = models.DateTimeField(
        auto_now_add=True,
        help_text='Hora y fecha del registro'
    )

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return 'Registro #{}'.format(self.id)
