import numpy as np
import random

pCrossover =0.75
pMutación = 0.05
poblacion=10
ciclos=100
cantGenes=30
cromosomas=[]
cromosomasValor=[]
cromosomasFuncObj=[]
cromosomasFitness=[]
nueva_generacion=[]
maxFuncObj=0
elitismo=True
cantCromosomasElite=2

def aplicarElitismo():
  global cromosomas, cromosomasFitness
  cromosomasElite=[]
  for i in range(cantCromosomasElite):
    #seleccionar cromosoma con mayor fitness
    indice_maximo =cromosomasFitness.index(max(cromosomasFitness))
    #cromosoma=cromosomas.pop(indice_maximo)
    cromosomasElite.append(cromosomas[indice_maximo])
  return(cromosomasElite)


def seleccionParejas():
    parejas = []  # Lista que almacenará las dos parejas
    for i in range(2):
        numero_aleatorio = random.uniform(0, 1)
        probabilidad_acumulada = 0
        for j, probabilidad in enumerate(cromosomasFitness):
            probabilidad_acumulada += probabilidad
            if probabilidad_acumulada >= numero_aleatorio:
                parejas.append(j)  # Agregamos el elemento seleccionado a la lista de parejas
                break
    return parejas  # Retornamos la lista con las dos parejas seleccionadas




def funcFitness(valorFuncObj):
  return valorFuncObj/sum(cromosomasFuncObj)


def funcObjetivo(x):
  return (x/((2**30)-1))

def iniciarCromosomas():
  global maxFuncObj
  for i in range(0,poblacion):
    genes = np.random.rand(cantGenes) < 0.5 #genera una lista con true o false
    #Genera la cadena de genes binario
    genes_binario=""
    for g in genes:
      genes_binario+=str(int(g))
    #Agrega los genes a la lista de cromosomas, el valor entero y valor de la funcion objetivo
    cromosomas.append(genes_binario)
    cromosomasValor.append(int(genes_binario, 2))
    cromosomasFuncObj.append(funcObjetivo(cromosomasValor[i]))
  #Agrega los cromosomas a la lista de cromosomas fitness
  for x in cromosomasFuncObj:
    cromosomasFitness.append(funcFitness(x))
  maxFuncObj=max(cromosomasFuncObj)
    
def nuevaGenracion(cromo1, cromo2):
    cromosoma1=cromosomas[cromo1]
    cromosoma2=cromosomas[cromo2]
    #crossover
    if((random.uniform(0,1)) < pCrossover):
        rango = random.randrange(cantGenes) #punto de corte de los genes
        aux1 = cromosoma1[:rango] + cromosoma2[rango:]
        aux2 = cromosoma2[:rango] + cromosoma1[rango:]  
        cromosoma1 = aux1
        cromosoma2 = aux2
    #mutacion
    for i in range(cantGenes):
        if random.uniform(0, 1) < pMutación:
            cromosoma1 = cromosoma1[:i] + str(int(not int(cromosoma1[i]))) + cromosoma1[i+1:]
        if random.uniform(0, 1) < pMutación:
            cromosoma2 = cromosoma2[:i] + str(int(not int(cromosoma2[i]))) + cromosoma2[i+1:]
    return cromosoma1, cromosoma2


def calcularValores(nueva_generacion):
  global cromosomasFitness, maxFuncObj
  i=0
  cromosomasFitness=[]
  for genes in nueva_generacion:
    cromosomasValor.append(int(genes, 2))
    cromosomasFuncObj.append(funcObjetivo(cromosomasValor[i]))
    i+=1
  for x in cromosomasFuncObj:
    cromosomasFitness.append(funcFitness(x))
  maxFuncObj=max(cromosomasFuncObj)



def iniciar():
  global cromosomas, cromosomasValor, cromosomasFuncObj
  #iniciar primera generacion
  iniciarCromosomas()
  #generar nuevas generaciones
  nueva_generacion=cromosomas.copy()
  for i in range(ciclos):
    cromosomas=nueva_generacion
    print(f'GENERACION {i+1}')
    print(f'Cromosomas, {cromosomas}')
    print(f'maximo cromosomas: {max(cromosomas)} ')
    print(f'valores, {cromosomasValor}')
    print(f'Funcion objetivo, {cromosomasFuncObj}')
    print(f'Funcion Fitness, {cromosomasFitness}')
    print(f'Maximo funcObj, {maxFuncObj}')
    nueva_generacion=[]
    cromosomasValor=[]
    cromosomasFuncObj=[]
    if (elitismo):
      cromosomasElite= aplicarElitismo();
      nueva_generacion.append(cromosomasElite[0])
      nueva_generacion.append(cromosomasElite[1])
      for i in range(int((poblacion-cantCromosomasElite)/2)):
        #Seleccion de parejas  
        parejas=seleccionParejas()
        #Generar nueva generacion
        result= nuevaGenracion(parejas[0], parejas[1])
        nueva_generacion.append(result[0])
        nueva_generacion.append(result[1])
      calcularValores(nueva_generacion)
    else:
      for i in range(int(poblacion/2)):
        #Seleccion de parejas  
        parejas=seleccionParejas()
        #Generar nueva generacion
        result= nuevaGenracion(parejas[0], parejas[1])
        nueva_generacion.append(result[0])
        nueva_generacion.append(result[1])
      calcularValores(nueva_generacion)
      




iniciar()