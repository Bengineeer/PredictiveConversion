word_data_path = "./data/500-english-words.csv"


def get_word_data(data_path, option=0):
    with open(data_path, "r") as f:
        if option:
            result = [word.split(";")[0:2] for word in f.readlines()[4:-8]]
        else:
            result = {word.split(";")[1]: 0 for word in f.readlines()[4:-8]}
    return result


class PredictiveConversion:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.target = ""

    def predict(self, target):
        result = []
        for word in self.vocabulary:
            flag = 0
            if len(word) >= len(target):
                for i in range(len(target)):
                    if word[i] != target[i]:
                        flag = 1
                if flag != 1:
                    result.append(word)
        return result

    def add_word(self, word):
        self.vocabulary.append(word)

    def del_word(self, word):
        try:
            self.vocabulary.remove(word)
            print("Delete word : ", word)
        except ValueError:
            print("There is not ", word)

    def recode_count(self, word):
        if word in self.vocabulary:
            pass


data = get_word_data(word_data_path)
first = PredictiveConversion(data)
print(first.predict("th"))
