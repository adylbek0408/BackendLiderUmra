from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import logging
from .models import Client

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Client)
def notify_new_client(sender, instance, created, **kwargs):
    if created and instance.status == 'new':
        try:
            bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

            # Проверяем, что у клиента есть пакет
            if not instance.package:
                logger.error("Client %d has no package assigned", instance.id)
                return

            # Получаем филиал из пакета
            branch = instance.package.place

            # Получаем chat_id для филиала
            chat_id = settings.TELEGRAM_GROUP_IDS.get(branch)
            if not chat_id:
                logger.error("No group chat for branch %s", branch)
                return

            # Подготавливаем сообщение
            message = (
                f"📣 Новая заявка ({branch})❗️\n"
                f"👤 Имя: {instance.full_name}\n"
                f"📞 Телефон: {instance.phone}\n"
                f"🌍 Место: {instance.country}, {instance.city}\n"
                f"📦 Пакет: {instance.package.name or 'Не указан'}"
            )

            # Подготавливаем кнопку "Принять заявку"
            keyboard = [[
                InlineKeyboardButton(
                    "✅ Принять заявку",
                    callback_data=f"accept_{instance.id}"
                )
            ]]

            # Отправляем сообщение в группу филиала
            bot.send_message(
                chat_id=chat_id,
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                timeout=30
            )

        except Exception as e:
            logger.exception("Critical error in notification system: %s", str(e))
    