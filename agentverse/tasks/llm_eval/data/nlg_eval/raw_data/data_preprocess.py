import json


test = []

# summeval data has output from 16 models
with open("summeval.json", encoding="utf-8") as f:
    inss = json.load(f)
    for ins_id in inss:
        ins = inss[ins_id]
        to_append = {}
        to_append["src"] = ins["src"]
        to_append["references"] = ins["ref_summs"]
        to_append["reference"] = ins["ref_summ"]
        to_append["outputs"] = []
        for sys_ins_id in ins["sys_summs"]:
            to_append["outputs"].append(ins["sys_summs"][sys_ins_id])

        test.append(to_append)

new_form_test = []

for model_index in range(16):
    to_append = []

    for ins_index in range(100):

        cur_ins = test[ins_index]
        to_append.append({
            "src": cur_ins["src"],
            "references": cur_ins["references"],
            "reference": cur_ins["reference"],
            "outputs": cur_ins["outputs"][model_index]["sys_summ"],
            "evaluation": cur_ins["outputs"][model_index]["scores"]
        })
    new_form_test.append(to_append)

with open("../preprocessed_data/human_results.json", "w") as f:
    json.dump(new_form_test, f, indent=4)

pass

# with open("../preprocessed_data/test.json", "w") as f:
#     json.dump(test, f, indent=4)
#
# pass

# with open("./test_gt_origin.txt") as f:
#     test_gt = f.readlines()
#     print(test_gt)