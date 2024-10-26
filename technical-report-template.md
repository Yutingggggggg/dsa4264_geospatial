# Technical Report

**Project: {insert project name}**  
**Members: {insert project members}**  
Last updated on {last updated date}

## Section 1: Context

*In this section, you should explain how this project came about. Retain all relevant details about the project’s history and context, especially if this is a continuation of a previous project.*

*If there are any slide decks or email threads that started before this project, you should include them as well.*
In recent years, the launch of new Mass Rapid Transit (MRT) lines, such as the Downtown Line and the Thomson-East Coast line, has resulted in a decline in the ridership of trunk services. Trunk services are long bus routes that connect different neighbourhoods across Singapore. Relying on trunk services to get to a destination usually takes longer and is generally less predictable. Hence, the Land Transport Authority (LTA) wishes to streamline Singapore's public transport options and encourage commuters to use the new MRT lines, instead of continuing to rely on trunk services.

## Section 2: Scope

### 2.1 Problem

*In this subsection, you should explain what is the key business problem that you are trying to solve through your data science project. You should aim to answer the following questions:*

* *What is the problem that the business unit faces? Be specific about who faces the problem, how frequently it occurs, and how it affects their ability to meet their desired goals.*
The Ministry of Transport's (MOT) Land Division, specifically the Public Transportation team, is in charge of examining the overall planning for public tranportation routes and to find ways to optimise them for cost and coverage. Due to budget constraints, failing to optimise Singapore's bus routes could lead to the team being unable to finance other bus routes in Singapore that better meet the commuters' needs.

* *What is the significance or impact of this problem? Provide tangible metrics that demonstrate the cost of not addressing this problem.*


* *Why is data science / machine learning the appropriate solution to the problem?*

Manually identifying which bus routes have enough "overlap" with MRT lines is imprecise and time-consuming. Data science / machine learning can be used to systematically and efficiently identify which trunk services overlap, and to what extent, with MRT lines. This analysis could also be extended to future lines that are being released, such as the Jurong Region Line.

### 2.2 Success Criteria

*In this subsection, you should explain how you will measure or assess success for your data science project. You need to specify at least 2 business and/or operational goals that will be met if this project is successful. Business goals directly relate to the business’s objectives, such as reduced fraud rates or improved customer satisfaction. Operational goals relate to the system’s needs, such as better reliability, faster operations, etc.*

Success would be identifying at least 2 to 3 routes that can be either entirely removed, or partially rerouted, to better streamline public transportation operations, which would enable the MOT's Public Transportation team to free up funding for 3 proposed bus routes that are needed in response to public demand.

(need to include metrics on how to evaluate whether a route should be re-routed & how a new route is decided)

### 2.3 Assumptions

*In this subsection, you should set out the key assumptions for this data science project that, if changed, will affect the problem statement, success criteria, or feasibility. You do not need to detail out every single assumption if the expected impact is not significant.*

*For example, if we are building an automated fraud detection model, one important assumption may be whether there is enough manpower to review each individual decision before proceeding with it.*

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
* *Collection: What datasets did you use and how are they collected?*
Our datasets are retrieved from LTA Datamall.

* *Cleaning: How did you clean the data? How did you treat outliers or missing values?*
* *Features: What feature engineering did you do? Was anything dropped?*
* *Splitting: How did you split the data between training and test sets?*

### 3.3 Experimental Design

*In this subsection, you should clearly explain the key steps of your model development process, such as:*
* *Algorithms: Which ML algorithms did you choose to experiment with, and why?*
* *Evaluation: Which evaluation metric did you optimise and assess the model on? Why is this the most appropriate?*
* *Training: How did you arrive at the final set of hyperparameters? How did you manage imbalanced data or regularisation?*

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