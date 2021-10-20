from multiprocessing import Process
def fibonacci(indice):
    terme0=0
    terme1=1
    listFib=[]
    listFib.append(terme0)
    listFib.append(terme1)
    for i in range (0,indice+1):
        suivant=terme0+terme1
        listFib.append(suivant)
        terme0=terme1
        terme1=suivant
    print("La suite de fibonacci est:")
    print(*listFib)
    return listFib
if __name__ == "__main__":
    p = Process(target=fibonacci, args=(5,))
    p.start()
    p.join()