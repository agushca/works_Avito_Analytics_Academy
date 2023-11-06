from cnt_vec import CountVectorizer

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
          f'\n  {count_matrix[1]}')