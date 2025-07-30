# Restaurant Analysis App

A comprehensive web application that combines restaurant recommendations with machine learning-powered rating predictions. Built with Streamlit and powered by data analysis of Zomato restaurant data.

## Features

### 🔍 Restaurant Recommendations
- **Pocket-Friendly Plates**: Curated list of budget-friendly restaurants with high ratings
- **Top-Tier Tastes**: Premium dining options with excellent ratings and high vote counts
- **Pre-analyzed Data**: Shows restaurants filtered by cost and rating criteria

### ⭐ Rating Prediction
- **ML-Powered Predictions**: Uses Extra Trees Regressor for accurate rating predictions
- **Interactive Form Interface**: Easy-to-use dropdowns and input fields
- **Real-time Predictions**: Get instant rating predictions based on restaurant features
- **Comprehensive Features**: Predict based on location, cuisine, cost, votes, and more

## Dataset

The application uses the Zomato restaurant dataset containing information about:
- Restaurant locations
- Cuisine types
- Cost for two people
- Online ordering availability
- Table booking options
- User votes and ratings

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Scikit-learn**: Machine learning library
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Joblib**: Model serialization

## Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. Install required packages:
```bash
pip install streamlit pandas scikit-learn joblib numpy
```

3. Run the application:
```bash
streamlit run app.py
```

## Configuration

### For Local Development
The app runs locally on `http://localhost:8501` by default.

### For Public Access (Optional)
If you want to share your app publicly using ngrok:

1. Install ngrok and get an authentication token from [ngrok.com](https://ngrok.com)
2. In the notebook, replace `YOUR_NGROK_TOKEN_HERE` with your actual token:
```python
ngrok.set_auth_token("YOUR_NGROK_TOKEN_HERE")
```
3. Run the ngrok tunnel setup code in the notebook


## Usage

### Restaurant Recommendations Tab
1. Open the Streamlit app in your browser
2. Navigate to the "🔍 Restaurant Recommendations" tab
3. Choose your preference:
   - Click **"Pocket-Friendly Plates"** for budget-friendly options (₹100-₹1500)
   - Click **"Top-Tier Tastes"** for premium dining experiences (₹3000+)
4. Browse through the curated restaurant lists with details like cost, location, cuisine, and ratings

### Rating Prediction Tab
1. Navigate to the "⭐ Rating Prediction" tab
2. Fill in the restaurant details using the form:
   - **Online Order**: Select availability (True/False)
   - **Book Table**: Select table booking option (True/False)
   - **Location**: Choose from 92 available locations
   - **Restaurant Type**: Select from 87 restaurant types
   - **Cuisines**: Choose from 2367 cuisine combinations
   - **Votes**: Enter number of votes received
   - **Cost**: Enter approximate cost for two people (in ₹)
3. Click **"Predict Rating"** to get the ML-powered prediction
4. View the predicted rating (0-5 scale) with visual feedback

## Model Information

The rating prediction feature uses an Extra Trees Regressor model trained on Zomato restaurant data.

### Model Features (in order):
1. **Online order**: Binary (True/False for online ordering availability)
2. **Book table**: Binary (True/False for table booking option)
3. **Votes**: Numeric (number of user votes received)
4. **Location**: Categorical (92 unique locations in Bangalore)
5. **Restaurant type**: Categorical (87 unique restaurant types)
6. **Cuisines**: Categorical (2367 unique cuisine combinations)
7. **Cost**: Numeric (approximate cost for two people in ₹)
8. **Menu item**: Categorical (encoded menu categories)

### Model Performance:
- **Algorithm**: Extra Trees Regressor with 100 estimators
- **Training Data**: Zomato restaurant dataset with 40,000+ records
- **Features**: 8 engineered features from restaurant characteristics
- **Target**: Restaurant rating (0-5 scale)

## Application Structure

### Main Files
- **`app.py`**: Main Streamlit application with dual functionality
  - Restaurant recommendation system with curated lists
  - ML-powered rating prediction interface
- **`DMW_PROJECT.ipynb`**: Complete data analysis and model development notebook
  - Data preprocessing and cleaning
  - Exploratory data analysis
  - Model training and evaluation
  - Feature engineering and encoding
  - Contains ngrok setup with placeholder token (`YOUR_NGROK_TOKEN_HERE`)

### Data Files
- **`zomato.csv`**: Original Zomato restaurant dataset
- **`extra_trees_model.pkl`**: Trained Extra Trees Regressor model
- **`mappings.pkl`**: Feature encodings for categorical variables
- **`requirements.txt`**: Python dependencies for deployment

### Configuration Files
- **`README.md`**: Project documentation
- **`.gitignore`**: Git ignore rules for sensitive data and tokens
- **Security**: Sensitive information like ngrok tokens are replaced with placeholders

## Security & Privacy


### Data Privacy
- The app uses publicly available Zomato restaurant data
- No personal user data is collected or stored
- All predictions are processed locally

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.
