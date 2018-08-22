from django.db import models


class Builder(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Builder"
        verbose_name_plural = "Builders"


class Job(models.Model):
    job_name = models.CharField(db_index=True, max_length=50)
    job_address = models.CharField(max_length=50, blank=True)
    job_city = models.CharField(max_length=50, blank=True)
    job_county = models.CharField(max_length=50, blank=True)
    builder = models.ForeignKey(Builder, blank=True, null=True)
    customer_name = models.CharField(db_index=True, max_length=100, blank=True)
    home_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    cell_phone_2 = models.CharField(max_length=20, blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    email_1 = models.CharField(max_length=75, blank=True)
    email_2 = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.job_name

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"


class JobNote(models.Model):
    job = models.ForeignKey(Job)
    note_date = models.DateField(db_index=True)
    note_text = models.CharField(max_length=2048)  # just cuz it feels right to be actually 2K.

    def __str__(self):
        return str(self.job) + ': ' + str(self.note_date)

    class Meta:
        verbose_name = "Job Note"
        verbose_name_plural = "Job Notes"
