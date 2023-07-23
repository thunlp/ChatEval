
source activate agent
export OPENAI_API_KEY='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'
#cd "/mnt/c/Users/dalabengba/AgentVerse"
#"consistency" "fluency" "relevance"
for aspect in "fluency"
do

python llm_eval.py \
--task "llm_eval/multi_role/only_static_assign/geval_summeval_separate/three_turns_sequential/${aspect}/thought" \
--data_path "./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/multi_role/only_static_assign/geval_summeval_separate/three_turns_sequential/${aspect}_1-5/thought/gpt_3.5/"

done