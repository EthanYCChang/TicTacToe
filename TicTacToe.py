arrTTT = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

def display():
    os.system("cls")
    print("\n\tTic Tac Toe\n")
    print("Player 1 (X)  -  Player 2 (O)\n\n")
    print("     |     |")
    print("  " + arrTTT[0] + "  |  " + arrTTT[1] + "  |  " + arrTTT[2])
    print("_____|_____|_____")
    print("     |     |")
    print("  " + arrTTT[3] + "  |  " + arrTTT[4] + "  |  " + arrTTT[5])
    print("_____|_____|_____")
    print("     |     |")
    print("  " + arrTTT[6] + "  |  " + arrTTT[7] + "  |  " + arrTTT[8])
    print("     |     |     \n")

# illegal input at num = 0
def chkOX(idPlayer, symPlayer):
    num = 0
    while (num == 0):
        print("Player " + idPlayer + ", enter a number: ", end="")
        num = int(input())
        if ((num < 1) or (num > 9)):
            num = 0
        else:
            if (arrTTT[num - 1] == "O") or (arrTTT[num - 1] == "X"):
                num = 0
            else:
                arrTTT[num - 1] = symPlayer
                display()
        if (num == 0): print("Invalid move ")

def chkWin(symPlayer):
    chkSequencce = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    chkResult = False
    for i in chkSequencce:
        chkString = ""
        for j in i:
            chkString += arrTTT[j - 1]
        chkResult = (chkString == (symPlayer + symPlayer + symPlayer)) or chkResult
    return chkResult

display()

for i in range(9):
    idPlayer = str(i % 2 + 1)
    symPlayer = "O"
    if idPlayer == "1": symPlayer = "X"
    chkOX(idPlayer, symPlayer)
    if chkWin(symPlayer):
        print("==>Player " + idPlayer + " win ")
        num = input()
        break
