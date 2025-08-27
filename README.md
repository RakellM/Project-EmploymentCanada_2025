# Project: Employment Canada 2025

The Veteran's Dilemma: Navigating the New Data Talent Market

**Core Question**: What specific skills define high-demand, modern data roles in Ontario, and how can veterans bridge the gap?

**The Public**:
- The Industry Veteran: Experienced professionals (5-15+ years) who need to understand which modern skills (Python, Cloud, ML) are critical to learn to remain competitive and avoid obsolescence.
- Corporate Strategy & HR: Companies that must decide to either retrain their existing valuable workforce or engage in costly and competitive external hiring for new talent.

**The Proposed Solution**:
A strategic analysis that moves beyond job counts to skill mapping.
- _Market Diagnosis_: Identify high-growth industries for data talent in Ontario (Tech, Finance, etc.).
- _Skill Decoding_: Analyze hundreds of job descriptions to extract the key technical and soft skills required for these roles.
- _The Gap Analysis_: Contrast the skills demanded in the market with the traditional skill sets of veterans to identify priority learning areas.

**Final Deliverable**: A clear, actionable list of the most valuable skill "bundles" for veterans to target their professional development.

**Technical Approach & Feasibility**:
Data Strategy:
- _Demand Signal_: Manual collection of job postings for data roles in Ontario, tagged by industry.
- _Skill Data_: Text analysis of these postings to create a binary matrix of required skills (Python, SQL, Cloud, Power BI, etc.).
- _Context_: Augmented with StatCan data on industry health and wages.

Modeling Suite:
- _k-Means Clustering_: To group jobs into natural categories (e.g., "Modern Data Engineer" vs. "Traditional Business Analyst") based on their skill profiles.
- _Regression_: To identify which skills are most predictive of a senior-level role.
- _Trend Analysis_: To show the growth of specific skills over time.

**Feasibility**: Scope is tight but perfect for a one-month project. Core risk (manual data collection) is mitigated by a standardized process.

**The Value & The Ask**
Why This Matters:
- _Relevance_: Directly addresses the anxiety and strategic need of a large segment of the professional workforce.
- _Novelty_: Moves beyond generic advice to provide data-driven, specific guidance for career investment.
- _Academic Rigor_: Perfectly demonstrates application of course techniques (Clustering, Regression) to a complex, meaningful problem.

**The Ask**: The outcome will be a valuable, evidence-based resource for navigating the data talent market, proving the practical application of our analytical toolkit.

## Data Source

### StatCan
Macro data from public sources.

#### Labour force characteristics by industry, annual (x 1,000)
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410002301

`14100023` = Labor

#### Employment and average weekly earnings (including overtime) for all employees by province and territory, monthly, seasonally adjusted
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410022301

`14100223` = Labor Earnings

#### Labour force characteristics by province, monthly, seasonally adjusted 
https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=1410028703

`14100287` = Labor Seasonally Adjusted

#### Canadian undergraduate tuition fees by field of study (current dollars)
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710000301

`37100003` = Undergrad

#### Postsecondary enrolments, by registration status, institution type, status of student in Canada and gender
https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710001801

`37100018` = Post grad


### Kaggle
Data for augmentation, to be able to split between different data jobs.


## Data Server

We will used a local MySQL database.
