from django.contrib import admin

from trains.models import Train


class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train

    list_display = ("name", "from_city", "to_city", "travel_table")
    list_editable = ("travel_table",)


admin.site.register(Train, TrainAdmin)
