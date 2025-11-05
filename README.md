# 🧠 MarketMind - Documentação de Desenvolvimento

## 📋 Objetivo do Projeto

**Desenvolver um sistema multiagente para análise automatizada de mercado que gere relatórios executivos consultando 15+ fontes de dados.**

### Requisitos Funcionais
- [ ] Análise de mercado (tamanho, crescimento, segmentação)
- [ ] Mapeamento de competidores (identificação, análise, posicionamento)
- [ ] Análise de presença digital (redes sociais, SEO, sentiment)
- [ ] Identificação de tendências (notícias, papers, sinais emergentes)
- [ ] Pesquisa acadêmica (papers, estudos científicos, alinhamento com academia)
- [ ] Inteligência financeira (investimentos, valuations)
- [ ] Query rewriting para expansão de contexto
- [ ] Geração de relatório executivo estruturado
- [ ] Sistema RAG para Q&A sobre dados coletados

### Requisitos Não-Funcionais
- [ ] Paralelização: Agentes executam simultaneamente
- [ ] Cache: Reduzir chamadas repetidas de API
- [ ] Rastreabilidade: Toda informação com fonte citada
- [ ] UI real-time: Mostrar progresso dos agentes

## 🏗️ Arquitetura do Sistema

### Fluxo Geral
```mermaid
graph TD
    A[User Input] --> B[Synthesis Agent]
    B --> C{Task Decomposition + Query Rewriting}
    
    C -->|Parallel| D[Market Research Agent]
    C -->|Parallel| E[Competitor Agent]
    C -->|Parallel| F[Digital Presence Agent]
    C -->|Parallel| G[News & Trends Agent]
    C -->|Parallel| H[Financial Agent]
    C -->|Parallel| I[Paper Research Agent]
    
    D --> J[Shared Context]
    E --> J
    F --> J
    G --> J
    H --> J
    I --> J
    
    J --> K[Synthesis Agent]
    K --> L[Report Generation]
    L --> M[Vector Store/RAG]
    M --> N[Output]
```

### Arquitetura de Componentes
```mermaid
graph TB
    subgraph "Frontend Layer"
        UI[React App]
        WS[WebSocket Client]
    end
    
    subgraph "API Layer"
        API[FastAPI]
        WSS[WebSocket Server]
    end
    
    subgraph "Processing Layer"
        ORCH[Orchestrator/LangGraph]
        QR[Query Rewriter]
        AGENTS[Agent Pool]
        TOOLS[Tool Registry]
    end
    
    subgraph "Data Layer"
        PG[(PostgreSQL)]
        REDIS[(Redis Cache)]
        VECTOR[(Qdrant)]
    end
    
    UI <--> API
    WS <--> WSS
    API --> ORCH
    ORCH --> QR
    QR --> AGENTS
    ORCH --> AGENTS
    AGENTS --> TOOLS
    ORCH --> PG
    TOOLS --> REDIS
    AGENTS --> VECTOR
```

## 🤖 Definição dos Agentes

### 1. Synthesis Agent (Orquestrador)
```python
class SynthesisAgent:
    """
    Responsável por:
    - Decompor query em tarefas
    - Implementar query rewriting para expansão de contexto
    - Coordenar execução paralela
    - Resolver conflitos de dados
    - Gerar insights finais
    """
    
    tools = []  # Não usa tools externas
    llm = "gemini-2.5-flash-lite"
    
    def rewrite_queries(query: str) -> List[str]:
        """
        Gera variações da query original para aumentar cobertura:
        - Reformulação técnica
        - Variações de linguagem
        - Expansão de termos
        - Queries relacionadas
        """
        pass
    
    def decompose_task(query: str, rewritten_queries: List[str]) -> List[Task]:
        # Lógica de decomposição com contexto expandido
        pass
    
    def synthesize_results(results: Dict) -> Report:
        # Consolidação e insights
        pass
```

### 2. Market Research Agent
```python
class MarketResearchAgent:
    """
    Coleta: TAM, SAM, SOM, crescimento, segmentação
    """
    tools = [
        "ibge_api",        # Dados BR
        "world_bank_api",  # Dados globais
        "statista_api",    # Estatísticas setoriais
        "web_search"       # Relatórios públicos
    ]
    llm = "gemini-2.5-flash-lite"
```

