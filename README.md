# Comprehensive Crime Data Analysis Tool

This repository contains a Python-based tool for performing comprehensive analysis on crime datasets. It includes modules for temporal, spatial, demographic, and categorical crime data analysis, utilizing advanced visualization and geospatial mapping techniques.

---

## Features

- **Data Cleaning and Preparation**: Automated data parsing and cleaning for seamless analysis.
- **Temporal Analysis**: Crime distribution across time (hour, day, month, and year).
- **Crime Type Analysis**: Identification of most common crime types and their temporal patterns.
- **Victim Demographics**: Insights into victim age, gender, and descent distributions.
- **Spatial Analysis**: Heatmaps and area-based visualizations to identify high-crime zones.
- **Weapon Usage Analysis**: Analysis of weapon types commonly used in reported crimes.
- **Interactive Heatmaps**: Geospatial mapping using Folium for dynamic exploration of crime hotspots.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Crime-Data-Analysis.git
   cd Crime-Data-Analysis
2.Install the required dependencies:
   ```bash
   pip install -r requirements.txt
```
3.Place the crime dataset in the Datasets folder and ensure the file path matches in the script.py.

## Usage

1. Run the script:
```bash
python script.py
```
2. Analyze outputs:
- **The script generates visualizations for different aspects of crime data.
- **Interactive heatmaps are saved for spatial exploration.
3. Modify configurations:
  - **Update file paths and configurations in script.py as needed.

## Code Overview
script.py
- **Functions:
- -**load_and_clean_data(file_path): Loads and preprocesses the dataset.
- **temporal_analysis(df): Analyzes temporal patterns in crimes.
- **crime_type_analysis(df): Explores most common crime types.
- **victim_analysis(df): Studies victim demographics.
- **location_analysis(df): Maps crimes spatially and analyzes area patterns.
- **weapon_analysis(df): Examines patterns in weapon usage.


Main Script:

Automatically processes the dataset and performs all analyses.
Displays visualizations and statistical summaries.
Example Dataset
Ensure your dataset contains the following columns for optimal performance:

Date Rptd, DATE OCC, TIME OCC, Crm Cd Desc, Vict Age, Vict Sex, Vict Descent, LAT, LON, AREA NAME, Weapon Desc.
Sample data path: Datasets/Crime_Data.csv

Requirements
Python 3.7+
Libraries:
pandas
numpy
matplotlib
seaborn
folium
Outputs
Visualizations:
Crime trends (line plots, bar charts).
Victim demographics (histograms, count plots).
Area analysis (heatmaps, bar charts).
Interactive Maps:
Heatmaps of crime hotspots.
Statistical summaries:
Incident counts, date ranges, missing values.
Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to all contributors and open-source libraries that made this project possible.
