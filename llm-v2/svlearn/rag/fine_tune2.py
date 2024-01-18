import os
import json
import tiktoken  # Uncomment this if you have the tiktoken library for token counting
from openai import OpenAI

# Set the OpenAI API key from the environment variable
openai_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)


def get_file_paths(directory):
    """
    Returns a list of file paths for all files in the given directory.
    """
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_paths.append(os.path.join(root, file))
    return file_paths

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_tokens(string: str, encoding_name="gpt-3.5-turbo") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def chunk_text(text, max_token_limit):
    """
    Splits the text into chunks where each chunk has a maximum of max_token_limit tokens.
    """
    tokens = text.split()
    chunks = []
    current_chunk = []

    for token in tokens:
        if count_tokens(' '.join(current_chunk + [token])) <= max_token_limit:
            current_chunk.append(token)
        else:
            chunks.append(' '.join(current_chunk))
            current_chunk = [token]
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks


def generate_segmented_qa(chunk):
    """
    Generates segmented context and Q&A pairs for a given chunk of text using OpenAI's GPT-3.5-turbo.
    """
    prompt = f"You are a helpful assistant designed to output JSON.Segment the following transcript into detailed paragraphs based on subtopics. For each paragraph, generate a question and answer pair that maintains the original tone and content of the lecture:\n\n{chunk}"
 
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
    )
    print(response.choices[0].message.content)
 

    segmented_qa_pairs = []
    for message in response['choices'][0]['message']['content']:
        if message['role'] == 'assistant':
            segmented_qa_pairs.append({
                'context': chunk,
                'question': message['content'],
                'answer': ''
            })
    return segmented_qa_pairs

def generate_poem():
    """
    Generates a poem that explains the concept of recursion in programming using OpenAI's GPT-3.5-turbo.
    """
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    print(completion.choices[0].message)

def main():
    directory = 'path_to_directory_with_files'  # Directory containing the text files
    output_file = 'output.jsonl'
    max_token_limit = 4000  # Maximum token limit for each API request

    file_paths = get_file_paths(directory)

    with open(output_file, 'w') as outfile:
        for file_path in file_paths:
            try:
                content = read_file(file_path)
                chunks = chunk_text(content, max_token_limit)
                
                for chunk in chunks:
                    segmented_qa_pairs = generate_segmented_qa(chunk)
                    for pair in segmented_qa_pairs:
                        outfile.write(json.dumps(pair) + '\n')
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # main()
    generate_poem()