### 3. Competitor Agent
```python
class CompetitorAgent:
    """
    Identifica e analisa competidores
    """
    tools = [
        "firecrawl",       # Web scraping
        "similarweb_api",  # Analytics
        "google_places",   # Localização
        "linkedin_api"     # Dados corporativos
    ]
    llm = "gemini-2.5-flash-lite"
```

### 4. Digital Presence Agent
```python
class DigitalPresenceAgent:
    """
    Analisa presença digital e sentiment
    """
    tools = [
        "social_media_api", # Twitter, Instagram, etc
        "seo_tools",        # Análise SEO
        "sentiment_api",    # Análise de sentimento
        "reddit_api"        # Discussões públicas
    ]
    llm = "gemini-2.5-flash-lite"
```

### 5. News & Trends Agent
```python
class NewsTrendsAgent:
    """
    Identifica tendências e notícias recentes
    """
    tools = [
        "newsapi",         # Notícias
        "google_trends",   # Tendências de busca
        "web_search",      # Busca geral
        "rss_feeds"        # Feeds especializados
    ]
    llm = "gemini-2.5-flash-lite"
```

### 6. Paper Research Agent 🆕
```python
class PaperResearchAgent:
    """
    Busca e analisa papers acadêmicos para:
    - Validar tendências de mercado com evidências científicas
    - Identificar tecnologias emergentes
    - Fornecer embasamento técnico para insights
    - Alinhar análise de mercado com pesquisa acadêmica
    
    Utiliza query rewriting para maximizar cobertura:
    - Termos técnicos vs coloquiais
    - Sinônimos e variações
    - Queries em inglês (maioria dos papers)
    """
    tools = [
        "arxiv_api",           # Papers de CS, Physics, Math
        "semantic_scholar",    # Busca acadêmica geral
        "pubmed_api",          # Papers médicos/biológicos
        "google_scholar",      # Busca ampla
        "crossref_api",        # Metadados de publicações
        "core_api"             # Open access papers
    ]
    llm = "gemini-2.5-flash-lite"
    
    def rewrite_academic_query(self, query: str) -> List[str]:
        """
        Gera variações acadêmicas da query:
        - Tradução para inglês
        - Termos técnicos
        - Sinônimos científicos
        - Queries relacionadas
        """
        pass
    
    def filter_relevant_papers(self, papers: List[Paper], query: str) -> List[Paper]:
        """
        Filtra papers por relevância, recência e citações
        """
        pass
    
    def extract_insights(self, papers: List[Paper]) -> Dict:
        """
        Extrai insights dos papers:
        - Tendências tecnológicas
        - Validação científica de claims
        - Gaps de pesquisa = oportunidades
        """
        pass
```

### 7. Financial Agent
```python
class FinancialAgent:
    """
    Coleta inteligência financeira
    """
    tools = [
        "alpha_vantage",   # Dados de ações
        "crunchbase",      # Funding de startups
        "yahoo_finance",   # Dados financeiros
        "sec_edgar"        # Relatórios corporativos
    ]
    llm = "gemini-2.5-flash-lite"
```

## 📦 Estrutura de Diretórios
```
marketmind/
├── backend/
│   ├── agents/
│   │   ├── base.py              # Classe base dos agentes
│   │   ├── synthesis.py         # Orquestrador + Query Rewriting
│   │   ├── market.py
│   │   ├── competitor.py
│   │   ├── digital.py
│   │   ├── news.py
│   │   ├── paper_research.py    # 🆕 Agente de Papers
│   │   └── financial.py
│   ├── tools/
│   │   ├── registry.py          # Registro de ferramentas
│   │   ├── apis/
│   │   │   ├── ibge.py
│   │   │   ├── serpapi.py
│   │   │   ├── newsapi.py
│   │   │   ├── arxiv.py         # 🆕
│   │   │   ├── semantic_scholar.py  # 🆕
│   │   │   ├── pubmed.py        # 🆕
│   │   │   └── ...
│   │   └── scrapers/
│   │       ├── firecrawl.py
│   │       └── beautifulsoup.py
│   ├── core/
│   │   ├── orchestrator.py      # LangGraph
│   │   ├── query_rewriter.py    # 🆕 Query Rewriting
│   │   ├── config.py
│   │   ├── cache.py             # Redis
│   │   └── vectorstore.py       # Qdrant
│   ├── api/
│   │   ├── main.py              # FastAPI
│   │   ├── routes/
│   │   └── websocket.py
│   └── reports/
│       ├── generator.py
│       └── templates/
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── AgentStatus.tsx
    │   │   ├── ProgressBar.tsx
    │   │   └── Report.tsx
    │   └── pages/
    └── package.json
```

