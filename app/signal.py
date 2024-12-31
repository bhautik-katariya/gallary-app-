from django.db.models.signals import pre_save,pre_delete,post_save,post_delete
from .models import *

def pre_s(sender , instance ,**kwargs):
    print("pre_save")
    
def pre_d(sender , instance ,**kwargs):
    print("pre_delete")

def post_s(sender , instance ,**kwargs):
    print("post_save")

def post_d(sender , instance ,**kwargs):
    print("post_delete")

pre_save.connect(pre_s,sender=gallary)
pre_delete.connect(pre_d,sender=gallary)
post_save.connect(post_s,sender=gallary)
post_save.connect(post_d,sender=gallary)
