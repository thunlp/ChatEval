# from .agent import Agent
from agentverse.registry import Registry

agent_registry = Registry(name="AgentRegistry")

from .base import BaseAgent
from .conversation_agent import ConversationAgent

from .llm_eval_agent import LLMEvalAgent
from .llm_eval_multi_agent import LLMEvalAgent
from .llm_eval_multi_agent_con import LLMEvalAgent