from django.db import models

# Opción A: Uso de ArrayField (Requiere PostgreSQL)
# from django.contrib.postgres.fields import ArrayField 

class DeviceIoT(models.Model):
    # Opciones de Modelos (como una lista de tuplas para usar ChoiceField)
    MODEL_CHOICES = [
        ('ESP32', 'ESP32'),
        ('ESP32-S2', 'ESP32-S2'),
        ('ESP32-S3', 'ESP32-S3'),
        ('ARDUINO_UNO', 'Arduino Uno'),
        ('ARDUINO_MEGA', 'Arduino Mega'),
        ('STM32F407', 'STM32F407'),
        ('DESCONOCIDO', 'Desconocido'),
        # Puedes añadir más modelos aquí
    ]

    # 1. Modelo (usa opciones predefinidas)
    modelo = models.CharField(
        max_length=20,
        choices=MODEL_CHOICES,
        default='DESCONOCIDO',
        verbose_name='Modelo del Dispositivo'
    )

    # 2. ID del dispositivo (debe ser único)
    device_id = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='ID del Dispositivo'
    )

    # 3. Nombre del dispositivo
    nombre = models.CharField(
        max_length=255,
        verbose_name='Nombre'
    )

    # 4. Fecha de última vez conectado
    ultima_conexion = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Última Conexión'
    )

    # 5. Booleano de si está en línea
    en_linea = models.BooleanField(
        default=False,
        verbose_name='En Línea'
    )

    # 6. Tópicos de publicación y suscripción
    # Utilizamos JSONField para almacenar listas de cadenas de texto (tópicos).
    # Es más versátil que ArrayField (que solo funciona con PostgreSQL).
    topicos_pub = models.JSONField(
        default=list, # Almacena una lista vacía por defecto
        verbose_name='Tópicos de Publicación (Pub)'
    )
    topicos_sub = models.JSONField(
        default=list, # Almacena una lista vacía por defecto
        verbose_name='Tópicos de Suscripción (Sub)'
    )

    class Meta:
        verbose_name = "Dispositivo IoT"
        verbose_name_plural = "Dispositivos IoT"

    def __str__(self):
        return f"{self.nombre} ({self.device_id}) - {self.modelo}"

# NOTA: Para usar este modelo, debes agregarlo a tu archivo models.py de tu aplicación 
# y ejecutar:
# python manage.py makemigrations
# python manage.py migrate