## 🛠️ Stack de Desenvolvimento

### Backend
| Tecnologia | Versão | Uso | Responsável |
|------------|--------|-----|-------------|
| Python | 3.11+ | Core | Todos |
| FastAPI | 0.104+ | API REST | - |
| LangChain | 0.1.x | Framework LLM | - |
| LangGraph | 0.0.x | Orquestração | - |
| Celery | 5.3+ | Tasks assíncronas | - |
| Redis | 7+ | Cache + Queue | - |
| PostgreSQL | 15+ | Dados persistentes | - |
| Qdrant | 0.4+ | Vector store | - |

### Frontend
| Tecnologia | Versão | Uso | Responsável |
|------------|--------|-----|-------------|
| React | 18+ | UI Framework | - |
| TypeScript | 5+ | Type safety | - |
| TailwindCSS | 3+ | Styling | - |
| shadcn/ui | latest | Components | - |
| Recharts | 2+ | Gráficos | - |
| Socket.io | 4+ | WebSocket | - |

## 🔑 APIs e Integrações

### Tier Gratuito Disponível
```yaml
Essenciais:
  OpenAI:
    - Custo: ~$0.01 por request
    - Uso: LLMs e embeddings
    
  Firecrawl:
    - Free: 500 pages/mês
    - Uso: Scraping de sites
    
  SerpAPI:
    - Free: 100 searches/mês
    - Uso: Google search
    
  NewsAPI:
    - Free: 100 requests/dia
    - Uso: Notícias recentes

Papers/Academia: # 🆕
  arXiv API:
    - Free: Ilimitado
    - Uso: Papers de CS, Physics, Math
    
  Semantic Scholar:
    - Free: 100 req/5min
    - Uso: Busca acadêmica + citações
    
  PubMed API:
    - Free: Ilimitado (com rate limit)
    - Uso: Papers médicos/biológicos
    
  CORE API:
    - Free: 1000 req/dia
    - Uso: Open access papers
    
  CrossRef:
    - Free: Ilimitado
    - Uso: Metadados de publicações

Complementares:
  Alpha Vantage:
    - Free: 500 calls/dia
    - Uso: Dados financeiros
    
  Google Trends:
    - Free: Ilimitado (com rate limit)
    - Uso: Tendências
    
  IBGE APIs:
    - Free: Ilimitado
    - Uso: Dados Brasil
    
  Reddit API:
    - Free: 60 req/min
    - Uso: Discussões

Opcionais (melhoram qualidade):
  Crunchbase:
    - Trial: 100 calls
    - Uso: Startups/funding
    
  SimilarWeb:
    - Trial: 50 queries
    - Uso: Analytics
```

## 📅 Cronograma de Desenvolvimento

### SÁBADO (11h de desenvolvimento)

#### Manhã (8h-13h) - 5h - CORE
```mermaid
gantt
    title Sábado Manhã
    dateFormat HH:mm
    section Setup
    Estrutura base      :08:00, 30m
    Configurações       :08:30, 30m
    section Backend Core
    Synthesis Agent + Query Rewriting :09:00, 1h
    2 Agentes básicos   :10:00, 2h
    section Integração
    3 APIs principais   :12:00, 1h
```

**Entregáveis Manhã:**
- [ ] Projeto estruturado
- [ ] Synthesis Agent com query rewriting
- [ ] Market + Competitor agents básicos
- [ ] Integração com SerpAPI, NewsAPI, Firecrawl

#### Tarde (14h-19h) - 5h - EXPANSÃO
```mermaid
gantt
    title Sábado Tarde
    dateFormat HH:mm
    section Agentes
    Digital Agent       :14:00, 1h
    News Agent          :15:00, 45m
    Paper Research Agent :15:45, 1h15m
    Financial Agent     :17:00, 45m
    section Orquestração
    LangGraph setup     :17:45, 45m
    Execução paralela   :18:30, 30m
```

