import cv2, mediapipe as mp
class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()
