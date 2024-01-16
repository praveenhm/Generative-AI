import os
import re
import pandas as pd
import tiktoken

def consolidate_files(directory_path):
    """
    Consolidate multiple text files into a single string.
    """
    all_text = ""
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):  # Assuming all files are .txt
            with open(os.path.join(directory_path, filename), 'r') as file:
                all_text += file.read() + " "  # Add a space between files' contents

    # Write all_text to a file in the current directory
    with open('output_file.txt', 'w') as output_file:
        output_file.write(all_text)
                
    return all_text

# path/filename: /home/user/consolidate_files.py

def consolidate_file(directory_path, output_file_path):
    """
    Read multiple text files from a directory and consolidate them into a single large file.
    """
    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):  # Assuming all files are .txt
                with open(os.path.join(directory_path, filename), 'r') as file:
                    file_content = file.read()
                    output_file.write(file_content + "\n\n")  # Add newlines between files' contents

def clean_text(text):
    """
    Clean the raw text by removing unwanted characters and standardizing format.
    """
    # Remove non-textual elements, standardize whitespace, etc.
    cleaned_text = re.sub(r'\s+', ' ', text)  # Example: replace multiple spaces with a single space
    return cleaned_text

def extract_qa_pairs(text):
    """
    Extract question-answer pairs from the text.
    This function needs to be customized based on the text's format.
    """
    # Placeholder for extracting Q&A pairs
    # Example: Use regex or other methods to identify questions and corresponding answers
    qa_pairs = []
    return qa_pairs

def prepare_dataset(directory_path):
    """
    Prepare the dataset by consolidating, cleaning, and structuring the text.
    """
    consolidated_text = consolidate_files(directory_path)
    cleaned_text = clean_text(consolidated_text)
    qa_pairs = extract_qa_pairs(cleaned_text)
       
    # Convert to DataFrame for easier handling (if applicable)
    df = pd.DataFrame(qa_pairs, columns=['Question', 'Answer'])

    # Splitting the dataset (this can be adjusted as needed)
    train_df = df.sample(frac=0.8, random_state=123)  # 80% for training
    test_val_df = df.drop(train_df.index)
    validation_df = test_val_df.sample(frac=0.5, random_state=123)  # 10% for validation
    test_df = test_val_df.drop(validation_df.index)  # 10% for testing

    # Save the DataFrame as a text file
    df.to_csv('output_file.csv', index=False)

    return train_df, validation_df, test_df


def count_tokens(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Example usage
    # train_df, validation_df, test_df = prepare_dataset('/Users/praveen/dev/llm-bootcamp/data/asif-text/chunks')
    # Add your code here to further process the datasets or perform other operations
    # Example usage
    # consolidate_file('/Users/praveen/dev/llm-bootcamp/data/asif-text/chunks', '/Users/praveen/dev/llm-bootcamp/data/asif-text/consolidated_file.txt')
    file_path = '/Users/praveen/dev/llm-bootcamp/data/asif-text/consolidated_file.txt'  # Update with the path to your data file
    text = read_file(file_path)
    total_tokens = count_tokens(text,"gpt-4-turbo")
    print(f"Total number of tokens in the dataset: {total_tokens}")


if __name__ == "__main__":
    main()
