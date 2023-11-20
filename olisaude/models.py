from django.db import models


class Costumer(models.Model):
    """
        model to create costumer.
    """
    gender_choice = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    code = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    gender = models.CharField(max_length=1, choices=gender_choice)
    birth_date = models.DateField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Costumer"
        verbose_name_plural = "Costumers"


class HearthProblem(models.Model):
    """
        model to create hearth problem.
    """

    degre_choice = [
        (1, "Low"),
        (2, "High"),
    ]
    name = models.CharField(max_length=80, null=False, blank=False)
    degree = models.IntegerField(choices=degre_choice)
    code_costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Hearth Problem"
        verbose_name_plural = "Hearth Problems"

    def __str__(self):
        return self.name

