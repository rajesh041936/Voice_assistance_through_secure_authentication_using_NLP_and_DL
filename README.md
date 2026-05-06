# Voice Assistance through Secure Authentication using NLP & Deep Learning

## Overview

This project is an intelligent **voice-enabled authentication and assistance system** that combines **Natural Language Processing (NLP)**, **Deep Learning**, and **Speech Recognition** to provide secure and interactive user authentication. The system verifies user identity through voice patterns and processes user queries with NLP-based semantic understanding.

The application is designed to improve security and user experience by integrating **biometric voice authentication** with **AI-powered conversational assistance**.


## Key Features

* **Secure Voice Authentication** – Verifies user identity using voice biometrics.
* **Natural Language Understanding** – Processes and understands spoken commands using NLP.
* **Deep Learning Integration** – Uses transformer-based embeddings for semantic similarity.
* **Fallback AI Response System** – Uses Gemini API when no local response is found.
* **Fast Query Matching** – Retrieves answers using pre-trained embeddings.
* **Scalable Architecture** – Easily extendable with new datasets and models.


## Tech Stack

### Programming Language

* Python 3.x

### Frameworks & Libraries

* Flask
* NLTK
* spaCy
* Sentence Transformers
* NumPy
* Pickle

### AI & NLP Models

* Sentence-BERT (`all-MiniLM-L6-v2`)
* Gemini API (fallback response generation)



## Project Structure

```text
Voice_assistance_through_secure_authentication_using_NLP_and_DL/
│── app.py                    # Flask application entry point
│── nlp_processor.py          # NLP query processing module
│── data.json                 # Dataset containing questions and answers
│── answers.pkl               # Serialized answer storage
│── question_embeddings.pkl   # Precomputed embeddings
│── face_encodings.pkl        # Biometric authentication encodings
│── README.md                 # Project documentation
```



## System Workflow

1. User provides voice input.
2. Speech is converted into text.
3. Voice authentication verifies user identity.
4. NLP preprocessing cleans and analyzes the query.
5. Sentence-BERT generates semantic embeddings.
6. Similarity matching retrieves the best response.
7. If no relevant response exists, Gemini API generates a fallback answer.



## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Voice_assistance_through_secure_authentication_using_NLP_and_DL
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```


## Usage

Run the application:

```bash
python app.py
```

Run NLP processor separately:

```bash
python nlp_processor.py
```


## Example Queries

* What is artificial intelligence?
* Explain deep learning.
* How does machine learning work?


## Applications

* Secure login systems
* Smart assistants
* Voice-based customer support
* Biometric verification systems
* AI-powered virtual assistants


## Future Enhancements

* Multi-language voice authentication
* Real-time speech recognition
* Cloud deployment
* Advanced biometric security layers
* Personalized AI assistant integration

