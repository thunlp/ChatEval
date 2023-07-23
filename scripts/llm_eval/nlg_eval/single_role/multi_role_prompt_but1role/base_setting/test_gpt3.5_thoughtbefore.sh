
source activate agent
export OPENAI_API_KEY='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'
#cd "/mnt/c/Users/dalabengba/AgentVerse"

for role in "General_Public" "Critic" "News_Author"
do

python llm_eval.py \
--task "llm_eval/single_role/multi_role_prompt_but1role/base_setting/${role}" \
--data_path "./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/nlg_eval/single_role/multi_role_prompt_but1role/base_setting/${role}/test_gpt3.5_thoughtbefore/"

done