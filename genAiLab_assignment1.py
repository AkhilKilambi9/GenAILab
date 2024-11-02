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
def generate_response(prompt, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7):
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
    "Sentiment Analysis": load_prompts("SENTIMENT_PROMPT", 5),
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

# Run and save experiments
experiment_results = run_experiments(tasks)
with open("prompt_engineering_results.json", "w") as outfile:
    json.dump(experiment_results, outfile, indent=4)

print("Experiments completed and results saved to JSON files.")
