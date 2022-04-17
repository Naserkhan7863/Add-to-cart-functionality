from django.db import models

# Create your models here.
class UserDetailsModel(models.Model):


     user_id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=100,help_text="Enter FullName")
     contact=models.BigIntegerField(help_text="Enter Mobile Number")
     email=models.EmailField(max_length=100,help_text="Enter Email id")
     subject=models.CharField(max_length=100,help_text="Enter Password")


     def __str__(self):
         return self.name
         
     
     class Meta:
         db_table="user_details"
    

class UserEnquiryModel(models.Model):


     user_id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=100,help_text="Enter FullName")
     subject=models.CharField(max_length=100,help_text="Enter Password")
     email=models.EmailField(max_length=100,help_text="Enter Email id")
     contact=models.BigIntegerField(help_text="Enter Mobile Number")
     message=models.TextField(help_text="Enter Password")


     def __str__(self):
         return self.name
         
     
     class Meta:
         db_table="user_enquiry_details"
    