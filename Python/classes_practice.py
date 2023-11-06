from math import log

class CountVectorizer:
    def __init__(self):
        self.feature_names = []
        self.vocabulary = {}

    def fit_transform(self, corpus: list[str]) -> list[list]:
        """ Transforms the text into a feature matrix """

        if not isinstance(corpus, list):
            raise TypeError('corpus must be a list')

        for row in corpus:
            if not isinstance(row, str):
                raise TypeError(f'corpus must content strings')

        for row in corpus:
            for word in row.split():
                word = word.lower()
                if word not in self.vocabulary:
                    self.vocabulary[word] = len(self.vocabulary)
                    self.feature_names.append(word)

        result = []
        for row in corpus:
            words_counts = [0] * len(self.feature_names)
            for word in row.split():
                word = word.lower()
                words_counts[self.vocabulary[word]] += 1
            result.append(words_counts)
        return result

    def get_feature_names(self):
        """Get output feature names for transformation."""
        return self.feature_names

    def tf_transform(self, count_matrix: list):
        res = []
        for string in count_matrix:
            str_sum = sum(string)
            res.append([round(elem/str_sum, 3) for elem in string])
        return res

    def idf_transform(self, count_matrix: list):
        res = []
        len_mat = len(count_matrix) + 1
        n = len(self.feature_names)
        idf = [0] * n
        for string in count_matrix:
            for i in range(n):
                if string[i] != 0:
                    idf[i] += 1
        for i in range(n):
            res.append(round(log((len_mat)/(idf[i]+1)) + 1, 3))
        return res

class TfidfTransformer:
    def tf_transform(self, count_matrix: list) -> list[list]:
        """Transform a Term Frequency matrix with a count_matrix"""
        res = []
        for string in count_matrix:
            str_sum = sum(string)
            res.append([round(elem/str_sum, 3) for elem in string])
        return res

    def idf_transform(self, count_matrix: list) -> list[float]:
        """Transform an Inverse Document Frequency (IDF) vector"""
        res = []
        len_mat = len(count_matrix) + 1
        n = len(count_matrix[0])
        idf = [0] * n
        for string in count_matrix:
            for i in range(n):
                if string[i] != 0:
                    idf[i] += 1
        for i in range(n):
            res.append(round(log((len_mat)/(idf[i]+1)) + 1, 3))
        return res

    def fit_transform(self, count_matrix: list[float]) -> list[list]:
        """Make TF-IDF transformation from idf_transform and tf_transform"""
        tf_trans = self.tf_transform(count_matrix)
        idf_trans = self.idf_transform(count_matrix)
        n = len(idf_trans)
        res = []
        lst = [0]*n
        for string in tf_trans:
            res.append([round(string[i]*idf_trans[i],3) for i in range(n)])
        return res


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, data: list[str]) -> list[list[str]]:
        """
        Makes feature from text with CountVectorizer class;
        Makes tf-idf matrix from count matrix with
        TfidfTransformer class
        """
        count_matrix = super().fit_transform(data)
        return self.tf_idf_transformer.fit_transform(count_matrix)


