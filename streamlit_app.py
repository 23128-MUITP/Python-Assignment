Here's your updated code with the suggested comments added at the appropriate places:

```python
# Import necessary libraries
import pandas as pd  # For data handling
import matplotlib.pyplot as plt  # For static plotting (not used)
import plotly.graph_objs as go  # For interactive plots
from datetime import date  # For date range setup
import os  # For environment variable manipulation
import streamlit as st  # For building the web app UI
from jugaad_data.nse import stock_df  # To fetch historical stock data from NSE

# Set cache directory for jugaad_data (important for hosted environments like Streamlit Cloud)
os.environ["JUGAAD_DATA_DIR"] = "/tmp/jugaad_data_cache"

# Load list of NSE stock symbols and company names
@st.cache_data
def load_symbol_data():
    # Read the NSE equity list CSV from NSE website
    url = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
    df = pd.read_csv(url)
    # Keep only symbol and company name columns
    df = df[["SYMBOL", "NAME OF COMPANY"]]
    # Create a display column combining company name and symbol
    df["DISPLAY"] = df["NAME OF COMPANY"].str.title() + " (" + df["SYMBOL"] + ")"
    # Sort for easier selection in dropdown
    df.sort_values("DISPLAY", inplace=True)
    return df

symbol_df = load_symbol_data()

# Fetch historical stock data and calculate indicators
def get_data(instr, ma):
    # Fetch historical data for selected stock using jugaad_data
    df = stock_df(symbol=instr, from_date=date(2024, 5, 5),
                  to_date=date(2025, 5, 5), series="EQ")
    # Calculate moving average (default 20-day)
    df["MA_20"] = df["CLOSE"].rolling(window=ma).mean()
    # Calculate daily percentage change in closing price
    df["DAILY_PCT_CHANGE"] = df["CLOSE"].pct_change() * 100
    # Round percentage change for display
    df["DAILY_PCT_CHANGE"] = df["DAILY_PCT_CHANGE"].round(2)
    return df

# Create an interactive Plotly chart with price, MA, and daily % change
def plot_interactive(df, symbol, fullscreen=False):
    fig = go.Figure()

    # Line chart for Close price
    fig.add_trace(go.Scatter(x=df["DATE"], y=df["CLOSE"],
                             mode='lines', name='Close Price',
                             line=dict(color='dodgerblue')))
    
    # Dashed line chart for 20-day Moving Average
    fig.add_trace(go.Scatter(x=df["DATE"], y=df["MA_20"],
                             mode='lines', name='20-Day MA',
                             line=dict(color='orange', dash='dash')))

    # Bar chart for daily % change, green for gains, red for losses
    fig.add_trace(go.Bar(x=df["DATE"], y=df["DAILY_PCT_CHANGE"],
                         name='Daily % Change',
                         marker_color=['green' if x >= 0 else 'red' for x in df["DAILY_PCT_CHANGE"]],
                         yaxis='y2', opacity=0.5))

    # Configure chart layout, axes, legends, and interactivity
    fig.update_layout(
        title=f"{symbol} Price & Moving Average with Daily % Change",
        xaxis_title="Date",
        yaxis=dict(title='Close Price / MA'),
        yaxis2=dict(title='Daily % Change', overlaying='y', side='right', showgrid=False),
        legend=dict(x=0, y=1),
        height=800 if fullscreen else 600,
        template='plotly_white',
        hovermode='x unified'
    )

    st.plotly_chart(fig, use_container_width=True)

# === Streamlit App UI ===
# Set wide layout for better chart display
st.set_page_config(layout="wide")

# App title
st.title("📈 Stock Price & MA Viewer")

# Company selector with a default placeholder
company_list = ["Select Company"] + symbol_df["DISPLAY"].tolist()
selected_display = st.selectbox("Search for a stock (by name or symbol):", company_list)

# Proceed only if a company is selected
if selected_display != "Select Company":
    # Extract the stock symbol from the selected display
    symbol = symbol_df[symbol_df["DISPLAY"] == selected_display]["SYMBOL"].values[0]

    # Input for user-defined moving average window
    ma = st.number_input("Enter the length of moving average:", min_value=1, max_value=100, value=20)
    # Toggle for fullscreen chart option
    fullscreen = st.toggle("🖥️ Fullscreen Chart")

    # Generate chart and data only when button is clicked
    if st.button("Generate Chart"):
        # Fetch and sort data
        df = get_data(symbol, ma)
        df.sort_values('DATE', inplace=True)
        
        # Plot chart in Streamlit
        plot_interactive(df, symbol, fullscreen)

        # Expandable section to view raw data
        with st.expander("📋 View Raw Data"):
            st.dataframe(df)

        # Generate downloadable CSV link
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download CSV",
            data=csv,
            file_name=f"{symbol}_data.csv",
            mime='text/csv'
        )
else:
    # Prompt user to select a company if none is chosen
    st.info("Please select a company to continue.")
```

Let me know if you want this code converted into a downloadable `.py` file or need help deploying it on Streamlit Cloud.
