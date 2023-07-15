source activate agent
export OPENAI_API_KEY='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'
cd "/mnt/c/Users/dalabengba/AgentVerse"

conda activate agent
python llm_eval.py \
--task "llm_eval/multi_role/only_static_assign/base_setting" \
--data_path "./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/nlg_eval/multi_role/only_static_assign/base_setting/3Round/test_gpt3.5_thoughtbefore/" \