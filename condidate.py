class EditDistance:
    def __init__(self):
        self.f_tokens = open("tokens.fa", "r", encoding="utf8")
        self.f_incorrect = open("incorrect.fa", "r", encoding="utf8")
        self.en_tokens = open("tokens.en", "r")
        self.en_incorrect = open("incorrect.en", "r")
        self.INDEX = 500

    def minimum_edit_distance(self, string_1, string_2):
        D = []
        t = []
        for i in range(len(string_2) + 1):
            t.append(0)
        for j in range(len(string_1) + 1):
            D.append(t)

        for i in range(len(string_1) + 1):
            for j in range(len(string_2) + 1):

                if i == 0:
                    D[i][j] = j

                elif j == 0:
                    D[i][j] = i

                elif string_1[i - 1] == string_2[j - 1]:
                    D[i][j] = D[i - 1][j - 1]

                else:
                    D[i][j] = 1 + min(D[i][j - 1],
                                      D[i - 1][j],
                                      D[i - 1][j - 1])

        return D[len(string_1)][len(string_2)]

    def get_con_words(self, word, tokens):
        ED_array = []
        ConWords = []
        for token in tokens:
            ED_array.append(self.minimum_edit_distance(word, token))

        for counter in range(10):
            ConWords.append(tokens[ED_array.index(min(ED_array))])
            ED_array[ED_array.index(min(ED_array))] = self.INDEX

        return ConWords

    def write_to_file(self, language):
        token_array_en = []
        incorrect_array_en = []
        token_array_fa = []
        incorrect_array_fa = []
        for line in self.en_tokens:
            token_array_en.append(line.split('\n')[0])

        for line in self.en_incorrect:
            incorrect_array_en.append(line.split('\n')[0])
        for line in self.f_tokens:
            token_array_fa.append(line.split('\n')[0])

        for line in self.f_incorrect:
            incorrect_array_fa.append(line.split('\n')[0])
        if language == "farsi":
            with open("94463106_Assignment3_Part2_FA.fa", "w+", encoding="utf-8") as F_Output:
                for incorrectWord in incorrect_array_fa:
                    ConWords = self.get_con_words(incorrectWord, token_array_fa)

                    F_Output.write(' {} : '.format(incorrectWord))
                    for conWord in ConWords:
                        F_Output.write(' ، {}'.format(conWord))
                    F_Output.write('\n')
        else:
            with open("94463106_Assignment3_Part1_EN.en", "w+", encoding="utf-8") as E_Output:
                for incorrectWord in incorrect_array_en:
                    ConWords = self.get_con_words(incorrectWord, token_array_en)

                    E_Output.write(' {} : '.format(incorrectWord))
                    for conWord in ConWords:
                        E_Output.write('  {},'.format(conWord))
                    E_Output.write('\n')


if __name__ == "__main__":
    ed_fa = EditDistance()
    ed_fa.write_to_file("farsi")
    ed_en = EditDistance()
    ed_en.write_to_file('english')
