from typing import Dict, Any
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from backend.agents.models import ResearchState
from backend.tools.firecrawl import FirecrawlService
from backend.agents.prompts import CompetitorPrompts
from backend.core.query_rewriter import QueryRewriter
from backend.agents.extract_competitor_info_agent import ExtractCompetitorInfoAgent
from backend.agents.analyze_competitor_agent import AnalyzeCompetitorAgent



class CompetitorWorkflow:
    """
    Fluxo completo de análise de competidores:
    1️⃣ Busca e extração de informações sobre empresas do mercado.
    2️⃣ Geração de uma análise estruturada com base nas informações coletadas.
    """

    def __init__(self):
        # Modelos e ferramentas
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
        self.firecrawl = FirecrawlService()
        self.rewriter = QueryRewriter()
        self.prompts = CompetitorPrompts()

        # Agentes
        self.extract_agent = ExtractCompetitorInfoAgent(
            self.llm, self.firecrawl, self.rewriter, self.prompts
        )
        self.analyze_agent = AnalyzeCompetitorAgent(self.llm, self.prompts)

        # Monta o grafo do workflow
        self.workflow = self._build_workflow()

    def _build_workflow(self):
        graph = StateGraph(ResearchState)

        # Etapas do pipeline
        graph.add_node("extract_competitor_info", self._extract_competitor_info_step)
        graph.add_node("analyze_competitor", self._analyze_competitor_step)

        # Fluxo sequencial
        graph.set_entry_point("extract_competitor_info")
        graph.add_edge("extract_competitor_info", "analyze_competitor")
        graph.add_edge("analyze_competitor", END)

        return graph.compile()

    # ======== Etapas individuais ========

    def _extract_competitor_info_step(self, state: ResearchState) -> Dict[str, Any]:
        """Executa o agente que coleta e estrutura os dados de empresas/competidores."""
        return self.extract_agent.run(state)

    def _analyze_competitor_step(self, state: ResearchState) -> Dict[str, Any]:
        """Executa o agente que gera a análise de mercado dos competidores."""
        return self.analyze_agent.run(state)

    # ======== Execução do pipeline completo ========

    def run(self, query: str) -> ResearchState:
        """Inicia o fluxo de pesquisa e análise de competidores."""
        initial_state = ResearchState(query=query)
        final_state = self.workflow.invoke(initial_state)
        return ResearchState(**final_state)
