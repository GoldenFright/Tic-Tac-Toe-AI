import random
import time


def board(a):
    print(a[0], "|", a[1], "|", a[2])
    print("--|---|--")
    print(a[3], "|", a[4], "|", a[5])
    print("--|---|--")
    print(a[6], "|", a[7], "|", a[8])


ans = 0
turn = "X"
win = ""
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wp = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [6, 7, 8], [3, 4, 5], [0, 1, 2], [2, 4, 6], [0, 4, 8]]
while win != 1 or win != 0:
    best = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    play = []
    board(pos)
    im = int(input("Play your turn on the numbers : "))
    if im < 10 and (pos[im - 1]) != "X" and (pos[im - 1]) != "O":
        pos[im - 1] = "X"

        # win check
        for i in range(0, len(wp)):
            if pos[wp[i][0]] == "X" and pos[wp[i][1]] == "X" and pos[wp[i][2]] == "X":
                board(pos)
                win = 1
            elif pos[wp[i][0]] == "O" and pos[wp[i][1]] == "O" and pos[wp[i][2]] == "O":
                board(pos)
                win = 0
            else:
                pass
        ans = 0
        if 1 not in pos and 2 not in pos and 3 not in pos and 4 not in pos and 5 not in pos and 6 not in pos and \
                7 not in pos and 8 not in pos and 9 not in pos:
            win = -1
        if win == 1:
            print("X won!")
            time.sleep(1)
            break
        elif win == 0:
            print("O won!")
            time.sleep(1)
            break
        elif win == -1:
            print("TIE!")
            time.sleep(1)
            break
        else:
            pass
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    else:
        print("Wrong position entered!")
    # AI
    fix = 0
    if turn == "O":
        for i in range(9):
            try:
                int(pos[i])
            except ValueError:
                pass
            else:
                play.append(pos[i])
        for i in range(len(play)):
            for test in range(0, len(wp)):
                if pos[wp[test][0]] == "X" and pos[wp[test][1]] == "X":
                    best[wp[test][2] - 0] = 3
                elif pos[wp[test][1]] == "X" and pos[wp[test][2]] == "X":
                    best[wp[test][0] - 0] = 3
                elif pos[wp[test][0]] == "X" and pos[wp[test][2]] == "X":
                    best[wp[test][1] - 0] = 3

            for test in range(0, len(wp)):
                if pos[wp[test][0]] == "O" and pos[wp[test][1]] == "O":
                    best[wp[test][2]] = 4
                elif pos[wp[test][1]] == "O" and pos[wp[test][2]] == "O":
                    best[wp[test][0]] = 4
                elif pos[wp[test][0]] == "O" and pos[wp[test][2]] == "O":
                    best[wp[test][1]] = 4
        if "O" not in pos:
            afri = 0
            while afri < 1:
                guess = random.randint(0, 8)
                if pos[guess] == "X":
                    pass
                else:
                    best[guess] = 1
                    afri += 1
        for i in range(9):
            if i + 1 in play:
                pass
            else:
                best[i] = 0
        maxi = 0
        for i in range(9):
            if best[maxi] < best[i]:
                maxi = i
        pos[maxi] = "O"
        turn = "X"

        # win check
        for i in range(0, len(wp)):
            if pos[wp[i][0]] == "X" and pos[wp[i][1]] == "X" and pos[wp[i][2]] == "X":
                board(pos)
                win = 1
            elif pos[wp[i][0]] == "O" and pos[wp[i][1]] == "O" and pos[wp[i][2]] == "O":
                board(pos)
                win = 0
            else:
                pass
        ans = 0
        if 1 not in pos and 2 not in pos and 3 not in pos and 4 not in pos and 5 not in pos and 6 not in pos and \
                7 not in pos and 8 not in pos and 9 not in pos:
            win = -1
        if win == 1:
            print("X won!")
            time.sleep(1)
            break
        elif win == 0:
            print("O won!")
            time.sleep(1)
            break
        elif win == -1:
            print("TIE!")
            time.sleep(1)
            break
        else:
            pass
