from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import os

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=os.getenv("GROQ_API_KEY"))

# Initialize the CSV agent
agent = create_csv_agent(
    llm, 
    'sales_performance_data.csv', 
    verbose=True,
    allow_dangerous_code=True,
    handle_parsing_errors=True,
)

# Create Flask app
app = Flask(__name__)

# 1. Individual Sales Representative Performance Analysis
@app.route('/api/rep_performance', methods=['GET'])
def rep_performance():
    rep_id = request.args.get('rep_id')
    
    if rep_id:
        # Create a custom prompt for the employee's performance analysis
        prompt = f"""
        Provide a detailed analysis for the sales representative with employee_id: {rep_id}.
        Include the following metrics:
        - Total leads, tours, and applications
        - Total tours this week and tours run rate
        - Confirmed revenue and pending revenue
        - Tours scheduled, tours cancelled, and tours in pipeline
        """
        try:
            response = agent.invoke(prompt)
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Sales representative ID not provided'}), 400

# 2. Overall Sales Team Performance Summary
@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    prompt = """
    Provide a summary analysis of the overall sales team performance, including:
    - Total leads, tours, and applications
    - Total revenue (confirmed and pending)
    - Overall tours scheduled, tours cancelled, and tours in pipeline
    """
    try:
        response = agent.invoke(prompt)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. Sales Performance Trends and Forecasting
@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    time_period = request.args.get('time_period')
    
    if time_period:
        prompt = f"""
        Analyze sales performance trends over the specified time period: {time_period}.
        Identify key trends and provide a forecast for future performance.
        """
        try:
            response = agent.invoke(prompt)
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid time period'}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
