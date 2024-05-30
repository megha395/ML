# Logistic Regression Classification Model

This project involves building, training, and evaluating a classification model using Logistic Regression. 

## Project Structure

- `global_imports.py`: Contains all the necessary imports and global variables used across various scripts.
- `preprocessing.py`: Handles data preprocessing tasks such as data cleaning, feature engineering, and splitting the data into training and testing sets.
- `analysis.ipynb`: A Jupyter notebook for exploratory data analysis (EDA). This includes visualizations and insights derived from the data.
- `model.py`: Defines and trains the Logistic Regression model. It includes functions for model training and saving the trained model.
- `evaluation.ipynb`: A Jupyter notebook for evaluating the performance of the trained model. This includes metrics such as accuracy, precision, recall, and ROC-AUC.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-repo/logistic-regression-classification.git
    cd logistic-regression-classification
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Project

### Step 1: Preprocessing

Run the `preprocessing.py` script to preprocess the data. This script will:
- Load the raw data.
- Clean the data and handle missing values.
- Perform feature engineering.
- Split the data into training and testing sets.

```bash
python preprocessing.py
