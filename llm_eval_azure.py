import os
os.environ["OPENAI_API_KEY"] = "DUMMY"
os.environ["AZURE_OPENAI_KEY"] = "21281145da034df49bdd6744b4a7a6d1"
# always remember to put these lines at the top of your code
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["all_proxy"] = "socks5://127.0.0.1:7890"

import openai

# will reset by agentverse code, need to get again in openai.py
# openai.api_key = os.getenv("AZURE_OPENAI_KEY")
# openai.api_key = "21281145da034df49bdd6744b4a7a6d1"
openai.api_base = "https://conmmunity-openai-4.openai.azure.com/"
openai.RPM = 10

openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

# deployment_name='gpt-4-6'



import json
from string import Template
from eval_helper.get_evaluation import get_evaluation
import types

from agentverse.agentverse import AgentVerse
from argparse import ArgumentParser



parser = ArgumentParser()

# geval_summeval
# Multi_role setting
# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/base_setting")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/nlg_eval/multi_role/only_static_assign/base_setting/test_gpt3.5_thoughtbefore/")

# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/base_setting")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/nlg_eval/multi_role/only_static_assign/base_setting/test_gpt3.5_thoughtbefore/")

# Single_role setting
# parser.add_argument("--task", type=str, default="llm_eval/single_role/multi_role_prompt_but1role/base_setting/News_Author")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/nlg_eval/single_role/multi_role_prompt_but1role/base_setting/News_Author/test_gpt3.5_thoughtbefore/")

# parser.add_argument("--task", type=str, default="llm_eval/single_role/geval_summeval_separate/coherence/thought")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/test")

# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/geval_summeval_separate/three_turns_sequential/coherence/thought")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/test")

# faireval
# single
# parser.add_argument("--task", type=str, default="llm_eval/single_role/faireval/calc_score_comparison")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/single_role/faireval/calc_score_comparison_reverse")
# parser.add_argument("--reverse_input", type=bool, default=True)

# parser.add_argument("--task", type=str, default="llm_eval/single_role/faireval/calc_score_comparison")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/single_role/faireval/calc_score_comparison")
# parser.add_argument("--reverse_input", type=bool, default=False)

# multi
# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/faireval/three_turns_sequential/direct_pair_comparison")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/multi_role/only_static_assign/faireval/three_turns_sequential/direct_pair_comparison")
# parser.add_argument("--reverse_input", type=bool, default=False)

# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/calc_score_comparison")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/calc_score_comparison")
# parser.add_argument("--reverse_input", type=bool, default=False)

# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/calc_score_comparison")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/calc_score_comparison_reverse_test")
# parser.add_argument("--reverse_input", default=False, action="store_true")


parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/geval_summeval_separate/two_turns_sequential/two_different_role/consistency/thought/gpt_4")
parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json")
parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/multi_role/only_static_assign/geval_summeval_separate/two_turns_sequential/two_different_role/consistency/thought/gpt_4")
parser.add_argument("--reverse_input", default=False, action="store_true")



# medical_report
# single
# parser.add_argument("--task", type=str, default="llm_eval/single_role/medical_report/base_abnormality")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/medical_report/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/single_role/medical_report/base_abnormality")
# multi
# parser.add_argument("--task", type=str, default="llm_eval/multi_role/only_static_assign/faireval/three_turns_sequential/direct_pair_comparison")
# parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json")
# parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/multi_role/only_static_assign/faireval/three_turns_sequential/direct_pair_comparison")



args = parser.parse_args()

print(args)

os.makedirs(args.output_dir, exist_ok=True)
with open(os.path.join(args.output_dir, "args.txt"), "w") as f:
    f.writelines(str(args))


if os.path.exists(args.output_dir) and len(os.listdir(args.output_dir)) > 1 :

    raise ValueError("the output_dir is not empty, check if is expected.")

with open(args.data_path) as f:
    data = json.load(f)

agentverse = AgentVerse.from_task(args.task)

if "nlg_eval" in args.data_path or "geval_summeval_separate" in args.data_path:

    # there are 16 outputs generated from different models
    gt_sysn_output = []

    # TODO let's test 1 model's output first (ignored)
    for model_index in range(16):
        gt_sys_output = []
        # TODO let's test 16 instance first (ignored)
        for num, ins in enumerate(data[:100]):

            print(f"================================instance {num}====================================")

            # reassign the text to agents, and set final_prompt to null for debate at first round
            for agent_id in range(len(agentverse.agents)):
                agentverse.agents[agent_id].source_text = ins["src"]
                agentverse.agents[agent_id].generated_text = ins["outputs"][model_index]["sys_summ"]
                agentverse.agents[agent_id].final_prompt = ""

            agentverse.run()

            evaluation = get_evaluation(setting="every_agent", messages=agentverse.agents[0].memory.messages, agent_nums=len(agentverse.agents))

            gt_sys_output.append({"src": ins["src"],
                                  "outputs": ins["outputs"][model_index]["sys_summ"],
                                  "evaluation": evaluation})

        gt_sysn_output.append(gt_sys_output)
        # I write save func here because I do not have to wait for all models' results to be done, I can save intermediately
        os.makedirs(args.output_dir, exist_ok=True)
        with open(os.path.join(args.output_dir, "gt_sysn_results.json"), "w") as f:
            json.dump(gt_sysn_output, f, indent=4)

