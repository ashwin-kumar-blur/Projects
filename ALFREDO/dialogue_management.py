from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
from rasa_core.agent import Agent
from rasa_core.channels.console import CmdlineInput
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter


logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'domain.yml',
					model_path = './models/dialogue',
					training_data = './data/stories.md'):

	agent = Agent(domain_file, policies = [MemoizationPolicy(max_history=2),
			 KerasPolicy(epochs = 500, batch_size=10)])
	data = agent.load_data(training_data)
	agent.train(
		data,
		augmentation_factor = 50,
		validation_split = 0.2)
	agent.persist(model_path)
	return agent

def run_bot(serve_forever = True):
	interpreter = RasaNLUInterpreter('./models/current/nlu/')
	agent = Agent.load('./models/dialogue/', interpreter = interpreter)
	if serve_forever:
		agent.handle_channels([CmdlineInput()])
	return agent

if __name__ == '__main__':
	train_dialogue()
	run_bot()
