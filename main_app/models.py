from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class book(models.Model):
    book_name=models.CharField( max_length=50)
    author=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    class Meta:
        db_table='book'
    def __str__(self):
        return f"{self.book_name} - {self.author}"
    
class member(models.Model):
    m_nid= models.IntegerField()
    m_fname= models.CharField( max_length=50)
    m_lname= models.CharField( max_length=50)
    p_number=models.IntegerField()
    m_gender= models.CharField( max_length=50)
    m_dob= models.DateField()
    class Meta:
        db_table='member'
    def __str__(self):
        return f"{self.m_fname} {self.m_lname}"

class brower(models.Model):
    member_id = models.ForeignKey(member, on_delete=models.CASCADE)
    book_id = models.ForeignKey(book, on_delete=models.CASCADE)
    brow_date = models.DateField()
    date_to_return = models.DateField()
    returned_on = models.DateField(null=True, blank=True, default=None)
    decision = models.CharField(default='No', max_length=5)
    class Meta:
        db_table= 'brower'
    def clean(self):
        if self.brow_date > self.date_to_return:
            raise ValidationError("Borrow date can not be after the return date!.")
        if self.returned_on and self.brow_date > self.returned_on:
            raise ValidationError("date book returned must be after brow date!.")
        if self.returned_on and self.returned_on >now().date():
            raise ValidationError("date book returned can not greater than today!.")
    def __str__(self):
        return f"{self.member_id} browed {self.book_id}"
