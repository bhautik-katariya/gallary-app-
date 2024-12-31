# from django.contrib.auth.base_user import BaseUserManager


# class usermanger(BaseUserManager):
#     def c_user(self,phone_no,password=None,**extra_fields):
#         if not phone_no:
#             raise ValueError(".............")
        
#         extra_fields['email']=self.normalize_email(extra_fields['email'])
#         user = self.model(phone_no=phone_no,**extra_fields)
#         user.set_password(password)
#         user.save(using = self.db)
#         return user
    
#     def create_superuser(self,phone_no,password=None,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         return self.create_superuser(phone_no,password,**extra_fields)