from __future__ import annotations

import logging
import bdb
from string import Template
from typing import TYPE_CHECKING, List

from agentverse.message import Message
from openai import RateLimitError

from . import agent_registry
from .base import BaseAgent

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from agentverse.environments.base import BaseEnvironment

@agent_registry.register("llm_eval_multi")
class LLMEvalAgent(BaseAgent):

    source_text: str = ""
    # for direct score
    reference_text: str = ""
    generated_text: str = ""

    # for pair comparison
    compared_text_one: str = ""
    compared_text_two: str = ""

    final_prompt: str = ""
    final_prompt_to_use: str = ""

    def step(self, env_description: str = "") -> Message:
        prompt = self._fill_prompt_template(env_description)

        parsed_response = None
        for i in range(self.max_retry):
            try:
                response = self.llm.generate_response(prompt, self.memory.messages, self.final_prompt)
                parsed_response = self.output_parser.parse(response)
                break
            except KeyboardInterrupt:
                raise
            except Exception as e:
                logging.error(e)
                logging.warning("Retrying...")
                continue

        if parsed_response is None:
            logging.error(f"{self.name} failed to generate valid response.")

        message = Message(
            content=""
            if parsed_response is None
            else parsed_response.return_values["output"],
            sender=self.name,
            receiver=self.get_receiver(),
        )
        return message

    async def astep(self, env: BaseEnvironment = None, env_description: str = "") -> Message:
        """Asynchronous version of step"""

        # TODO modify this line, if it is the final round, add some instruction in the prompt
        # you must use the following format, first give the rate of the summary of the above 4 aspects then finally give the reasoning on why you give this rate
        # Relevance:
        # Consistency:
        # Fluency:
        # Coherence:
        # Thought: (your thought)

        if env.cnt_turn >= env.max_turns - len(env.agents):
            # self.final_prompt = "Now, please give your final judgement, and you must use the following format, first start with 'This is my final judgement!' and briefly give the thought on why you give this rate, then finally give the rate of the summary of the above 4 aspects." \
            #                     "This is my final judgement!\n" \
            #                     "Thought: (your thought)\n" \
            #                     "Relevance:\n" \
            #                     "Consistency:\n" \
            #                     "Fluency:\n" \
            #                     "Coherence:\n" \
            self.final_prompt = self.final_prompt_to_use

        prompt = self._fill_prompt_template(env_description)

        parsed_response = None

        should_break = False
        while True:

            for i in range(self.max_retry):
                try:
                    response = await self.llm.agenerate_response(prompt, self.memory.messages, self.final_prompt)
                    parsed_response = self.output_parser.parse(response, env.cnt_turn, env.max_turns, len(env.agents))
                    should_break = True
                    break
                except (KeyboardInterrupt, bdb.BdbQuit):
                    raise
                except Exception as e:
                    if isinstance(e, RateLimitError):
                        logging.error(e)
                        logging.warning("Retrying Until rate limit error disappear...")
                        break
                    else:
                        logging.error(e)
                        logging.warning("Retrying...")
                        continue
            else:
                logging.error(f"After {self.max_retry} failed try, end the loop")
                break
            if should_break:
                break
            else:
                continue

        if parsed_response is None:
            logging.error(f"{self.name} failed to generate valid response.")

        message = Message(
            content=""
            if parsed_response is None
            else parsed_response.return_values["output"],
            sender=self.name,
            receiver=self.get_receiver(),
        )
        return message

    def _fill_prompt_template(self, env_description: str = "") -> str:
        """Fill the placeholders in the prompt template

        In the conversation agent, three placeholders are supported:
        - ${agent_name}: the name of the agent
        - ${env_description}: the description of the environment
        - ${role_description}: the description of the role of the agent
        - ${chat_history}: the chat history of the agent
        """
        input_arguments = {
            "agent_name": self.name,
            "env_description": env_description,
            "role_description": self.role_description,
            "source_text": self.source_text,
            "reference_text": self.reference_text,
            "generated_text": self.generated_text,
            "compared_text_one": self.compared_text_one,
            "compared_text_two": self.compared_text_two,
            "final_prompt": self.final_prompt,
            # "chat_history": self.memory.to_string(add_sender_prefix=True),
        }
        return Template(self.prompt_template).safe_substitute(input_arguments)

    def add_message_to_memory(self, messages: List[Message]) -> None:
        self.memory.add_message(messages)

    def reset(self) -> None:
        """Reset the agent"""
        self.memory.reset()
        # TODO: reset receiver
