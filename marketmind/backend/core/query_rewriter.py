from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage



class QueryRewriter:
    """ Agente responsável por gerar múltiplas reformulações de uma consulta original.
    Útil para enriquecer buscas e capturar contextos diferentes. """

    def __init__(self, model: str = "gemini-2.5-flash", temperature: float = 0.7):
        self.llm = ChatGoogleGenerativeAI(model=model, temperature=temperature)

    def rewrite(self, query: str, num_queries: int = 3) -> List[str]:
        """ Gera `num_queries` variações de uma query. """

        system_msg = SystemMessage(content=(
            "Você é um especialista em análise de mercado encarregado de reformular consultas "
            "de busca para coletar competidores no ramo, notícias recentes, lançamentos."
            "Dada uma consulta inicial, gere variações curtas e naturais, "
            "que ampliem o contexto e tragam resultados relevantes. "
            f"Retorne exatamente {num_queries} consultas, separadas por quebras de linha. "
            "Não inclua explicações ou comentários."
        ))

        user_msg = HumanMessage(content=f"Consulta original: {query}")

        try:
            response = self.llm.invoke([system_msg, user_msg])
            queries = [
                q.strip() for q in response.content.split("\n")
                if q.strip()
            ]

            return queries[:num_queries]

        except Exception as e:
            print("❌ Erro no QueryRewriter:", e)

            return []