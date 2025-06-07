# Life Expectancy Prediction Using Health and Socioeconomic Factors
This project aims to predict life expectancy based on various health and socioeconomic factors across 193 countries from 2000 to 2015, using data from the World Health Organization (WHO) and United Nations. The analysis utilizes machine learning models to explore how indicators like immunization rates, education levels, income composition, and healthcare infrastructure correlate with life expectancy outcomes.

Table of Contents
- Installation
- Dataset
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Modeling
- Evaluation
- Reproducibility
- Conclusion

## Installation
To run this project locally, clone the repository and install the necessary dependencies:
git clone https://github.com/peixuanyap/Predicting-Life-Expectancy.git

## Dataset
The dataset used in this project is sourced from Kaggle. The dataset includes various health and socioeconomic indicators along with life expectancy data for different countries.
Link to Kaggle Dataset: [Life Expectancy Data](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)

## Data Preprocessing
The following preprocessing steps are performed:
- Missing value imputation using median for numerical columns and mode for categorical data.
- Removal of columns with excessive missing values (e.g., BMI).
- Outlier detection using the Interquartile Range (IQR) 
- Feature scaling using Min-Max Scaling.

## Exploratory Data Analysis (EDA)
- Data visualizations: Various visualizations, including histograms, boxplots, and scatter plots, were created to explore the distribution of Life Expectancy, relationships with other features, and trends over time.
- Statistical Analysis: Statistical tests, such as the Shapiro-Wilk test for normality and skewness, were performed to assess the distribution characteristics of key variables.
- Correlation Analysis: A correlation matrix and heatmap were used to identify and visualize the relationships between Life Expectancy and other numerical features.
- Dimensionality Reduction: Principal Component Analysis (PCA) was applied to reduce the feature space while retaining most of the variance, with 10 components chosen to capture 90% of the variance.

## Modeling
The project evaluates multiple machine learning models, including:
- Random Forest
- Support Vector Machines (SVM)
- Linear Regression
- Gradient Boosting
- Neural Networks (MLP)
Hyperparameter tuning is performed using RandomizedSearchCV for each model, and performance is evaluated using cross-validation and R-squared metrics.

## Evaluation
The models are compared based on the following metrics:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

### Best Model
The Random Forest model achieved the best performance with the following metrics:
- MSE: 10.6233
- RMSE: 3.2593
- R-squared: 0.8864

## Reproducibility
The analysis is fully reproducible:
- Code: All notebooks are available in the repository.
- Data: The dataset can be downloaded from Kaggle and is linked in the README.
- Environment: Ensure all dependencies are installed via the requirements.txt file.

## Conclusion
The project successfully predicts life expectancy using multiple health and socioeconomic factors. Random Forest performed the best, balancing accuracy and generalization. This project helps inform policymakers about key factors impacting life expectancy globally and highlights areas for potential intervention.
