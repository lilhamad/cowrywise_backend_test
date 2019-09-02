from django.db import models
from  django.contrib.auth.models import User

class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, editable = False, default= '1',blank=True , null=True)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    weekly_amount = models.IntegerField()
    capacity = models.IntegerField()
    searchable = models.BooleanField(default=True)
    members = models.ManyToManyField(User, related_name='group_member', default = '', blank=True)
    
    def save_form(self, request, form, change):
            obj = super(Group, self).save_form(request, form, change)
            if not change:
                obj.admin = request.user
            return obj