from django.db import models

# Create your models here.


class Department(models.Model):
    dep_name= models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self):
        return self.dep_name


class Doctors(models.Model):
    d_name= models.CharField(max_length=100)
    d_spec= models.CharField(max_length=100)
    dep_name=models.ForeignKey(Department, on_delete=models.CASCADE)
    d_img= models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr' + self.d_name+'-('+self.d_spec +')'


class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    d_name=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    b_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


    # def __str__(self):
    #     return 'Dr'+self.d_name

    def __str__(self):
        return self.d_name

