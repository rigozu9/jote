import os
import tiktoken
import numpy as np

# Define the path to the dataset
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# Ensure the dataset file exists
if not os.path.exists(input_file_path):
    raise FileNotFoundError(f"The dataset file '{input_file_path}' does not exist. Please provide the 'input.txt' file in the same directory.")

# Read the dataset
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = f.read()

# Split into training and validation sets (90% train, 10% validation)
n = len(data)
train_data = data[:int(n * 0.9)]
val_data = data[int(n * 0.9):]

# Encode the data using GPT-2 tokenizer (tiktoken)
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# Save the encoded data as binary files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_output_path = os.path.join(os.path.dirname(__file__), 'train.bin')
val_output_path = os.path.join(os.path.dirname(__file__), 'val.bin')

train_ids.tofile(train_output_path)
val_ids.tofile(val_output_path)

print(f"Number of training tokens: {len(train_ids)}")
print(f"Number of validation tokens: {len(val_ids)}")
print(f"Saved train.bin ({len(train_ids):,} tokens) and val.bin ({len(val_ids):,} tokens) to {os.path.dirname(__file__)}")
