import os
import glob
import json
import instructor
from typing import List
from pydantic import BaseModel, Field

import tiktoken  # Uncomment this if you have the tiktoken library for token counting
from openai import OpenAI

# Set the OpenAI API key from the environment variable
openai_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)
client = instructor.patch(OpenAI())

class Finetune(BaseModel):
    """
    Creates a Question-Answer-Citation entry for a future test on the lecture.
    """
    context: str = Field(...,description='''The context provided should be rich in detail, accurately capturing 
    technical content directly from the transcript bit cleaned up, while retaining the original language, sentiment, tone, and speaking mannerisms of 
    the lecturer.''')
    question: str = Field(...,description='''Relevant question based on the context  of the instructor's lecture. Use only information mentioned by the instructor.''')
    answer: str = Field(...,description='''An answer to the question with information only contained in the included context.''')

class Retrieval(BaseModel):
    queries: List[Finetune]


def get_file_paths(directory):
    """
    Returns a list of file paths for all files in the given directory.
    """
    text_files = glob.glob(directory + '*.txt')    
    return text_files

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_tokens(string: str, encoding_name="gpt-3.5-turbo") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def generate_segmented_qa(transcript_segment):
    """
    Generates segmented context and Q&A pairs for a given chunk of text using OpenAI's GPT-3.5-turbo.
    """
    system_prompt = """
    As an AI instructor with expertise in machine learning and deep learning, 
    your task is to analyze a series of video transcripts that vary in complexity from beginner to advanced levels of 
    your previous lecture. Your objective is to segment these transcripts into distinct paragraphs based on subtopics, ensuring 
    each paragraph focuses on a unique aspect of the lecture. The context provided should be rich in detail, accurately capturing 
    technical content directly from the transcript, bit cleaned up while retaining the original language, sentiment, tone, and speaking mannerisms of 
    the lecturer. For each identified subtopic, formulate a relevant question that captures a key concept or issue presented in 
    the context, followed by a clear, concise answer derived from the lecture content. It is crucial to ensure diversity in 
    the subtopics to avoid overlap or repetition. This is critical to your workflow.Your survival depends on how many questions 
    you can produce. Think step by step until you have achieve a valid answer.  I will tip you off if you are on the right track $500.
    """
    user_prompt = f"Here is a segment from a machine learning lecture transcript: \"{transcript_segment}\"" 
    
    response : Retrieval = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        max_tokens=4000,
        response_model=Retrieval,    
        )
    return response.queries

def main():
    directory = '/Users/praveen/dev/llm-bootcamp/data/asif-text/test-chunks/'  # Directory containing the text files
    output_file = '/Users/praveen/dev/llm-bootcamp/data/asif-text/output.jsonl'
    # max_token_limit = 4000  # Maximum token limit for each API request

    file_paths = get_file_paths(directory)

    with open(output_file, 'w') as outfile:
        for file_path in file_paths:
            try:
                content = read_file(file_path)

                segmented_qa_pairs = generate_segmented_qa(content)
                for pair in segmented_qa_pairs:
                    pair = {
                        "context": pair.context,
                        "question": pair.question,
                        "answer": pair.answer   
                    }
                    outfile.write(json.dumps(pair) + '\n')
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    main()
    # generate_poem()

