# ESTRUTURA DE DADOS
empresa_data = {

    "Matriz": {

        "TI": {

            "Infraestrutura": {
                "Servidores": 50000,
                "Seguranca": 30000,
                "Backup": 12000,
                "Cloud": 45000
            },

            "Desenvolvimento": {
                "Frontend": 20000,
                "Backend": 25000,
                "DevOps": 15000,
                "QA": 10000,

                "Mobile": {
                    "Android": 12000,
                    "iOS": 14000
                }
            },

            "Suporte": {
                "HelpDesk": 8000,
                "Monitoramento": 6000
            }
        },

        "RH": {

            "Recrutamento": 10000,
            "Treinamento": 12000,

            "Cultura": {
                "Eventos": 5000,
                "Brindes": 2000,
                "Campanhas": 3500
            }
        },

        "Financeiro": {
            "Auditoria": 18000,
            "Contabilidade": 22000,
            "FolhaPagamento": 40000
        },

        "Logistica": {

            "Transportes": {
                "Frota": 30000,
                "Combustivel": 12000
            },

            "Estoque": {
                "Armazem": 20000,
                "Controle": 8000
            }
        }
    }
}


# Biblioteca time
import time

# Decorator de auditoria
def auditor(func):

    def wrapper(*args, **kwargs):

        print("\n--- AUDITORIA FINANCEIRA ---")
        print("Iniciando cálculo do orçamento...\n")

        print(f"Departamentos ignorados (*args): {args[1:]}")
        print(f"Parâmetros financeiros (**kwargs): {kwargs}")

        inicio = time.time()

        resultado = func(*args, **kwargs)

        fim = time.time()

        print(f"\nTempo total de execução: {fim - inicio:.6f} segundos")
        print("--- FIM DA AUDITORIA ---\n")

        return resultado

    return wrapper

# FUNÇÃO RECURSIVA
@auditor
def calcular_orcamento(
        estrutura,
        *departamentos_ignorados,
        moeda_destino="BRL",
        taxa_cambio=1.0):

    total = 0

    # Percorre todo o dicionário
    for chave, valor in estrutura.items():

        # Ignora departamentos
        if chave in departamentos_ignorados:
            print(f"\nDepartamento ignorado: {chave}")
            continue

        # Se for outro dicionário -> recursão
        if isinstance(valor, dict):

            total += calcular_orcamento(
                valor,
                *departamentos_ignorados,
                moeda_destino=moeda_destino,
                taxa_cambio=1.0
            )

        # Se for número -> soma
        elif isinstance(valor, (int, float)):

            total += valor

    # Conversão financeira
    total_convertido = total * taxa_cambio

    return total_convertido


# ORÇAMENTO COMPLETO
print("--- ORÇAMENTO COMPLETO ---")

orcamento_total = calcular_orcamento(
    empresa_data,
    moeda_destino="BRL",
    taxa_cambio=1.0
)

print(f"\nOrçamento total: R$ {orcamento_total:,.2f}")


# IGNORANDO RH E LOGÍSTICA
print("\n--- ORÇAMENTO FILTRADO ---")

orcamento_filtrado = calcular_orcamento(
    empresa_data,
    "RH",
    "Logistica",
    moeda_destino="USD",
    taxa_cambio=0.20
)

print(f"\nOrçamento convertido: US$ {orcamento_filtrado:,.2f}")
