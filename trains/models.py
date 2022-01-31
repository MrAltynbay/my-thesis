from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            verbose_name="Номер поезда")
    travel_table = models.PositiveSmallIntegerField(
        verbose_name="Время в пути")
    # Это время в пути, почему-то не travel_time, нужно будет пофиксить
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="from_city_set",
        verbose_name="Из какого города",
    )
    to_city = models.ForeignKey(
        "cities.City",
        on_delete=models.CASCADE,
        related_name="to_city_set",
        verbose_name="В какой город",
    )

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError("Изменить город прибытия")
        qs = Train.objects.filter(
            from_city=self.from_city,
            to_city=self.to_city,
            travel_table=self.travel_table,
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Необходимо изменить время в пути")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Поезд из города {self.from_city} в город" \
               f" {self.to_city}  с номером {self.name}"

    class Meta:
        verbose_name = "Поезд"
        verbose_name_plural = "Поезда"
        ordering = ["name"]
