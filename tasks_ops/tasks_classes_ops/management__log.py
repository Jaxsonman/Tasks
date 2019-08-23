from tasks_ops.models import *
from django.utils import timezone


class Management:
    print("=====================")
    print("Management hit")
    print("=====================")
    log = None

    def __init__(self, title):
        self.log = ManagementLog(task=title, count=0, started=timezone.now(), state=1)
        self.log.save()

    def in_progress(self):
        print("=====================")
        print("in_progress hit")
        print("=====================")
        self.log.state = 2
        self.log.save()

    def update_count(self, x):
        print("=====================")
        print("update_count hit")
        print("=====================")
        self.log.count = x
        self.log.save()

    def completed(self):
        print("=====================")
        print("completed hit")
        print("=====================")
        self.log.state = 3
        self.log.finished = timezone.now()
        self.log.save()