# **Memory-Augmented Study Assistant (AI Agent)**

### _An intelligent agent that reads course documents, stores memory, retrieves context, and generates study guides.

---

# Overview  
This project implements a **Memory-Augmented AI Study Assistant** that processes PDF/DOCX files, embeds text locally, stores memory using a vector database, and optionally generates a full AI-powered study guide.  

It is designed for academic exploration into **AI Agents**, **memory systems**, and **PEAS (Performance, Environment, Actuators, Sensors)** — connecting classical agent theory to modern LLM-based architectures.

---

# Features  
✔ Read PDF/DOCX files  
✔ Extract & clean text  
✔ Generate embeddings locally (no API required)  
✔ Store long-term memory in ChromaDB  
✔ Retrieve relevant past context  
✔ Generate study previews w/out OpenAI  
✔ Generate full AI study guides w/ OpenAI (optional)

---

# Project Structure

🏗️ Project Structure
📂 ai-study-agent/
│── agent.py                # Core AI agent with memory & study guide logic
│── main.py                 # CLI application
│── reader.py               # PDF/DOCX text extraction
│── utils.py                # Output-saving tools
│── memory_db/              # Local vector database (auto-created)
│── requirements.txt
│── README.md


---

# 🔧 Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-study-agent.git
cd ai-study-agent

### **2. Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows


### **3. Install Dependencies**
```bash
pip install -r requirements.txt

### **4. (Optional) Add OpenAI Key**
#### Create .env file:
OPENAI_API_KEY=your-key-here
#### Agent works without OpenAI, but full study guides require it.

# Usage
Run the application:
```bash
python main.py

You will be prompted to:
- Enter a file path
- Preview document
- Save summary + schedule
- Optionally generate a full study guide with OpenAI

# Screenshots
(Insert here)

# PEAS (Performance, Environment, Actuators, Sensors) Definition
## **Performance**
- Accuracy of summaries
- Relevant memory retrieval
- Coherence of study guide
- User study efficiency

## **Environment**
- Local filesystem
- PDF/DOCX files
- Chroma vector DB
- Optional OpenAI API

## **Actuators**
- Generated text
- Study guides
- Key concepts
- Schedules
- File-saving actions

## **Sensors**
- Extracted document text
- Retrieved memory vectors
- User input through CLI