from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv



load_dotenv()

groq_api_key = os.getenv("groq_api_key")

# Initialize FastAPI
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    groq_api_key=groq_api_key,
)

# Define Prompt Template for Job Extraction
prompt_extract = PromptTemplate.from_template(
   """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: company , location , role, experience, skills and description.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
)

# Define Prompt Template for Question Answering
prompt_qa = PromptTemplate.from_template(
   """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### USER'S QUESTION:
        {question}
        ### INSTRUCTION:
        Based on the provided scraped text, generate a precise and informative response to the user's question.
        If the answer is not found in the text, respond with "I could not find relevant information."
        ### ANSWER:
        """
)

# API Route to Extract Job Postings
@app.get("/fetch-job/")
def fetch_job(url: str):
    try:
        # Load page content
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content

        # Extract information
        chain_extract = prompt_extract | llm
        res = chain_extract.invoke({"page_data": page_data})

        # Parse JSON output
        json_parser = JsonOutputParser()
        json_res = json_parser.parse(res.content)

        return {"status": "success", "data": json_res}

    except Exception as e:
        return {"status": "error", "message": str(e)}


# API Route to Ask Questions Based on Scraped Text
@app.get("/ask-question/")
def ask_question(url: str, question: str):
    try:
        # Load page content
        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content

        # Answer the question using scraped data
        chain_qa = prompt_qa | llm
        answer = chain_qa.invoke({"page_data": page_data, "question": question})

        return {"status": "success", "answer": answer.content}

    except Exception as e:
        return {"status": "error", "message": str(e)}

# Run the server using:
# uvicorn main:app --reload