elif "medical_report" in args.data_path:

    if "base_abnormality" in args.task:

        gt_abnormality_output = []
        ours_abnormality_output = []

        # # TODO extract ground truth abnormality let's test the first 5 report
        # for num, ins in enumerate(data):
        #     print(f"================================instance {num}====================================")
        #     gt = ins["gt"]
        #
        #     agentverse.agents[0].generated_text = gt
        #     agentverse.run()
        #     gt_abnormality_output.append({"gt": gt,
        #                            "evaluation": agentverse.agents[0].memory.messages[0].content})
        #
        #     os.makedirs(args.output_dir, exist_ok=True)
        #     with open(os.path.join(args.output_dir, "gt_abnormality_results.json"), "w") as f:
        #         json.dump(gt_abnormality_output, f, indent=4)

        # TODO extract our model_outputs abnormality, let's test the first 5 report
        for num, ins in enumerate(data):
            print(f"================================instance {num}====================================")
            ours = ins["ours"]

            agentverse.agents[0].generated_text = ours
            agentverse.run()
            ours_abnormality_output.append({"ours": ours,
                                   "evaluation": agentverse.agents[0].memory.messages[0].content})

            os.makedirs(args.output_dir, exist_ok=True)
            with open(os.path.join(args.output_dir, "ours_abnormality_results.json"), "w") as f:
                json.dump(ours_abnormality_output, f, indent=4)

    else:
        gt_ours_output = []
        gt_origin_output = []

        for ins in data:
            gt = ins["gt"]
            ours = ins["ours"]
            origin = ins["origin"]

            agentverse.agents[0].reference_text = gt


            agentverse.agents[0].generated_text = ours
            agentverse.run()
            gt_ours_output.append({"gt": gt,
                                   "ours": ours,
                                   "evaluation": agentverse.agents[0].memory.messages[0].content})

            # agentverse.agents[0].generated_text = origin
            # agentverse.run()
            # gt_origin_output.append({"gt": gt,
            #                        "origin": origin,
            #                        "evaluation": agentverse.agents[0].memory.messages[0].content})


        os.makedirs(args.output_dir, exist_ok=True)
        with open(os.path.join(args.output_dir, "gt_ours_results.json"), "w") as f:
            json.dump(gt_ours_output, f, indent=4)
        # with open(os.path.join(args.output_dir, "gt_origin_results.json"), "w") as f:
        #     json.dump(gt_origin_output, f, indent=4)

elif "faireval" in args.data_path:

    pair_comparison_output = []

    for num, ins in enumerate(data[:80]):

        print(f"================================instance {num}====================================")

        # reassign the text to agents, and set final_prompt to null for debate at first round
        for agent_id in range(len(agentverse.agents)):
            agentverse.agents[agent_id].source_text = ins["question"]

            if args.reverse_input:
                agentverse.agents[agent_id].compared_text_one = ins["response"]["vicuna"]
                agentverse.agents[agent_id].compared_text_two = ins["response"]["gpt35"]
            else:
                agentverse.agents[agent_id].compared_text_one = ins["response"]["gpt35"]
                agentverse.agents[agent_id].compared_text_two = ins["response"]["vicuna"]

            agentverse.agents[agent_id].final_prompt = ""

        agentverse.run()

        evaluation = get_evaluation(setting="every_agent", messages=agentverse.agents[0].memory.messages, agent_nums=len(agentverse.agents))

        pair_comparison_output.append({"question": ins["question"],
                                       "response": {"gpt35": ins["response"]["gpt35"],
                                                    "vicuna": ins["response"]["vicuna"]},
                                       "evaluation": evaluation})

        os.makedirs(args.output_dir, exist_ok=True)
        with open(os.path.join(args.output_dir, "pair_comparison_results.json"), "w") as f:
            json.dump(pair_comparison_output, f, indent=4)
    # with open(os.path.join(args.output_dir, "gt_origin_results.json"), "w") as f:
    #     json.dump(gt_origin_output, f, indent=4)