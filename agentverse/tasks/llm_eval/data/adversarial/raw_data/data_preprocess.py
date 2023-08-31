import json
import os

test = []
instances = []

# summjson.loads data has output from 16 models
with open("dataset.json", encoding="utf-8") as f:
    lines = json.load(f)
    for line in lines:
        instances.append(line)

for ins_id in range(len(instances)):
    to_append = {}
    to_append["question_id"] = ins_id
    to_append["question"] = instances[ins_id]['input']
    to_append["response"] = {}
    to_append["response"]["output_1"] = instances[ins_id]["output_1"]
    to_append["response"]["output_2"] = instances[ins_id]["output_2"]

    if instances[ins_id]["label"] == 1:
        to_append["human_results"] = "output_1"
    elif instances[ins_id]["label"] == 2:
        to_append["human_results"] = "output_2"
    else:
        raise ValueError("check your label")

    test.append(to_append)


os.makedirs("../preprocessed_data", exist_ok=True)

with open("../preprocessed_data/test.json", "w") as f:
    json.dump(test, f, indent=4)

pass

# with open("./test_gt_origin.txt") as f:
#     test_gt = f.readlines()
#     print(test_gt)