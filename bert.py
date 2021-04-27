import pandas as pd
from bert_serving.client import BertClient
import numpy as np

base_questions = pd.read_csv('data/faqs.csv')

def getResults(questions, fn):
    def getResult(q):
        answer, score, prediction = fn(q)
        return [q, prediction, answer, score]

    return pd.DataFrame(list(map(getResult, questions)), columns=["Q", "Prediction", "A", "Score"])

def encode_questions(data = base_questions):
    bc = BertClient()
    questions = data["Question"].values.tolist()
    print("Questions count", len(questions))
    print("Start to calculate encoder....")
    questions_encoder = bc.encode(questions)
    np.save("questions", questions_encoder)
    questions_encoder_len = np.sqrt(
        np.sum(questions_encoder * questions_encoder, axis=1)
    )
    np.save("questions_len", questions_encoder_len)
    print("Encoder ready")


class BertAnswer():
    def __init__(self, data=base_questions):
        self.bc = BertClient()
        self.q_data = data["Question"].values.tolist()
        self.a_data = data["Answer"].values.tolist()
        self.questions_encoder = np.load("questions.npy")
        self.questions_encoder_len = np.load("questions_len.npy")

    def get(self, q, minScore = 0.9):
        query_vector = self.bc.encode([q])[0]
        score = np.sum((query_vector * self.questions_encoder), axis=1) / (
            self.questions_encoder_len * (np.sum(query_vector * query_vector) ** 0.5)
        )
        top_id = np.argsort(score)[::-1][0]
        if float(score[top_id]) > minScore:
            return self.a_data[top_id], score[top_id], self.q_data[top_id]
        return "Sorry, I didn't get you.", score[top_id], self.q_data[top_id]

bm = BertAnswer()

def getBertAnswer(q):
    return bm.get(q)
