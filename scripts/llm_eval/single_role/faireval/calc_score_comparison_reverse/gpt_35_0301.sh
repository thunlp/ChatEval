
source activate agent
export OPENAI_API_KEY='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'
#cd "/mnt/c/Users/dalabengba/AgentVerse"
#"consistency" "fluency" "relevance"


python llm_eval.py \
--task "llm_eval/single_role/faireval/calc_score_comparison/gpt_35_0301" \
--data_path "./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/single_role/faireval/calc_score_comparison_reverse/gpt_35_0301" \
--reverse_input
