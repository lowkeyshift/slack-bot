
from __future__ import print_function
from __future__ import unicode_literals

from rtmbot.core import Plugin
import random
import re
from slackclient import SlackClient
outputs = []
crontable = []

trigger_message = re.compile(r'^!m\s?(\<@(?P<user>\w+)\>)?', re.I)

congratulations = [
    "Great job",
    "Amazing,",
    "You rock",
    "OMG",
    "You're awesome,"
]

group_pronouns = [
    "everyone",
    "everybody",
    "y'all",
    "mortals",
    "peeps",
    "folks",
    "minions"
]

class MotivationPlugin(Plugin):
    
    def _lookup_user(user):
        return slack_client.api_call(
            'users.info',
            user=user
            )

    def process_message(self, data):
        catch = trigger_message.match(data['text'])
        if catch:
            username = catch.groupdict()['user']
            if username is not None:
                user = _lookup_user(username)
                message = "@{}".format(user['user']['name'])
            else:
                text = data['text'][3:]
                message = text or random.choice(group_pronouns)
            self.outputs.append([
                data["channel"],
                ":tada: {} {}! :tada:".format(
                    random.choice(congratulations),
                    message
                    )
                ])