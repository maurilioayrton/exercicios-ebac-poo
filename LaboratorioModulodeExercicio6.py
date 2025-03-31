import sys
sys.path.insert(0, '/data')
from arquivo_texto import ArquivoTexto

class ArquivoCSV(ArquivoTexto):

    def __init__(self, arquivo: str):
        super().__init__(arquivo=arquivo)  # Herda os atributos de ArquivoTexto
        self.colunas = self.extrair_nome_colunas()  # Define as colunas ao inicializar

    def extrair_nome_colunas(self):
        if not self.conteudo:  # Se o arquivo estiver vazio, retorna lista vazia
            return []
        primeira_linha = self.conteudo[0].strip()  # Remove espaços e quebras de linha
        return primeira_linha.split(',')  # Divide a linha por vírgulas (formato CSV)

    def extrair_coluna(self, indice_coluna: int):
        if indice_coluna < 1 or indice_coluna > len(self.colunas):  # Verifica índice válido
            return None
        
        coluna = []
        for linha in self.conteudo[1:]:  # Pula a primeira linha (cabeçalho)
            valores = linha.strip().split(',')  # Divide os valores por vírgula
            if len(valores) >= indice_coluna:  # Verifica se a coluna existe na linha
                coluna.append(valores[indice_coluna - 1])  # Ajusta índice para 0-based
        return coluna
