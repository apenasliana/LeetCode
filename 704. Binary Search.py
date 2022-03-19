import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def BuscaBinaria(minimo, maximo, Lista, numProcurado):


            meio = (int(minimo)+int(maximo))/2 #+1?
            #print('meio antes: ',meio)
            meio = math.floor(meio)
            #print('meio arredondad:' ,meio)
            if Lista[int(meio)] == numProcurado:
                return meio
            if minimo > maximo:
                return -1

            else:
                if numProcurado < Lista[int(meio)] :
                    #print('menor||meio:',meio , '||minimo:', minimo, 'maximo: ', maximo  )
                    maximo = meio-1
                    return BuscaBinaria(minimo, maximo, Lista, numProcurado)

                else:
                    #print('maior||meio: ',meio, '||minimo:',minimo, 'maximo: ', maximo  )
                    minimo= meio+1
                    #print(minimo)
                    return BuscaBinaria(minimo, maximo, Lista, numProcurado)
        return BuscaBinaria(0, len(nums)-1, nums, target)      