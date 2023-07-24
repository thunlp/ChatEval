import os
import json
from typing import List
from agentverse.message import Message


def get_evaluation(setting: str = None, messages: List[Message] = None, agent_nums: int = None) -> List[dict]:

    results = []
    if setting == "every_agent":
        # Currently 2 round, concurrent, so the response will start from messages[-3:]
        for message in messages[-agent_nums:]:
            results.append({"role": message.sender,
                            "evaluation": message.content})

    return results
