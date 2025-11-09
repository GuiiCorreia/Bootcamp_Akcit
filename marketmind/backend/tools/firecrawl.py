import os
import requests
from dotenv import load_dotenv



load_dotenv()

class FirecrawlService:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("Missing FIRECRAWL_API_KEY environment variable")
        self.api_key = api_key

    def search_competitors(self, query: str, num_results: int = 10):
        """ Busca por páginas de uma query específica """
        url = "https://api.firecrawl.dev/v2/search"

        payload = {
            "query": query,
            "limit": num_results,
            "scrapeOptions": {
                "formats": ["markdown"]
            }
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            print(f"\n🧭 Buscando por: {query}")
            data = requests.post(url, json=payload, headers=headers).json()

            if not data.get("success"):
                print("❌ Erro na requisição Firecrawl:", data)
                return []

            results = data.get("data", {}).get("web", [])

            return results

        except Exception as e:
            print(f"❌ Erro geral ao buscar times: {e}")
            return []

    def scrape_competitors_page(self, url: str):
        """ Raspa o conteúdo de uma página específica """
        endpoint = "https://api.firecrawl.dev/v2/scrape"

        payload = {
            "url": url,
            "formats": ["markdown"]
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(endpoint, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            return data.get("data", {}).get("content", data)
        except Exception as e:
            print(f"❌ Erro ao raspar página {url}: {e}")
            return None