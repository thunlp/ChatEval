from __future__ import annotations

import re
from typing import Union

from agentverse.parser import OutputParser, LLMResult

from agentverse.utils import AgentAction, AgentFinish

from agentverse.parser import OutputParserError, output_parser_registry


@output_parser_registry.register("llm_eval/multi_role/only_static_assign/base_setting")
class LLMEvalMultiParser(OutputParser):
    def parse(self, output: LLMResult) -> Union[AgentAction, AgentFinish]:
        text = output.content
        cleaned_output = text.strip()
        cleaned_output = re.sub(r"\n+", "\n", cleaned_output)
        # cleaned_output = cleaned_output.split("\n")

        # TODO chimin modify here

        if "This is my final judgement" in cleaned_output:
            cleaned_output = cleaned_output.split("\n")

            if not (
                len(cleaned_output) == 6
                and cleaned_output[0].startswith("This is my final judgement")
                and cleaned_output[1].startswith("Thought:")
                and cleaned_output[2].startswith("Relevance:")
                and cleaned_output[3].startswith("Consistency:")
                and cleaned_output[4].startswith("Fluency:")
                and cleaned_output[5].startswith("Coherence:")
            ):
                raise OutputParserError(text)

        return AgentFinish({"output": text}, text)
