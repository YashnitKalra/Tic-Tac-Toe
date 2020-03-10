def checkWinning(mat,win,player):
    for i in range(3):
        if mat[i][0]==mat[i][1]==mat[i][2]!="_":      # vertical
            win[player]=True
            return
        if mat[0][i]==mat[1][i]==mat[2][i]!="_":      # horizontal
            win[player]=True
            return
    if mat[0][0]==mat[1][1]==mat[2][2]!="_":          # diagonal_1
        win[player]=True
        return
    if mat[0][2]==mat[1][1]==mat[2][0]!="_":          # diagonal_2
        win[player]=True
        return

if __name__=="__main__":
    players=[input("Enter Name of Player 1 (X): "),input("Enter Name of Player 2 (0): ")]
    marked=0
    turn=0
    print("\nGRID:\n1 2 3\n4 5 6\n7 8 9")
    positions={
        '1':[0,0], '2':[0,1], '3':[0,2],
        '4':[1,0], '5':[1,1], '6':[1,2],
        '7':[2,0], '8':[2,1], '9':[2,2],
    }
    matrix=[["_"]*3 for _ in range(3)]
    win=[False,False]
    while marked<9 and not (win[0] or win[1]):
        print("\n{}'s Turn".format(players[turn]))
        for mat in matrix:
            print(*mat)
        pos=input("Enter Position: ")
        try:
            r,c=positions[pos]
            if matrix[r][c]=='_':
                matrix[r][c]='X' if turn==0 else '0'
                checkWinning(matrix,win,turn)
                turn=1-turn
                marked+=1
            else:
                print("Already Occupied")
        except:
            print("Invalid Position")
    for mat in matrix:
        print(*mat)
    if win[0]:
        print("\n{} WINS".format(players[0]))
    elif win[1]:
        print("\n{} WINS".format(players[1]))
    else:
        print("\nDRAW")