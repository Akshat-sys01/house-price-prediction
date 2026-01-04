# 🏡 House Price Prediction Web App (Machine Learning + Django)

A **production-ready end-to-end Machine Learning project** that predicts house prices based on user inputs such as area, number of bedrooms, bathrooms, and age of the house.

This project is designed as a **learning-to-industry bridge** — covering the *complete ML lifecycle* (data analysis → model training → evaluation → deployment-ready integration) and exposing the model through a **Django-based web application**.

This repository reflects a real-world workflow followed in ML-backed web applications.

---

## 🔗 Live Demo

🚀 **Deployed on Render**:
👉 [https://house-price-prediction-jppg.onrender.com/](https://house-price-prediction-jppg.onrender.com/)

> The application is fully deployed and accessible online, demonstrating real-time machine learning inference through a Django web interface.

---

## 🎯 Project Objectives

* Learn and implement the **complete Machine Learning pipeline**
* Understand how ML models are **integrated into backend frameworks (Django)**
* Build a **clean, modular, and deployable project** suitable for portfolios
* Follow **industry-style structure, evaluation, and serialization practices**

---

## 🚀 Key Features

* 📊 **Machine Learning–based price prediction** using Random Forest Regressor
* 🧠 Full ML pipeline: EDA → preprocessing → training → evaluation
* 🌐 **Django Web Interface** for real-time predictions
* 🔄 **Serialized ML model (`pickle`)** loaded directly in Django views
* 🛠️ Clean and scalable project structure
* 📦 Deployment-ready configuration

---

## 🧩 Tech Stack

| Layer            | Technology                  |
| ---------------- | --------------------------- |
| Language         | Python                      |
| Machine Learning | NumPy, Pandas, Scikit-learn |
| Web Framework    | Django                      |
| Frontend         | HTML, CSS                   |
| Model Storage    | Pickle                      |
| Version Control  | Git & GitHub                |

---

## 📁 Project Structure

```
house-price-prediction/
│
├── data/                     # Raw & processed datasets
├── notebooks/                # EDA & model training notebooks
├── model/                    # Trained ML model (.pkl)
├── src/                      # ML scripts & utilities
│
├── house_price_web/          # Django project
│   ├── templates/            # HTML templates
│   ├── static/               # CSS & assets
│   ├── views.py              # Prediction logic
│   ├── urls.py               # URL routing
│   └── settings.py           # Project settings
│
├── build.sh                  # Build / deployment script
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

---

## 📊 Machine Learning Workflow

This project follows a **standard industry-level ML pipeline**:

### 1️⃣ Data Inspection

* Understanding data distributions
* Identifying missing values and outliers
* Checking correlations between features

### 2️⃣ Data Preprocessing

* Handling missing values
* Encoding categorical features (if any)
* Scaling numerical features

### 3️⃣ Feature Selection

* Identifying the most impactful predictors such as:

  * Square Footage
  * Number of Bedrooms
  * Age of the House

### 4️⃣ Model Training

* Training a **Random Forest Regressor** for capturing non-linear relationships
* Splitting data into training and testing sets

### 5️⃣ Model Evaluation

* Evaluated using standard regression metrics:

  * **R² Score**
  * **MAE (Mean Absolute Error)**
  * **RMSE (Root Mean Square Error)**

### 6️⃣ Model Serialization

* Saving the trained model using **`pickle`**
* Loading the model inside Django for real-time inference

---

## 🧪 Model Performance

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.9589 |
| MAE      | 4.125  |
| RMSE     | 4.939  |

> These results indicate a **highly accurate Random Forest model**, significantly outperforming simple linear baselines and demonstrating strong generalization capability.

---

## 🌐 Web Application Workflow

1. User opens the web application
2. Inputs house details (area, bedrooms, age, etc.)
3. Django validates user input
4. Serialized ML model generates prediction
5. Predicted house price is displayed on the UI

---

## 🛠️ Setup & Installation

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Akshat-sys01/house-price-prediction.git
cd house-price-prediction
```

### 2️⃣ Create & Activate Virtual Environment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Django Migrations

```bash
cd house_price_web
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 📌 Usage Guide

* Open the home page
* Enter house details (area, bedrooms, age)
* Click **Predict**
* View the estimated house price instantly

---

## 📦 Deployment

This project can be deployed on:

* Render
* Railway
* Heroku
* PythonAnywhere
* AWS Elastic Beanstalk

**Before deploying to production:**

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Use environment variables for secrets

---

## 🔮 Future Improvements

* Hyperparameter tuning for Random Forest
* Experiment with Gradient Boosting and XGBoost
* Feature engineering for better accuracy
* Model comparison & cross-validation
* User authentication
* Database-backed prediction history
* Docker-based deployment

---

## 💡 Contributing

This project is primarily built for **learning and demonstration**.

Suggestions, improvements, and discussions are welcome:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes
4. Open a Pull Request

---

## 🙌 Acknowledgements

* Open-source datasets and ML community resources
* **Scikit-learn** documentation
* **Django** official documentation

---

## 👤 Author

**Akshat Raj**

BCA Student | Machine Learning & Web Development Enthusiast

This project reflects my learning journey in **Machine Learning, Django, and real-world project structuring**.
