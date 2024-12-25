# HR Analytics: Job Change Predictor

This is a Flask-based web application that predicts whether a data scientist will stay with a company or leave. The project provides tools for training machine learning models, evaluating their performance, and making predictions based on user inputs. The application is designed for HR analytics and aims to assist in decision-making processes.

## Features

- **Train Machine Learning Models:** Train Logistic Regression, K-Nearest Neighbors, or SVM models on different datasets (normal, oversampled, or undersampled).
- **Evaluate Models:** View evaluation metrics, including train/test scores and a detailed classification report.
- **Make Predictions:** Predict an employee's likelihood of staying or leaving based on their features.
- **User-Friendly Interface:** Interact with the application through a clean and intuitive web interface.

## Installation

### Prerequisites

- Python 3.7+
- Flask
- scikit-learn
- pandas
- numpy
- matplotlib
- joblib

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hr-analytics-predictor.git
   cd hr-analytics-predictor
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place your datasets (`normal_data.csv`, `oversample.csv`, `undersample_data.csv`) in the `data` folder.

5. Run the application:
   ```bash
   python main.py
   ```

6. Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Project Structure

```
hr-analytics-predictor/
├── main.py                 # Main Flask application
├── train.py               # Handles model training and evaluation
├── predict.py             # Handles predictions
├── templates/             # HTML templates for the web interface 
├── data/                  # Folder for datasets
├── static/                # Static files (CSS, JS, etc.)
└── requirements.txt       # Python dependencies
```

## Usage

### 1. Train a Model
- Navigate to the **Train Models** page.
- Select a dataset type (normal, oversampled, or undersampled).
- Choose a model (Logistic Regression, KNN, or SVM).
- Train the model and view its evaluation metrics.

### 2. Make Predictions
- Navigate to the **Predict** page.
- Input the employee's details (e.g., city development index, gender, experience, etc.).
- Submit the form to get the prediction result.

## Datasets

The project expects datasets in CSV format with the following columns:
- `city_development_index`
- `gender`
- `relevant_experience`
- `enrolled_university`
- `education_level`
- `major_discipline`
- `experience`
- `company_size`
- `company_type`
- `last_new_job`
- `training_hours`
- `target` (0: Stays, 1: Leaves)

## Acknowledgements

- [scikit-learn](https://scikit-learn.org/) for machine learning tools
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Kaggle](https://www.kaggle.com/) for providing the HR Analytics dataset
