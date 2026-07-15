SUMMARY_PROMPT = """
You are an expert text summarizer.

Your task is to summarize the given text.

Instructions:
1. Write exactly 3 complete sentences as the summary.
2. Then write exactly 5 bullet points containing the most important takeaways.
3. Keep the language clear and easy to understand.
4. Do not add any information that is not present in the original text.
5. Return the response in the following format:

Summary:
<3 sentences>

Key Takeaways:
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

Text to summarize:

{text}
"""