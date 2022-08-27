from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
# Create your models here.


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    # Field name made lowercase.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'cliente'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    # Field name made lowercase.
    employee_dni = models.TextField(db_column='employee_DNI')
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleado'


class Direccion(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_street = models.TextField()
    address_number = models.TextField()
    address_city = models.TextField()
    address_province = models.TextField()
    address_country = models.TextField()
    address_customer = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column='address_customer', blank=True, null=True)
    address_employee = models.ForeignKey(
        'Empleado', models.DO_NOTHING, db_column='address_employee', blank=True, null=True)
    address_branch = models.OneToOneField(
        'Sucursal', models.DO_NOTHING, db_column='address_branch', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class Tiposclientes(models.Model):
    # Field name made lowercase.
    tipoid = models.AutoField(
        db_column='TipoId', primary_key=True, blank=True)
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'TiposClientes'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class TipoCuenta(models.Model):
    act_id = models.AutoField(primary_key=True)
    act_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    account_type = models.ForeignKey(
        TipoCuenta, models.DO_NOTHING, db_column='account_type')
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


class MarcaTarjeta(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_brand = models.ForeignKey(
        MarcaTarjeta, models.DO_NOTHING, db_column='card_brand')
    card_number = models.TextField(unique=True)
    card_cvv = models.IntegerField()
    card_from_date = models.DateTimeField()
    card_expiration_date = models.DateTimeField()
    card_type = models.TextField()
    card_customer = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column='card_customer')

    class Meta:
        managed = False
        db_table = 'tarjeta'


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer = models.OneToOneField(
        Cliente, on_delete=models.CASCADE, null=True, blank=True)
    employer = models.OneToOneField(
        Empleado, on_delete=models.CASCADE, null=True, blank=True)
    is_employee = models.BooleanField(default=False)
