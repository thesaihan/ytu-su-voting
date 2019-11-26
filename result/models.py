from django.db import models

# Create your models here.

class Candidate(models.Model):
    id = models.IntegerField(primary_key=True)
    cand_no = models.IntegerField(blank=True, null=True)
    cand_type = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate'

    def __str__(self):
        return str(self.cand_no)+self.cand_type+" : "+self.name