# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import string
import json

class Admin(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50, blank=True, null=True)
    admintype = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'

    def __str__(self):
        templ = string.Template('{ "username":"${username}",'+
        ' "password":"${password}",'+
        ' "admintype":"${admintype}" }')
        return templ.safe_substitute(username=self.username,
        password=self.password,
        admintype=self.admintype)

class Vote(models.Model):
    entrance_id = models.CharField(primary_key=True, max_length=8)
    c_id = models.IntegerField(blank=True, null=True)
    s_id = models.IntegerField(blank=True, null=True)
    a_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vote'

    def __str__(self):
        return (self.entrance_id+" : "+str(self.c_id)+str(self.s_id)+str(self.a_id))