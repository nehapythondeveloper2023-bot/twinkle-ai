import httpx
from config import SERPER_API_KEY


async def web_search(query: str, num_results: int = 5) -> list:
    """Search the web using Serper API (free tier at serper.dev)"""
    if not SERPER_API_KEY:
        # Return mock results if no API key set yet
        return [
            {
                "title": "Example Result 1 - Add your SERPER_API_KEY in .env",
                "link": "https://serper.dev",
                "snippet": "Sign up at serper.dev to get your free API key (2500 free searches/month)."
            },
            {
                "title": "Example Result 2 - Twinkle AI is working!",
                "link": "https://docs.anthropic.com",
                "snippet": "Your Twinkle AI backend is running. Add API keys to .env to enable real search."
            }
        ]

    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query, "num": num_results}

    async with httpx.AsyncClient(timeout=10.0) as client:
        resp = await client.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    results = []
    for item in data.get("organic", []):
        results.append({
            "title":   item.get("title", ""),
            "link":    item.get("link", ""),
            "snippet": item.get("snippet", ""),
        })
    return results
