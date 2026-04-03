import math
import re

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

class SearchEngine:
    def __init__(self, notes):
        self.notes = notes
        self.documents = []
        self.vocab = set()
        self.tf = []
        self.idf = {}

        self.prepare()

    def prepare(self):
        for note in self.notes:
            words = tokenize(note.title + " " + note.content)
            self.documents.append(words)
            self.vocab.update(words)

        self.compute_tf()
        self.compute_idf()

    def compute_tf(self):
        for doc in self.documents:
            tf_dict = {}
            for word in doc:
                tf_dict[word] = tf_dict.get(word, 0) + 1
            for word in tf_dict:
                tf_dict[word] /= len(doc)
            self.tf.append(tf_dict)

    def compute_idf(self):
        total_docs = len(self.documents)
        for word in self.vocab:
            count = sum(1 for doc in self.documents if word in doc)
            self.idf[word] = math.log(total_docs / (1 + count))

    def search(self, query):
        query_words = tokenize(query)
        scores = []

        for i, doc in enumerate(self.documents):
            score = 0
            for word in query_words:
                if word in self.tf[i]:
                    score += self.tf[i][word] * self.idf.get(word, 0)
            scores.append((i, score))

        ranked = sorted(scores, key=lambda x: x[1], reverse=True)

        results = []
        for idx, score in ranked:
            if score > 0:
                results.append({
                    "title": self.notes[idx].title,
                    "content": self.notes[idx].content,
                    "score": score
                })

        return results