from django.db import models

# Create your models here.


class Badanie(models.Model):
    kategorie = (
        ('Lekka', 'L'),
        ('Ciężka', 'H'),
    )

    wapnowanie = (
        ('Potrzebne', 'P'),
        ('Ograniczone', 'O'),
        ('Zbędne', 'Z'),
    )

    oznakowanie = models.IntegerField(unique=True, blank=False, verbose_name="Oznakowanie")
    kategoria = models.CharField(max_length=30, choices=kategorie, verbose_name="Kategoria")
    pHwKCL = models.FloatField(null=True)
    potrz_wapn = models.CharField(max_length=30, choices=wapnowanie, verbose_name="Potrz_wapn")
    p2o5 = models.FloatField(null=True, verbose_name="P2O5")
    k2o = models.FloatField(null=True, verbose_name="K2O")
    mg = models.FloatField(null=True, verbose_name="Mg")
    b = models.FloatField(null=True, verbose_name="B")
    mn = models.FloatField(null=True, verbose_name="Mn")
    cu = models.FloatField(null=True, verbose_name="Cu")
    zn = models.FloatField(null=True, verbose_name="Zn")
    fe = models.FloatField(null=True, verbose_name="Fe")
    lat = models.FloatField(null=True, verbose_name="Lattitude")
    long = models.FloatField(null=True, verbose_name="Longitude")



