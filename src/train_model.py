import pandas as pd
import pickle
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv(r"C:\Academics 25-26\4th Sem\My Work\Projects\house_price_prediction\data\house_data.csv")

# Features and target
X = data[['area', 'bedrooms', 'bathrooms', 'age']]
y = data['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Import r2 Score
from sklearn.metrics import r2_score

# Calculate r2 score
score = r2_score(y_test, y_pred)
print("R2 Score:", score)

# Model coefficients
print(model.coef_)
print(model.intercept_)

# Save model
with open(r"C:\Academics 25-26\4th Sem\My Work\Projects\house_price_prediction\model/house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")