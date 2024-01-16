import openai
from svlearn.service.rest.fastapi.search_fastapi_service import HybridSearch

# Setting up the API base and dummy API key
openai.api_base = "http://localhost:8001/v1"
openai.api_key =  "DUMMY_KEY_NOT_USED"  

class OpenAISummarizer:
    def __init__(self, api_key, max_tokens=2048, summary_max_tokens=150):
        openai.api_key = api_key
        self.max_tokens = max_tokens
        self.summary_max_tokens = summary_max_tokens

    def extract_context_from_output(self, result):
        result = [item[1] for item in result.get("neighbours", [])]
        return result

    def limit_context_length(self, contexts):
        token_count = 0
        limited_contexts = []

        for context in contexts:
            tokens = len(context.split())  # Simplistic token estimation
            if token_count + tokens > self.max_tokens:
                break
            token_count += tokens
            limited_contexts.append(context)

        return limited_contexts

    def format_context_for_summarization(self, contexts):
        segmented_context = "\n---\n".join(contexts)
        prompt = f"Given the following texts, provide a concise summary:\n---\n{segmented_context}\n"
        return prompt

    def summarize(self, search_result):
        # Extracting contexts from search output
        contexts = self.extract_context_from_output(search_result)

        # Limiting context length
        limited_contexts = self.limit_context_length(contexts)

        # Formatting the context for summarization
        formatted_prompt = self.format_context_for_summarization(limited_contexts)

        # Making the request to OpenAI using GPT-4
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=formatted_prompt,
            max_tokens=self.summary_max_tokens,
        )
        return response.choices[0].text.strip()


def main():
    dispatcher = HybridSearch()
    dispatcher.initialize()
    search_results = dispatcher.hybrid_search(query='spark', k=5)
    summarizer = OpenAISummarizer(api_key=openai.api_key)
    summary = summarizer.summarize(search_result=search_results)
    print(summary)

if __name__ == "__main__":
    main()
