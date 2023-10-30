from clients.emotion_detector import EmotionDetector
from concurrent import futures

from src.types.emotion import Emotion


executor = futures.ThreadPoolExecutor(max_workers=2)

emotion_detector = EmotionDetector()

def callback(emotion: Emotion):
    print(f'Emotion detected: {emotion.name}')

#executor.submit(emotion_detector.start_detection, 5, callback)
emotion_detector.start_detection(1, callback)
