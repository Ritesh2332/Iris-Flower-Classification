# Iris

This is a small Iris classifier demo with three parts:

- `data/iris_data.csv` contains the Iris dataset used for training
- `model/model.pkl` contains a trained model
- `notebook/Iris.ipynb` is the notebook where the model is built and evaluated
- `app.py` is a Streamlit app where you can enter flower measurements and get a prediction

## Run the app

1. Create/activate a virtualenv (recommended), then install dependencies:
   - `pip install -r requirements.txt`
2. Start Streamlit:
   - `streamlit run app.py`

## What to enter

Use the inputs in the UI:

- Sepal length and width
- Petal length and width

