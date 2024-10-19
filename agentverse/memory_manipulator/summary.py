from __future__ import annotations

from abc import abstractmethod
from typing import Dict, List, TYPE_CHECKING
from string import Template

from pydantic import BaseModel, Field
import logging
import bdb
from openai import RateLimitError


from agentverse.message import Message

from agentverse.memory_manipulator import BaseMemoryManipulator
from agentverse.memory.base import BaseMemory
from agentverse.llms.base import BaseLLM

from . import memory_manipulator_registry


if TYPE_CHECKING:
    from agentverse.agents.base import BaseAgent


@memory_manipulator_registry.register("summary")
class SummaryMemoryManipulator(BaseMemoryManipulator):

    memory: BaseMemory = None
    agent: BaseAgent = None
    llm: BaseLLM
    summary_template: str = None

    buffer: str = ""

    def __init__(self, *args, **kwargs):
        from agentverse.initialization import load_llm
        llm_config = kwargs.pop("llm")
        llm = load_llm(llm_config)
        super().__init__(llm=llm, *args, **kwargs)

    def manipulate_memory(self):

        if len(self.agent.memory.messages) == 0:
            # nothing to summary
            return
        else:

            new_lines = ""
            for message in self.agent.memory.messages:
                new_lines += f"[{message.sender}] : "
                new_lines += message.content
                new_lines += "\n"

            prompt = self._fill_in_prompt_template(new_lines)

            should_break = False
            while True:

                for i in range(3):
                    try:
                        final_prompt = ""
                        response = self.llm.generate_response(prompt, self.memory.messages, final_prompt)
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
                            logging.error(f"cur_agent's {self.agent.name} summary process failed")
                            logging.warning("Retrying...")
                            continue
                else:
                    logging.error(f"After {self.max_retry} failed try, end the loop")
                    break
                if should_break:
                    break
                else:
                    continue

            summary = Message(
                content=response.content,
                sender="Summarizer",
                receiver={self.agent.name})

            self.buffer = response.content
            self.memory.add_message([summary])

            logging.info(f"Summarizer generating summary for previous talk : {response.content}")

            return summary

    def _fill_in_prompt_template(self, new_lines: str) -> str:
        """Fill in the prompt template with the given arguments.

        SummaryMemory supports the following arguments:
        - summary: The summary so far.
        - new_lines: The new lines to be added to the summary.
        """
        input_arguments = {"summary": self.buffer, "new_lines": new_lines}
        return Template(self.summary_template).safe_substitute(input_arguments)

    def reset(self) -> None:
        self.buffer = ""
