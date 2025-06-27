from typing import List  
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
        return self.encontrar_mediana_otimizada(nums1, nums2)  
    def encontrar_mediana_otimizada(self, lista1: List[int], lista2: List[int]) -> float:
        if len(lista1) > len(lista2): lista1, lista2 = lista2, lista1  # Garante que lista1 seja a menor
        tam1, tam2 = len(lista1), len(lista2)  # Tamanhos das listas
        total = tam1 + tam2  # Total de elementos
        meio = (total + 1) // 2  
        inicio, final = 0, tam1  # Limites para busca binária
        def valor_seguro(lista: List[int], idx: int) -> float:
            if idx < 0: return float('-inf') 
            if idx >= len(lista): return float('inf')  
            return lista[idx]  # Valor válido dentro dos índices
        def particao_valida(esq1, dir1, esq2, dir2) -> bool:
            return esq1 <= dir2 and esq2 <= dir1  # Verifica se partição está correta
        def calcular_mediana(esq1, dir1, esq2, dir2) -> float:
            max_esq = max(esq1, esq2)  # Maior da esquerda
            min_dir = min(dir1, dir2)  # Menor da direita
            if total % 2 == 1: return float(max_esq)  # Se total ímpar, retorna maior da esquerda
            return (max_esq + min_dir) / 2.0  # Se total par, retorna média dos centrais
        for _ in range(tam1 + 1):  
            if inicio > final: break  
            corte1 = (inicio + final) // 2  # Corte na primeira lista
            corte2 = meio - corte1  # Complemento na segunda lista
            esquerdo1 = valor_seguro(lista1, corte1 - 1)  # Valor à esquerda do corte1
            direito1 = valor_seguro(lista1, corte1)  # Valor à direita do corte1
            esquerdo2 = valor_seguro(lista2, corte2 - 1)  # Valor à esquerda do corte2
            direito2 = valor_seguro(lista2, corte2)  # Valor à direita do corte2
            if particao_valida(esquerdo1, direito1, esquerdo2, direito2):
                return calcular_mediana(esquerdo1, direito1, esquerdo2, direito2)
            elif esquerdo1 > direito2: final = corte1 - 1  # Move para esquerda se corte1 muito grande
            else: inicio = corte1 + 1  # Move para direita se corte1 muito pequeno
        return 0.0 
