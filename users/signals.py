
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
# from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User


# @receiver(post_save, sender=Profile)
def createUpdated(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        # subject = "Welcome ti Devsearch"
        # message = "this is a test message we are glad you are here"
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email],
        #     fail_silently = False,
        # )





def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.emali = profile.email
        user.username = profile.username
        user.save()

def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
    

    # in ordinary when we delete user profile will delete but if we delete 
    # profile will not delete we should use two line code for delete user at the time 
    # that will delete prfile

post_save.connect(createUpdated, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)