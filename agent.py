# Loads environment variables, such as API keys from a .env file
from dotenv import load_dotenv
load_dotenv()

#Standard library
import os # Used to access environment variables and file paths
import numpy as np

# Langchain imports for AI Agent functionality
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma # Local vector database for storing and retrieving memory
from langchain.messages import HumanMessage # Messages for the chat model
from sentence_transformers import SentenceTransformer # Sentence transformers for local embedding generation


'''
Local Embedding setup
Loads a pre-trained model to convert text into numerical vectors
'''
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class LocalEmbeddingWrapper:
    """
    Wrapper class to provide embeddings for Chroma database.
    Can handle single strings or lists of strings.
    """
    def __call__(self, texts):
        if isinstance(texts, str):
            return embedding_model.encode([texts])[0].tolist()
        elif isinstance(texts, list):
            return embedding_model.encode(texts).tolist()
        else:
            raise ValueError("Input must be a string or a list of strings")

    def embed_query(self, text):
        '''Return embedding for a query (single string)'''
        return embedding_model.encode([text]).tolist()[0]

    def embed_documents(self, texts):
        '''Return embeddings for a list of documents.'''
        return self.__call__(texts)

# Create embedding instance
embeddings = LocalEmbeddingWrapper()

'''
Local Memory database setup
Stores past content for retreival later (memory context)
'''
memory_db = Chroma(collection_name="study_memory",
                   embedding_function=embeddings, # Uses local embeddings instead of API
                   persist_directory="./memory_db"
                   )
'''
AI Model setup
'''
llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY"))

# Memory function
def add_to_memory(text):
    memory_db.add_texts([text])

def retrieve_from_memory(query, k=3):
    results = memory_db.similarity_search(query, k=k)
    return "\n".join([r.page_content for r in results]) if results else ""

# Main study assistant function
def study_helper_agent(text, use_api=True):
    """
    Process input text and generate:
    - Document preview (without API) OR
    - Full study guide (with API)

    Returns a structured dictionary
    {
        "content": processed text or study guide,
        "summary": key information,
        "key_concepts" list of bullet points,
        "mock_schedule": suggested study plan
    }
    """

    try:
        # Add the current text to memory
        add_to_memory(text)
        memory_context = retrieve_from_memory(text)

        def clean_text_block(block):
            paragraphs = block.split("\n\n")  # split on paragraph breaks
            cleaned_paragraphs = []
            for para in paragraphs:
                # Remove extra spaces within the paragraph
                stripped = " ".join(para.split())
                if stripped:
                    cleaned_paragraphs.append(stripped)
            # Join paragraphs with a double newline for readability
            return "\n\n".join(cleaned_paragraphs)

        clean_text = clean_text_block(text)
        clean_memory = clean_text_block(memory_context)

        if not use_api:
            # Local preview version
            sentences = clean_text.split(". ")
            key_sentences = sentences[:5]
            mock_schedule = "Day 1: Read introduction\nDay 2: Review key concepts\nDay 3: Practice questions"
            return {
                "content": f"Processed document preview:\n{clean_text[:1000]}...\nMemory context:\n{clean_memory[:500]}...",
                "summary": " ".join(key_sentences),
                "key_concepts": [s.strip() for s in key_sentences],
                "mock_schedule": mock_schedule
            }

        # --- Full AI Version (requires OpenAI API) ---
        prompt = f"""
        You are a Study Helper AI designed to support a college student preparing for an exam.
    
        Your responsibilities are to read the provided study material and create a comprehensive, 
        easy-to-understand study guide that the student can use to prepare effectively.
    
    
        Use BOTH:
        1. The newly uploaded content.
        2. Relevant memory from previous study sessions.
    
        _____________________
        New Material: {text}
        Memory Context: {memory_context}
        _____________________
    
        Follow these instructions:
        1. Concise and thorough summary. Explain core ideas and key themes.
        2. Study schedule, including what to study first + why and a realistic timeline (days or hours)
        3. Practice Questions - Mix of multiple choice questions, short answer, T/F, scenario-based
        4. Key Concepts & Formulas - Definitions, formulas, explanations, examples.
        5. Study Tips / Exam Strategy - include common mistakes
        """


        messages =  [[HumanMessage(content=prompt)]]
        try:
            response = llm.generate(messages)
            response_text = response.generations[0][0].text
            return {"content": response_text}
        except Exception as e:
            return {"error": f"OpenAI API error: {e}"}


    except Exception as e:
        return {"error": str(e)}
