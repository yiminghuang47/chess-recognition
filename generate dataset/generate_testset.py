import os
import numpy as np
import cv2

test_path = "data\\test_chessboards"
transformed_path = "data\\test_chessboards_transformed"
board_to_corner_coordinates = {
    "test_1.jpg": [[58,55],[1735,61],[1730,1728],[67,1731]],
    "test_2.jpg": [[438,101],[1273,123],[1286,1649],[385,1647]],
    "test_3.jpg": [[171,151],[1681,215],[1688,1586],[172,1622]],
    "test_4.jpg" : [[479,241],[1318,251],[1328,1359],[478,1352]],
    "test_5.jpg": [[124,109],[1648,112],[1659,1552],[135,1560]],
    "test_6.jpg": [[375,171],[1226,151],[1253,1673],[367,1703]],
    "test_7_bl.jpg": [[562,306],[1228,296],[1237,1479],[568,1478]],
    "test_7_br.jpg": [[521,288],[1203,281],[1206,1489],[529,1494]],
    "test_7_tl.jpg": [[332,300],[1130,323],[1144,1722],[318,1749]],
    "test_7_tr.jpg": [[552,342],[1244,332],[1254,1578],[555,1590]],
}

def warp(img,coordinates):
   
    dest_img = np.zeros((1792,1792,3))
    dest_coordinates = np.array([[0, 0],[1792, 0],[1792, 1792],[0, 1792]])
    coordinates = np.array(coordinates)
    h, status = cv2.findHomography(coordinates, dest_coordinates)

    warped_img = cv2.warpPerspective(img, h, (dest_img.shape[1],dest_img.shape[0]))
    return warped_img


for filename in os.listdir(test_path):
    img = cv2.imread(os.path.join(test_path,filename))
    img = cv2.resize(img,(1792,1792))
    cv2.imwrite(os.path.join(transformed_path,filename),img)

for filename in os.listdir(transformed_path):
    img = cv2.imread(os.path.join(transformed_path,filename))
    if filename not in board_to_corner_coordinates:
        continue
    warped_img = warp(img,board_to_corner_coordinates[filename])
    
    cv2.imwrite(os.path.join(transformed_path,filename),warped_img)


tl = cv2.imread(os.path.join(transformed_path,"test_7_tl.jpg"))
tr = cv2.imread(os.path.join(transformed_path,"test_7_tr.jpg"))
bl = cv2.imread(os.path.join(transformed_path,"test_7_bl.jpg"))
br = cv2.imread(os.path.join(transformed_path,"test_7_br.jpg"))
combined_img = np.concatenate((np.concatenate((tl,tr),axis=1),np.concatenate((bl,br),axis=1)),axis=0)
combined_img = cv2.resize(combined_img,(1792,1792))
cv2.imwrite(os.path.join(transformed_path,"test_7_combined.jpg"),combined_img)