# **Memory-Augmented Study Assistant (AI Agent)**

### An intelligent agent that reads course documents, stores memory, retrieves context, and generates study guides.

## 🔰 Badges

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-yellow)
![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

## Overview  
This project implements a Memory-Augmented Study Assistant that helps students work with course materials (PDFs and DOCX files). It reads and stores important information locally, recalls relevant context from previous sessions, and generates detailed study guides using a large language model (LLM).

The project also serves as an academic exploration of AI agents, memory systems, and the PEAS framework (Performance, Environment, Actuators, Sensors), connecting traditional agent concepts with modern LLM-based architectures.

---

# Features  
✔ **Read PDF/DOCX files**  
✔ **Local Embeddings**: Generates text embeddings on your local machine using SentenceTransformers, requiring no API calls for this step.
✔ **Long-Term Memory**: Utilizes ChromaDB, a local vector database, to store and persist memory from study sessions.
✔ **Contextual Retrieval**: Retrieves relevant information from past documents to provide context for new material.
✔ **API-Free Previews**: Generates document previews, summaries, and key concepts without needing an OpenAI API key.
✔ **AI-Powered Study Guides**: Optionally generates a full, detailed study guide using the OpenAI API, integrating new material with retrieved memories.



## 🏗️ Project Structure
```
/️ 📂Memory-Augmented-AI-Agent-Project
│
├── agent.py            # Core AI agent with memory, retrieval, and generation logic
├── main.py             # Command-Line Interface (CLI) to run the application
├── reader.py           # Functions for PDF/DOCX text extraction
├── utils.py            # Utility for saving output to files
├── requirements.txt    # Project dependencies
└── memory_db/          # Directory for the persistent local vector database (auto-created)
```

## 🔧 Installation

**1. Clone the Repository**
```bash
git clone https://github.com/Denita06/Memory-Augmented-AI-Agent-Project.git
cd Memory-Augmented-AI-Agent-Project
```
**2. Create and Activate a Virtual Environment**
*   **Mac/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
*   **Windows:**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. (Optional) Set Up OpenAI API Key**

To generate full, AI-powered study guides, you need an OpenAI API key. The agent can generate document previews without it.

Create a file named `.env` in the project's root directory and add your key:
```
OPENAI_API_KEY="your-key-here"
```

## ▶️ Usage

Run the application from your terminal:
```bash
python main.py
```
The CLI will guide you through the following steps:
1.  **Enter File Path**: Provide the local path to your PDF or DOCX study document.
2.  **Document Preview**: The agent will process the file, add it to its memory, and generate a preview including a summary, key concepts, and a mock schedule. This step runs entirely locally.
3.  **Save Preview**: You will have the option to save this preview content to `study_preview.txt`.
4.  **Generate Full Study Guide**: You can then choose to generate a comprehensive study guide using the OpenAI API. This guide will be more detailed and will integrate context from past documents stored in memory.
5.  **Save Full Guide**: If generated, you can save the full guide to `study_guide.txt`.
6.  You can then choose to process another file, continuing the session.

## 🧩 PEAS (Performance, Environment, Actuators, Sensors) Definition

This project can be defined using the classical AI agent framework:

*   **Performance:**
    *   Accuracy and relevance of retrieved memories.
    *   Coherence and conciseness of generated summaries and study guides.
    *   Effectiveness of the study schedule in improving user learning efficiency.

*   **Environment:**
    *   Local filesystem for reading documents.
    *   Chroma vector database for storing and querying memories.
    *   Optional OpenAI API for advanced text generation.

*   **Actuators:**
    *   Generated text output to the console (previews, guides, concepts, schedules).
    *   File-saving actions that write output to `.txt` files.
    *   Additions of new document vectors to the memory database.

*   **Sensors:**
    *   User input from the CLI (file paths, choices).
    *   Extracted text content from input documents.
    *   Retrieved memory vectors from the Chroma database.

## 🧭 Future Work

*   Improve long-term memory summarization techniques.
*   Develop a graphical user interface (GUI) for a more user-friendly experience.
*   Add support for more file types (e.g., `.txt`, `.pptx`).


