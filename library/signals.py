from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Book
from datetime import datetime


@receiver(pre_save, sender=Book)
def normalize_fields(sender, instance, **kwargs):
    instance.title = instance.title.strip().title()
    instance.author = instance.author.strip().title()
    instance.genre = instance.genre.strip().title()
    
    captialized_sentences = [sentence.strip().capitalize() for sentence in instance.summary.split(".")]
    instance.summary = ". ".join(captialized_sentences)


@receiver(post_save, sender=Book)
def book_added(sender, instance, created, **kwargs):
    if created:
        print("-"*50)
        print(f"{instance.title} added to the library at {datetime.now()}.")
        print("-"*50)
        

@receiver(post_delete, sender=Book)
def book_removed(sender, instance, **kwargs):
    
    print("-"*50)
    print(f"{instance.title} removed from the library at {datetime.now()}.")
    print("-"*50)