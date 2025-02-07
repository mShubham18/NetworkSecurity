# Network Security: Phishing Detection & Data Analysis

Welcome to the **Network Security MLOps** repository, which focuses on **phishing detection, data analysis, and ETL pipelines** for processing network security data.

## 📱 Working
![Working Demo](Resources/Working.gif)


## 📌 Overview  

This project involves **analyzing and detecting phishing attempts** by leveraging **machine learning models** and **ETL pipelines** to process network traffic data efficiently. The repository includes **data schemas, trained models, a Flask-based web interface, and MongoDB integration** for real-time phishing detection.

## ✨ Key Features  

- **Phishing Detection Model**: Uses machine learning algorithms to classify network traffic as legitimate or phishing attempts.  
- **ETL Pipelines**: Extracts raw network data, transforms it into a structured format, and loads it into a MongoDB database.  
- **Web Interface**: A Flask application allowing users to input data and get phishing predictions.  
- **Dockerized Deployment**: Includes Docker support for easy setup and deployment.  
- **MongoDB Integration**: Stores and retrieves processed data for analysis.  

## 🔄 ETL Pipeline for Phishing Detection  

The **ETL (Extract, Transform, Load) pipeline** is crucial for processing network data and preparing it for phishing detection.

### 📥 1. Extract  
- Collects raw network traffic data from log files, databases, or APIs.  
- Uses scripts to **scrape phishing data sources** and gather new phishing URLs.  
- Stores extracted data in **CSV or JSON format**.  

### 🛠️ 2. Transform  
- Cleans and preprocesses data by **removing duplicates and handling missing values**.  
- Normalizes network traffic patterns for **consistent feature engineering**.  
- Converts raw data into a structured format matching the `data_schema/`.  
- Feature selection for **training the phishing detection model**.  

### 📤 3. Load  
- Stores processed data into **MongoDB** for real-time analysis.  
- Enables the Flask app (`app.py`) to retrieve and display phishing detection results.  
- `push_data.py` handles automatic updates to the database.  


## 🚀 Getting Started  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/mShubham18/NetworkSecurity.git
cd NetworkSecurity
```

### 2️⃣ Install dependencies
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```
### 3️⃣ Set up MongoDB
Ensure MongoDB is running locally or configure a remote database: 
- create a .env in the root and add a environment variable `MONGO_DB_URL` and paste your Mongo DB connection url
- Also add a `PORT` variable with a port value ex. `8000`
- Test the working by running `test_mongo_db.py` and `push_data.py` for pushing the data on the Mongo DB Atlas server

### 4️⃣ Run the ETL pipeline
Run the main command by:
```bash
uvicorn app:app
```
or
```bash
python app.py
```

### 5️⃣ Start the Flask web appa

Visit the link being shown in the terminal:
```bash
http://127.0.0.1:8000
```

### 🔍 Usage
Automated ETL Pipelines: New phishing data is processed periodically and updated in the database.
Web Interface: Users can check network data against phishing detection models via the Flask app.
Database Storage: MongoDB stores structured data for further analysis.

### 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements. Ensure all changes are well-documented and tested.

Keep Coding ;)