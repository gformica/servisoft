from django.db import models

# Create your models here.

class Cliente(models.Model):
	user = models.OneToOneField('auth.user')
	id_cliente = models.CharField(primary_key=True,max_length=20)
	nomb_cliente = models.CharField(max_length=50)
	nac_cliente = models.DateField()
	dir_cliente = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.id_cliente 

class Tarjeta(models.Model):
	nro_tarjeta = models.IntegerField(default=0)
	TIPO_TARJETA_CHOICES = (
		('C', 'credito'),
		('D', 'debito'),
	)
	tipo_tarjeta = models.CharField(max_length=1, choices=TIPO_TARJETA_CHOICES,
					default='C')
	banc_tarjeta = models.CharField(max_length=20)
	ci_tarjeta = models.ForeignKey(Cliente)
	venc_tarjeta = models.DateField()
	
	def __unicode__(self):
		return "tarjeta de " + self.tipo_tarjeta + " de " + self.ci_tarjeta.id_cliente

class Servicio(models.Model):
	id_servicio = models.CharField(max_length=20,primary_key=True)
	nomb_servicio = models.CharField(max_length=50)
	desc_servicio = models.CharField(max_length=200)
	monto = models.DecimalField(max_digits=10,decimal_places=3)
	
	def __unicode__(self):
		return self.id_servicio + " --- Nombre: " + self.nomb_servicio + " --- Descripcion: " + self.desc_servicio

class Paquete(models.Model):
	id_paquete = models.CharField(max_length=20,primary_key=True)
	nomb_paquete = models.CharField(max_length=50)
	monto_paquete = models.DecimalField(max_digits=10,decimal_places=3)
	desc_paquete = models.CharField(max_length=200)
	TIPO_PAQUETE_CHOICES = (
		('prepago', 'prepago'),
		('postpago', 'postpago'),
		('ambos', 'ambos'),
		('ninguno','ninguno'),
	)
	tipo_paquete = models.CharField(max_length=10,choices=TIPO_PAQUETE_CHOICES)

	def __unicode__(self):
		return self.id_paquete + "- " + self.desc_paquete

class Plan(models.Model):
	id_plan = models.CharField(max_length=20,primary_key=True)
	nomb_plan = models.CharField(max_length=50)
	monto_plan = models.DecimalField(max_digits=10,decimal_places=3)
	desc_plan = models.CharField(max_length=200)
	TIPO_PLAN_CHOICES = (
		('prepago','prepago'),
		('postpago', 'postpago'),
	)
	tipo_plan = models.CharField(max_length=10,choices=TIPO_PLAN_CHOICES)
	
	def __unicode__(self):
		return "Id: " + self.id_plan + " --- Nombre: " + self.nomb_plan + " --- Descripcion : " + self.desc_plan

class Producto(models.Model):
	nomb_producto = models.CharField(max_length=30)
	id_producto = models.CharField(max_length=20,primary_key=True)
	id_cliente = models.ForeignKey(Cliente)
	saldo = models.DecimalField(max_digits=10,decimal_places=3)

	def __unicode__(self):
		return self.id_producto + " --- " + self.nomb_producto

class Factura(models.Model):
	nro_factura = models.IntegerField(primary_key=True)
	fecha_factura = models.DateField()
	id_producto = models.ForeignKey(Producto)
	monto_factura = models.DecimalField(max_digits=10,decimal_places=3)
	pagada_factura = models.BooleanField()
	nro_tarjeta = models.ForeignKey(Tarjeta)
	obs_factura = models.CharField(max_length=200)

	def __unicode__(self):
		return selfid_producto.id_producto + " --- " + str(self.fecha_factura) 
	
class Consumo(models.Model):
	id_producto = models.ForeignKey(Producto)
	id_servicio = models.ForeignKey(Servicio)
	fecha_consumo = models.DateTimeField()
	cant_consumo = models.IntegerField(default=0)
	cant_total_consumo = models.IntegerField(default=0)

	def __unicode__(self):
		return self.id_producto.id_producto + " --- consume " + self.id_servicio.id_servicio + " la cantidad de  " + self.cant_consumo

class Conforma(models.Model):
	id_paquete = models.ForeignKey(Paquete)
	id_servicio = models.ForeignKey(Servicio)
	cant_conforma = models.IntegerField(default=0)	
	
	def __unicode__(self):
		return self.id_paquete.id_paquete + " --- esta conformado en parte por " + self.id_servicio.id_servicio
	
class Posee(models.Model):	
	id_plan = models.ForeignKey(Plan)
	id_paquete = models.ForeignKey(Paquete)

	def __unicode__(self):
		return self.id_plan.id_plan + " --- posee el paquete " + self.id_paquete.id_paquete
	
class Agrega(models.Model):
	id_producto = models.ForeignKey(Producto)
	id_paquete = models.ForeignKey(Paquete)
	fecha_agrega = models.DateField()
	vigente_agrega = models.BooleanField()

	def __unicode__(self):
		return "el producto " + self.id_producto.id_producto + " agrega el paquete " + self.id_paquete.id_paquete

class Afilia(models.Model):
	id_producto = models.ForeignKey(Producto)
	id_plan = models.ForeignKey(Plan)
	fecha_afilia = models.DateField()
	dia_cobro = models.IntegerField(default=0)
	vigente_afilia = models.BooleanField()

	def __unicode__(self):
		return "El producto " + self.id_producto.id_producto + " se afilio al plan " + self.id_plan.id_plan + " el dia " + str(self.fecha_afilia)



class Adiciona(models.Model):
	id_producto = models.ForeignKey(Producto)
	id_servicio = models.ForeignKey(Servicio)
	fecha_adicion = models.DateField()
	vigente_adiciona = models.BooleanField()

	def __unicode__(self):
		return "el producto " + self.id_producto.id_producto + "adiciono un servicio " + self.id_servicio.id_servicio
