from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage
from .models import ResearchState, CompetitorInfo



class ExtractCompetitorInfoAgent:
    """Agente responsável por buscar e extrair informações estruturadas sobre competidores de mercado."""

    def __init__(self, llm, firecrawl, rewriter, prompts):
        self.llm = llm
        self.firecrawl = firecrawl
        self.rewriter = rewriter
        self.prompts = prompts

    def run(self, state: ResearchState) -> Dict[str, Any]:
        print(f"🔎 Buscando informações sobre competidores do setor: {state.query}")

        current_query = state.query
        all_content = ""
        attempt = 1

        while True:
            print(f"\n🧭 Tentativa {attempt}: buscando '{current_query}'")

            try:
                # 🔍 Busca inicial com Firecrawl
                search_results = self.firecrawl.search_competitors(current_query, num_results=5)

                for result in search_results:
                    url = result.get("url", "")
                    scraped = self.firecrawl.scrape_competitors_page(url)

                    if scraped and "data" in scraped:
                        markdown = scraped["data"].get("markdown", "")
                        if markdown:
                            all_content += markdown[:1500] + "\n\n"

                if all_content.strip():
                    print(f"✅ Conteúdo encontrado após {attempt} tentativa(s).")
                    break

                print("⚠️ Nenhum conteúdo relevante encontrado. Gerando novas variações de busca...")
                rewritten_queries = self.rewriter.rewrite(current_query, num_queries=2)

                found_content = False
                for new_query in rewritten_queries:
                    print(f"🧠 Testando variação: '{new_query}'")
                    search_results = self.firecrawl.search_competitors(new_query, num_results=5)

                    for result in search_results:
                        url = result.get("url", "")
                        scraped = self.firecrawl.scrape_competitors_page(url)
                        if scraped and "data" in scraped:
                            markdown = scraped["data"].get("markdown", "")
                            if markdown:
                                all_content += markdown[:1500] + "\n\n"
                                found_content = True
                                current_query = new_query
                                break

                    if found_content:
                        print(f"✅ Conteúdo encontrado com variação: {new_query}")
                        break

                if found_content:
                    break

                attempt += 1

            except Exception as e:
                print(f"❌ Erro na tentativa {attempt}: {e}")
                attempt += 1
                continue

        try:
            competitor_info = self.llm.with_structured_output(CompetitorInfo).invoke([
                SystemMessage(content=self.prompts.COMPETITOR_EXTRACTION_SYSTEM),
                HumanMessage(content=self.prompts.competitor_extraction_user(state.query, all_content))
            ])

            print(f"✅ Informações extraídas: {competitor_info.nome} ({competitor_info.setor})")
            return {"competidores": [competitor_info]}

        except Exception as e:
            print("❌ Erro na extração:", e)
            return {"competidores": []}
