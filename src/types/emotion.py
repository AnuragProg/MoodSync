'''{
    'emotion': {'angry': 67.43950247764587, 'disgust': 0.019645628344733268, 'fear': 2.957110106945038, 'happy': 0.10799904121086001, 'sad': 19.105184078216553, 'surprise': 0.005862799298483878, 'neutral': 10.364698618650436}, 
    'dominant_emotion': 'angry', 
    'region': {'x': 242, 'y': 273, 'w': 185, 'h': 185}
}'''

from enum import Enum

class Emotion(Enum):
    ANGRY = 'angry'
    DISGUST = 'disgust'
    FEAR = 'fear'
    HAPPY = 'happy'
    SAD = 'sad'
    SURPRISE = 'surprise'
    NEUTRAL = 'neutral'

class EmotionStats:
    def __init__(self, emotion) -> None:
        self.angry = emotion['angry']
        self.disgust = emotion['disgust']
        self.fear = emotion['fear']
        self.happy = emotion['happy']
        self.sad = emotion['sad']
        self.surprise = emotion['surprise']
        self.neutral = emotion['neutral']

class EmotionTracker:

    def __init__(self, obj) -> None:
        if type(obj) != dict:
            raise TypeError('obj must be a dict')

        if 'emotion' not in obj.keys():
            raise KeyError('obj must have emotion key')

        if 'dominant_emotion' not in obj.keys():
            raise KeyError('obj must have dominant_emotion key')

        if 'region' not in obj.keys():
            raise KeyError('obj must have region key')

        self.dominant_emotion : Emotion = obj['dominant_emotion']

        self.region = obj['region']
        
        self.emotionStats = EmotionStats(obj['emotion'])

    def __str__(self) -> str:
        return f'EmotionTracker({self.dominant_emotion}'