**Entregáveis Tarde:**
- [ ] Todos 6 agentes especializados (incluindo Paper Research)
- [ ] Orquestração com LangGraph
- [ ] Query rewriting implementado
- [ ] Integração com APIs acadêmicas (arXiv, Semantic Scholar)
- [ ] Compartilhamento de contexto
- [ ] Cache Redis básico

### DOMINGO (11h30min de desenvolvimento)

#### Manhã (8h-13h) - 5h - INTERFACE & POLISH
```mermaid
gantt
    title Domingo Manhã
    dateFormat HH:mm
    section Frontend
    Setup React         :08:00, 30m
    Dashboard básico    :08:30, 1h30m
    WebSocket updates   :10:00, 1h
    section Reports
    Template design     :11:00, 1h
    PDF generation      :12:00, 1h
```

**Entregáveis Manhã:**
- [ ] Frontend funcionando
- [ ] Visualização real-time dos agentes (incluindo Paper Research)
- [ ] Geração de relatório PDF com seção acadêmica
- [ ] UI polida

#### Tarde (14h-19h30) - 5h30min - FINALIZAÇÃO
```mermaid
gantt
    title Domingo Tarde
    dateFormat HH:mm
    section RAG
    Qdrant setup      :14:00, 1h
    RAG implementation  :15:00, 1h
    section Testing
    Testes integrados   :16:00, 1h
    Ajustes finais      :17:00, 1h
    section Deploy
    Easypanel deploy    :18:00, 30m
    section Apresentação
    Demo prep           :18:30, 30m
    Pitch practice      :19:00, 30m
```

**Entregáveis Tarde:**
- [ ] RAG funcionando (incluindo papers no vector store)
- [ ] Sistema testado end-to-end
- [ ] Deploy em produção
- [ ] Apresentação preparada

## 🧪 Plano de Testes

### Casos de Teste Prioritários

1. **Teste Básico**: "Energia solar em Goiás"
   - Validar todos os agentes retornam dados
   - Paper Research Agent encontra papers relevantes
   - Tempo < 5 minutos
   - Relatório gerado com seção acadêmica

2. **Teste Query Rewriting**: Verificar expansão de contexto
   - Query original gera 3-5 variações
   - Variações capturam dados complementares
   - Papers encontrados são relevantes

3. **Teste de Stress**: Executar 3 análises simultâneas
   - Verificar paralelização
   - Monitorar uso de memória
   - Validar cache

4. **Teste de Qualidade**: Comparar com pesquisa manual
   - Precisão dos dados de mercado
   - Competidores identificados corretamente
   - Papers são relevantes e recentes
   - Insights fazem sentido

## 🚨 Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Rate limit de APIs | Alta | Alto | Cache agressivo + APIs alternativas |
| LLM hallucination | Média | Alto | Validação cruzada + citação obrigatória |
| Papers irrelevantes | Média | Médio | Filtros de relevância + threshold de citações |
| Tempo > 5 min | Média | Médio | Timeout + resultado parcial |
| Query rewriting ineficaz | Baixa | Médio | Prompts bem calibrados + exemplos |
| Crash durante demo | Baixa | Alto | Video backup + deploy redundante |

## 💡 Benefícios do Paper Research Agent

### Para o Sistema
- ✅ **Validação Científica**: Claims de mercado validados com papers
- ✅ **Contexto Expandido**: Query rewriting aumenta cobertura de dados
- ✅ **Diferencial Competitivo**: Poucos sistemas integram academia + mercado
- ✅ **Identificação de Trends**: Papers mostram tecnologias antes do mercado

### Para o Relatório
- 📊 **Seção "Evidências Acadêmicas"**: Papers relevantes citados
- 🔬 **Validação Técnica**: Insights embasados cientificamente
- 🚀 **Tecnologias Emergentes**: Pesquisas apontam futuro do setor
- 📈 **Gaps de Pesquisa**: Oportunidades de mercado não exploradas

---

**FOCO**: Entregar um MVP funcional que impressione. Better done than perfect! 🚀
