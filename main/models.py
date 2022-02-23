from django.db import models


class CustomerData(models.Model):

    customer = models.ForeignKey('self', verbose_name='ID клиента', primary_key=True, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    middle_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return "Клиент: {} {}".format(self.first_name, self.last_name)


class CustomerAccount(models.Model):

    customer = models.ForeignKey(CustomerData, verbose_name='ID клиента', on_delete=models.CASCADE)
    account = models.ForeignKey('self', verbose_name='Номер договора', primary_key=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Остаток по счету')

    def __str__(self):
        return self.customer


class Transactions(models.Model):

    account = models.ForeignKey(CustomerAccount, verbose_name='Номер договора', primary_key=True, on_delete=models.CASCADE)
    translations_dt = models.DateTimeField(auto_now=True, auto_now_add=False)
    total = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='Сумма')

    def __str__(self):
        return self.account

    def get_absolute_url(self):
        pass


class CustomerToAccount(models.Model):

    customer = models.ForeignKey(CustomerData, verbose_name='ID клиента', on_delete=models.CASCADE)
    account = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer