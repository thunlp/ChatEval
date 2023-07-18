import os
import argparse
import json

def get_accuracy(human_results, model_results, method="single", example_nums=100):

    assert method in ["single", "majority_vote"]

    predictions = []
    targets = []

    if method == "single":
        for model_result in model_results[:example_nums]:

            try:
                prediction = model_result["evaluation"][0]['evaluation'].split("\n")[-1].split("Answer: ")[-1]
                if prediction == "Assistant 1":
                    predictions.append("gpt35")
                elif prediction == "Assistant 2":
                    predictions.append("vicuna")
                elif prediction == "Tie":
                    predictions.append("tie")

                else:
                    raise ValueError("check")
            except BaseException as e:
                predictions.append("tie")

        for human_result in human_results[:example_nums]:
            targets.append(human_result["human_results"])

        correct = 0
        for prediction, target in zip(predictions, targets):
            if prediction == target:
                correct += 1
        return correct / len(targets)

    elif method == "majority_vote":

        for model_result in model_results[:example_nums]:

            to_vote = []

            for role in model_result["evaluation"]:
                prediction = role['evaluation'].split("\n")[-1].split("Answer: ")[-1]

                try:
                    if prediction == "Assistant 1":
                        to_vote.append("gpt35")
                    elif prediction == "Assistant 2":
                        to_vote.append("vicuna")
                    elif prediction == "Tie":
                        to_vote.append("tie")

                    else:
                        raise ValueError("check")
                except BaseException as e:
                    to_vote.append("tie")

            gpt35_num, vicuna_num, tie_num = 0, 0, 0

            for ans in to_vote:
                if ans == "gpt35":
                    gpt35_num += 1
                elif ans == "vicuna":
                    vicuna_num += 1
                elif ans == "tie":
                    tie_num += 1

            dummy = [gpt35_num, vicuna_num, tie_num]

            if len(set(dummy)) == 1:
                predictions.append("tie")
            elif dummy.index(max(dummy)) == 0:
                predictions.append("gpt35")
            elif dummy.index(max(dummy)) == 1:
                predictions.append("vicuna")
            elif dummy.index(max(dummy)) == 2:
                predictions.append("tie")

        for human_result in human_results[:example_nums]:
            targets.append(human_result["human_results"])

        correct = 0
        for _, (prediction, target) in enumerate(zip(predictions, targets)):
            if prediction == target:
                correct += 1
        return correct / len(targets)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # # single
    # parser.add_argument("--human_results_path", default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data"
    #                                                     "/test.json")
    # parser.add_argument("--model_results_path", default="./outputs/llm_eval/single_role/test")
    # parser.add_argument("--output_path", default="./outputs/llm_eval/single_role/test")
    # parser.add_argument("--ensemble_method", default="single")

    # # multi
    parser.add_argument("--human_results_path", default="./agentverse/tasks/llm_eval/data/faireval/preprocessed_data"
                                                        "/test.json")
    parser.add_argument("--model_results_path", default="./outputs/llm_eval/multi_role/only_static_assign/faireval/direct_pair_comparison")
    parser.add_argument("--output_path", default="./outputs/llm_eval/multi_role/only_static_assign/faireval/direct_pair_comparison")
    parser.add_argument("--ensemble_method", default="majority_vote")


    args = parser.parse_args()

    with open(args.human_results_path) as f:
        human_results = json.load(f)
    with open(os.path.join(args.model_results_path, "pair_comparison_results.json")) as f:
        model_results = json.load(f)

    accuracy = get_accuracy(human_results=human_results,
                            model_results=model_results,
                            method=args.ensemble_method,
                            example_nums=80)

    print(accuracy)