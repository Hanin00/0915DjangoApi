from django.db import models

class Lift(models.Model):
    lift_id = models.AutoField(primary_key=True)
    lift_name = models.CharField(max_length=45)
    lift_status = models.CharField(max_length=45)
    address = models.CharField(max_length=80)
    addr_state = models.CharField(max_length=45, blank=True, null=True)
    addr_city = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lift'


class Liftcheck(models.Model):
    check_id = models.AutoField(primary_key=True)
    lift_id = models.IntegerField()
    checker_id = models.IntegerField(blank=True, null=True)
    checker_name = models.CharField(max_length=45)
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'liftcheck'




class Checker(models.Model):
    checker_id = models.AutoField(primary_key=True)
    checker_name = models.CharField(max_length=45)
    charge_state = models.CharField(max_length=45, blank=True, null=True)
    charge_city = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'checker'

