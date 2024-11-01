# Technical Report

**Project: Comprehensive Analysis of Parallel Bus Routes to MRT Lines for Service Optimizations**  
**Members: Jiya, Ko-shyan, Choo Jin Yi, Kang Yu Ting, Kai Lin**  
Last updated on 1/11/2024

## Section 1: Context

*In this section, you should explain how this project came about. Retain all relevant details about the project’s history and context, especially if this is a continuation of a previous project.*

*If there are any slide decks or email threads that started before this project, you should include them as well.*

In recent years, the launch of new Mass Rapid Transit (MRT) lines, including the Downtown Line and Thomson-East Coast Line, has resulted in a decline in ridership for certain trunk bus services—long routes that connect various neighborhoods across Singapore. These trunk services tend to be slower and less predictable than MRT travel. To improve efficiency and optimize resources, the Land Transport Authority (LTA) is seeking to streamline Singapore's public transport options by encouraging commuters to transition to these new MRT lines instead of relying on overlapping bus routes. This project was initiated to identify bus routes that closely parallel MRT lines, allowing LTA to prioritize potential adjustments for cost-effectiveness and enhanced commuter experience.

## Section 2: Scope

### 2.1 Problem

*In this subsection, you should explain what is the key business problem that you are trying to solve through your data science project. You should aim to answer the following questions:*

* *What is the problem that the business unit faces? Be specific about who faces the problem, how frequently it occurs, and how it affects their ability to meet their desired goals.*

The Ministry of Transport’s (MOT) Land Division, specifically the Public Transportation team, is responsible for overseeing the planning and optimization of public transportation routes in Singapore. Due to budget constraints, it’s crucial for the team to ensure that public transport resources are allocated efficiently. However, the introduction of new MRT lines, such as the Downtown Line and Thomson-East Coast Line, has resulted in decreased ridership on certain trunk bus services, which are long bus routes connecting various neighborhoods across Singapore. These services are now underutilized, as commuters prefer the faster and more predictable MRT options.


* *What is the significance or impact of this problem? Provide tangible metrics that demonstrate the cost of not addressing this problem.*

The challenge facing the Public Transportation team is to identify and streamline bus routes that significantly overlap with MRT lines. Failing to optimize these bus routes will lead to wasted resources, limiting the team's ability to finance new routes that could better serve unmet commuter needs. If left unaddressed, this inefficiency could result in a misallocation of MOT’s limited budget, potentially impacting the overall effectiveness of Singapore’s public transport system.


* *Why is data science / machine learning the appropriate solution to the problem?*

Data science offers a systematic and efficient solution to this problem. Manually identifying overlapping routes is imprecise and time-consuming, whereas data science enables us to analyze large-scale route data and quantify the extent of overlap between bus and MRT services. By leveraging data science techniques, we can rapidly identify routes worth reviewing for potential adjustments. This approach is scalable and can also be applied to assess future MRT lines, such as the Jurong Region and Cross Island Line, ensuring that the public transport network remains cost-effective and responsive to commuter needs.


### 2.2 Success Criteria

*In this subsection, you should explain how you will measure or assess success for your data science project. You need to specify at least 2 business and/or operational goals that will be met if this project is successful. Business goals directly relate to the business’s objectives, such as reduced fraud rates or improved customer satisfaction. Operational goals relate to the system’s needs, such as better reliability, faster operations, etc.*

*(need to include metrics on how to evaluate whether a route should be re-routed & how a new route is decided)*

Success for this data science project will be measured through both business and operational outcomes, aimed at optimizing public transport resources by identifying overlapping bus routes for potential adjustments. Achieving these outcomes will allow the Ministry of Transport's (MOT) Public Transportation team to improve resource allocation and meet public demand in underserved areas.

<b>Business Goal</b>: Identify 2 to 3 bus routes with significant overlap with MRT lines that can be partially rerouted or adjusted. This will allow MOT to free up funding and redirect resources toward implementing 3 proposed bus routes in areas with unmet commuter demand.

<b>Operational Goal</b>: Streamline public transport by eliminating redundancy and ensuring that re-routed or adjusted bus services still maintain commuter convenience without creating significant disruption. This will be assessed by:

* <b> Route Overlap Distance </b>: Using geospatial analysis, calculate the overlap distance of each bus route within a 150-meter buffer around MRT lines. Routes with the highest overlap distances will be prioritized for review as they represent the most redundant services.

* <b> Alternative Access Feasibility </b>: For each route identified, evaluate the accessibility and convenience of alternative transport options, such as other bus routes or MRT stations. Adjustments will only be recommended if these alternatives are reasonably convenient, minimizing impact on commuter experience.

Meeting these criteria will demonstrate that the project has successfully provided actionable insights for MOT and LTA to optimize Singapore’s public transportation system effectively.


### 2.3 Assumptions

*In this subsection, you should set out the key assumptions for this data science project that, if changed, will affect the problem statement, success criteria, or feasibility. You do not need to detail out every single assumption if the expected impact is not significant.*

*For example, if we are building an automated fraud detection model, one important assumption may be whether there is enough manpower to review each individual decision before proceeding with it.*

This project is based on several key assumptions, each of which affects the problem definition, success criteria, and feasibility of our analysis. These assumptions include:

* <b> Data Availability and Accuracy </b> : LTA Datamall data on bus routes and Kaggle data on MRT lines provide sufficient accuracy and detail to identify significant overlap. Since we lack access to internal ridership data, our analysis will depend solely on spatial proximity between bus routes and MRT lines as an indicator of redundancy.

* <b> Public Responsiveness to Adjustments </b>: Public will adjust to recommended bus route changes without significant backlash if the adjustments are communicated clearly and effective alternative transport options are available. However, past experiences with route adjustments indicate a risk of public dissatisfaction, which could impact the feasibility of proposed changes.

