from classes_practice import CountVectorizer, TfidfTransformer, TfidfVectorizer

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(f'The result of .get_feature_names method:'
          f'\n  {vectorizer.get_feature_names()}\n')
    print(f'The count matrix:'
          f'\n  {count_matrix[0]},'
          f'\n  {count_matrix[1]}\n ')

    transformer = TfidfTransformer()
    tf_matrix = transformer.tf_transform(count_matrix)
    print(f'The result of .tf_transform method:'
          f'\n {tf_matrix[0]},'
          f'\n {tf_matrix[1]}\n')

    idf_matrix = transformer.idf_transform(count_matrix)
    print(f'The result of .idf_transform method:'
          f'\n {idf_matrix}\n')

    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(f'The result of .fit_transform method:'
          f'\n {tfidf_matrix[0]},'
          f'\n {tfidf_matrix[1]}\n')

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(f'The result of .fit_transform method:'
          f'\n {tfidf_matrix[0]},'
          f'\n {tfidf_matrix[1]}\n')