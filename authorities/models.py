# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class permissions(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    parentid = models.IntegerField()
    level = models.IntegerField()
    icon = models.CharField(max_length=255)
    status = models.IntegerField(null=False, default=1)
    visible = models.IntegerField(null=False, default=1)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    view_order = models.IntegerField()

    def __unicode__(self):
        return self.name

class users(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    zh_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=255, unique=True, default='basicFramework')
    remember_token = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, null=False)
    ip = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class roles(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    display_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class permission_role(models.Model):
    permission_id = models.ForeignKey(permissions)
    role_id = models.ForeignKey(roles)
    permission_status = models.IntegerField(default=1)

class role_user(models.Model):
    user_id = models.ForeignKey(users)
    role_id = models.ForeignKey(roles)
    role_status = models.IntegerField(default=1)
