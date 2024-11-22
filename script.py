import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import folium
from folium.plugins import HeatMap
import calendar

# Define the file path
FILE_PATH = "Datasets\Crime_Data.csv"

def load_and_clean_data(file_path):
    """Load and perform initial data cleaning"""
    print("Loading data from:", file_path)
    try:
        df = pd.read_csv(file_path)
        # Convert date columns to datetime
        df['Date Rptd'] = pd.to_datetime(df['Date Rptd'], errors='coerce')
        df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], errors='coerce')
        # Calculate reporting delay
        df['Reporting_Delay'] = (df['Date Rptd'] - df['DATE OCC']).dt.days
    except Exception as e:
        print("Error loading or cleaning data:", str(e))
    return df

def temporal_analysis(df):
    """Analyze temporal patterns in crime data"""
    try:
        df['Year'] = df['DATE OCC'].dt.year
        df['Month'] = df['DATE OCC'].dt.month
        df['Day'] = df['DATE OCC'].dt.day
        df['Hour'] = pd.to_datetime(df['TIME OCC'], format='%H%M', errors='coerce').dt.hour
        df['DayOfWeek'] = df['DATE OCC'].dt.day_name()

        plt.figure(figsize=(15, 10))

        # Crimes by hour
        plt.subplot(2, 2, 1)
        sns.histplot(data=df, x='Hour', bins=24)
        plt.title('Crime Distribution by Hour')

        # Crimes by day of week
        plt.subplot(2, 2, 2)
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        sns.countplot(data=df, x='DayOfWeek', order=day_order)
        plt.xticks(rotation=45)
        plt.title('Crime Distribution by Day of Week')

        # Crimes by month
        plt.subplot(2, 2, 3)
        monthly_crimes = df['Month'].value_counts().sort_index()
        monthly_crimes.index = [calendar.month_abbr[m] for m in monthly_crimes.index]
        monthly_crimes.plot(kind='bar')
        plt.title('Crime Distribution by Month')

        # Trend over years
        plt.subplot(2, 2, 4)
        yearly_crimes = df['Year'].value_counts().sort_index()
        yearly_crimes.plot(kind='line', marker='o')
        plt.title('Crime Trend Over Years')

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error in temporal analysis:", str(e))

def crime_type_analysis(df):
    """Analyze crime types and patterns"""
    try:
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, y='Crm Cd Desc', order=df['Crm Cd Desc'].value_counts().iloc[:10].index)
        plt.title('Top 10 Most Common Crime Types')
        plt.show()

        # Crime type by time of day heatmap
        crime_hour_pivot = pd.crosstab(df['Hour'], df['Crm Cd Desc'])
        plt.figure(figsize=(15, 8))
        sns.heatmap(crime_hour_pivot.iloc[:, :10], cmap='YlOrRd')
        plt.title('Crime Types by Hour of Day')
        plt.show()

    except Exception as e:
        print("Error in crime type analysis:", str(e))

def victim_analysis(df):
    """Analyze victim demographics"""
    try:
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        # Age distribution
        sns.histplot(data=df, x='Vict Age', bins=50, ax=axes[0])
        axes[0].set_title('Victim Age Distribution')

        # Gender distribution
        sns.countplot(data=df, x='Vict Sex', ax=axes[1])
        axes[1].set_title('Victim Gender Distribution')

        # Descent distribution
        sns.countplot(data=df, x='Vict Descent', ax=axes[2])
        axes[2].set_title('Victim Descent Distribution')
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error in victim analysis:", str(e))

def location_analysis(df):
    """Analyze spatial patterns"""
    try:
        # Create a base map centered on the mean coordinates
        base_map = folium.Map(
            location=[df['LAT'].mean(), df['LON'].mean()],
            zoom_start=11
        )

        # Create a heatmap layer
        heat_data = df[['LAT', 'LON']].dropna().values.tolist()
        HeatMap(heat_data).add_to(base_map)

        # Area-based analysis
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, y='AREA NAME', order=df['AREA NAME'].value_counts().index)
        plt.title('Crime Distribution by Area')
        plt.show()

        return base_map

    except Exception as e:
        print("Error in location analysis:", str(e))
        return None

def weapon_analysis(df):
    """Analyze weapon usage patterns"""
    try:
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, y='Weapon Desc',
                    order=df['Weapon Desc'].value_counts().iloc[:10].index)
        plt.title('Top 10 Most Common Weapons Used')
        plt.show()

    except Exception as e:
        print("Error in weapon analysis:", str(e))

# Main execution
if __name__ == "__main__":
    try:
        print("Starting analysis...")
        # Load and clean data
        df = load_and_clean_data(FILE_PATH)

        # Generate summary statistics
        print("\nDataset Summary:")
        print(f"Total number of incidents: {len(df)}")
        print(f"Date range: {df['DATE OCC'].min()} to {df['DATE OCC'].max()}")
        print("\nMissing values:")
        print(df.isnull().sum())

        # Run all analyses
        # crime type gives top 10 crime type    victim gives age gender dist by area given on location
        
        temporal_analysis(df)
        crime_type_analysis(df)
        victim_analysis(df)
        location_analysis(df)
        weapon_analysis(df)

        print("\nAnalysis completed successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
