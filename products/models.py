from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=100)


    class Meta:
        db_table='category'

    def __str__(self) -> str:
        return self.name


class Phones(models.Model):
    category=models.ForeignKey(to='Category',on_delete=models.CASCADE)   
    model=models.CharField(max_length=100)
    storage=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='rasm/',blank=True,null=True)

    class Meta:
        db_table='Phones'

    def __str__(self) -> str:
        return f"{self.category.name}  {self.model}"
    
        

    