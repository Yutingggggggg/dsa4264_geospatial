# DSA4264 Sense-making Case Analysis: Public Policy and Society

This project aims to perform a comprehensive geospatial analysis of bus routes that run parallel to MRT lines.

## Problem 1: Geospatial

The geospatial component of this project involves analyzing the spatial overlap between bus routes and MRT lines to identify redundancies and potential service optimizations.

## Static Datasets
1. Download the static datasets from LTA Datamall: 'TrainStation' & 'TrainStationExit'
2. Download the static dataset from Kaggle: [MRT Stations](https://www.kaggle.com/code/lzytim/singapore-mrt-map-in-folium/input?select=mrt_stations)

## Setting Up the Environment

To set up your environment:

1. Run the following command to install all required dependencies:
   pip install -r requirements.txt
2. Set your API key as an environment variable:
   - For Unix-like systems (macOS & LINUX):
     ```bash
     export LTA_API_KEY='your_api_key'
     ```
   - For Windows:
     ```cmd
     setx LTA_API_KEY 'your_api_key'
     ```
   2.1 If the above does not work for Unix-like systems, run
   ```
   nano ~/.zshrc
   ```
   and set the environment variable:
   ```bash
   export LTA_API_KEY='your_api_key'
   ```


### Workflow

1. **Accessing Datasets**:
   - Open and run the `lta_datamall_data.ipynb` notebook located in the `workingfiles` directory.
   - This step retrieves data from the LTA Datamall API, and processes and cleans the raw data obtained.

2. **Overlap Distance Calculation**:
   - Run the `overlap_distance.ipynb` notebook.
   - This script calculates the overlap distances between bus routes and MRT stations to identify bus routes that can be removed or re-routed.

3. **Visualization**:
   - Execute the `visualisation.ipynb` notebook.
   - This will provide interactive, visual representation based on the overlap distances of the bus and MRT routes, aiding in the decision-making process regarding bus route adjustments.

