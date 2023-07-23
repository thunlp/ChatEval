
source activate agent
export OPENAI_API_KEY='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'
#cd "/mnt/c/Users/dalabengba/AgentVerse"
#"coherence" "consistency" "relevance"
for aspect in "fluency"
do

python llm_eval.py \
--task "llm_eval/single_role/geval_summeval_separate/${aspect}/thought" \
--data_path "./agentverse/tasks/llm_eval/data/nlg_eval/preprocessed_data/test.json" \
--output_dir "./outputs/llm_eval/single_role/geval_summeval_separate/${aspect}_1-5/thought/gpt_3.5/"

done