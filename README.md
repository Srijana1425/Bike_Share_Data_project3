# 🚲 Bikeshare Analysis

## 🌟 Overview
In this project, you'll use Python to explore data related to bike share systems for three major U.S. cities—Chicago, New York City, and Washington. The goal is to import data, compute descriptive statistics, and create an interactive terminal-based script to present these statistics.

## 📂 Datasets
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

## 🚀 Getting Started
1. 📥 Download and unzip the project files.
2. 📦 Install dependencies:
    ```bash
    pip install pandas numpy
    ```
3. 🏃‍♂️ Run the script:
    ```bash
    python bikeshare.py
    ```

## 🛠️ Code Explanation
The main functions in the `bikeshare.py` script include:
- `get_filters()`: Prompts user for city, month, and day.
- `load_data(city, month, day)`: Loads and filters data.
- `time_stats(df)`: Displays common travel times.
- `station_stats(df)`: Shows popular stations and trips.
- `trip_duration_stats(df)`: Provides trip duration statistics.
- `user_stats(df)`: Presents user demographics.
- `display_raw_data(df)`: Allows user to view raw data in chunks.

## 📄 Here is the Code File
`bikeshare.py`

## 🖼️ Output
