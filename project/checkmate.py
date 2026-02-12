def checkmate(board):
    # ถ้าไม่มีตาราง
    if not board:
        print("Fail")
        return
    # เอากระดานมาใส่เป็น list
    rows = board.splitlines()
    size = len(rows)

    # ถ้าไม่จัตุรัส
    for row in rows:
        if len(row) != size:
            print("Fail")
            return

    # หา King
    king = None
    for i in range(size):
        for j in range(size):
            if rows[i][j] == 'K':
                king = (i, j)
                break
        if king:
            break
    
    #ไม่เจอ king
    if not king:
        print("Fail2")
        return
    # กำหนดตำแหน่ง king
    ki, kj = king

    # เช็คแนวตรง
    straight = [(-1,0), (1,0), (0,-1), (0,1)]

    for di, dj in straight:
        i = ki + di
        j = kj + dj
        while 0 <= i < size and 0 <= j < size:
            piece = rows[i][j]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break
            i += di
            j += dj
    
    #เช็คแนวเฉียง
    diagonal = [(-1,-1), (-1,1), (1,-1), (1,1)]

    for di, dj in diagonal:
        i = ki + di
        j = kj + dj
        while 0 <= i < size and 0 <= j < size:
            piece = rows[i][j]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            i += di
            j += dj

    # เช็ค Pawn  
    for di, dj in [(-1, -1), (-1, 1)]:
        i = ki + di
        j = kj + dj
        if 0 <= i < size and 0 <= j < size:
            if rows[i][j] == 'P':
                print("Success")
                return

    print("Fail3")