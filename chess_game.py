tablero = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

tablero_llaves = []

print("\nDISPOSICIÓN DEL TABLERO:")
print("(Escribe un número para seleccionar el espacio)\n")

print('7' + '|' + '8' + '|' + '9')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('1' + '|' + '2' + '|' + '3')

print("\n_______________\n")

for key in tablero:
    tablero_llaves.append(key)

def imprime_tablero(tablero):
    print(tablero['7'] + '|' + tablero['8'] + '|' + tablero['9'])
    print('-+-+-')
    print(tablero['4'] + '|' + tablero['5'] + '|' + tablero['6'])
    print('-+-+-')
    print(tablero['1'] + '|' + tablero['2'] + '|' + tablero['3'])

def main():

    turno = 'X'
    contador = 0

    for i in range(10):
        imprime_tablero(tablero)
        print("Es tu turno, " + turno + ".  Elige un lugar:  ")

        jugada = input()        

        if tablero[jugada] == ' ':
            tablero[jugada] = turno
            contador += 1
        else:
            print("Ese lugar ya esta ocupado. \n Elige un lugar: ")
            continue

        if contador >= 5:
            # Caso en linea horizontal
            if tablero['7'] == tablero['8'] == tablero['9'] != ' ': 
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")                
                break
            elif tablero['4'] == tablero['5'] == tablero['6'] != ' ':
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break
            elif tablero['1'] == tablero['2'] == tablero['3'] != ' ': 
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break
            elif tablero['1'] == tablero['4'] == tablero['7'] != ' ':
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break
            elif tablero['2'] == tablero['5'] == tablero['8'] != ' ': 
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break
            elif tablero['3'] == tablero['6'] == tablero['9'] != ' ':
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break 

            # En diagonal

            elif tablero['7'] == tablero['5'] == tablero['3'] != ' ':
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break
            elif tablero['1'] == tablero['5'] == tablero['9'] != ' ': 
                imprime_tablero(tablero)
                print("\nFin del juego.\n")                
                print(" **** " +turno + " ganó. ****")
                break 

        # En caso de empate
        if contador == 9:
            print("\nFin del juego!!.\n")                
            print("Es un emptate!!")

        # Se cambia el nombre del jugador
        if turno =='X':
            turno = 'O'
        else:
            turno = 'X'        
    
    # Para reestablecer el juego
    restart = input("Jugar otra vez?(s/n)")
    if restart == "s" or restart == "S":  
        for key in tablero_llaves:
            tablero[key] = " "

        main()

if __name__ == "__main__":
    main()