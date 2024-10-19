ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate
---

<p align="center">
  <a href="https://arxiv.org/abs/2308.07201">Paper</a> •
  <a href="#-simple-video-demo">Video Demo</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#citation">Citation</a>    
</p>

**ChatEval** is designed to simplify the process of human evaluation on generated text. When given different pieces of text, roles (acted by LLMs) within ChatEval can autonomously debate the nuances and disparities, drawing upon their assigned personas, and subsequently provide their judgments. Understanding its workflow and functionalities is crucial for optimal usage. First, check out our video demo to know how it works!

![better_compare](./imgs/better_compare.png)

## 🎥 Simple Video Demo

Our video demo illustrates how users can utilize ChatEval to compare two different generated texts. While [FastChat](https://github.com/lm-sys/FastChat) chatbot arena allows users to vote for the superior response manually, we leverage **multiple LLMs** to autonomously determine which response stands out. Throughout the debate, you can observe a transparent procedure revealing how our LLM referees evaluate each answer based on their distinct assigned traits.

1. Use the selection dropdown to pick the two models you wish to compare.
2. Patiently wait for the models to craft their responses.
3. It's time for the **LLM referees** to pick the superior response! Start by clicking the 'Reset' button, followed by the 'Judge' button.

https://github.com/chanchimin/ChatEval/assets/75533759/35834dfd-5472-482a-905f-44b92708c90b

We'd like to extend our heartfelt gratitude to [FastChat](https://github.com/lm-sys/FastChat) for their outstanding framework. Our demo was built upon the foundation they provided.

If you like to run the above arena-style demo, first make sure that you install FastChat correctly as stated in [Installation](#installation) and follow these steps:

1. **Navigate to FastChat folder under our project**
```bash
cd ChatEval/FastChat
```
2. **Launch the controller which is used to coordinate the webserver and model workers**
```python
python3 -m fastchat.serve.controller
```
3. **Register multiple model workers to a single controller**
```bash
# worker 0
CUDA_VISIBLE_DEVICES=0 python3 -m fastchat.serve.model_worker --model-path lmsys/vicuna-7b-v1.3 --controller http://localhost:21001 --port 31000 --worker http://localhost:31000
# worker 1
CUDA_VISIBLE_DEVICES=1 python3 -m fastchat.serve.model_worker --model-path lmsys/fastchat-t5-3b-v1.0 --controller http://localhost:21001 --port 31001 --worker http://localhost:31001
```
4. **Run the gradio server, which integrates with the chatbots and our referee team**
```python
python3 -m fastchat.serve.gradio_web_server_multi
```

Now, you can open your browser and chat with the models, and then receive a judgment from an autonomous referee team.



## 🚀 Getting Started

### Installation

First, clone our latest repository
```bash
git clone https://github.com/chanchimin/ChatEval.git
cd ChatEval
pip install -r requirements.txt
```

We basically call the OpenAI's API for our LLMs, so you also need to export your OpenAI key as follows before running our code

1. **Using Environment Variable:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```
2. **Or, directly specifying in the Python file:**
```python
import os
os.environ["OPENAI_API_KEY"] = "your_api_key_here"
```

If you wish to run our arena-style demo, you need to install FastChat following these steps:

```bash
cd ChatEval/FastChat
pip3 install --upgrade pip  # enable PEP 660 support
pip3 install -e ".[model_worker,webui]"
```




### Prepare Dataset

We provide the data examples in `agentverse/tasks/llm_eval/data/faireval/preprocessed_data/test.json`.
 
Your custom data should look like

```json
[
    {
        "question_id": 1,
        "question": "What are the primary factors that influence consumer behavior?",
        "response": {
            "gpt35": "There are several primary factors that influence consumer behavior, including:\n\n1. Personal factors - These include individual characteristics such as age, gender, income, education, personality, and lifestyle.\n\n2. Psychological factors - These include the consumer's perception of the product or service, motives, attitudes, beliefs, and values.\n\n3. Social factors - These include the consumer's family, friends, social class, culture, and reference groups.\n\n4. Situational factors - These include the physical environment, time, and mood of the consumer.\n\n5. Marketing mix factors - These include product, price, promotion, and distribution, and how they affect the consumer's decision-making process.",
            "vicuna": "There are several primary factors that can influence consumer behavior, including:\n\n1. Personal factors: These include individual characteristics such as age, gender, education, income, personality, and values.\n2. Psychological factors: These include emotional, cognitive, and perceptual factors that can influence how a consumer perceives and processes information about products and services.\n3. Social factors: These include cultural, social, and environmental factors that can affect how consumers view and use products and services.\n4. Economic factors: These include factors such as the price of a product or service, the availability of alternative products or services, and the consumer's purchasing power.\n5. Marketing factors: These include the way a product or service is marketed, including advertising, packaging, and distribution.\n6. Product and service factors: These include the quality, features, and benefits of a product or service, as well as its design, performance, and warranty.\n\nUnderstanding these factors can help businesses and organizations develop effective marketing strategies and tailor their products and services to meet the needs and preferences of their target audience."
        }
    }
]
```

The question and responses you provide will be integrated into the **prompt_template**, which our referee team uses to evaluate and determine the superior response.


### Configure Custom Debater Agent

You should modify your custom designed agent in `agentverse/tasks` folders.
Take `agentverse/tasks/llm_eval/config.yaml` as an example, your agent configuration in config.yaml should look like:

```yaml
# config.yaml
agents:
  -
    agent_type: llm_eval_multi  # this should be one of the types in ./agentverse/agents/
    name: Critic  # name your agent
    final_prompt_to_use: |-   # this is used to control agents' behaviour in the last round.
      Please first provide a comprehensive explanation of your evaluation, avoiding any potential bias and ensuring that the order in which the responses were presented does not affect your judgment.
      Then, output two lines indicating the scores for Assistant 1 and 2, respectively.

      Remember that you are not required to output the same value as other referees !
      Output with the following format strictly:
      Evaluation evidence: [your explanation here]
      The score of Assistant 1: [score only]
      The score of Assistant 2: [score only]
    role_description: |-    # give your agent its personality
      You are now ... You like ... You 
    memory:
      memory_type: chat_history
    memory_manipulator:
      memory_manipulator_type: basic
    prompt_template: your prompt template  # substitute it with your custom prompt template
    llm:
      model: "gpt-3.5-turbo-0301"
      llm_type: gpt-3.5-turbo-0301
      temperature: 0
      max_tokens: 512
```

### Run the scripts

Now, you are good to run the experiments.
Try out the following lines first, it employs **one-by-one communication** and **2 agent roles** for **2 discussion turns** in the paper.
```shell
python llm_eval.py --config agentverse/tasks/llm_eval/config.yaml
```

### Check the evaluation results

The evaluation results will be saved in 
```config.output_dir```
The results will look like

```json
[
    {
        "question": "What are the primary factors that influence consumer behavior?",
        "response": {
            "gpt35": "There are several primary factors that influence consumer behavior, including:\n\n1. Personal factors - These include individual characteristics such as age, gender, income, education, personality, and lifestyle.\n\n2. Psychological factors - These include the consumer's perception of the product or service, motives, attitudes, beliefs, and values.\n\n3. Social factors - These include the consumer's family, friends, social class, culture, and reference groups.\n\n4. Situational factors - These include the physical environment, time, and mood of the consumer.\n\n5. Marketing mix factors - These include product, price, promotion, and distribution, and how they affect the consumer's decision-making process.",
            "vicuna": "There are several primary factors that can influence consumer behavior, including:\n\n1. Personal factors: These include individual characteristics such as age, gender, education, income, personality, and values.\n2. Psychological factors: These include emotional, cognitive, and perceptual factors that can influence how a consumer perceives and processes information about products and services.\n3. Social factors: These include cultural, social, and environmental factors that can affect how consumers view and use products and services.\n4. Economic factors: These include factors such as the price of a product or service, the availability of alternative products or services, and the consumer's purchasing power.\n5. Marketing factors: These include the way a product or service is marketed, including advertising, packaging, and distribution.\n6. Product and service factors: These include the quality, features, and benefits of a product or service, as well as its design, performance, and warranty.\n\nUnderstanding these factors can help businesses and organizations develop effective marketing strategies and tailor their products and services to meet the needs and preferences of their target audience."
        },
        "evaluation": [
            {
                "role": "General Public",
                "evaluation": "Evaluation evidence: Both Assistant 1 and Assistant 2 provided comprehensive and relevant information on the primary factors that influence consumer behavior. Assistant 1's response was more concise and easier to read, while still covering all the necessary factors. Assistant 2 provided more detailed information on economic factors and product and service factors, which could be helpful for businesses in developing effective marketing strategies. However, Assistant 2's response was slightly longer and could be overwhelming for some readers.\n\nThe score of Assistant 1: 8\nThe score of Assistant 2: 9"
            },
            {
                "role": "Critic",
                "evaluation": "Evaluation evidence: Both Assistant 1 and Assistant 2 provided comprehensive and relevant information on the primary factors that influence consumer behavior. Although Assistant 2 delved deeper into economic factors and product and service factors, offering valuable insights for businesses crafting marketing strategies, the response was slightly longer and could be daunting for some readers. \n\nThe score of Assistant 1: 8\nThe score of Assistant 2: 8"
            }
        ]
    }
]
```


## Citation
If you find this repo helpful, feel free to cite us.
```bibtex
@misc{chan2023chateval,
      title={ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate}, 
      author={Chi-Min Chan and Weize Chen and Yusheng Su and Jianxuan Yu and Wei Xue and Shanghang Zhang and Jie Fu and Zhiyuan Liu},
      year={2023},
      eprint={2308.07201},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
