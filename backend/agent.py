import anthropic
from search import web_search
from config import ANTHROPIC_API_KEY


async def twinkle_respond(user_query: str) -> dict:
    """Main AI brain: search the web, then synthesize answer with Claude"""

    # Step 1: Search the web
    search_results = await web_search(user_query)

    # Step 2: Format results as context
    if search_results:
        context = "\n\n".join([
            f"Source [{i+1}]: {r['title']}\nURL: {r['link']}\nInfo: {r['snippet']}"
            for i, r in enumerate(search_results)
        ])
    else:
        context = "No search results found."

    # Step 3: Use Claude to synthesize the answer
    if not ANTHROPIC_API_KEY:
        return {
            "answer": (
                "⚠️ ANTHROPIC_API_KEY is missing in your .env file.\n\n"
                "Please add your Anthropic API key to backend/.env:\n"
                "ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx\n\n"
                "Get your key at: https://console.anthropic.com"
            ),
            "sources": search_results
        }

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    system_prompt = """You are Twinkle AI — a smart, friendly, and concise search assistant.
You receive real-time web search results and answer the user's query clearly.
Always cite sources by mentioning [1], [2], etc. when referencing them.
Keep answers focused, helpful, and easy to read."""

    user_message = f"""User asked: {user_query}

Here are the latest web search results:
{context}

Please provide a helpful, accurate answer based on these results. 
Cite sources using [1], [2], etc."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}]
    )

    return {
        "answer":  response.content[0].text,
        "sources": search_results
    }
