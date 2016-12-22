outputs = []
crontable = []

from rtmbot.core import Plugin

class MotivationPlugin(Plugin):

	def process_message(self, data):
		if data['text'].lower().startswith("!m"):
			self.outputs.append([
				data['channel'],
				"Great job!"
				])