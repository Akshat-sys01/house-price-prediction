import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Age category function
def age_category(age):
    if age <= 5:
        return 0  # New
    elif age <= 15:
        return 1  # Mid-age
    else:
        return 2  # Old

# Model evaluation function
def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    return r2, mae, rmse

# Load dataset
data = pd.read_csv(r"C:\Academics 25-26\4th Sem\My Work\Projects\house_price_prediction\data\house_data.csv")

# Outlier detection (IQR Method)
Q1 = data['price'].quantile(0.25)
Q3 = data['price'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)

# Inspect outliers
outliers = data[(data['price'] < lower_limit) | (data['price'] > upper_limit)]
print("Number of outliers:", outliers.shape[0], "\n")

# Remove outliers
data_cleaned = data[
    (data['price'] >= lower_limit) &
    (data['price'] <= upper_limit)
]

data = data_cleaned.copy()

# Create new features
data['total_rooms'] = data['bedrooms'] + data['bathrooms']
data['price_per_sqft'] = data['price'] / data['area'] 
data['age_category'] = data['age'].apply(age_category)
data['area_per_room'] = data['area'] / (data['bedrooms'] + data['bathrooms'])

# Features and target
X = data[
    ['area',
     'bedrooms',
     'bathrooms', 
     'age',
     'total_rooms',
     'age_category',
     'area_per_room'
    ]
]
y = data['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create scaler
scaler = StandardScaler()

# Fit on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

# Create models
lr_model = LinearRegression()

lr_r2, lr_mae, lr_rmse = evaluate_model(
    lr_model,
    X_train_scaled, X_test_scaled,
    y_train, y_test
)

dt_model = DecisionTreeRegressor(random_state=42)

dt_r2, dt_mae, dt_rmse = evaluate_model(
    dt_model,
    X_train, X_test,
    y_train, y_test
)

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_r2, rf_mae, rf_rmse = evaluate_model(
    rf_model,
    X_train, X_test,
    y_train, y_test
)

# Calculate metrics
print("MODEL COMPARISON RESULTS:\n")

print("Linear Regression:")
print("R2:", lr_r2)
print("MAE:", lr_mae)
print("RMSE:", lr_rmse, "\n")

print("Decision Tree:")
print("R2:", dt_r2)
print("MAE:", dt_mae)
print("RMSE:", dt_rmse, "\n")

print("Random Forest:")
print("R2:", rf_r2)
print("MAE:", rf_mae)
print("RMSE:", rf_rmse, "\n")

# Save the best model
with open(r"C:\Academics 25-26\4th Sem\My Work\Projects\house_price_prediction\model/house_price_model.pkl", "wb") as f:
    pickle.dump(rf_model, f)

print("Best model saved successfully!")

# Save scaler
with open(r"C:\Academics 25-26\4th Sem\My Work\Projects\house_price_prediction\model/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Scaler saved successfully!")

# Save comparision results
with open(r"C:\Academics 25-26\4th Sem\My Work\Projects\house_price_prediction\model/model_comparision.txt", "w") as f:
    f.write("Model Comparison Results\n\n")

    f.write("Linear Regression\n")
    f.write(f"R2: {lr_r2}, MAE: {lr_mae}, RMSE: {lr_rmse}\n\n")

    f.write("Decision Tree\n")
    f.write(f"R2: {dt_r2}, MAE: {dt_mae}, RMSE: {dt_rmse}\n\n")

    f.write("Random Forest\n")
    f.write(f"R2: {rf_r2}, MAE: {rf_mae}, RMSE: {rf_rmse}")

print("Comparison results saved successfully!")