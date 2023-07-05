import json


test_gt = []
test_ours = []
test_origin = []

with open("./test_answer_true.json", encoding="utf-8") as f:
    inss = json.load(f)
    for ins in inss[:51]:
        try:
            test_gt.append(ins["report"])
            test_ours.append(ins["llama_answer"])
        except Exception as e:
            print(e)


with open("./test_llama_origin.txt") as f:
    inss = f.readlines()
    for ins in inss[:51]:
        test_origin.append(ins)


final = []

for gt, ours, origin in zip(test_gt, test_ours, test_origin):
    final.append({"gt": gt, "ours": ours, "origin": origin})

with open("../preprocessed_data/test.json", "w") as f:
    json.dump(final, f, indent=4)

pass




# with open("./test_gt_origin.txt") as f:
#     test_gt = f.readlines()
#     print(test_gt)