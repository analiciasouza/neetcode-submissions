class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_palavras = {}
        for i in strs:
            valor_ord = sorted(i)
            valor_final = "".join(valor_ord)

            if valor_final in map_palavras:
                map_palavras[valor_final].append(i)

            else:
                map_palavras[valor_final] = [i]

        result = []

        for i in map_palavras.values():
            result.append(i)

        return result