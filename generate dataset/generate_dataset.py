
import cv2
import os
import numpy as np

transformed_chessboard_path = "data\\train_chessboards_transformed"
dest_path = "data\\balanced_chess_pieces\\train"


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


# Initialize the chess board with black pieces on top
chess_board = [
    [5, 2, 0, 4, 1, 0, 2, 5],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [10, 10, 10, 10, 10, 10, 10, 10],
    [12, 9, 7, 11, 8, 7, 9, 12]
]


for filename in os.listdir(transformed_chessboard_path):
    
    img = cv2.imread(os.path.join(transformed_chessboard_path, filename))
    
    

    height, width = img.shape[:2]

    rect_width = int(width / 8)
    rect_height = int(height / 8)

    for i in range(8):
        for j in range(8):
            x = j * rect_width
            y = i * rect_height
            window = 0.1
            y_begin = max(0, int(y-window*rect_height))
            y_end = min(int(y+(1+window)*rect_height), height)
            x_begin = max(0, int(x-window*rect_width))
            x_end = min(int(x+(1+window)*rect_width), width)
            crop_img = img[y_begin:y_end, x_begin:x_end]
            piece = number_to_piece[chess_board[i][j]]
            piece_folder_path = os.path.join(dest_path, piece)
            if not os.path.exists(piece_folder_path):
                os.makedirs(piece_folder_path)
            cv2.imwrite(os.path.join(piece_folder_path,
                        f"{filename[:-4]}_{i}_{j}.jpg"), crop_img)
