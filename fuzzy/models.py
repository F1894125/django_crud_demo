from django.db import models

class TriangularMembership(models.Model):
    x = models.FloatField(unique=True, null=False)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    membership = models.FloatField()

    def __str__(self):
        return f"triangular_test_{self.id}"
    
class TrapezoidalMembership(models.Model):
    x = models.FloatField(unique=True, null=False)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    membership = models.FloatField()

    def __str__(self):
        return f"trapezoidal_test_{self.id}"

class GaussianMembership(models.Model):
    x = models.FloatField(unique=True, null=False)
    mu = models.FloatField()
    sigma = models.FloatField()
    membership = models.FloatField()

    def __str__(self):
        return f"gaussian_test_{self.id}"