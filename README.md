# README

## Overview

This project simulates the generation of banking products and accounts for a set of banks, calculates their loan processing times, and trains a machine learning model to predict these processing times based on various account and product features. It then includes SHAP analysis to understand feature importance.

## Contents
### data
- `bank.py`: Defines the classes `Bank`, `Product`, and `Account`.
- `feature_weights.py`: Contains a dictionary `weights` with weights for different features affecting loan processing time.
### eod feature analysis
- `bank_gen.py`: Generates synthetic data for banks, products, and accounts.
- `regression_bank_model.py`: Trains an XGBoost model to predict loan processing time, then performs SHAP analysis to interpret the trained model.

## Getting Started

### Prerequisites

- Python 3.7+
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `shap`, `matplotlib`, `joblib`

### Installing

1. Clone the repository.
2. Install the required libraries:

```bash
pip install pandas numpy scikit-learn xgboost shap matplotlib joblib
```

### Running the Project

1. Generate synthetic data:

```python
python bank_gen.py
```

2. Train the model and perform SHAP analysis:

```python
python regression_bank_model.py
```

### Understanding the Code
![Architecture for feature explanation pipeline](final_architecture.png)

#### Data Generation

`bank_gen.py`:

- **generate_products(n)**: Generates `n` products with randomly assigned features.
- **generate_accounts(n, product)**: Generates `n` accounts for a given product with randomly assigned features.
- **generate_banks(n_banks, n_products, n_acc_per_bank)**: Creates `n_banks` banks, generates and assigns products and accounts to each bank, and calculates the loan processing time based on feature weights. The generated data is saved in `account_data.csv` and `bank_data.csv`.

#### Model Training

`regression_bank_model.py`:

- Loads the generated data from `bank.csv` and `processing_time.csv`.
- Prepares the data for training by splitting it into training and testing sets.
- Defines a pipeline with preprocessing and the XGBoost regressor.
- Trains the model and evaluates its performance using Mean Squared Error (MSE) and R^2 Score.
- Saves the trained model to `100_banks_8_products_xgboost.pkl`.

#### SHAP Analysis

- Loads the trained model and test data.
- Uses SHAP to explain the model predictions.
- Generates and saves a SHAP summary plot.

## Results

The SHAP analysis reveals the importance of various features in predicting the loan processing time. The summary plot provides a visual representation of these feature importances.

## Acknowledgments

- This project uses the XGBoost library for training the machine learning model.
- The SHAP library is used for model interpretation and feature importance analysis.
- This project was made possible by the great people at Mambu. Our sincerest thank you for the time, office space, and most of all, the free lunches. 😊

## Authors

- Daniel Amidirad - https://github.com/damidirad/
- Wim Berkelmans - https://github.com/TCGWim
- Teun van der Maas - https://github.com/TeunvdMaas
- Popke Snoek - https://github.com/popkesnoek
- Lucas Woudstra - https://github.com/LucasWoudstra

## Contact

If you have any questions or suggestions, please feel free to contact us at danielamidirad@gmail.com
