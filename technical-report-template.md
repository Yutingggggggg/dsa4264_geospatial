# Technical Report

**Project: Comprehensive Analysis of Parallel Bus Routes to MRT Lines for Service Optimizations**  
**Members: Choo Jin Yi, Jiya Dutta, Kang Yu Ting, Lian Ko-Shyan, Toh Kai Lin**  
Last updated on 6/11/2024

## Section 1: Context

In recent years, the launch of new Mass Rapid Transit (MRT) lines, including the Downtown Line and Thomson-East Coast Line, has resulted in a decline in ridership for certain trunk bus services — long routes that connect various neighborhoods across Singapore.

This project was initiated to identify bus routes that run closely parallel MRT lines, allowing LTA to prioritize potential adjustments for cost-effectiveness and enhanced commuter experience.

## Section 2: Scope

### 2.1 Problem

The Ministry of Transport’s (MOT) Land Division, specifically the Public Transportation team, is responsible for overseeing the planning and optimization of public transportation routes in Singapore. Due to budget constraints, it’s crucial for the team to ensure that public transport resources are allocated efficiently. However, the introduction of new MRT lines, such as the Downtown Line and Thomson-East Coast Line, has resulted in decreased ridership on certain trunk bus services, which are long bus routes connecting various neighborhoods across Singapore. Some of these services are now underutilized, as commuters prefer the faster and more predictable MRT options.

The challenge facing the Public Transportation team is to identify and streamline bus routes that significantly overlap with MRT lines. Failing to optimize these bus routes will lead to wasted resources, limiting the team's ability to finance new routes that could better serve unmet commuter needs. If left unaddressed, this inefficiency could result in a misallocation of MOT’s limited budget, potentially impacting the overall effectiveness of Singapore’s public transport system.

Data science provides an efficient and systematic solution to identifying route redundancies within Singapore’s complex transport network. Manually analyzing bus and MRT overlaps would be both time-consuming and prone to error. By using data science techniques, we can process large-scale geospatial data to accurately calculate overlap distances within defined buffer zones of MRT lines, allowing us to quantify which bus routes duplicate MRT lines, and to what extent.

This approach not only provides clear, data-driven insights for potential route adjustments but also allows us to incorporate factors like accessibility of alternative routes and commuter convenience into our recommendations. This leads to more balanced, informed decisions that prioritize commuter needs.

Furthermore, data science ensures scalability and adaptability. As Singapore’s MRT network expands with new lines like the Jurong Region and Cross Island Lines, the same data-driven approach can be readily applied to assess overlaps, ensuring that our public transport system remains optimized, cost-effective, and responsive to future commuter demands.

### 2.2 Success Criteria

Success for this data science project will be measured through both business and operational outcomes, aimed at optimizing public transport resources by identifying overlapping bus routes for potential adjustments. Achieving these outcomes will allow the Ministry of Transport's (MOT) Public Transportation team to improve resource allocation, cut costs and meet public demand in underserved areas.

<b>Business Goal</b>: Identify 3 bus routes that significantly overlap with MRT lines for partial reroute or adjustment. This will allow MOT to free up funding and redirect resources.

<b>Operational Goal</b>: Streamline public transport by eliminating redundancy and ensuring that re-routed or adjusted bus services still maintain commuter convenience without creating significant disruption. This will be assessed by:

* <b> Route Overlap Distance </b>: Using geospatial analysis, calculate the overlap distance of each bus route within a 150-meter buffer around MRT lines. Routes with the highest overlap distances will be prioritized for review as they represent potential redundant routes in the public transport network. 

* <b> Alternative Access Feasibility </b>: For each route identified, evaluate the accessibility and convenience of alternative transport options, such as other bus routes or MRT stations. Adjustments will only be recommended if these alternatives are reasonably convenient, minimizing impact on commuter experience.

Meeting these criteria will demonstrate that the project has successfully provided actionable insights for MOT and LTA to optimize Singapore’s public transportation system effectively.


### 2.3 Assumptions

This project is based on several key assumptions, each of which affects the problem definition, success criteria, and feasibility of our analysis. These assumptions include:

* <b> Data Availability and Accuracy </b> : LTA Datamall data on bus routes and Kaggle data on MRT lines provide sufficient accuracy and detail to identify significant overlap. Since we lack access to internal ridership data, our analysis will depend solely on spatial proximity between bus routes and MRT lines as an indicator of redundancy.

* <b> Public Responsiveness to Adjustments </b>: Public will adjust to recommended bus route changes without significant backlash if the adjustments are communicated clearly and effective alternative transport options are available. However, past experiences with route adjustments indicate a risk of public dissatisfaction, which could impact the feasibility of proposed changes.

