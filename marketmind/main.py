from dotenv import load_dotenv
from backend.core.workflow import CompetitorWorkflow

load_dotenv()


def main():
    workflow = CompetitorWorkflow()
    print("💼 Agente de Análise de Mercado e Competidores 💼")

    while True:
        query = input("\n🔍 Qual empresa ou mercado deseja pesquisar? ").strip()
        if query.lower() in {"sair", "exit", "quit"}:
            print("Encerrando o agente. 👋")
            break

        if query:
            result = workflow.run(query)

            print(f"\n📊 Resultados para: {query}")
            print("=" * 70)

            # Exibe informações extraídas sobre os competidores
            for i, company in enumerate(result.competidores, 1):
                print(f"\n{i}. 🏢 {company.nome}")

                if company.setor:
                    print(f"   🏭 Setor: {company.setor}")
                if company.sede:
                    print(f"   🌍 Sede: {company.sede}")
                if company.fundacao:
                    print(f"   📅 Fundação: {company.fundacao}")
                if company.executivos:
                    print(f"   👤 Executivos: {', '.join(company.executivos)}")
                if company.site_oficial:
                    print(f"   🌐 Site Oficial: {company.site_oficial}")
                if company.descricao:
                    print(f"   📝 Descrição: {company.descricao}")

                # Estatísticas e desempenho
                if company.desempenho:
                    print("   📊 Indicadores de Desempenho:")
                    if company.desempenho.receita_anual:
                        print(f"      💰 Receita Anual: {company.desempenho.receita_anual}")
                    if company.desempenho.crescimento_anual:
                        print(f"      📈 Crescimento Anual: {company.desempenho.crescimento_anual}")
                    if company.desempenho.numero_funcionarios:
                        print(f"      👥 Funcionários: {company.desempenho.numero_funcionarios}")
                    if company.desempenho.principais_produtos:
                        print(f"      📦 Produtos: {', '.join(company.desempenho.principais_produtos[:5])}")
                    if company.desempenho.presenca_mercado:
                        print(f"      🌎 Presença no Mercado: {company.desempenho.presenca_mercado}")
                    if company.desempenho.avaliacoes_clientes:
                        print(f"      ⭐ Avaliações: {company.desempenho.avaliacoes_clientes}")

                print()

            # Exibe análise estratégica
            if result.analise:
                print("🧩 Análise de Competitividade e Mercado:")
                print("-" * 60)
                if result.analise.forca_geral:
                    print(f"💪 Força Geral: {result.analise.forca_geral}")
                if result.analise.oportunidades:
                    print(f"💡 Oportunidades: {', '.join(result.analise.oportunidades)}")
                if result.analise.ameacas:
                    print(f"🔥 Ameaças: {', '.join(result.analise.ameacas)}")
                if result.analise.desafios_atuais:
                    print(f"⚠️ Desafios Atuais: {result.analise.desafios_atuais}")
                if result.analise.perspectiva_futura:
                    print(f"🔮 Perspectiva Futura: {result.analise.perspectiva_futura}")
                if result.analise.resumo_analitico:
                    print(f"\n📝 Resumo Analítico:\n{result.analise.resumo_analitico}")
                print()


if __name__ == "__main__":
    main()
