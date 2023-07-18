from __future__ import annotations

import re
from typing import Union

from agentverse.parser import OutputParser, LLMResult

from agentverse.utils import AgentAction, AgentFinish

from agentverse.parser import OutputParserError, output_parser_registry


@output_parser_registry.register("llm_eval/multi_role/only_static_assign/faireval/three_turns_sequential/direct_pair_comparison")
class LLMEvalParser(OutputParser):
    def parse(self, output: LLMResult, cnt_turn: int, max_turns: int, agent_nums: int) -> Union[AgentAction, AgentFinish]:
        text = output.content
        cleaned_output = text.strip()
        cleaned_output = re.sub(r"\n+", "\n", cleaned_output)
        cleaned_output = cleaned_output.split("\n")

        # TODO chimin modify here

        if cnt_turn >= max_turns - agent_nums:

            # if not cleaned_output[0].startswith("Answer") :
            if not cleaned_output[0] in ["Assistant 1", "Assistant 2", "Same"]:
                raise OutputParserError(text)

        return AgentFinish({"output": text}, text)
