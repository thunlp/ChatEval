import os
import json

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["all_proxy"] = "socks5://127.0.0.1:7890"

from agentverse.agentverse import AgentVerse
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--task", type=str, default="llm_eval/single_role/pair_comparison/")
parser.add_argument("--data_path", type=str, default="./agentverse/tasks/llm_eval/data/preprocessed_data/test.json")
parser.add_argument("--output_dir", type=str, default="./outputs/llm_eval/test/")

args = parser.parse_args()

with open(args.data_path) as f:
    data = json.load(f)


agentverse = AgentVerse.from_task(args.task)

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