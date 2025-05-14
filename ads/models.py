from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Модель объявления


class Ad(models.Model):
    CONDITION_CHOICES = [
        ("new", "Новый"),
        ("used", "Б/у"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ads", verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на изображение")
    category = models.CharField(max_length=100, verbose_name="Категория")
    condition = models.CharField(
        max_length=10, choices=CONDITION_CHOICES, verbose_name="Состояние")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Объявление (Ad)"
        verbose_name_plural = "Объявления (Ads)"

    def __str__(self):
        return self.title

# Модель предложения обмена


class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидает"),
        ("accepted", "Принята"),
        ("declined", "Отклонена"),
    ]

    ad_sender = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name="sent_proposals", verbose_name="Объявление отправителя")
    ad_receiver = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name="received_proposals", verbose_name="Объявление получателя")
    comment = models.TextField(verbose_name="Комментарий")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending", verbose_name="Статус")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Предложение обмена (Exchange proposal)"
        verbose_name_plural = "Предложения обмена (Exchange proposals)"

    def __str__(self):
        return f"Обмен от '{self.ad_sender}' на '{self.ad_receiver}'"
