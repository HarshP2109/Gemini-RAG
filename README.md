# RAG Implementation Using Gemini, Chroma, and FAISS
This repository contains a Retrieval-Augmented Generation (RAG) implementation using Gemini with Chroma and FAISS Vector Database, focusing on the Wikipedia page for Luke Skywalker. The RAG model combines retrieval and generation capabilities to provide accurate and contextually relevant responses by leveraging external knowledge.

RAG is a powerful approach for enhancing natural language processing applications by incorporating external knowledge sources into the generation process. This project demonstrates how to set up and use RAG with Gemini for question-answering tasks based on the Wikipedia page of Luke Skywalker.

# Features
Gemini Integration: Utilize Gemini for efficient knowledge retrieval.
Chroma and FAISS: Leverage Chroma and FAISS for fast and accurate similarity search.
Preprocessed Data: The repository includes preprocessed data from Luke Skywalker's Wikipedia page.
Question Answering: Provide answers to questions about Luke Skywalker using retrieved knowledge.

# Installation
Clone the repository:
bash
```
git clone https://github.com/HarshP2109/Gemini-RAG.git
cd Gemini-RAG
```

# Create and activate a virtual environment:
bash
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

# Install dependencies:
bash
```
pip install -r requirements.txt
```

# Setup Server (Backend)
```
fastapi dev mainServer.py
```

# Setup Streamlit (Frontend)
```
streamlit run streampost.py
```

# License
This project is licensed under the MIT License. See the LICENSE file for details.
