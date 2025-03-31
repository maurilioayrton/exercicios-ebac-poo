class ArquivoTexto(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self.extrair_conteudo()  # Chama o método para extrair o conteúdo ao inicializar
    
    def extrair_conteudo(self):
        # Monta o caminho completo do arquivo
        caminho_arquivo = f"/data/{self.arquivo}"
        conteudo = []
        try:
            with open(file=caminho_arquivo, mode='r', encoding='utf8') as arquivo:
                conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo
        except FileNotFoundError:
            print(f"Arquivo {caminho_arquivo} não encontrado.")
        return conteudo
    
    def extrair_linha(self, numero_linha: int):
        if 1 <= numero_linha <= len(self.conteudo):
            return self.conteudo[numero_linha - 1]  # Ajusta o índice para começar em 1
        else:
            return None  # Retorna None se o número da linha for inválido

# Exemplo de uso
musica = ArquivoTexto('musica.txt')
print(musica.conteudo)  # Imprime o conteúdo do arquivo como uma lista de linhas
