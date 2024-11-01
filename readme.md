
# Flask App Setup and API Access Guide

## Step 1: Create a Virtual Environment

To ensure that the project runs in an isolated environment, create a virtual environment using the following command:

```bash
# Create a virtual environment named 'venv'
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:
    ```bash
    venv\Scripts\activate
    ```
- On **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

## Step 2: Install Dependencies from `requirements.txt`

Once the virtual environment is activated, install the required dependencies for the Flask app using the `requirements.txt` file:

```bash
# Install the required packages
pip install -r requirements.txt
```

Make sure that the `requirements.txt` file contains all necessary dependencies such as Flask, dotenv, Langchain, etc.

## Step 3: Run the Flask App

After the dependencies are installed, run the Flask app by executing the following command:

```bash
# Run the main Flask application
python main2.py
```

This will start the Flask server, and the app will be available locally at `http://127.0.0.1:5000/`.

## API Endpoints Overview

### 1. **Individual Sales Representative Performance Analysis**

- **Endpoint:** `/api/rep_performance`
- **Method:** `GET`
- **Parameters:** 
    - `rep_id`: The unique identifier for the sales representative whose performance you want to analyze.

- **Example Request:**

    ```bash
    curl "http://127.0.0.1:5000/api/rep_performance?rep_id=183"
    ```

- **Functionality:** 
    - This endpoint returns a detailed performance analysis for the sales representative with the given `rep_id`. It provides metrics such as total leads, tours, applications, confirmed revenue, pending revenue, tours scheduled, tours cancelled, and tours in pipeline.

- **Response Example:**
    ```json
    {
      "total_leads": 50,
      "total_tours": 20,
      "confirmed_revenue": 50000,
      "pending_revenue": 10000,
      "tours_scheduled": 25,
      "tours_cancelled": 5,
      "tours_in_pipeline": 3
    }
    ```

### 2. **Overall Sales Team Performance Summary**

- **Endpoint:** `/api/team_performance`
- **Method:** `GET`

- **Example Request:**

    ```bash
    curl "http://127.0.0.1:5000/api/team_performance"
    ```

- **Functionality:**
    - This endpoint provides an overall summary of the sales team's performance, including total leads, tours, applications, total revenue (confirmed and pending), tours scheduled, cancelled, and those in the pipeline.

- **Response Example:**
    ```json
    {
      "total_leads": 300,
      "total_tours": 150,
      "confirmed_revenue": 250000,
      "pending_revenue": 50000,
      "tours_scheduled": 180,
      "tours_cancelled": 20,
      "tours_in_pipeline": 10
    }
    ```

### 3. **Sales Performance Trends and Forecasting**

- **Endpoint:** `/api/performance_trends`
- **Method:** `GET`
- **Parameters:** 
    - `time_period`: A string indicating the time period for analysis (e.g., `monthly`, `quarterly`, etc.).

- **Example Request:**

    ```bash
    curl "http://127.0.0.1:5000/api/performance_trends?time_period=monthly"
    ```

- **Functionality:** 
    - This endpoint analyzes sales performance trends over the specified time period and provides a forecast for future performance based on the trends.

- **Response Example:**
    ```json
    {
      "time_period": "monthly",
      "performance_trend": "positive",
      "forecasted_growth": "5%"
    }
    ```

## Conclusion

By following these steps, you will set up the Flask app, run it, and access the sales performance APIs. Each API is designed to analyze and return detailed performance insights for both individual sales representatives and the entire team, as well as provide forecasting based on sales trends.
```

### Key Points:
1. **Setup Instructions**: Walkthrough for setting up a Python virtual environment, installing dependencies, and running the Flask app.
2. **API Overview**: Each endpoint is explained in terms of its functionality, expected input, and example responses.
3. **Accessing the APIs**: Use the provided `curl` commands to test each API. You can also use tools like Postman or a browser to interact with the endpoints.
