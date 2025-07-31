from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tool(models.Model):
    STATUS_CHOICES = [
        ('sklad', 'Na sklade'),
        ('vydane', 'Vydané'),
        ('poskodene', 'Poškodené'),
        ('cakajuci_servis', 'Čaká sa na opravu'),
        ('v_servise', 'V oprave'),
        ('vyradene', 'Vyradené'),
        ('stratene', 'Stratené'),
    ]

    name = models.CharField("Názov náradia", max_length=200)
    tool_type = models.CharField("Typ", max_length=100)
    category = models.CharField("Kategória", max_length=100)
    serial_number = models.CharField("Sériové číslo", max_length=100, unique=True)
    purchase_date = models.DateField("Dátum zakúpenia")
    warranty_until = models.DateField("Platnosť záruky")
    issue_date = models.DateField("Dátum výdaja", null=True, blank=True)
    return_date = models.DateField("Dátum príjmu na sklad", null=True, blank=True)
    status = models.CharField("Stav", max_length=20, choices=STATUS_CHOICES, default='sklad')
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, verbose_name="Pobočka")
    notes = models.TextField("Poznámky", blank=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class ServiceRecord(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="services")
    service_date = models.DateField("Dátum servisu")
    description = models.TextField("Popis opravy alebo úkonu")

    def __str__(self):
        return f"Servis {self.tool.name} - {self.service_date}"


class ToolHistory(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)
    changed_by = models.CharField(max_length=100)
    change_description = models.TextField()

    def __str__(self):
        return f"Zmena {self.tool.name} ({self.changed_at.strftime('%Y-%m-%d %H:%M')})"
