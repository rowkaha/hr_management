from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

# office setup ===================================================================
class Office(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description =  models.TextField(blank=True)
    address  = models.CharField(max_length=255, blank=True)
    phone=models.CharField(blank=True,max_length=20)
    email = models.EmailField(blank=True)
    registrationNo = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='uploads/company/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    def register(self):
        self.save()

# office setup ===================================================================
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    email = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    def register(self):
        self.save()
# office setup ===================================================================
class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    office_id = models.ForeignKey(Office,on_delete=models.DO_NOTHING)
    branchName =  models.CharField(max_length=255)
    address  = models.CharField(max_length=255, blank=True)
    phone=models.CharField(blank=True,max_length=20)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    def register(self):
        self.save()


# office setup ===================================================================
class Designation(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    def register(self):
        self.save()

# office setup ===================================================================
class Shift(models.Model):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.CharField(max_length=255)
    objects = models.Manager()
    
    def register(self):
        self.save()
        
class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address  = models.CharField(max_length=255, blank=True)
    phone = models.CharField(blank=True,max_length=20)
    image = models.ImageField(upload_to='uploads/user/',blank=True)
    office_id = models.ForeignKey(Office,on_delete=models.DO_NOTHING)
    # branch = models.OneToOneField(Branch, on_delete = models.CASCADE)
    # department = models.OneToOneField(Department, on_delete = models.CASCADE)
    # shift = models.OneToOneField(Shift, on_delete = models.CASCADE)
    # designation = models.OneToOneField(Designation, on_delete = models.CASCADE)
    # duty_type  = models.CharField(max_length=255, blank=True)
    # card_no  = models.CharField(max_length=255, blank=True)
    # gender  = models.CharField(max_length=255, blank=True)
    # marital_status = models.CharField(max_length=255, blank=True)
    # date_of_birth = models.DateTimeField(blank=True)
    # sallery  = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    # sallery_type  = models.CharField(max_length=255, blank=True)
    # date_of_joining  = models.DateTimeField(blank=True)
    # emergency_contact =  models.CharField(blank=True,max_length=20)
    # cityzenshipno = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save,sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance,**kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()