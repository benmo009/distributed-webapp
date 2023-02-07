from django.core.management.base import BaseCommand, CommandError
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from counter.models import CountProcess
import asyncio
class Command(BaseCommand):
    help = "Listens to counter updates"

    # def add_arguments(self, parser):
    #     parser.add_argument("counter_ids", nargs="+", type=int)
    
    async def listener(self):
        channel_layer = get_channel_layer()
        channel_group = "counter_1"
        for i in range(5):
            await channel_layer.group_send(
                channel_group, 
                {"type": "test", "message": "hello from command"}
            )
            await asyncio.sleep(1)


    def handle(self, *args, **options):
        # for counter_id in options['counter_ids']:
        #     try:
        #         count = CountProcess.objects.get(pk=counter_id)
        #     except CountProcess.DoesNotExist:
        #         raise CommandError(f'CountProcess {counter_id} does not exist')

        #     channel_layer = get_channel_layer()
        #     channel_group = f"counter_{counter_id}"
        #     async_to_sync(channel_layer.group_send)(
        #         channel_group, {"type": "test", "message": "hello from command"}
        #     )

        asyncio.run(self.listener())