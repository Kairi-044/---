import os

from win import check_win

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    while True:
        print("="*40)
        print("КРЕСТИКИ-НОЛИКИ")
        print("="*40)
        print("1. ИГРАТЬ ")
        print("2. ВЫЙТИ")
        choice =input("Введите номер: ").strip()
         
        if choice == '1':
                turns_counter = 1
                x_turns=[]
                o_turns=[]

                is_finished = False   
                desk=["_","_","_","_","_","_","_","_","_"]
                while not is_finished:
                    clear_screen()
                    
                    x_win = check_win(x_turns)
                    o_win = check_win(o_turns)
                    is_finished = x_win or o_win
                    
                    print(desk[0],desk[1],desk[2])
                    print(desk[3],desk[4],desk[5])
                    print(desk[6],desk[7],desk[8])

                    if turns_counter %2==1:
                        turn=int(input("Введите клетку: "))
                        desk[turn-1]="X"
                        x_turns.append(turn)
                    else:
                        turn=int(input("Введите клетку: "))
                        desk[turn-1]="0"
                        o_turns.append(turn)
                    turns_counter+=1






















        elif choice == '2':
            clear_screen()
            print("Выход из программы")
            break
        else:
            print("Неверный выбор,введите 1 или 2")
            







if __name__ == "__main__":
    main()