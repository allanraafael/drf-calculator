from django.db import models


SYMBOLS = (
    ('+', 'Addition'),
    ('-', 'Subtraction'),
    ('*', 'Multiplication'),
    ('//', 'FloorDivision'),
)


class GenericOperation(models.Model):
    parameter_a = models.IntegerField()
    parameter_b = models.IntegerField()
    symbol = models.CharField(max_length=2, choices=SYMBOLS)
    result = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    class Meta:
        abstract = True


class Operation(GenericOperation):
    pass


class Addition(Operation):

    def __str__(self):
        return f'{self.parameter_a} + {self.parameter_b} = {self.result}'


class Subtraction(Operation):

    def __str__(self):
        return f'{self.parameter_a} - {self.parameter_b} = {self.result}'


class Multiplication(Operation):
    def __str__(self):
        return f'{self.parameter_a} * {self.parameter_b} = {self.result}'


class FloorDivision(Operation):

    def __str__(self):
        return f'{self.parameter_a} // {self.parameter_b} = {self.result}'
