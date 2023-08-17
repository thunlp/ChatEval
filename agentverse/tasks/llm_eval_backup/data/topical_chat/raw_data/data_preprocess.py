import json


test = []

with open("topicalchat.json", encoding="utf-8") as f:
    inss = json.load(f)
    for ins in inss:
        to_append = {}
        to_append["src"] = ins["context"]
        to_append["fact"] = ins["fact"]
        to_append["outputs"] = ins["responses"]
        test.append(to_append)

new_form_test = []

for model_index in range(6):
    to_append = []
    for ins_index in range(60):
        cur_ins = test[ins_index]
        tmp = {}
        tmp["src"] = cur_ins["src"]
        tmp["fact"] = cur_ins["fact"]
        tmp["outputs"] = cur_ins["outputs"][model_index]["response"]
        tmp["Understandable"] = cur_ins["outputs"][model_index]["Understandable"]
        tmp["Natural"] = cur_ins["outputs"][model_index]["Natural"]
        tmp["Maintains Context"] = cur_ins["outputs"][model_index]["Maintains Context"]
        tmp["Engaging"] = cur_ins["outputs"][model_index]["Engaging"]
        tmp["Uses Knowledge"] = cur_ins["outputs"][model_index]["Uses Knowledge"]
        tmp["Overall"] = cur_ins["outputs"][model_index]["Overall"]
        to_append.append(tmp)
    new_form_test.append(to_append)

with open("../preprocessed_data/human_results.json", "w") as f:
    json.dump(new_form_test, f, indent=4)

pass

# with open("../preprocessed_data/test.json", "w") as f:
#     json.dump(test, f, indent=4)

# pass
