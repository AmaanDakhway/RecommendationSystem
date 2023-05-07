from flask import Flask, request, jsonify
from recommendation_engine import recommended_course  # Importing engine function
import pandas as pd
import pickle

app = Flask(__name__)

# Avoid switching the order of 'title' and 'confidence' keys
app.config['JSON_SORT_KEYS'] = False

course_titles_df = pd.read_csv('coursera_dataset.csv', usecols=[2])

tfidf_vect_pkl = pickle.load(open('tfidf_vectorizer.pickle', 'rb'))


# API endpoint
@app.route('/')
def home():
    return "Hello World this is another test"


@app.route('/api/', methods=['POST'])
def process_request():
    # Parse received JSON request
    # user_input = request.get_json()

    # Extract show title
    title = request.form.get('course')
    # # Call recommendation engine
    recommended_course_dict = recommended_course(title, course_titles_df, tfidf_vect_pkl)
    # return jsonify(title)
    return jsonify(recommended_course_dict)


if __name__ == '__main__':
    app.run()
