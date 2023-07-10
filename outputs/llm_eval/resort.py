import json
import re

with open("./test/gt_ours_results.json") as f:
    gt_ours = json.load(f)

with open("./test/gt_origin_results.json") as f:
    gt_origin = json.load(f)

ours_relevance = 0
ours_consistency = 0
ours_fluency = 0
ours_coherence = 0

origin_relevance = 0
origin_consistency = 0
origin_fluency = 0
origin_coherence = 0

for ins in gt_ours:

    results = ins["evaluation"].split("\n")

    ours_relevance += int(re.search(r"Relevance: (\d+)", results[0]).groups(0)[0])
    ours_consistency += int(re.search(r"Consistency: (\d+)", results[1]).groups(0)[0])
    ours_fluency += int(re.search(r"Fluency: (\d+)", results[2]).groups(0)[0])
    ours_coherence += int(re.search(r"Coherence: (\d+)", results[3]).groups(0)[0])

for ins in gt_origin:

    results = ins["evaluation"].split("\n")

    origin_relevance += int(re.search(r"Relevance: (\d+)", results[0]).groups(0)[0])
    origin_consistency += int(re.search(r"Consistency: (\d+)", results[1]).groups(0)[0])
    origin_fluency += int(re.search(r"Fluency: (\d+)", results[2]).groups(0)[0])
    origin_coherence += int(re.search(r"Coherence: (\d+)", results[3]).groups(0)[0])

ours_relevance /= len(gt_ours)
ours_consistency /= len(gt_ours)
ours_fluency /= len(gt_ours)
ours_coherence /= len(gt_ours)

origin_relevance /= len(gt_origin)
origin_consistency /= len(gt_origin)
origin_fluency /= len(gt_origin)
origin_coherence /= len(gt_origin)

scores = {}

scores["ours_relevance"] = ours_relevance
scores["ours_consistency"] = ours_consistency
scores["ours_fluency"] = ours_fluency
scores["ours_coherence"] = ours_coherence

scores["origin_relevance"] = origin_relevance
scores["origin_consistency"] = origin_consistency
scores["origin_fluency"] = origin_fluency
scores["origin_coherence"] = origin_coherence

print(scores)