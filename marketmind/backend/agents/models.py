from typing import List, Optional, Dict, Any
from pydantic import BaseModel



class CompetitorStats(BaseModel):
    """📊 Indicadores de desempenho da empresa concorrente"""
    receita_anual: Optional[str] = None         # Ex: "R$ 12 milhões"
    crescimento_anual: Optional[str] = None     # Ex: "15% ao ano"
    numero_funcionarios: Optional[int] = None
    principais_produtos: List[str] = []
    presenca_mercado: Optional[str] = None      # Ex: "líder nacional", "em expansão"
    avaliacoes_clientes: Optional[str] = None   # Ex: "avaliações positivas sobre sustentabilidade"



class CompetitorInfo(BaseModel):
    """🏢 Informações principais sobre o competidor"""
    nome: str
    setor: Optional[str] = None                 # Ex: "reciclagem", "energia solar"
    sede: Optional[str] = None                  # Ex: "São Paulo, Brasil"
    fundacao: Optional[str] = None              # Ex: "1999"
    executivos: List[str] = []                  # Ex: ["Maria Silva (CEO)"]
    site_oficial: Optional[str] = None
    descricao: Optional[str] = None             # Ex: resumo textual
    desempenho: Optional[CompetitorStats] = None



class CompetitorAnalysis(BaseModel):
    """🧠 Análise interpretativa do momento da empresa"""
    forca_geral: Optional[str] = None           # Ex: "forte", "em expansão", "em crise"
    oportunidades: List[str] = []               # Ex: ["crescimento do mercado verde"]
    ameacas: List[str] = []                     # Ex: ["alta concorrência internacional"]
    desafios_atuais: Optional[str] = None       # Ex: "falta de investimentos"
    perspectiva_futura: Optional[str] = None    # Ex: "deve crescer 10% no próximo ano"
    resumo_analitico: Optional[str] = None      # Ex: texto de 3–5 frases



class ResearchState(BaseModel):
    """🌐 Estado do fluxo de pesquisa de mercado"""
    query: str                                  # Ex: "empresas de reciclagem no Brasil"
    empresas_extraidas: List[str] = []          # Lista de empresas identificadas
    competidores: List[CompetitorInfo] = []     # Dados detalhados de cada competidor
    resultados_pesquisa: List[Dict[str, Any]] = []
    analise: Optional[CompetitorAnalysis] = None