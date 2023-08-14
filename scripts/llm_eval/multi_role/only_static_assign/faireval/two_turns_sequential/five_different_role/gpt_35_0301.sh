
source activate agent
export OPENAI_API_KEY='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'
#cd "/mnt/c/Users/dalabengba/AgentVerse"
#"consistency" "fluency" "relevance"


python llm_eval.py \
--task "llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/five_different_role/calc_score_comparison/gpt_35_0301" \
--data_path "./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/five_different_role/calc_score_comparison/gpt_35_0301" \
#--reverse_input


python llm_eval.py \
--task "llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/five_different_role/calc_score_comparison/gpt_35_0301" \
--data_path "./agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/multi_role/only_static_assign/faireval/two_turns_sequential/five_different_role/calc_score_comparison_reverse/gpt_35_0301" \
--reverse_input
