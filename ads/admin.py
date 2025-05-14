from django.contrib import admin
from .models import Ad, ExchangeProposal


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "category",
                    "condition", "created_at")
    search_fields = ("title", "description")
    list_filter = ("category", "condition", "created_at")

    def condition_display(self, obj):
        return obj.get_condition_display()
    condition_display.short_description = "Состояние"


@admin.register(ExchangeProposal)
class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_sender", "ad_receiver", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("comment", )

    def status_display(self, obj):
        return obj.get_status_display()
    status_display.short_description = "Статус"
