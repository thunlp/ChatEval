import json


test = []
question = []
gpt35 = []
gpt4 = []
vicuna = []
alpaca = []
answer = []

# summjson.loads data has output from 16 models
with open("question.jsonl", encoding="utf-8") as f:
    for line in f:
        question.append(json.loads(line))

with open("answer/answer_gpt35.jsonl", encoding="utf-8") as f:
    for line in f:
        gpt35.append(json.loads(line))

with open("answer/answer_gpt-4.jsonl", encoding="utf-8") as f:
    for line in f:
        gpt4.append(json.loads(line))

with open("answer/answer_vicuna-13b.jsonl", encoding="utf-8") as f:
    for line in f:
        vicuna.append(json.loads(line))

with open("answer/answer_alpaca-13b.jsonl", encoding="utf-8") as f:
    for line in f:
        alpaca.append(json.loads(line))

with open("review/review_gpt35_vicuna-13b_human.txt", encoding="utf-8") as f:
    for line in f:
        answer.append(line.split("\n")[0])

for ins_id in range(80):
    to_append = {}
    to_append["question_id"] = ins_id
    to_append["question"] = question[ins_id]['text']
    to_append["category"] = question[ins_id]['category']
    to_append["response"] = {}
    to_append["response"]["gpt4"] = gpt4[ins_id]["text"]
    to_append["response"]["gpt35"] = gpt35[ins_id]["text"]
    to_append["response"]["vicuna"] = vicuna[ins_id]["text"]
    to_append["response"]["alpaca"] = alpaca[ins_id]["text"]

    if answer[ins_id] == 'CHATGPT':
        to_append["human_results"] = "gpt35"
    elif answer[ins_id] == 'VICUNA13B':
        to_append["human_results"] = "vicuna"
    elif answer[ins_id] == "TIE":
        to_append["human_results"] = "tie"
    else:
        raise ValueError("check")

    test.append(to_append)

with open("../preprocessed_data/test.json", "w") as f:
    json.dump(test, f, indent=4)

pass

# with open("./test_gt_origin.txt") as f:
#     test_gt = f.readlines()
#     print(test_gt)