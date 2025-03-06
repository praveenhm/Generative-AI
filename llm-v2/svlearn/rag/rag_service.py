import logging as _log

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import requests

from svlearn.config import ConfigurationMixin

# from svlearn.compute.image_embedding_job import text_query
from svlearn.service.rest.fastapi.search_fastapi_service import HybridSearch


# Setting up the API base and dummy API key
openai.api_base = "http://localhost:8001/v1"
openai.api_key = (
    "DUMMY_KEY_NOT_USED"  
)

dispatcher = HybridSearch()
dispatcher.initialize()


def search_corpus(query):
    # Use your search engine to retrieve relevant passages.
    # This is a placeholder and will depend on how you've indexed your corpus.
    search_results = dispatcher.hybrid_search(query=req.query, k=req.top_k)
    return results


def get_llm_response(query, context):
    # Combine query and context
    input_text = f"Query: {query}\nContext: {context}"

    # Request LLM for a response using the local LLM server
    response = requests.post(
        "http://localhost:your_llm_port/generate", json={"text": input_text}
    )

    # Extract the model's output from the response
    generated_text = response.json().get("text", "")
    return generated_text


def get_gpt4_response(query, context):
    # Define API endpoint and headers
    url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
    headers = {
        "Authorization": "Bearer YOUR_OPENAI_API_KEY",
        "Content-Type": "application/json",
    }

    # Combine query and context
    prompt = f"Query: {query}\nContext: {context}"

    # Define API payload
    data = {"prompt": prompt, "max_tokens": 150}

    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    # Extract and return the generated text
    return response_json["choices"][0]["text"].strip()


# Main Function
def main():
    query = "Your input query here"

    # Retrieve relevant passages/documents based on the query
    search_results = search_corpus(query)

    # Use the LLM to generate a response using the search results as context
    # llm_response = get_llm_response(query, search_results)

    # print(llm_response)

    # Test the function
    query = "Your input query here"
    context = "Relevant information or search result here"
    print(get_gpt4_response(query, context))


if __name__ == "__main__":
    main()
