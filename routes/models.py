from django.db import models
from cities.models import City


class Route(models.Model):
    name = models.CharField(
        max_length=50, unique=True, verbose_name="Название маршрута"
    )
    travel_times = models.PositiveSmallIntegerField(
        verbose_name="Общее время в пути")
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="route_from_city_set",
        verbose_name="Из какого города",
    )
    to_city = models.ForeignKey(
        "cities.City",
        on_delete=models.CASCADE,
        related_name="route_to_city_set",
        verbose_name="В какой город",
    )
    trains = models.ManyToManyField("trains.Train",
                                    verbose_name="Список поездов")

    def __str__(self):
        return (
            f"Маршрут из города {self.from_city} в город"
            f" {self.to_city}  с номером {self.name}"
        )

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"
        ordering = ["name"]
