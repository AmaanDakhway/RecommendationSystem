from sklearn.metrics.pairwise import cosine_similarity


def recommended_course(title, courses_df, tfidf_vect):
    '''
    Recommends the top 5 similar shows to provided show title.
            Arguments:
                    title (str): Show title extracted from JSON API request
                    courses_df (pandas.DataFrame): Dataframe of Course dataset
                    tfidf_vect (scipy.sparse.matrix): sklearn TF-IDF vectorizer sparse matrix
            Returns:
                    response (dict): Recommended shows and similarity confidence in JSON format
    '''

    try:

        title_iloc = courses_df.index[courses_df['Course Name'] == title][0]

    except:

        return 'Course title not found. Please make sure it is one of the titles in this dataset'

    course_cos_sim = cosine_similarity(tfidf_vect[title_iloc], tfidf_vect).flatten()

    sim_titles_vects = sorted(list(enumerate(course_cos_sim)), key=lambda x: x[1], reverse=True)[1:10]

    response = {'result': [{'title': courses_df.iloc[t_vect[0]][0], 'confidence': round(t_vect[1], 1)} for t_vect in
                           sim_titles_vects]}

    return response