from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.contagem = 0  # Armazena total de pares reversos
        self._ordenar_contando(nums, 0, len(nums) - 1)  # Inicia processo de ordenação com contagem
        return self.contagem  # Retorna resultado final
    def _ordenar_contando(self, numeros: List[int], ini: int, fim: int) -> None:
        if ini >= fim: return  # Caso base: subvetor com 1 elemento
        meio = (ini + fim) // 2  # Calcula meio
        self._ordenar_contando(numeros, ini, meio)  # Divide esquerda
        self._ordenar_contando(numeros, meio + 1, fim)  # Divide direita
        self._contar_e_intercalar(numeros, ini, meio, fim)  # Conquista e combina
    def _contar_e_intercalar(self, numeros: List[int], ini: int, meio: int, fim: int) -> None:
        esquerda = numeros[ini:meio + 1]  # Cópia da parte esquerda
        direita = numeros[meio + 1:fim + 1]  # Cópia da parte direita
        j = 0  # Ponteiro da direita
        for i in range(len(esquerda)):  # Para cada valor da esquerda
            for k in range(j, len(direita)):  # Avança até quebrar condição
                if esquerda[i] <= 2 * direita[k]: break
                j += 1  # Atualiza j apenas se condição válida
            self.contagem += j  # Soma os pares válidos para este i
        i = j = k = 0  # Ponteiros para merge
        resultado = []  # Vetor final
        for _ in range(len(esquerda) + len(direita)):  # Merge usando for
            if i < len(esquerda) and (j >= len(direita) or esquerda[i] <= direita[j]): resultado.append(esquerda[i]); i += 1  # Copia da esquerda
            elif j < len(direita): resultado.append(direita[j]); j += 1  # Copia da direita
        for x in range(len(resultado)): numeros[ini + x] = resultado[x]  # Substitui no original
