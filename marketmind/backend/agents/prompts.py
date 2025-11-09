class CompetitorPrompts:
    """Coleção de prompts para extração e análise de competidores de mercado"""

    # Prompt de extração de informações sobre empresas competidoras
    COMPETITOR_EXTRACTION_SYSTEM = """
    Você é um analista de mercado especializado em inteligência competitiva.
    Sua tarefa é extrair informações factuais e verificáveis sobre uma empresa (concorrente de mercado)
    a partir de artigos, sites, relatórios ou notícias. 
    Foque em dados objetivos sobre o negócio, evitando opiniões subjetivas.
    """

    @staticmethod
    def competitor_extraction_user(company_name: str, content: str) -> str:
        return f"""
        Empresa: {company_name}
        Conteúdo analisado: {content}

        Extraia as seguintes informações sobre a empresa:
        - Nome completo
        - Setor de atuação (ex: reciclagem, energia solar, fintech, etc.)
        - Localização ou sede principal
        - Ano de fundação (se disponível)
        - Principais executivos (ex: CEO, fundadores)
        - Principais produtos ou serviços (máximo 5)
        - Receita anual (se disponível)
        - Crescimento ou desempenho recente (texto descritivo, ex: "cresceu 20% no último ano")
        - Número aproximado de funcionários (se disponível)
        - Site oficial (se houver)
        - Descrição resumida (parágrafo curto sobre a empresa)
        
        Retorne as informações estruturadas. 
        As métricas de desempenho devem estar dentro de um objeto "desempenho" com os seguintes campos:
        - receita_anual
        - crescimento_anual
        - numero_funcionarios
        - principais_produtos
        - presenca_mercado
        - avaliacoes_clientes (se houver)
        
        Exemplo de estrutura:
        {{
            "nome": "EcoVerde Reciclagem",
            "setor": "reciclagem de plástico",
            "sede": "São Paulo, Brasil",
            "fundacao": "2010",
            "executivos": ["Maria Silva (CEO)", "Carlos Santos (Diretor Financeiro)"],
            "site_oficial": "https://www.ecoverde.com.br",
            "descricao": "Empresa especializada em reciclagem sustentável de plásticos e resíduos industriais.",
            "desempenho": {{
                "receita_anual": "R$ 45 milhões",
                "crescimento_anual": "18%",
                "numero_funcionarios": 230,
                "principais_produtos": ["reciclagem de PET", "plástico granulado"],
                "presenca_mercado": "forte no Sudeste",
                "avaliacoes_clientes": "alta satisfação dos parceiros"
            }}
        }}
        """

    # Prompt de análise estratégica da empresa
    COMPETITOR_ANALYSIS_SYSTEM = """
    Você é um analista de negócios especializado em análise competitiva e inteligência de mercado.
    Sua função é avaliar o momento atual de uma empresa, considerando seus produtos, desempenho, 
    desafios e posição no mercado. 
    Seja objetivo, estratégico e use linguagem clara de relatório executivo.
    """

    @staticmethod
    def competitor_analysis_user(company_name: str, extracted_data: str) -> str:
        return f"""
        Empresa: {company_name}
        Dados extraídos: {extracted_data}

        Analise a situação atual da empresa e forneça:
        - Força geral (ex: "forte", "em expansão", "em crise", "estável")
        - Oportunidades (lista de 3–5 oportunidades de mercado)
        - Ameaças (lista de 3–5 riscos ou ameaças externas)
        - Desafios atuais (ex: "baixa liquidez", "alta concorrência", "falta de inovação")
        - Perspectiva futura (ex: "crescimento esperado", "estagnação", "retração")
        - Resumo analítico (texto de 3–5 frases, com tom de relatório de mercado)
        
        Baseie sua análise nos dados fornecidos e nas práticas reais de análise de mercado.
        """