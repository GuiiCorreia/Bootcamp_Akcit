from typing import Dict, Any
from langchain_core.messages import SystemMessage, HumanMessage
from .models import ResearchState, CompetitorAnalysis


class AnalyzeCompetitorAgent:
    """Agente responsável por gerar uma análise estratégica sobre os competidores de mercado encontrados."""

    def __init__(self, llm, prompts):
        self.llm = llm
        self.prompts = prompts

    def run(self, state: ResearchState) -> Dict[str, Any]:
        print("📊 Gerando análise sobre a situação atual dos competidores")

        if not state.competidores:
            print("⚠️ Nenhum competidor disponível para análise.")
            return {"analise": None}

        competitor = state.competidores[0]  # Foco inicial no principal competidor

        try:
            analysis = self.llm.with_structured_output(CompetitorAnalysis).invoke([
                SystemMessage(content=self.prompts.COMPETITOR_ANALYSIS_SYSTEM),
                HumanMessage(content=self.prompts.competitor_analysis_user(
                    competitor.nome,
                    competitor.json()
                ))
            ])

            print("✅ Análise de competidor gerada com sucesso.")
            return {"analise": analysis}

        except Exception as e:
            print(f"❌ Erro na análise de competidor: {e}")
            return {"analise": None}
