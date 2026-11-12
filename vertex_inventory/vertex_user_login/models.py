from django.db import models

# Create your models here.

class VertexUsers(models.Model):
    user_id = models.CharField(primary_key=True, max_length=36)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    user_role = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    account_created_by = models.CharField(max_length=36)
    date_account_created = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    user_password = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'vertex_users'
