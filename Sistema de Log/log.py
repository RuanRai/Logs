import logging

logging.basicConfig(level=logging.INFO, filename="programa.log", format="%(asctime)s - %(levelname)s - %(message)s")

def resultado_operacional(faturamento, custo):
    return faturamento - custo

def lucro_liquido(faturamento, custo, percentual_imposto):
    if percentual_imposto == 0:
        logging.warning("Percentual de imposto é igual a 0")
    return (faturamento - custo) * (1 - percentual_imposto)

def lucro_por_acoes(faturamento, custo, percentual_imposto, acoes):
    return lucro_liquido(faturamento, custo, percentual_imposto) / acoes

faturamento = 1000
custo = 400
percentual_imposto = 0.3
acoes = 100

resultado = resultado_operacional(faturamento, custo)
logging.info(f"Resultado: {resultado}")

lucro = lucro_liquido(faturamento, custo, percentual_imposto)
logging.info(f"Lucro: {lucro}")

lucro_acao = lucro_por_acoes(faturamento, custo, percentual_imposto, acoes) 
logging.info(f"Lucro por ação: {lucro_acao}")
