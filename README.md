# Chessboard Recognition with MobileNetV2

This project aims to recognize different chess pieces using a deep learning model based on MobileNetV2. The model is trained and evaluated on a dataset of chess piece images and can generate Forsyth–Edwards Notation (FEN) strings from chessboard images.

## Project Structure

- `Chess Pieces Recognition MobileNetv2.ipynb`: Jupyter Notebook containing data preprocessing, model training, evaluation, and visualization.
- `Chess Recognition Test.ipynb`: Jupyter Notebook for testing the trained model on new images and generating FEN strings for chess board states.
- `generate dataset/generate_dataset.py`: Script to generate a dataset of chess piece images from transformed chessboard images at their starting positions.
- `generate dataset/create_balanced_dataset.py`: Script to balance the dataset by removing excess images of pawns and empty squares.

## Requirements

To run this project, you need to have the following libraries installed:

- `torch`
- `torchvision`
- `numpy`
- `matplotlib`
- `opencv-python`
- `Pillow`
- `fentoimage`

You can install the required packages using pip:

```bash
pip install torch torchvision numpy matplotlib opencv-python Pillow fentoimage
```