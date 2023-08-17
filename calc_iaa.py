import os
import argparse
import json
import numpy as np
import pandas as pd
import pingouin as pg

def get_iaa(human_results,
            model_results,
            model_results_reverse,
            method="icc_1",
            example_nums=80, ):

    assert method in ["icc_1", "icc_2"]

    if method == "icc_1":
        icc = 0
        rt1 = []
        rt2 = []
        rt3 = []
        rt4 = []
        rt5 = []
        for model_result in model_results[:example_nums]:
            for model_role in model_result["evaluation"]:
                if model_role["role"] == "General Public":
                    rt1.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt1.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "News Author":
                    rt3.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt3.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "Psychologist":
                    rt4.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt4.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "Scientist":
                    rt5.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt5.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                else:
                    rt2.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt2.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
        for model_result in model_results_reverse[:example_nums]:
            for model_role in model_result["evaluation"]:
                if model_role["role"] == "General Public":
                    rt1.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt1.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "News Author":
                    rt3.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt3.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "Psychologist":
                    rt4.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt4.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "Scientist":
                    rt5.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt5.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                else:
                    rt2.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt2.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
        
        data = list(zip(rt1, rt2, rt3, rt4, rt5))
        print(data)
        ratings = np.array(data)
        n = ratings.shape[0]
        k = ratings.shape[1]
        SStotal = np.sum((ratings - np.mean(ratings))**2)
        MSwithin = SStotal / (n * (k - 1))
        MSbetween = np.sum((np.mean(ratings, axis=1) - np.mean(ratings))**2) / (k - 1)
        icc = (MSbetween - MSwithin) / (MSbetween + (k - 1) * MSwithin)
        print("icc1:", icc)
        return icc
        
    elif method == "icc_2":
        icc = 0
        rt1 = []
        rt2 = []
        rt3 = []
        rt4 = []
        rt5 = []
        total_num = 0
        for model_result in model_results[:example_nums]:
            print("num:", total_num)
            total_num = total_num + 1
            for model_role in model_result["evaluation"]:
                if model_role["role"] == "General Public":
                    rt1.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt1.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "News Author":
                    rt3.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt3.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "Psychologist":
                    rt4.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt4.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                elif model_role["role"] == "Scientist":
                    rt5.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt5.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
                else:
                    rt2.append(float(model_role['evaluation'].split("\n")[-2].split("The score of Assistant 1:")[-1]))
                    rt2.append(float(model_role['evaluation'].split("\n")[-1].split("The score of Assistant 2:")[-1]))
        print(rt1)
        print(rt2)
        print(rt3)
        print(rt4)
        print(rt5)
        data = list(zip(rt1, rt2, rt3, rt4, rt5))
        print(data)
        ratings = np.array(data)
        n = ratings.shape[0]
        k = ratings.shape[1]
        SStotal = np.sum((ratings - np.mean(ratings))**2)
        MSwithin = SStotal / (n * (k - 1))
        MSbetween = np.sum((np.mean(ratings, axis=1) - np.mean(ratings))**2) / (k - 1)
        icc = (MSbetween - MSwithin) / (MSbetween + (k - 1) * MSwithin)
        print("icc2:", icc)
        return icc
        
    else:
        return 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--human_results_path", default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data"
                                                        "/test.json")
    parser.add_argument("--model_results_path",
                        default="./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/five_different_role/calc_score_comparison/gpt_35_0301")
    parser.add_argument("--model_results_reverse_path",
                        default="./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/five_different_role/calc_score_comparison_reverse/gpt_35_0301")
    parser.add_argument("--output_path", default="./outputs/llm_eval/test")
    parser.add_argument("--ensemble_method", default="icc_1")

    args = parser.parse_args()

    with open(args.human_results_path) as f:
        human_results = json.load(f)
    with open(os.path.join(args.model_results_path, "pair_comparison_results.json")) as f:
        model_results = json.load(f)
    with open(os.path.join(args.model_results_reverse_path, "pair_comparison_results.json")) as f:
        model_results_reverse = json.load(f)

    iaa = get_iaa(human_results=human_results,
                model_results=model_results,
                model_results_reverse=model_results_reverse,
                method=args.ensemble_method,
                example_nums=80,
                )

    print(iaa)