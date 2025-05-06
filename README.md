# Python-Assignment
Financial Analyser Tool 
Stock Price & MA Viewer

A Python Streamlit app for interactive visualization of NSE stock prices, moving averages, and daily percentage changes. This project demonstrates clean modular code, user-friendly design, and reproducibility, as per group project guidelines.

---

##  Project Objective

•⁠  ⁠Reinforce Python and data processing skills  
•⁠  ⁠Practice modular programming and Streamlit UI development  
•⁠  ⁠Experience real-world app design, version control, and documentation  
•⁠  ⁠Collaborate and simulate product building using data and logic

---

##  Project Structure

your-repo/
│
├── app.py # Main Streamlit app file (contains all logic)
├── requirements.txt # List of Python dependencies
├── README.md # Project documentation (this file)
└── ... # (Optional) assets or data folders
text
	⁠The code is modular with clear function separation for data loading, processing, and visualization.

---

##  Features

•⁠  ⁠*NSE Stock Search:* Select any NSE-listed company by name or symbol.
•⁠  ⁠*Data Fetching:* Retrieves one year of daily stock price data using [jugaad-data](https://github.com/vinayak-mehta/jugaad-data).
•⁠  ⁠*Custom Moving Average:* User sets the moving average window (default: 20 days).
•⁠  ⁠*Interactive Plotly Chart:* Visualizes close price, moving average, and daily % change.
•⁠  ⁠*Data Table & Download:* View and export processed data as CSV.
•⁠  ⁠*Responsive UI:* Fullscreen chart toggle, expandable raw data, and helpful messages.
•⁠  ⁠*Efficient Caching:* Uses Streamlit's cache for faster symbol data loading.

---

##  Setup & Installation

1.⁠ ⁠*Clone the repository*
git clone <your-repo-url>
cd <your-project-directory>
text

2.⁠ ⁠*Create and activate a virtual environment*
python -m venv venv
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate
text

3.⁠ ⁠*Install dependencies*
pip install -r requirements.txt
text
	⁠All required packages are listed in ⁠ requirements.txt ⁠ for reproducibility.
