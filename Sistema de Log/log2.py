import logging
    
logging.basicConfig(
    filename='programa2.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def log_usuario_ativo(usuario):
    logging.info(f'Usuário {usuario} está ativo.')

def log_operacao_realizada(operacao):
    logging.info(f'Operação realizada: {operacao}')

def log_erro(erro):
    logging.error(f'Ocorreu um erro: {erro}')

def log_aviso(aviso):
    logging.warning(f'Aviso: {aviso}')

if __name__ == '__main__':
    log_usuario_ativo('João')
    log_operacao_realizada('Cadastro de produto')
    log_aviso('Espaço em disco baixo')
    log_erro('Falha ao conectar ao banco de dados')
    print("Logs registrados em 'meu_log.log'")