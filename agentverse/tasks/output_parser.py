from __future__ import annotations

import re
from typing import Union

from agentverse.parser import OutputParser, LLMResult

from agentverse.utils import AgentAction, AgentFinish

from agentverse.parser import OutputParserError, output_parser_registry


@output_parser_registry.register("")
class LLMEvalParser(OutputParser):
    def parse(self, output: LLMResult, cnt_turn: int, max_turns: int, agent_nums: int) -> Union[AgentAction, AgentFinish]:
        text = output.content
        cleaned_output = text.strip()
        cleaned_output = re.sub(r"\n+", "\n", cleaned_output)
        cleaned_output = cleaned_output.split("\n")

        # TODO chimin modify here

        if cnt_turn >= max_turns - agent_nums:
            # if not cleaned_output[0].startswith("Answer") :
            if not (cleaned_output[-2].startswith("The score of Assistant 1:") and \
                    cleaned_output[-1].startswith("The score of Assistant 2:")):
                raise OutputParserError(text)

        return AgentFinish({"output": text}, text)
