# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

print('CLASSIFICAÇÃO DAS MÚSICAS: ROCK E POP')
print("********************************************************************************")
print("* NOTAS DO ROCK = ",sorted(notas_rock))
print("********************************************************************************")
print("Ruim:",notas_rock.count(0) + notas_rock.count(1))
print("Mediana:",notas_rock.count(2) + notas_rock.count(3))
print("Boa:",notas_rock.count(4) + notas_rock.count(5))

print("*******************************************************************************")
print("* NOTAS DO POP = ",sorted(notas_pop))
print("*******************************************************************************")
print("Ruim:",notas_pop.count(0) + notas_pop.count(1))
print("Mediana:",notas_pop.count(2) + notas_pop.count(3))
print("Boa:",notas_pop.count(4) + notas_pop.count(5))

print("Exixtem",notas_rock.count(2) + notas_rock.count(3),"avaliações para músicas medianas de Rock!")
print("De",notas_pop.count(0) + notas_pop.count(1) + notas_pop.count(2) + notas_pop.count(3) + notas_pop.count(4) + notas_pop.count(5),"avaliações feitas das músicas de pop,",notas_pop.count(4) + notas_pop.count(5),"são boas!")

