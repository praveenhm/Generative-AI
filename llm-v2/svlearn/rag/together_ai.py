# Description: This script converts the input data to the format required by the RAG model
# Usage: python3 convert_format.py
# Converts {“context”: “...“, “question”: “...“, “answer”: “...“} to {"text": "<human>:  Q: ? A: Rosey: ", "metadata": {"source": " ML"}}

import json

# File paths
input_file_path = '/Users/praveen/dev/llm-bootcamp/data/asif-text/fine-tune/combined.jsonl'  # replace with your input file path
output_file_path = '/Users/praveen/dev/llm-bootcamp/data/asif-text/fine-tune/together_ai.jsonl'  # replace with your output file path

def convert_entry(entry):
    """Converts a single entry to the new format."""
    return {
        "text": f"Background: {entry['context']}<human>: {entry['question']} <bot>: {entry['answer']}"
    }

def convert_jsonl_file(input_file, output_file):
    """Reads a JSONL file, converts each entry, and writes to a new file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            original_entry = json.loads(line)
            converted_entry = convert_entry(original_entry)
            json.dump(converted_entry, outfile)
            outfile.write('\n')

def main():
    input_filename = input_file_path
    output_filename = output_file_path
    convert_jsonl_file(input_filename, output_filename)
    print(f"Conversion complete. Data written to {output_filename}")

if __name__ == "__main__":
    main()
