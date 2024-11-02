# ADD this to the .env file locally
#  pip install python-dotenv      

OPENAI_API_KEY = "YOUR_API_KEY"
# Text Summarization Prompts
SUMMARIZATION_PROMPT_1=Summarize the following text: '  '
SUMMARIZATION_PROMPT_2=Provide a concise summary in two sentences: ' '
SUMMARIZATION_PROMPT_3=Generate a brief overview of this content: '  '
SUMMARIZATION_PROMPT_4=Write a short summary in 3 sentences: ' '
SUMMARIZATION_PROMPT_5=Can you summarize this paragraph? '  '

# Sentiment Analysis Prompts
SENTIMENT_PROMPT_1=Identify the sentiment of this statement: 'I absolutely loved the performance; it was stunning!'
SENTIMENT_PROMPT_2=Is this review positive or negative? 'The product did not meet my expectations and was of poor quality.' Please respond with 'Positive' or 'Negative.'
SENTIMENT_PROMPT_3=Determine whether the sentiment is positive, negative, or neutral: 'The movie had some good parts, but overall it was average.'
SENTIMENT_PROMPT_4=What sentiment does this sentence convey? 'The service at the restaurant was exceptional, and I enjoyed every moment.'
SENTIMENT_PROMPT_5=Analyze the tone and indicate if it is positive, negative, or neutral: 'The car broke down unexpectedly, causing a lot of inconvenience.'

# Creative Writing Prompts
WRITING_PROMPT_1=Write a story about a journey.
WRITING_PROMPT_2=Imagine a character who embarks on a journey. Describe their adventure.
WRITING_PROMPT_3=Write a short story about a challenging adventure.
WRITING_PROMPT_4=Tell a story where someone travels and learns something valuable.
WRITING_PROMPT_5=Create a narrative about a hero's journey in three paragraphs.


# Chain-of-Thought Prompts
COT_PROMPT_1=Analyze the sentiment of this movie review. Think step-by-step to decide if its positive or negative.
COT_PROMPT_2=Is this statement positive or negative? First, describe the key words, then conclude the sentiment.
COT_PROMPT_3=Determine the sentiment. First, find any positive or negative phrases, then conclude the sentiment.

# Few-Shot Prompts
FEW_SHOT_PROMPT_1=Analyze the sentiment of this movie review: 'The plot was dull and uninspiring.' Sentiment: Negative.
FEW_SHOT_PROMPT_2=Analyze the sentiment of this movie review: 'The plot was dull and uninspiring.' Sentiment: Negative.\n'Great acting and plot twists make this a must-watch!' Sentiment: Positive.
FEW_SHOT_PROMPT_3=Analyze the sentiment with three examples before the prompt.
FEW_SHOT_PROMPT_4=Provide sentiment analysis with five labeled examples before the prompt.

