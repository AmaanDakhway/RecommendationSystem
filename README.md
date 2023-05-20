# Simple Content-based Recommendation Engine API With Flask [Render Deployed]

>This repository contains code for a recommendation system that utilizes content-based filtering and deploys a Postman collection for testing. The recommendation system is built using Python and utilizes the pickle library for model serialization.

## Setup and Installation

>1. Clone the repository:

```bash
git clone https://github.com/amaandakhway1234/RecommendationSystem.git
```
>2. Navigate to the project directory:

```bash
cd RecommendationSystem
```

>3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

>4. Create the Model Vectorizer:

```bash
python course_vectorizer.py
```
>5. Run the API:

```bash
python app.py
```


## Usage

- Run `course_vectorizer.py` to generate a pickle file of TF-IDF vectorizer.

- Start the recommendation engine API locally by running `app.py`.

- Test the API on Postman by running on the localhost workspace (http://127.0.0.1:5000/)

- To run it on Render.com, publish it as a static website by uploading it to your github and accessing it via Render.com .

- Communicating with the API can be either through sending Form POST requests to endpoint /api/ 
    - Example 1: POST request to https://course-recommend-engine.onrender.com/api/ with payload:

 ```

        Key : course
        Value : Build a Machine Learning Web App with Streamlit and Python 
        ```
         is responded to with
         ```
{
    "result": [
        {
            "title": "Build a Data Science Web App with Streamlit and Python",
            "confidence": 0.6
        },
        {
            "title": "Create Interactive Dashboards with Streamlit and Python",
            "confidence": 0.5
        },
        {
            "title": "Create Your First Web App with Python and Flask",
            "confidence": 0.2
        },
        {
            "title": "Support Vector Machines with scikit-learn",
            "confidence": 0.2
        },
        {
            "title": "Neural Network Visualizer Web App with Python",
            "confidence": 0.1
        },
        {
            "title": "Logistic Regression with NumPy and Python",
            "confidence": 0.1
        },
        {
            "title": "Medical Diagnosis using Support Vector Machines",
            "confidence": 0.1
        },
        {
            "title": "Build a film club web app on Google AppEngine",
            "confidence": 0.1
        },
        {
            "title": "Machine Learning Pipelines with Azure ML Studio",
            "confidence": 0.1
        }
    ]
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
