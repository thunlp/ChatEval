from __future__ import annotations

from typing import TYPE_CHECKING, Any

from . import visibility_registry as VisibilityRegistry
from .base import BaseVisibility

if TYPE_CHECKING:
    from agentverse.environments import BaseEnvironment


@VisibilityRegistry.register("llmeval_blind_judge")
class LLMEVALVisibility(BaseVisibility):
    """All the messages can be seen by all the agents"""

    def update_visible_agents(self, environment: BaseEnvironment):

        agents_nums = len(environment.agents)
        discussion_turns = environment.max_turns

        # import pdb
        # pdb.set_trace()

        if environment.cnt_turn >= discussion_turns - agents_nums:
            for agent in environment.agents:
                agent.set_receiver(set({agent.name}))

