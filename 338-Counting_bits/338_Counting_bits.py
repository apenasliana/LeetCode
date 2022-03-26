class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def marcela(n):
            lista = [0]*(n+1)
            for i in range(n+1):
                lista[i] = DecimalParaBinario(i)            
            return lista

        def DecimalParaBinario(numero):
            
            
            numerosDeUM = 1
            if numero == 0:
                return 0
            else:
                while numero > 1:
                    numerosDeUM += numero % 2 
                    numero = math.floor(numero /2)
            return numerosDeUM
        
        return marcela(n)
        
        