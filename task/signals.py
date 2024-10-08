from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from task.models import Task, COMPLETE, NOT_COMPLETE


@receiver(post_save, sender=Task)
def update_house_points(sender, instance, created, **kwargs):
    task = instance
    house = task.task_list.house
    if task.status == COMPLETE:
        house.points += 10
    elif task.status == NOT_COMPLETE:
        if house.points > 10:
            house.points -= 10
    house.save()


@receiver(post_save, sender=Task)
def update_tasklist_status(sender, instance, created, **kwargs):
    task = instance
    task_list = task.task_list
    is_complete = True
    for task in task_list.tasks.all():
        if task.status != COMPLETE:
            is_complete = False
            break
    task_list.status = COMPLETE if is_complete else NOT_COMPLETE
    task_list.save()