* <b> Alternative Transport Accessibility </b>: Alternative MRT or bus services are reasonably accessible for routes identified for potential adjustment. Any significant gaps in alternative access would alter the feasibility of rerouting recommendations, as they could reduce commuter convenience.

## Section 3: Methodology

### 3.1 Technical Assumptions

*In this subsection, you should set out the assumptions that are directly related to your model development process. Some general categories include:*
* *How to define certain terms as variables*
* *What features are available / not available*
* *What kind of computational resources are available to you (ie on-premise vs cloud, GPU vs CPU, RAM availability)*
* *What the key hypotheses of interest are*
* *What the data quality is like (especially if incomplete / unreliable)*

### 3.2 Data

*In this subsection, you should provide a clear and detailed explanation of how your data is collected, processed, and used. Some specific parts you should explain are:*

#### **3.2.1 Collection** 
(What datasets did you use and how are they collected?)

Our datasets are retrieved from the Land Transport Authority (LTA) Datamall API, utilising the following endpoints:

* `Bus Services`: Retrieved detailed service information for all buses currently in operation.
* `Bus Routes`: Retrieved detailed route information for all services currently in operation.
* `Bus Stops`: Retrieved detailed information for all bus stops currently being serviced by buses.
* `Train Station`: Retrieved a point representation to indicate the location of the MRT station.
* `Train Station Exits`: Retrieved a point representation to indicate the location of a train station exit point.


#### **3.2.2 Cleaning** 
How did you clean the data? How did you treat outliers or missing values?

- **Geospatial Transformation:** We converted the `Bus Stops` and `Bus Routes` datasets into geospatial data frames (`bus_stops_gdf` and `bus_routes_gdf`) using GeoPandas, defining geometries based on longitude and latitude for each stop. For MRT station exits, we read in spatial data from the `TrainStationExit` shapefile as `train_station_exits_gdf`, allowing us to map out all station exit points.

- **Coordinate System Alignment:** To ensure accuracy in distance calculations, we transformed the bus routes and train station geodataframes into a common coordinate reference system (CRS), EPSG:3857, suitable for metric distance calculations.

#### **3.2.3 Features** 
What feature engineering did you do? Was anything dropped?

* `bus_route_combined` : We aggregated bus stops into continuous route lines using the LineString function. We grouped the bus stops based on their ServiceNo (bus service number) and Direction (route direction) attributes to ensure each route was represented as a single, uninterrupted geometry. 

* `mrt_stations_gdf_3857` : GeoDataFrame containing the locations and attributes of MRT stations transformed to the EPSG:3857 coordinate reference system. [KIV]

* `mrt_stations_3857_2` : Contains `Line` column for MRT stations, which can be used for filtering. [KIV]

#### **3.2.4 Splitting** [might consider deleting this section]
How did you split the data between training and test sets?

#### **3.2.4 Data Analysis** 

* `nearest_train_stations` **Nearest MRT Station Calculation** : 
For each bus stop, the distance to all MRT station exits was computed using GeoPandas distance calculations. By identifying the nearest MRT station for each stop, we captured each bus stop’s proximity to the MRT network, providing insight into potential redundancies between bus and MRT routes.

* `bus_stops_with_mrt` : Bus stops within a 150-meter radius of any MRT station exit were selected, identifying the areas where bus routes closely parallel MRT lines. These bus stops were flagged as MRT-proximal, allowing for a refined analysis of routes with the greatest overlap.

### 3.3 Experimental Design

*In this subsection, you should clearly explain the key steps of your model development process, such as:*
* *Algorithms: Which ML algorithms did you choose to experiment with, and why?*
* *Evaluation: Which evaluation metric did you optimise and assess the model on? Why is this the most appropriate?*
* *Training: How did you arrive at the final set of hyperparameters? How did you manage imbalanced data or regularisation?*

#### **Overlap Distance Calculation with MRT Stations**


`brown_line_route` : LineString object is constructed from the centroid coordinates of the brown line stations, representing the overall route of the Thomson-East Coast Line.

`buffered_brown_line` : A buffer of 100 meters is applied to the    `brown_line_route` which broadens the line for intersection analysis with bus routes.

`overlap_distance_brown`: GeoDataFrame that contains a list of overlap distances converted from `overlap_distance_output_brown`, which calculates the intersection between the buffered brown line and each bus route geometry. The result includes bus service number, direction, overlap distance, MRT line name, and intersection geometry.

`bus_routes_overlap`: GeoDataFrame which include only those bus routes with a positive overlap distance with the brown line, sorting the results in descending order based on the overlap distance.

We did the same for the other MRT lines such as Downtown Line, North-East Line, East-West Line, Circle Line and North-South Line.

## Section 4: Findings

### 4.1 Results

*In this subsection, you should report the results from your experiments in a summary table, keeping only the most relevant results for your experiment (ie your best model, and two or three other options which you explored). You should also briefly explain the summary table and highlight key results.*

*Interpretability methods like LIME or SHAP should also be reported here, using the appropriate tables or charts.*

### 4.2 Discussion

*In this subsection, you should discuss what the results mean for the business user – specifically how the technical metrics translate into business value and costs, and whether this has sufficiently addressed the business problem.*

*You should also discuss or highlight other important issues like interpretability, fairness, and deployability.*

### 4.3 Recommendations

*In this subsection, you should highlight your recommendations for what to do next. For most projects, what to do next is either to deploy the model into production or to close off this project and move on to something else. Reasoning about this involves understanding the business value, and the potential IT costs of deploying and integrating the model.*

*Other things you can recommend would typically relate to data quality and availability, or other areas of experimentation that you did not have time or resources to do this time round.*
