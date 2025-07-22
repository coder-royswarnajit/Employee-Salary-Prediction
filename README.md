# Employee Salary Prediction App

A machine learning web application that predicts employee salaries based on years at company and job performance rating using Linear Regression.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Machine Learning Model**: Linear Regression model trained on employee data
- **Data Visualization**: Scatter plot showing relationship between years and salary
- **Real-time Predictions**: Instant salary predictions based on user inputs
- **Model Persistence**: Trained model saved and loaded for predictions

## 📋 Requirements

```
pandas
scikit-learn
streamlit
joblib
matplotlib
numpy
kagglehub
openpyxl
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd salary-prediction-app
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pandas scikit-learn streamlit joblib matplotlib numpy kagglehub openpyxl
```

## 📊 Dataset

The project uses the "Company Employees" dataset from Kaggle:
- **Source**: `abdallahwagih/company-employees`
- **File**: `employees.xlsx`
- **Features**:
  - Years at Company
  - Job Rating (0.0 - 5.0)
  - Annual Salary (Target variable)

## 🏃‍♂️ Usage

### 1. Train the Model

First, run the analysis and modeling script to train the Linear Regression model:

```bash
python Analysis_Modeling.py
```

This will:
- Download the dataset from Kaggle
- Clean the data (remove duplicates and null values)
- Train a Linear Regression model
- Save the model as `linearmodel.pkl`
- Generate a visualization (`years_vs_salary.png`)

### 2. Run the Web Application

Launch the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### 3. Make Predictions

1. Enter **Years at Company** (minimum 0)
2. Enter **Job Rating** (0.0 to 5.0)
3. Click **"Predict Salary"** to get the predicted annual salary

## 🔧 Project Structure

```
salary-prediction-app/
│
├── Analysis_Modeling.py    # Data analysis and model training
├── app.py                 # Streamlit web application
├── linearmodel.pkl        # Trained model (generated after running Analysis_Modeling.py)
├── years_vs_salary.png    # Visualization (generated after running Analysis_Modeling.py)
├── requirements.txt       # Package dependencies
└── README.md             # Project documentation
```

## 🤖 Model Details

- **Algorithm**: Linear Regression
- **Features**: 
  - Years at Company (numeric)
  - Job Rating (numeric, 0.0-5.0)
- **Target**: Annual Salary (in INR)
- **Train-Test Split**: 80-20
- **Evaluation Metric**: Mean Absolute Error (MAE)

## 📱 App Features

### Sidebar Information
- App description and usage instructions
- Model details and feature information

### Main Interface
- Input fields for years and job rating
- Prediction button with celebratory balloons
- Results display with formatted salary output

### Expandable Sections
- **Model Information**: Technical details about the model
- **Data Visualization**: Interactive scatter plot of the training data

## 🎯 Example Usage

**Input:**
- Years at Company: 5
- Job Rating: 4.2

**Output:**
- Predicted Salary: ₹X,XX,XXX.XX per year

## 🔍 Error Handling

The application includes robust error handling for:
- Model loading failures
- Prediction errors
- Data visualization issues
- Invalid input values

## 🚀 Future Enhancements

- Add more features (department, location, education level)
- Implement multiple ML algorithms for comparison
- Add model performance metrics display
- Include data upload functionality for custom datasets
- Add salary range predictions with confidence intervals

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request
