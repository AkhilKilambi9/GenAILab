import openai
import json
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the key is loaded correctly
if openai.api_key is None:
    print("API key not loaded. Check .env file and dotenv configuration.")
else:
    print("API key loaded successfully.")

# Function to generate a response from the OpenAI API
def generate_response(prompt, model="gpt-3.5-turbo", max_tokens=1000, temperature=0.7):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating response for prompt '{prompt}': {e}")
        return None

# Function to load prompts by prefix
def load_prompts(prefix, count):
    return [os.getenv(f"{prefix}_{i}") for i in range(1, count + 1)]

# Define tasks and load prompts from the .env file
tasks = {
    "Text Summarization": load_prompts("SUMMARIZATION_PROMPT", 5),
    "Sentiment Analysis": load_prompts("QA_PROMPT", 5),
    "Creative Writing": load_prompts("WRITING_PROMPT", 5),
}

# Function to run experiments for each task
def run_experiments(tasks):
    results = {}
    for task_name, prompts in tasks.items():
        results[task_name] = {}
        for i, prompt in enumerate(prompts):
            if prompt:  # Ensure prompt is not None
                print(f"Running prompt {i+1} for task '{task_name}'")
                output = generate_response(prompt)
                results[task_name][f"Prompt {i+1}"] = {
                    "prompt": prompt,
                    "output": output
                }
                time.sleep(1.5)  # Pause for rate limiting
    return results

# Run and save experiments for main tasks
experiment_results = run_experiments(tasks)
with open("prompt_engineering_results.json", "w") as outfile:
    json.dump(experiment_results, outfile, indent=4)

# Chain-of-Thought Experiment
def chain_of_thought_experiment():
    cot_prompts = load_prompts("COT_PROMPT", 3)
    cot_results = {}
    for i, prompt in enumerate(cot_prompts):
        if prompt:
            print(f"Running Chain-of-Thought prompt {i+1}")
            output = generate_response(prompt)
            cot_results[f"Chain-of-Thought Prompt {i+1}"] = {
                "prompt": prompt,
                "output": output
            }
            time.sleep(1.5)
    return cot_results

# Save Chain-of-Thought results
cot_results = chain_of_thought_experiment()
with open("chain_of_thought_results.json", "w") as cot_file:
    json.dump(cot_results, cot_file, indent=4)

# Few-Shot Prompting Experiment
def few_shot_experiment():
    few_shot_prompts = load_prompts("FEW_SHOT_PROMPT", 8)
    few_shot_results = {}
    for i, prompt in enumerate(few_shot_prompts):
        if prompt:
            print(f"Running Few-Shot prompt {i+1}")
            output = generate_response(prompt)
            few_shot_results[f"Few-Shot Prompt {i+1}"] = {
                "prompt": prompt,
                "output": output
            }
            time.sleep(1.5)
    return few_shot_results

# Save Few-Shot results
few_shot_results = few_shot_experiment()
with open("few_shot_results.json", "w") as few_shot_file:
    json.dump(few_shot_results, few_shot_file, indent=4)

print("Experiments completed and results saved to JSON files.")
