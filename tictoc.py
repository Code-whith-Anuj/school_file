bi = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fi():
    print(f" {bi[0]} | {bi[1]} | {bi[2]} ")
    print(f" {bi[3]} | {bi[4]} | {bi[5]} ")
    print(f" {bi[6]} | {bi[7]} | {bi[8]} ")

while True:
    fi()
    
    player1 = int(input("Enter number to change 'O': "))

    if player1 >= 1 and player1 <= 9 and bi[player1 - 1] == player1:
        bi[player1 - 1] = "O"
        fi()
        if (bi[0] == "O" and bi[1] == "O" and bi[2] == "O") or \
           (bi[3] == "O" and bi[4] == "O" and bi[5] == "O") or \
           (bi[6] == "O" and bi[7] == "O" and bi[8] == "O") or \
           (bi[2] == "O" and bi[4] == "O" and bi[6] == "O") or \
           (bi[0] == "O" and bi[4] == "O" and bi[8] == "O") or \
           (bi[2] == "O" and bi[5] == "O" and bi[8] == "O") or \
           (bi[1] == "O" and bi[4] == "O" and bi[7] == "O") or \
           (bi[0] == "O" and bi[3] == "O" and bi[6] == "O") :
            print("'O' wins")
            break
    else:
        print("Invalid move. Try again.")
        continue
    player2 = int(input("Enter number to change 'X': "))
    if player2 >= 1 and player2 <= 9 and bi[player2 - 1] == player2:
        bi[player2 - 1] = "X"
        if (bi[0] == "X" and bi[1] == "X" and bi[2] == "X") or \
           (bi[3] == "X" and bi[4] == "X" and bi[5] == "X") or \
           (bi[6] == "X" and bi[7] == "X" and bi[8] == "X") or \
           (bi[2] == "X" and bi[4] == "X" and bi[6] == "X") or \
           (bi[0] == "X" and bi[4] == "X" and bi[8] == "X") or \
           (bi[2] == "X" and bi[5] == "X" and bi[8] == "X") or \
           (bi[1] == "X" and bi[4] == "X" and bi[7] == "X") or \
           (bi[0] == "X" and bi[3] == "X" and bi[6] == "X") :
            print("'X' wins")
            break
        else:
            continue
    else:
        print("Invalid move. Try again.")
        continue
