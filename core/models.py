from django.db import models

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='productos')

class Colores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7)  # Código hexadecimal del color (#FFFFFF)

class Tamanos(models.Model):
    id = models.AutoField(primary_key=True)    
    tamano = models.Choices(
        ('S', 'Pequeño'),
        ('M', 'Mediano'),
        ('L', 'Grande'),
        ('XL', 'Extra Grande'),
    )

class VarianteProductos(models.Model):
    id = models.AutoField(primary_key=True)
    producto_id = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='variantes')
    tamano_id = models.ForeignKey(Tamanos, on_delete=models.CASCADE, related_name='variantes')
    color_id = models.ForeignKey(Colores, on_delete=models.CASCADE, related_name='variantes')
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='variantes/', blank=True, null=True)

class Ordenes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    direccion_envio = models.TextField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    status = models.Choices(
        ('P', 'Pendiente'),
        ('C', 'Completada'),
        ('E', 'Enviada'),
        ('A', 'Anulada'),
    )

class ItemsOrdenes(models.Model):
    id = models.AutoField(primary_key=True)
    orden_id = models.ForeignKey(Ordenes, on_delete=models.CASCADE, related_name='items')
    variante_producto_id = models.ForeignKey(VarianteProductos, on_delete=models.CASCADE, related_name='items')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
