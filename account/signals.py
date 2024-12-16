from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_delete, sender=User)
def post_delete_user(sender, instance, **kwargs):
    print(f"Delete user: {instance.email}")