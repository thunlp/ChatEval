import os
import json
import argparse
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import pearsonr, spearmanr, kendalltau
import json
from tabulate import tabulate
import pandas as pd
import re


def get_model_results_evaluation(method="average", evaluations=None, aspect=None) -> float:
    # since we have multi_role, choose the aggregate method, and the aspect to return

    aspect_results = []

    for role_ins in evaluations:
        # print(role)
        # evaluation = role_ins["evaluation"].split("\n")
        # for result in evaluation:
        #     try:
        #         aspect_results.append(float(result))
        #     except BaseException as e:
        #         print(e)
        evaluation = role_ins["evaluation"].split("\n")
        result = evaluation[-1][-1]
        try:
            aspect_results.append(float(result))
        except BaseException as e:
            print(e)

    if len(aspect_results) == 0:
        raise ValueError(f"skip this line:{aspect}")

    if method != "average":
        raise ValueError("check if method is average")

    return sum(aspect_results) / len(aspect_results)

def correlation_cal(human_metric, human_results, model_results) -> pd.DataFrame:
    print(f'Human metric: {human_metric}')

    assert human_metric in ['engagingness', 'naturalness', 'coherence', 'groundedness']

    result_in_file = ""

    if human_metric == 'engagingness':
        result_in_file = "Engaging"
    elif human_metric == 'naturalness':
        result_in_file = "Natural"
    elif human_metric == 'coherence':
        result_in_file = "Maintains Context"
    elif human_metric == 'groundedness':
        result_in_file = "Uses Knowledge"

    auto_metrics = [f"model_{human_metric}"]

    headers = ['metric', 'spearman', 'pearsonr', 'kendalltau']
    metric_with_corr = []

    for metric in auto_metrics:
        correlations = []
        model_num = len(human_results)
        for instance_index in range(len(human_results[0]))[:60]:
            target_scores = []
            prediction_scores = []
            for model_index in range(model_num)[:6]:
                try:
                    prediction_scores.append(get_model_results_evaluation(
                        evaluations=model_results[model_index][instance_index]["evaluation"],
                        aspect=human_metric))
                    if len(human_results[model_index][instance_index][result_in_file]) == 0:
                        raise ValueError(f"skip this line: {human_metric}")
                    target_score = sum(human_results[model_index][instance_index][result_in_file]) / len(human_results[model_index][instance_index][result_in_file])
                    target_scores.append(target_score)
                except BaseException as e:
                    print(e)
                    continue

            if len(set(prediction_scores)) == 1 or len(set(target_scores)) == 1:
                continue

            if len(prediction_scores) < 2 or len(target_scores) < 2:
                continue

            correlations.append([
                spearmanr(target_scores, prediction_scores)[0],
                pearsonr(target_scores, prediction_scores)[0],
                kendalltau(target_scores, prediction_scores)[0],
            ])

        corr_mat = np.array(correlations)
        spearman, pearman, ktau = np.mean(corr_mat[:, 0]), np.mean(corr_mat[:, 1]), np.mean(corr_mat[:, 2])
        metric_with_corr.append([metric, spearman, pearman, ktau])

    pd_results = pd.DataFrame.from_records(metric_with_corr)

    return pd_results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--human_results_path", default="./agentverse/tasks/llm_eval/data/topical_chat/preprocessed_data"
                                                        "/human_results.json")


    parser.add_argument("--model_results_path", default="./outputs/llm_eval/gpt4_yjx/topical/sig")
    parser.add_argument("--model_results_post_path", default="thought")

    # gt_sysn_results.json

    parser.add_argument("--output_path", default="./outputs/llm_eval/gpt4_yjx/topical/sig")

    args = parser.parse_args()

    with open(args.human_results_path) as f:
        human_results = json.load(f)

    final_pd = pd.DataFrame.from_records({})
    # "naturalness" "coherence", "engagingness" "groundedness"
    for aspect in ["naturalness", "coherence", "engagingness", "groundedness"]:
    # for aspect in ["naturalness"]:
        with open(os.path.join(args.model_results_path,
                               aspect,
                               args.model_results_post_path,
                               "gt_sysn_results.json")) as f:
            model_results = json.load(f)

        final_pd = pd.concat([final_pd, correlation_cal(aspect, human_results, model_results)])

    final_pd.columns = ['metric', 'spearman', 'pearsonr', 'kendalltau']

    print(
        tabulate(final_pd, headers=['metric', 'spearman', 'pearsonr', 'kendalltau'], showindex=False, tablefmt="psql"))
    with open(os.path.join(args.output_path, "roleless_correlation_results.json"), 'w') as f:
        json.dump(final_pd.to_dict(orient='records'), f, indent=4)
    final_pd.to_excel(os.path.join(args.output_path, "roleless_correlation_results.xlsx"), index=False)