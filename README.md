# Ultra Prime

Um script em python que recebe um número e mostra todos os números primos antecessores a ele.

O script trabalha com duas maneiras de resolver o problema, uma maneira lenta baseada no `Teorema de Wilson`
e outra muito mais rápida baseada no `The Sieve of Eratosthenes`.


## Comparativo de tempo

Utilizando o [código](https://github.com/axelriosg/ultraprime/blob/main/provatempo.py) com o comando:

```
time python provatempo.py
```

### Encontrando números primos até 1000:

Teorema de Wilson:

```
991
997
Teorema de Wilson

real	0m0,109s
user	0m0,109s
sys 	0m0,000s
```

The Sieve of Eratosthenes:

```
991
997
The Sieve of Eratosthenes

real	0m0,033s
user	0m0,023s
sys     0m0,010s
```

### Encontrando números primos até 10000:

Teorema de Wilson:

```
9967
9973
Teorema de Wilson

real	1m10,737s
user	1m10,634s
sys     0m0,017s
```

The Sieve of Eratosthenes:

```
9967
9973
The Sieve of Eratosthenes

real	0m0,042s
user	0m0,035s
sys     0m0,007s
```
