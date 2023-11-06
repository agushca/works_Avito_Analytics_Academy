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