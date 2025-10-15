from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        output = emotion_detector("I am glad this happened")
        self.assertEqual(output["dominant_emotion"],"joy")

        output = emotion_detector("I am really mad about this")
        self.assertEqual(output["dominant_emotion"],"anger")

        output = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(output["dominant_emotion"],"disgust")

        output = emotion_detector("I am so sad about this")
        self.assertEqual(output["dominant_emotion"],"sadness")

        output = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(output["dominant_emotion"],"fear")


if __name__ == "__main__":
    unittest.main()