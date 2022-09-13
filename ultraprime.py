#Repositorio do codigo: https://github.com/axelriosg/ultraprime

"""Para a realização deste trabalho o usuário pode escolher dois algoritmos, o primeiro é um algoritmo lento, que foi totalmente criado por nós
usando o Teorema de Wilson que diz que se o resultado de "(n-1)!^2 mod n" é 1, n é primo. Mas após testar nossa primeira abordagem 
ao problema demorou muito para encontrar os números primos, então pesquisamos melhores métodos. Encontramos um método super rápido
usando Numba e Numpy, outros usando teoremas e testes de primalidade mais rapidos, porém finalmente decidimos apenas criar o algoritmo usando 
«The Sieve of Eratosthenes», Github Copilot e nossos cérebros. O primeiro algoritmo foi feito por cérebros humanos com skills 
básicas de Python. O segundo pela fusão matricial de muitos cérebros avançando em Python.

Prezados, disfrutem o «Prime Generator.»

Atenciosamente, Pedro Piloto e Axel Ríos."""

# Importar biblioteca math( utilizada na função prime_len )
import math


print('''  
 ____       _                   ____                           _             
|  _ \ _ __(_)_ __ ___   ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) | '__| | '_ ` _ \ / _ \ | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/| |  | | | | | | |  __/ | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_|   |_|  |_|_| |_| |_|\___|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|        
''')

# Criação da função prime_rap
#função que gera os números primos eliminando os multiplos de 2, 3, 5 e 7. Inspirado no código de geeksforgeeks.org. sobre o Crivo de Eratóstenes. 
def prime_rap(limit):
    # Importa a biblioteca time para calcular o tempo de execução
    import time
    start = time.process_time()
    #using the Sieve of Eratosthenes algorithm for print all the numbers equals or less than the input(limit).
    #Cria uma lista com todos os números de 2 até o limite
    prime = [True for i in range(limit + 1)]
    p = 2
    # Enquanto o quadrado de p for menor ou igual ao limite
    while (p * p <= limit):
        # Se o valor de p for verdadeiro
        if (prime[p] == True):
            # Multiplica o valor de p por 2 até o limite
            for i in range(p * 2, limit + 1, p):
                # Se o valor de i for verdadeiro
                prime[i] = False
        p += 1
    # Imprime todos os números primos
    for p in range(2, limit):
        # Se o valor de p for verdadeiro
        if prime[p]:
            print(p)
    time.sleep (1)
    end = time.process_time()
    finaltime = ((end - start) * 1000)
    print(f"Tempo: {finaltime} ms")
    


# Criação da função prime_len
def prime_len(numer):
    # Importa a biblioteca time para calcular o tempo de execução
    import time
    start = time.process_time()
    #'(n-1)!^2 mod n' equals 1 if n is prime and 0 if it is not. Wilson's theorem.
    for x in range(1, numer):    
        x1 = (x - 1)
        result1 = math.prod(range(x1, 0, -1))
        p = ((result1)**2) % x
        if p == 1:
            print(x)
    time.sleep (1)
    end = time.process_time()
    finaltime = ((end - start)* 1000)
    print(f"Tempo: {finaltime} ms")


# Criação da função main
def main():
    # Cria as variáveis numero e tipo sendo 0 
    numero = 0
    tipo = 0

    # Cria a variável exep_error para o possível erro de digitação do usuário
    exep_error = "Valor deve ser um número inteiro"

    # Solicita um número inteiro que seja maior ou igual a 2, se for 1, 0 ou negativo solicita o número novamente
    while numero <= 1:
        # Se o número for diferente de int ele é solicitado novamente
        try:
            numero = int(input("\nColoque um número maior ou igual a 2\nNúmero: "))
        except:
            print(f"\n\033[31m{exep_error}\033[m")
    
    # Solicita um número inteiro que seja maior ou igual a 1 e menor que 3, se estiver fora do intervalo 1 e 2 o número é solicitado novamente
    while tipo <= 0 or tipo > 2:
        # Se o número for diferente de int ele é solicitado novamente
        try:
            tipo = int(input("\nSelecione o tipo de algoritmo:\n( 1 ) Algoritmo rápido\n( 2 ) Algoritmo lento\n: "))
        except:
            print(f"\n\033[31m{exep_error}\033[m")

    # Se o número for igul a 2 não precisa calcular os primos
    if numero == 2:
        print("2")
    # Se tipo for 1 ira chamar a função prime_rap
    elif tipo == 1:
        prime_rap(numero)
        print(f"\n\033[32mPara:{numero}, usando o algoritmo rapido\033[m")
    # Senão ira chamar a função prime_len
    else:
        prime_len(numero)
        print(f"\n\033[32mPara:{numero},usando o algoritmo lento\033[m")


# Uma boa prática, melhora a organização e o código executa o que foi definido
if __name__ == "__main__":
    main()
