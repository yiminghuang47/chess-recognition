
import cv2
import os
import numpy as np

raw_chessboard_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\raw_chessboards"
transformed_chessboard_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\raw_chessboards_transformed"
# dest_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\generated_pieces"
dest_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\chess_pieces\\train"


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


board_to_corner_coordinates = {
    "chess_board_1.jpg": [[0,0],[1755,23],[1792,1792],[0,1792]],
    "chess_board_2.jpg": [[16,31],[1780,27],[1754,1753],[18,1772]],
    "chess_board_3.jpg": [[36,45],[1769,40],[1783,1790],[31,1783]],
    #"chess_board_4.jpg": [[,],[,],[,],[,]],


}

for filename in os.listdir(raw_chessboard_path):
    img = cv2.imread(os.path.join(raw_chessboard_path, filename))
    img = cv2.resize(img,(1792,1792)) # 224*8
    cv2.imwrite(os.path.join(transformed_chessboard_path,filename),img)

def warp(img,coordinates):
    coordinates = np.array(coordinates)
    dest_img = np.zeros((1792,1792,3))
    dest_coordinates = np.array([[0, 0],[1792, 0],[1792, 1792],[0, 1792]])
    
    h, status = cv2.findHomography(coordinates, dest_coordinates)

    warped_img = cv2.warpPerspective(img, h, (dest_img.shape[1],dest_img.shape[0]))
    return warped_img


for filename in os.listdir(transformed_chessboard_path):
    img = cv2.imread(os.path.join(transformed_chessboard_path,filename))
    if filename not in board_to_corner_coordinates:
        continue
    coordinates = np.array(board_to_corner_coordinates[filename])
   

    warped_img = warp(img,coordinates)
    #cv2.imshow("Source Image", img)
    #cv2.imshow("Destination Image", dest_img)
    #cv2.imshow("Warped Source Image", warped_img)
 
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    cv2.imwrite(os.path.join(transformed_chessboard_path,filename),warped_img)


for filename in os.listdir(transformed_chessboard_path):
    
    img = cv2.imread(os.path.join(transformed_chessboard_path, filename))
    
    
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('img',gray)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #convert to square
    #ret, corners = cv2.findChessboardCorners(gray,(4,3), cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
     
    #print(ret)
    #if corners is None:
    #    continue
    #print(corners)
    #continue
    #corners = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1))
    #dst = np.array([[0, 0], [500, 0], [500, 500], [0, 500]], dtype=np.float32)
    #M, _ = cv2.findHomography(corners, dst)
    #img = cv2.warpPerspective(img, M, (500, 500))
    #cv2.imshow('Result', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #continue

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
