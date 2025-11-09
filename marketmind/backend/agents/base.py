from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from backend.tools.firecrawl import FirecrawlService
from .prompts import CompetitorPrompts



class BaseAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
        self.firecrawl = FirecrawlService()
        self.prompts = CompetitorPrompts()

    def log(self, msg: str):
        print(f"[{self.__class__.__name__}] {msg}")

    def run_llm(self, system_content: str, user_content: str, structured_output=None):
        """ Executa o LLM com mensagens formatadas. """
        messages = [
            SystemMessage(content=system_content),
            HumanMessage(content=user_content),
        ]
        if structured_output:
            return self.llm.with_structured_output(structured_output).invoke(messages)
        return self.llm.invoke(messages)
