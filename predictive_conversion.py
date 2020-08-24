word_data_path = "./data/new_vocabulary.csv"


def get_word_data(data_path, option=0):
    with open(data_path, "r") as f:
        return {word.split(",")[0]: word.split(",")[1].strip("\n") for word in f.readlines()}


class PredictiveConversion:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.target = ""

    def input_word(self, word):
        self.target = word
        if word in self.vocabulary:
            self.vocabulary[word] += 1
        else:
            self.registration(word)

    def predict(self):
        result = []
        for word in self.vocabulary:
            flag = 0
            if len(word) >= len(self.target):
                for i in range(len(self.target)):
                    if word[i] != self.target[i]:
                        flag = 1
                if flag != 1:
                    result.append(word)
        return result

    def registration(self, word):
        new_word = {word: 1}
        self.vocabulary.update(new_word)

    def deletion(self, word):
        try:
            self.vocabulary.pop(word)
            print("Delete word : ", word)
        except ValueError:
            print("There is not ", word)
        except KeyError:
            print("There is not ", word)

    def save_vocabulary(self):
        with open("./data/new_vocabulary.csv", "w") as f:
            for key in self.vocabulary:
                value = self.vocabulary[key]
                text = key + ", " + str(value) + "\n"
                f.write(text)


#vocabulary_data = get_word_data(word_data_path)
#typing = PredictiveConversion(data)
#typing.save_vocabulary()