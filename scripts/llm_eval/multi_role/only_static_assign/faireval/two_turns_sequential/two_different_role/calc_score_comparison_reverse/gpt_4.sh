
source activate agent
export OPENAI_API_KEY='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'
#cd "/mnt/c/Users/dalabengba/AgentVerse"
#"consistency" "fluency" "relevance"


python llm_eval.py \
--task "llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/two_different_role/calc_score_comparison/gpt_4" \
--data_path "./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/two_different_role/calc_score_comparison_reverse/gpt_4" \
--reverse_input
