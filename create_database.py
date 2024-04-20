from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.schema import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from pathlib import Path

import os
import shutil

CHROMA_PATH = "chroma"
DATA_PATH = "data/code"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    file_paths = []
  
    # # Iterate over the directory and its subdirectories
    # for file_path in Path(DATA_PATH).rglob('*'):
    #     # Check if the file is a regular file and has one of the specified extensions
    #     if file_path.is_file() and file_path.suffix.lower() in ['.jsx', '.js', '.css']:
    #         new_file_path = file_path.with_suffix('.txt')
        
    #         # Rename .js file to .txt
    #         os.rename(file_path, new_file_path)
            
    #         # Append the new file path to the list
    #         file_paths.append(str(new_file_path))
    
    # print(file_paths)
    
   

    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()
