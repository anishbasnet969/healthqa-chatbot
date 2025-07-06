# AI-Powered Healthcare Document Chat Application

This is a healthcare-focused document chat application built using FastAPI, LangChain, and Google Gemini API.

## Setup instructions

### Clone the repository

```bash
git clone https://github.com/anishbasnet969/healthqa-chatbot.git
```
or download the zip file from [here](https://github.com/anishbasnet969/healthqa-chatbot/archive/refs/heads/main.zip) and extract it

### Get a Google API key
- Visit [Google AI Studio](https://aistudio.google.com) and sign in with your Google account.  
- Click **Get API Key** at the top left corner.  
- Click **Create API Key** and follow the prompts to generate your key.  
- Copy the generated API key and keep it secure (do **not** share publicly).

### Create the .env file
- Create a file named .env in the root directory of the repository.
- Add the following line to the .env file:

```bash
GOOGLE_API_KEY=your-api-key
```

### Set up the environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Start the FASTAPI server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Start the streamlit app
```bash
streamlit run streamlit_app.py
```


### Access the application
You can now access the application on your computer at `http://localhost:8501`, which is the default URL for Streamlit.
