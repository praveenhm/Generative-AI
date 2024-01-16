from text_chunk import ChunkText
import glob
import os

# Input directory
#directory = '/home/praveen/dev/transcripts2/text-chunks/'
directory = 'chunkthis/'

# Output directory
#output_directory = '/home/praveen/dev/chunks2/'  # Update with your desired output directory path
output_directory = 'chunkthis/'  # Update with your desired output directory path
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist

text_files = glob.glob(directory + '*.txt')

contents = []

for file in text_files:
    with open(file, 'r') as f:
        text = f.read()
        contents.append(text)

print(text_files)

chunker = ChunkText()

sentences = chunker.batch_sentencize(contents)

print(f"Finished Sentencizing {len(sentences)} documents")

for i, doc in enumerate(sentences):
    # Use the output directory for saving the chunked file
    base_name = os.path.basename(text_files[i])  # Extract the base name of the file
    file_path = os.path.join(output_directory, base_name + '.chunks.txt')
    print(f'chunking {file_path}')
    embeddings = chunker.batch_embed(doc)

    chunks = chunker.chunk(embeddings, doc)

    # Open the file in write mode in the output directory
    with open(file_path, 'w') as file:
        # Write each element of the list to a new line in the file
        for chunk in chunks:
            file.write(chunk + '\n')

    print(f'finished writing {file_path}')