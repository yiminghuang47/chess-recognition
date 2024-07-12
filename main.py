import cv2
import os
import torch
import numpy as np
from torchvision import transforms


folder_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\test_chessboards"
# dest_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\generated_pieces"
dest_path = "C:\\Users\\yimin\\OneDrive\\Documents\\Coding Projects\\Chess Recognition\\chess_pieces\\train"


number_to_piece = {
    1: "black_bishop",
    2: "black_king",
    3: "black_knight",
    4: "black_pawn",
    5: "black_queen",
    6: "black_rook",
    7: "empty",
    8: "white_bishop",
    9: "white_king",
    10: "white_knight",
    11: "white_pawn",
    12: "white_queen",
    13: "white_rook",
}

# Initialize the chess board with black pieces on top
chess_board = [
    [6, 3, 1, 5, 2, 1, 3, 6],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [11, 11, 11, 11, 11, 11, 11, 11],
    [13, 10, 8, 12, 9, 8, 10, 13]
]

test_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

model = torch.jit.load('model_scripted.pt')
model.eval()

filename = "test_1.jpg"

img = cv2.imread(os.path.join(folder_path, filename))
height, width = img.shape[:2]

square_size = int(min(height, width) / 8)
preds = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        x = j * square_size
        y = i * square_size
        crop_img = img[y:y + square_size, x:x + square_size]
        
        crop_img = torch.from_numpy(crop_img)
        crop_img = test_transform(crop_img)
        print(crop_img.shape)
        with torch.no_grad():
          pred = model(crop_img).argmax(1).item()
          preds[i,j] = pred
