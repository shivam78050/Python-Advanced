#write a python function which takes 'Text, chunk size, overlap size' as argument to divide given text into chunks of given size with given overlapping size.abs
def chunk_text(text, chunk_size, overlap_size):
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")
    if overlap_size < 0:
        raise ValueError("Overlap size cannot be negative.")
    if overlap_size >= chunk_size:
        raise ValueError("Overlap size must be less than chunk size.")
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        start += (chunk_size - overlap_size)
    
    return chunks  

input_text = "This is an example of text that will be divided into chunks."
chunk_size = 10
overlap_size = 2
result = chunk_text(input_text, chunk_size, overlap_size)
for i, chunk in enumerate(result):
    print(f"Chunk {i + 1}: '{chunk}'")