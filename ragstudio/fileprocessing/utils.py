import random
from langchain_text_splitters import MarkdownTextSplitter, RecursiveCharacterTextSplitter

def chunk_document_fixed(document_content: str, chunk_size: int=20, chunk_overlap: int=0):
    """
        Method to chunk document based on fixed chunking strategy
        Args:
            document_content: Content to chunk
            chunk_size: Desired chunk of each size. Default is 20.
            chunk_overlap: Number of overlapping characters between chunks. Default is 0
        Returns:
            A list of objects containing chunk_id, chunk_text and chunk_color
    """
    chunk_data = []
    start_index = 0
    chunk_id_ctr = 0

    while start_index < len(document_content):
        end_index = min(start_index+chunk_size, len(document_content))
        current_chunk_text = document_content[start_index:end_index]

        # Generate a random color
        r = random.randint(200, 255)
        g = random.randint(200, 255)
        b = random.randint(200, 255)
        color_code = f"rgb({r}, {g}, {b})"
        chunk_data.append({
            'chunk_id': chunk_id_ctr,
            'chunk_text': current_chunk_text,
            'chunk_color': color_code
        })

        start_index += chunk_size - chunk_overlap
        start_index = max(0, start_index)
        chunk_id_ctr += 1

    return chunk_data


def fixed_chunk_document(document_content: str, chunk_size: int=20, chunk_overlap: int=0):
    """
        Method to chunk document based on fixed chunking strategy
        Args:
            document_content: Content to chunk
            chunk_size: Desired chunk of each size. Default is 20.
            chunk_overlap: Number of overlapping characters between chunks. Default is 0
        Returns:
            A list of objects containing chunk_id and chunk_text
    """
    text_splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_text(document_content)

    chunk_data = []
    chunk_id_ctr = 0

    for chunk in chunks:
        chunk_data.append({
            'chunk_id': chunk_id_ctr,
            'chunk_text': chunk
        })

        chunk_id_ctr += 1

    return chunk_data

def recursive_chunk_document(document_content: str, chunk_size: int=20, chunk_overlap: int=0):
    """
        Method to chunk document based on recursive chunking strategy
        Args:
            document_content: Content to chunk
            chunk_size: Desired chunk of each size. Default is 20.
            chunk_overlap: Number of overlapping characters between chunks. Default is 0
        Returns:
            A list of objects containing chunk_id and chunk_text
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_text(document_content)

    chunk_data = []
    chunk_id_ctr = 0

    for chunk in chunks:
        chunk_data.append({
            'chunk_id': chunk_id_ctr,
            'chunk_text': chunk
        })

        chunk_id_ctr += 1

    return chunk_data