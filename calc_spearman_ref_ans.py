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
        evaluation = role_ins["evaluation"].split("\n")
        for result in evaluation:
            if result.lower().startswith(aspect):
                pattern = fr"(?i){aspect}:\s*(\d+)"
                aspect_results.append(int(re.search(pattern, result).group(1)))

    # if len(aspect_results) != 3:
    #     print("1")
    if len(aspect_results) == 0:
        # skip this results
        # print("get wrong results, skip this line")
        raise ValueError("skip this line")
        # aspect_results.append(0)

    if method != "average":
        raise ValueError("check if method is average")

    return sum(aspect_results) / len(aspect_results)


def dataset_level_correlation_summeval(human_metric, human_results, model_results) -> pd.DataFrame:
    print(f'Human metric: {human_metric}')

    assert human_metric in ['relevance', 'consistency', 'fluency', 'coherence']

    # with open('data/summeval.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    # auto_metrics = ['rouge1_f', 'rouge2_f', 'rougel_f', 'bert_score_f', 'mover_score', 'prism_src_hypo',
    #                 'bart_score_src_hypo', 'bart_score_cnn_src_hypo', 'bart_score_para_src_hypo',
    #                 'chatgpt_%s' % human_metric]

    auto_metrics = [f"model_{human_metric}"]

    headers = ['metric', 'spearman', 'pearsonr', 'kendalltau']
    metric_with_corr = []

    for metric in auto_metrics:
        correlations = []

        target_scores = []
        prediction_scores = []

        model_num = len(human_results)
        # TODO now we just tust the first models' output
        for model_index in range(model_num)[:1]:

            # TODO now we just tust the first 16 instance
            for instance_index in range(len(human_results[0]))[:16]:
                
                try:
                    prediction_scores.append(get_model_results_evaluation(evaluations=model_results[model_index][instance_index]["evaluation"],
                                                                          aspect=human_metric))
                    target_scores.append(human_results[model_index][instance_index]["evaluation"][human_metric])
                    
                except BaseException as e:
                    print(e)
                    continue

                    

            # if len(set(prediction_scores)) == 1 or len(set(target_scores)) == 1:
            #     continue

        correlations.append([
            spearmanr(target_scores, prediction_scores)[0],
            pearsonr(target_scores, prediction_scores)[0],
            kendalltau(target_scores, prediction_scores)[0],
        ])

        corr_mat = np.array(correlations)
        spearman, pearman, ktau = np.mean(corr_mat[:, 0]), np.mean(corr_mat[:, 1]), np.mean(corr_mat[:, 2])
        metric_with_corr.append([metric, spearman, pearman, ktau])

    # print(tabulate(metric_with_corr, headers=headers, tablefmt='simple'))
    pd_results = pd.DataFrame.from_records(metric_with_corr)
    # pd_results.columns = headers

    return pd_results


def sample_level_correlation_summeval(human_metric, human_results, model_results) -> pd.DataFrame:
    print(f'Human metric: {human_metric}')

    assert human_metric in ['relevance', 'consistency', 'fluency', 'coherence']

    # with open('data/summeval.json', 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    # auto_metrics = ['rouge1_f', 'rouge2_f', 'rougel_f', 'bert_score_f', 'mover_score', 'prism_src_hypo',
    #                 'bart_score_src_hypo', 'bart_score_cnn_src_hypo', 'bart_score_para_src_hypo',
    #                 'chatgpt_%s' % human_metric]

    auto_metrics = [f"model_{human_metric}"]

    headers = ['metric', 'spearman', 'pearsonr', 'kendalltau']
    metric_with_corr = []

    for metric in auto_metrics:
        correlations = []

        target_scores = []
        prediction_scores = []

        model_num = len(human_results)
        # TODO now we just tust the first models' output
        for model_index in range(model_num)[:1]:

            # TODO now we just tust the first 16 instance
            for instance_index in range(len(human_results[0]))[:16]:

                try:
                    prediction_scores.append(get_model_results_evaluation(
                        evaluations=model_results[model_index][instance_index]["evaluation"],
                        aspect=human_metric))
                    target_scores.append(human_results[model_index][instance_index]["evaluation"][human_metric])

                except BaseException as e:
                    print(e)
                    continue

            # if len(set(prediction_scores)) == 1 or len(set(target_scores)) == 1:
            #     continue

        correlations.append([
            spearmanr(target_scores, prediction_scores)[0],
            pearsonr(target_scores, prediction_scores)[0],
            kendalltau(target_scores, prediction_scores)[0],
        ])

        corr_mat = np.array(correlations)
        spearman, pearman, ktau = np.mean(corr_mat[:, 0]), np.mean(corr_mat[:, 1]), np.mean(corr_mat[:, 2])
        metric_with_corr.append([metric, spearman, pearman, ktau])

    # print(tabulate(metric_with_corr, headers=headers, tablefmt='simple'))
    pd_results = pd.DataFrame.from_records(metric_with_corr)
    # pd_results.columns = headers

    return pd_results



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--human_results_path", default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data"
                                                        "/human_results.json")
    parser.add_argument("--model_results_path", default="./outputs/llm_eval/nlg_eval/multi_role/only_static_assign"
                                                        "/base_setting/3Round/test_gpt3.5_thoughtbefore/gt_sysn_results.json")
    parser.add_argument("--output_path", default="./outputs/llm_eval/nlg_eval/multi_role/only_static_assign"
                                                 "/base_setting/3Round/test_gpt3.5_thoughtbefore/")

    # parser.add_argument("--human_results_path", default="./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data"
    #                                                     "/human_results.json")
    # parser.add_argument("--model_results_path", default="./outputs/llm_eval/nlg_eval/single_role/multi_role_prompt_but1role"
    #                                                     "/base_setting/General_Public/test_gpt3.5_thoughtbefore/gt_sysn_results.json")
    # parser.add_argument("--output_path", default="./outputs/llm_eval/nlg_eval/single_role/multi_role_prompt_but1role"
    #                                              "/base_setting/General_Public/test_gpt3.5_thoughtbefore/")



    args = parser.parse_args()

    with open(args.human_results_path) as f:
        human_results = json.load(f)
    with open(args.model_results_path) as f:
        model_results = json.load(f)

    final_pd = pd.DataFrame.from_records({})

    for aspect in ['relevance', 'consistency', 'fluency', 'coherence']:
        final_pd = pd.concat([final_pd, dataset_level_correlation_summeval(aspect, human_results, model_results)])

    final_pd.columns = ['metric', 'spearman', 'pearsonr', 'kendalltau']

    print(tabulate(final_pd, headers=['metric', 'spearman', 'pearsonr', 'kendalltau'], showindex=False, tablefmt="psql"))
    with open(os.path.join(args.output_path, "correlation_results.json"), 'w') as f:
        json.dump(final_pd.to_dict(orient='records'), f, indent=4)
    final_pd.to_excel(os.path.join(args.output_path, "correlation_results.xlsx"), index=False)