* <b> Alternative Transport Accessibility </b>: Alternative MRT or bus services are reasonably accessible for routes identified for potential adjustment. Any significant gaps in alternative access would alter the feasibility of rerouting recommendations, as they could reduce commuter convenience.

## Section 3: Methodology

### 3.1 Technical Assumptions


#### 3.1.1 Definition of Key Variables and Terms
   - **Overlap Distance**: Defined as the total length (in meters) of each bus route that falls within a 150-meter buffer zone around MRT lines. This variable quantifies the extent to which a bus route runs parallel to an MRT line.
   - **Buffer Zone**: A 150-meter radius around MRT lines, which we assume sufficiently captures potential redundancies in coverage by nearby bus routes. The [Land Transport Master Plan 2040 ](https://www.lta.gov.sg/content/ltagov/en/who_we_are/our_work/land_transport_master_plan_2040.html)(LTMP 2040) focuses on creating a more integrated and sustainable transport system. Although specific buffer zone distances aren't always detailed, the plan emphasizes enhancing public transport connectivity and reducing travel times, which aligns with our use of the buffer zone. 
   - **Redundant Route**: Defined as any portion of a bus route that overlaps significantly with an MRT line within the buffer zone, making it a candidate for potential rerouting.

#### 3.1.2 Features Available / Unavailable

The features that were available to us were geospatial data on MRT line routes and stations, sourced from LTA DataMall and Kaggle, and bus stop locations for each bus route, also sourced from LTA DataMall.
There were also some features that we needed but were unavailable to us. These features include specific path data for each bus route, as the LTA DataMall only provided bus stop locations as point coordinates, but did not provide the exact routes connecting the bus stops. Also, we lacked ridership data specific to each bus route, which would have allowed for a more nuanced understanding of demand and usage patterns. Lastly, data on real-time traffic and congestion data, which we could have used to conduct a deeper analysis into route efficiency and commuter travel time, was also unavailable.

#### 3.1.3 Computational Resources

The analysis was conducted on a standard CPU-based setup, which limited the processing power available for large-scale geospatial computations. Also, limited RAM availability constrained the size of datasets that could be processed simultaneously, so we had to narrow down the bus routes for further and more detailed analysis that takes a longer time to run. The software tools we used were GIS (Geographic Information System) libraries in Python, such as GeoPandas, for spatial calculations, and these libraries were constrained by available local processing power.

#### 3.1.4 Key Hypotheses of Interest

Our first hypothesis is that bus routes with high overlap distances are likely redundant with MRT lines and may be candidates for rerouting or partial removal. This seemed plausible as MRT lines generally run faster than buses, have greater capacity and arrive at more predictable timings, so commuters are likely to prefer taking MRT to buses when possible to minimise their travel time.

Our second hypothesis is that a buffer zone of 150 meters is adequate for our current purposes to capture meaningful overlap that would impact commuter convenience and route redundancy. We chose a buffer zone of 150 meters as according to a statement made by the Minister for Transport, the median distance between an MRT station exit and the bus stop is 40 metres for the newer Downtown and Thomson-East Coast Lines. However, we had to be careful about being too strict to ensure that we do not exclude bus stops that may be further than 40 metres, especially for the older MRT lines. Also, as our analysis used the centroids of the MRT stations and not the specific exit locations, we thought it was reasonable to increase the buffer zone to account for this distance from the center of the MRT station to the exits. We also made sure not to be too generous, so as to avoid including bus stops that were not actually parallel to the MRT line. 

Our last hypothesis is that alternative routes or transport options are available for redundant bus routes, and work equally well to serve commuters' needs, which minimizes the impact on commuter access if these routes are removed or rerouted. While the redundant bus routes run parallel to MRT lines, giving commuters an alternative way to get to the MRT stations along the route, commuters may need access to bus stops in between MRT stations, and some commuters might simply prefer taking buses to MRT. Thus, we thought it would be important to ensure that there are alternative bus routes for the redundant bus routes before we choose to remove them.

#### 3.1.5 Data Quality and Limitations

While the data from LTA DataMall was detailed, it had several limitations. 

Firstly, while the data from LTA DataMall and Kaggle provided comprehensive route details, it lacked specific path data for bus routes. Since only bus stop locations were available as points, we approximated each bus route by connecting sequential bus stops in a straight line.

Secondly, the MRT datasets from LTA DataMall are as of July 2024. They do not account for temporary route diversions or construction, which could affect the real-world application of the analysis.

Lastly, geospatial precision of the data is assumed to be high, but any minor inaccuracies in the mapping of routes may slightly affect the calculated overlap distance.

### 3.2 Data


#### **3.2.1 Collection** 

Our datasets are retrieved from the Land Transport Authority (LTA) Datamall API, utilising the following endpoints:

* `Bus Services`: Retrieved detailed service information for all buses currently in operation.
* `Bus Routes`: Retrieved detailed route information for all services currently in operation.
* `Bus Stops`: Retrieved detailed information for all bus stops currently being serviced by buses.
* `Train Station`: Retrieved a point representation to indicate the location of the MRT station.
* `Train Station Exits`: Retrieved a point representation to indicate the location of a train station exit point.


Furthermore, we employed [Singapore MRT Map in Folium](https://www.kaggle.com/code/lzytim/singapore-mrt-map-in-folium/notebook) by Timothy Lim on Kaggle, which contains a complete map of Singapore's MRT network.


#### **3.2.2 Cleaning** 

Firstly, we had to add the new Thomson-East Coast Line stations to the dataset from Kaggle. As the Kaggle dataset on MRT stations was not updated to include the recently opened stations on the Thomson-East Coast line (`new_brown_line`), we manually added these missing stations to the dataset, so the visualisation of the MRT routes and the analysis of the overlap distance between bus routes and MRT lines will be more complete.

Secondly, as we were conducting geospatial analysis, we converted the `Bus Stops` and `Bus Routes` datasets into geospatial data frames (`bus_stops_gdf` and `bus_routes_gdf`) using GeoPandas, defining geometries based on longitude and latitude for each stop. For MRT station exits, we read in spatial data from the `TrainStationExit` shapefile as `train_station_exits_gdf`, allowing us to map out all station exit points.

Thirdly, to ensure accuracy in distance calculations, we reprojected the bus routes and train station geodataframes into a common coordinate reference system (CRS), EPSG:3857, suitable for metric distance calculations. For our visualisation, we utilised the EPSG:4326 CRS instead, which allowed us to accurately plot our bus and MRT routes onto folium maps.

#### **3.2.3 Features** 

* `bus_route_combined` : We aggregated bus stops into continuous route lines using the `LineString` function. We grouped the bus stops based on their `ServiceNo` (bus service number) and `Direction` (route direction) attributes to ensure each route was represented as a single, uninterrupted LineString geometry. 

* `mrt_stations_gdf_3857` : GeoDataFrame containing the locations and attributes of MRT stations transformed to the EPSG:3857 coordinate reference system. 

* `mrt_stations_3857_2` : We merged the Kaggle dataset with the MRT stations dataset from LTA Datamall, as the Kaggle dataset contained information on the lines that the MRT stations belonged to, and the order of the stations along the line, which we used to supplement the data from LTA Datamall containing the geographic information on the locations of the MRT stations.

#### **3.2.4 Data Analysis** 

For our preliminary data analysis, we wanted to get a sense of which bus stops were close to MRT station exits. To do so, we computed the distance from each bus stop to all MRT station exits using GeoPandas distance calculations. We then identified which was the nearest MRT station exit to each bus stop and what the distance between them was, in order to capture each bus stop's proximity to the MRT network and provide insight into potential redundancies between bus and MRT routes. This calculation was saved in the `nearest_train_stations` dataframe in the `overlap_distance.ipynb` file. 

After identifying the closest MRT station exit to each bus stop, we filtered out the bus stops that have a distance above 150 meters to the nearest MRT station exit. The remaining bus stops were flagged as MRT-proximal, allowing for a refined analysis of routes with the greatest overlap. This analysis was saved in the `bus_stops_with_mrt` dataframe in the `overlap_distance.ipynb` file.

### 3.3 Experimental Design

*In this subsection, you should clearly explain the key steps of your model development process, such as:*
* *Algorithms: Which ML algorithms did you choose to experiment with, and why?*
* *Evaluation: Which evaluation metric did you optimise and assess the model on? Why is this the most appropriate?*
* *Training: How did you arrive at the final set of hyperparameters? How did you manage imbalanced data or regularisation?*

#### Finding overlap distance between bus routes and MRT lines

To identify which bus routes run parallel to MRT lines, we constructed an algorithm to find the length of the bus route that overlaps with a buffered region of each MRT line. To explain our algorithm further, we will use the Thomson-East Coast Line as an example

First, we constructed a LineString object from the centroid coordinates of the MRT stations along the Thomson-East Coast Line (`TEL_route`), to represent the overall route of the line. Next, we added a buffer of 150 metres to the line, making it a polygon (`buffered_TEL`). After getting the polygon, we found the distance of each bus route that falls inside this polygon, which we took as the overlap distance between the bus routes and the Thomson-East Coast line, and saved the overlap distances for each bus route in the `overlap_distance_TEL` dataframe. From this dataframe, we filtered out the bus routes that do not overlap with the `buffered_TEL` polygon at all, and kept only the routes that had some overlap, sorting the results in descending order. This filtered data was saved in the `bus_routes_overlap` dataframe.

We repeated this process for all the other MRT lines (Downtown Line, North-East Line, North-South Line, East-West Line and Circle Line). In the end, we got the top 5 bus routes with the highest overlap distance with MRT lines and the MRT line that they overlap the most with from the `bus_routes_overlap` dataframe, which were 67, 36, 63, 23 and 2. 

| Bus Route | MRT Line | Overlap Distance (m) |
|-----------|-----------------------|---------------------|
| Bus 67    | Downtown Line | 14747.34           |
| Bus 36  | Thomson-East Coast Line | 13593.10               | 
| Bus 63  | East-West Line | 	12987.28             | 
| Bus 23  | Downtown Line | 	12799.11             | 
| Bus 2  | East-West Line | 	12440.27            | 

#### Finding alternative bus routes to further narrow down which bus routes to remove

After we narrowed down to the top 5 bus routes that have the highest overlap distance with MRT lines (target bus routes), we conducted further analysis into whether there are alternative bus routes for each of them. To do so, we tried to find the top 3 bus routes that overlapped with each of the target bus routes to see how much of the target bus route can be replicated by other buses. To explain the algorithm for this analysis, we will first focus on bus route 67.

We extracted the route of Bus 67 from the `bus_routes_combined` dataframe and named it `route_67_line`. Next, we converted the `bus_routes_combined` dataframe into a geodataframe with a CRS of EPSG:3857 (`bus_routes_combined_gdf`). We removed bus 67 and and all the variants of bus 67 from the geodataframe (`bus_routes_combined_gdf_67`). After that, we constructed a loop with 3 iterations. For each iteration, we run through all the bus routes in the `bus_routes_combined_gdf_67` geodataframe to find out the length of intersection between the bus routes and the route of Bus 67, which is the distance where the bus routes exactly overlap with Bus 67. We then picked out the bus route with the highest intersection length (`max_overlap_route`), and the line of the intersection between `max_overlap_route` and Bus 67 (`max_overlap`). We removed this line of intersection (`max_overlap`) from the Bus 67 route before starting the next iteration. In each progressive iteration, we find the top bus route that overlaps with the remaining sections of Bus 67 that did not overlap with the bus routes found in previous iterations. This way, we can find out to what extent different parts of the route of Bus 67 can be replicated with 3 alternative bus routes. The top 3 bus routes and their respective lengths of overlap were saved in the `overlap_routes` dataframe.

After finding the top 3 routes that overlapped the most with Bus 67, we found the bus stops that lie along the line where they overlap. These bus stops would be the bus stops where both Bus 67 and the overlapping bus route stop at. This was mainly for visualisation and validation purposes.

This process of finding alternative bus routes was repeated for each of the other 4 target bus routes. 

These were the results we found.



## Section 4: Findings

### 4.1 Results

### Summary Table of Overlap Distance with MRT Lines

| Bus Route | MRT Line | Overlap Distance (m) | Recommended Action | Alternative Route Availability      |
|-----------|---------------|-----------------------|---------------------|-------------------------------------|
| Bus 67    | Downtown Line | 14747.34           | Remove Segment from Choa Chu Kang to Newton    | MRT Downtown Line, Bus 170          |
| Bus 36  | Thomson-East Coast Line | 13593.10               | Retain             | MRT Thomson-East Coast Line       |
| Bus 63  | East-West Line | 	12987.28             | Remove Entirely   | MRT East-West Line, Bus 64 & 518               |
| Bus 23  | Downtown Line | 	12799.11             | Retain   | MRT Downtown Line               |
| Bus 2  | East-West Line | 	12440.27            | Remove Segment from Kampong Bahru to Tanah Merah  | MRT East-West Line, Bus 12 & 67               |


### Summary Table of Alternative Bus Routes

- **Bus 67 (total length: 31083.48 m)**

| Bus Route | Intersection Length (m) |
|-----------|-----------------------|
| Bus 170    | 14543.08         |
| Bus 2  | 7680.61               | 
| Bus 28  | 	2620.83             | 

Remaining un-overlapped length : 6238.97 m

- **Bus 36 (total length: 44666.59 m)**

| Bus Route | Intersection Length (m) |
|-----------|-----------------------|
| Bus 111    | 7028.45         |
| Bus 110  | 5088.40               | 
| Bus 47  | 	3949.24             | 

Remaining un-overlapped length : 29481.32 m

- **Bus 63 (total length: 33391.59 m)**

| Bus Route | Intersection Length (m) |
|-----------|-----------------------|
| Bus 51    |  7008.85         |

Remaining un-overlapped length : 26947.51 m

- **Bus 23 (total length: 27880.31 m)**

| Bus Route | Intersection Length (m) |
|-----------|-----------------------|
| Bus 518    | 7088.15         |
| Bus 64  | 5537.79               | 
| Bus 67  | 	982.75             | 

Remaining un-overlapped length : 14271.61 m

- **Bus 2 (total length: 24346.31 m)**

| Bus Route | Intersection Length (m) |
|-----------|-----------------------|
| Bus 67    | 7717.78         |
| Bus 9  | 4355.55               | 
| Bus 12  | 	4316.64             | 

Remaining un-overlapped length : 7956.34 m


Bus 67 has a significant overlap with the Downtown Line. For efficiency, we recommend removing a segment of this route, as it’s well-covered by both MRT and Bus 170. Bus 36, although it has some overlap, is essential to retain as it provides direct access to the airport, a critical route for travelers. Also, there are no alternative bus routes that cover a significant portion of Bus 36, so commuters will be very inconvenienced with having to make many transfers if they want to travel by bus along the Bus 36 route. Bus 63 shows considerable overlap with the East-West Line. Although from our algorithm, it appears that there are no alternative bus routes for Bus 63, upon further checking, we found that there are multiple buses that follow very similar routes even though they do not replicate the route exactly. Thus, due to ample alternative coverage, we recommend removing it entirely to streamline the network. Bus 23 also lacks good alternative options of buses, and the top 3 bus routes that overlap Bus 23 do not intersect much with each other, making it very troublesome for commuters to transfer. Bus 2 overlaps heavily with the East-West Line, and has alternative bus routes that overlap a significant portion of the route from Kampong Bahru Terminal to Tanah Merah Station, and connect with each other. Thus, as commuters have many alternative MRT and bus options, we recommend removing a segment of Bus 2.

### 4.2 Discussion

#### Business Value of Results

The overlap analysis between bus routes and MRT lines provides actionable insights to optimize the public transport network. By removing redundant segments of Bus 67, 63 and 2,  we can achieve 3 goals. Firstly, as reducing redundant segments lowers operational costs, allowing resources to be reallocated to other routes or underserved areas, it will result in cost savings. Secondly, streamlining routes to avoid duplication with MRT lines enhances the overall transport network, enabling buses to focus on areas outside MRT coverage, resulting in improved network efficiency. Lastly, by selectively retaining key routes (e.g., Bus 170) that serve stops between MRT stations, we maintain accessibility for commuters without unnecessary redundancy, allowing MOT to align with commuter needs.

This data-driven approach addresses the business goal of optimizing the network in a cost-effective and efficient way.

#### Key Issues

We also focused on some key issues when developing our approach. Firstly, we made sure that our results were interpretable. The overlap distance metric provides a clear, quantifiable basis for route adjustments, making the findings easy to communicate and justify. Secondly, we wanted to ensure fairness to commuters when removing or rerouting bus routes, so adjustments are made to avoid disproportionately impacting areas with limited transit alternatives, ensuring fair access to public transport.
Thirdly, we focused on the deployability of our recommendations. Route changes require clear public communication to minimize disruption, with plans for periodic reviews to adapt to future MRT developments and commuter needs.

### 4.3 Recommendations

#### Next Steps

We recommend implementing adjustments to Bus 67 and potentially Bus 63 to reduce redundancy with MRT lines. These changes should be communicated clearly to commuters to ensure a smooth transition.

#### Deployment Considerations

Deploying these changes involves:
- **Updating Public Transport Apps**: Ensure all bus route updates are reflected in apps like MyTransport.SG and Google Maps to avoid confusion among users.
- **Public Communication**: Inform commuters about the route changes through announcements in public transport apps, signage at affected bus stops, and media channels.

#### Additional Recommendations

In the future, we would also want to extend this analysis to new and future MRT lines.  As the Cross Island Line and Jurong Region Line are introduced, apply this overlap analysis to identify additional redundant bus routes and optimize the network. Regular reviews should be conducted to keep the public transport network aligned with new developments and evolving commuter patterns.

Also, future analyses would benefit from more granular data, such as detailed bus paths and ridership statistics, to improve overlap assessment and better understand commuter demand.
