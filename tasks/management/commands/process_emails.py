from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from tasks.models import *
from tasks_ops.models import ManagementLog
from tasks_ops.tasks_classes_ops.management__log import Management
import time

class Command(BaseCommand):
    title = "Process Emails"
    help = 'Runs through email queue and sends emails'

    log = Management(title)

    def add_arguments(self, parser):
        parser.add_argument('--id')
    
    def handle(self, *args, **options):
        self.log.in_progress()

        if options['id']:
            email_id = options['id']
            try:
                email = EmailQueue.objects.get(pk=email_id)
            except:
                raise CommandError("Email with tath ID doesn't exist")

            self.send_email(email)
            email.delete()
            self.log.update_count(1)
        else:
            emails = EmailQueue.EmailManager.emails()
            for index, email in enumerate(emails):
                self.send_email(email)
                email.delete()
                self.log.update_count(index + 1)
                time.sleep(15)
            self.log.completed()


    def send_email(self, email):
        try:
            # send logic would allow for success or fail result, for this example just print out to console
            print("Email sent to - {0}".format(email.auction.owner.email))
            self.update_bid_row(email.bid)
        except:
            raise CommandError("Email could not send for reason XYZ")
    
    def update_bid_row(self, bid):
        bid.email_sent = True
        bid.email_sent_time = timezone.now()
        bid.save()