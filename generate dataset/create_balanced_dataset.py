
import os


folder_path = "data\\chess_pieces\\train"


number_to_piece = {
    0: "black_bishop",
    1: "black_king",
    2: "black_knight",
    3: "black_pawn",
    4: "black_queen",
    5: "black_rook",
    6: "empty",
    7: "white_bishop",
    8: "white_king",
    9: "white_knight",
    10: "white_pawn",
    11: "white_queen",
    12: "white_rook",
}


# remove pawns

for filename in os.listdir(folder_path):
    if (filename[-4:] != "pawn"):
        continue
    print(filename)
    for img in os.listdir(os.path.join(folder_path, filename)):
        if img[:11] == "chess_board" and (img[-5] != "0" and img[-5] != "1"):
            print(img)
            os.remove(os.path.join(folder_path,filename,img))

# remove empty pawns

for filename in os.listdir(folder_path):
    if (filename != "empty"):
        continue
    print(filename)
    for img in os.listdir(os.path.join(folder_path, filename)):
        if img[:11] == "chess_board" and (img[-7:-4] != "2_0" and img[-7:-4] != "2_1"):
            print(img)
            os.remove(os.path.join(folder_path,filename,img))