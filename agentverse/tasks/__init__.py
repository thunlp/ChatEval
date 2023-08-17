import os
import yaml

from .math_problem_2players_tools.output_parser import MathProblem2PlayersToolsParser
from .nlp_classroom_3players.output_parser import NlpClassroom3PlayersParser
from .nlp_classroom_9players.output_parser import NlpClassroom9PlayersParser
from .nlp_classroom_3players_withtool.output_parser import (
    NlpClassroom3PlayersWithtoolParser,
)
from .nlp_classroom_9players_group.output_parser import NlpClassroom9PlayersGroupParser
from .db_diag.output_parser import DBDiag

from .prisoner_dilema.output_parser import PrisonerDilemaParser
from .prisoner_dilema.base.output_parser import PrisonerDilemaParser
from .prisoner_dilema.s1_p_r.output_parser import PrisonerDilemaParser
from .prisoner_dilema.police.output_parser import PrisonerDilemaParser
from .prisoner_dilema.s2_p_r.output_parser import PrisonerDilemaParser
from .prisoner_dilema.no_goal_s1.output_parser import PrisonerDilemaParser

from .traffic_junction.output_parser import TrafficParser


from .pokemon.output_parser import PokemonParser
from .alice_home.output_parser import AliceHomeParser
from .sde_team.sde_team_3players_nolc.output_parser import SdeTeamParser
from .sde_team.sde_team_2players_nolc.output_parser import SdeTeamGivenTestsParser

from .llm_eval.multi_role.only_static_assign.base_setting.output_parser import LLMEvalMultiParser
from .llm_eval.single_role.multi_role_prompt_but1role.base_setting.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.multi_role_prompt_but1role.base_setting.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.multi_role_prompt_but1role.base_setting.News_Author.output_parser import LLMEvalParser


from .llm_eval.single_role.geval_summeval_separate.coherence.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.coherence.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.coherence.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.coherence.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.geval_summeval_separate.consistency.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.consistency.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.consistency.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.consistency.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.geval_summeval_separate.fluency.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.fluency.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.fluency.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.fluency.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.geval_summeval_separate.relevance.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.relevance.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.relevance.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.geval_summeval_separate.relevance.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.faireval.direct_pair_comparison.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.faireval.two_turns_sequential.direct_pair_comparison.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.faireval.three_turns_sequential.direct_pair_comparison.output_parser import LLMEvalParser

from .llm_eval.multi_role.only_static_assign.geval_summeval_separate.two_turns_sequential.coherence.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.geval_summeval_separate.two_turns_sequential.consistency.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.geval_summeval_separate.two_turns_sequential.fluency.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.geval_summeval_separate.two_turns_sequential.relevance.thought.output_parser import LLMEvalParser

from .llm_eval.multi_role.only_static_assign.geval_summeval_separate.three_turns_sequential.coherence.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.geval_summeval_separate.three_turns_sequential.fluency.thought.output_parser import LLMEvalParser

from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.coherence.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.engagingness.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.groundedness.thought.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.naturalness.thought.output_parser import LLMEvalParser

from .llm_eval.single_role.topical_chat.coherence.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.coherence.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.coherence.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.topical_chat.engagingness.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.engagingness.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.engagingness.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.topical_chat.groundedness.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.groundedness.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.groundedness.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.topical_chat.naturalness.Critic.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.naturalness.General_Public.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.naturalness.News_Author.output_parser import LLMEvalParser

from .llm_eval.single_role.topical_chat.coherence.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.engagingness.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.groundedness.thought.output_parser import LLMEvalParser
from .llm_eval.single_role.topical_chat.naturalness.thought.output_parser import LLMEvalParser

from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.coherence.roleless.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.engagingness.roleless.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.groundedness.roleless.output_parser import LLMEvalParser
from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.naturalness.roleless.output_parser import LLMEvalParser

# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.coherence.rolethree.output_parser import LLMEvalParser
# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.engagingness.rolethree.output_parser import LLMEvalParser
# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.groundedness.rolethree.output_parser import LLMEvalParser
# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.naturalness.rolethree.output_parser import LLMEvalParser

# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.coherence.proless.output_parser import LLMEvalParser
# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.engagingness.proless.output_parser import LLMEvalParser
# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.groundedness.proless.output_parser import LLMEvalParser
# from .llm_eval.multi_role.only_static_assign.topical_chat.two_turns_sequential.naturalness.proless.output_parser import LLMEvalParser