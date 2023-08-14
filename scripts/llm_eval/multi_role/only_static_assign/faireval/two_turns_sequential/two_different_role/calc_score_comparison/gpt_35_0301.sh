

#cd "/mnt/c/Users/dalabengba/AgentVerse"
#"consistency" "fluency" "relevance"


python llm_eval.py \
--task "llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/two_different_role/calc_score_comparison/gpt_35_0301" \
--data_path "./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/two_different_role/calc_score_comparison/gpt_35_0301" \
#--reverse_input
