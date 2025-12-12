# 🚦 Smart Traffic Violation Pattern Detector Dashboard v0.1.0

## 📝 Overview

This project is a Streamlit web application designed to analyze traffic violation data. It provides a user-friendly interface to explore, visualize, and gain insights from traffic violation datasets. Users can upload their own data, perform analysis, and view summaries and trends.

> 📘 **Documentation**: For a comprehensive understanding of the project, please refer to our detailed core documentation:
>
> * **[1. System Architecture (Basic)](PROJECT_DOCUMENTATIONS/PROJECT_BLUEPRINT_1-BASIC.md)**: High-level overview, architecture diagrams, and directory structure.
> * **[2. Page Development Details](PROJECT_DOCUMENTATIONS/PROJECT_BLUEPRINT_2-PAGE_DEVELOPMENT_DETAILS.md)**: In-depth analysis of each page, purpose, and dependencies.
> * **[3. Visual Diagrams](PROJECT_DOCUMENTATIONS/PROJECT_BLUEPRINT_3-VISUAL_DIAGRAMS.md)**: Detailed Architecture, Data Flow, and Component Interaction diagrams.

## 🎯 Features

* **Dataset Management:**
  * Upload your own CSV datasets.
  * View and browse the loaded dataset.
* **Numerical Analysis:**
  * Get a quick overview of your dataset, including shape and sample rows.
  * View detailed information about each column, including data types and descriptive statistics.
* **Data Visualization:**
  * Generate various plots to visualize data distributions and relationships.
* **Trend Analysis:**
  * Analyze trends in the data over time.
* **Map Visualization:**
  * Visualize geographical data on an interactive map.
* **Correlation Analysis:**
  * Explore correlations between numerical columns with a heatmap.

## 🚀 How to Run

1. **Clone the repository:**

    ```bash
    git clone https://github.com/saidulalimallick04/smart-traffic-violation-pattern-detector-dashboard.git
    cd smart-traffic-violation-pattern-detector-dashboard
    ```

2. **Choose your package manager:**

    ---

   ### 🌟 Primary Method: Using `uv` (Recommended)

    1. **Create and activate a virtual environment:**

        ```bash
        # Create a virtual environment
        uv sync
        ```

    2. **Run the application:**

        ```bash
        uv run streamlit run app.py
        ```

    ---

   ### 🐢 Alternative Method: Using `pip`

    1. **Create and activate a virtual environment:**

        ```bash
        python -m venv .venv
        
        # Activate the virtual environment
        # On Windows (Command Prompt)
        .\.venv\Scripts\activate
        # On Windows (PowerShell)
        .\.venv\Scripts\Activate.ps1
        # On macOS/Linux
        source .venv/bin/activate
        ```

    2. **Install dependencies:**

        ```bash
        pip install .
        ```

    3. **Run the application:**

        ```bash
        streamlit run app.py
        ```

## 📂 Project Structure

```text
.
├── .gitignore
├── .python-version
├── app.py
├── core
│   ├── __init__.py
│   ├── analysis_plot.py
│   ├── dashboard_plot.py
│   ├── dashboard_summary.py
│   ├── data_generator.py
│   ├── data_variables.py
│   ├── sidebar.py
│   ├── trend_plot.py
│   ├── utils.py
│   └── visualization_plot.py
├── dataset
│   └── Indian_Traffic_Violations.csv
├── generated_fake_traffic_datasets
│   └── 2025-11-24
│       ├── 01_traffic_dataset.csv
│       └── 02_traffic_dataset.csv
├── map_data
│   ├── 01_INDIA_STATES.geojson
│   └── 02_INDIA_STATES.geojson
├── uploded_file_others
│   └── (empty)
├── pages
│   ├── 01_Numerical_Analysis.py
│   ├── 02_Visualize_Data.py
│   ├── 03_Trend_Analysis.py
│   ├── 04_Map_Visualization.py
│   ├── 09_Upload_Dataset.py
│   └── 10_View_Dataset.py
├── pyproject.toml
├── requirements.txt                              # Project Dependencies
├── PROJECT_DOCUMENTATIONS
│   ├── PROJECT_BLUEPRINT_1-BASIC.md                  # System Architecture & Overview
│   ├── PROJECT_BLUEPRINT_2-PAGE_DEVELOPMENT_DETAILS.md # Detailed Page Analysis
│   ├── PROJECT_BLUEPRINT_3-VISUAL_DIAGRAMS.md        # Architecture & Data Flow Diagrams
├── README.md
├── uploded_file_relateds
└── uv.lock
```

## 📦 Dependencies

The main dependencies for this project are listed in the `pyproject.toml` file. They include:

* `numpy>=2.3.5` - [Numpy](https://numpy.org/)
* `datetime` - Python Standard Library
* `pandas>=2.3.3` - [Pandas](https://pandas.pydata.org/)
* `seaborn>=0.13.2` - [Seaborn](https://seaborn.pydata.org/)
* `streamlit>=1.51.0` - [Streamlit](https://streamlit.io/)
* `streamlit-local-storage>=0.0.25` - [Streamlit Local Storage](https://pypi.org/project/streamlit-local-storage/)
* `folium>=0.16.0` - [Folium](https://python-visualization.github.io/folium/)
* `streamlit-folium>=0.18.0` - [Streamlit Folium](https://pypi.org/project/streamlit-folium/)
* `faker>=38.2.0` - [Faker](https://faker.readthedocs.io/)

## Recent Updates

* **2025-12-09:**
  * **Documentation & AI Integration:** **Saidul** finalized the comprehensive project blueprint and integrated AI analysis tools (Claude/Gemini) for advanced debugging.
  * **Agile Artifacts:** Created detailed Product and Sprint backlogs to track team velocity.

* **2025-12-05:**
  * **Branding:** **Mrunalini** unveiled the new **"CollisionX India"** platform identity, incorporating a custom logo and unified color theme across the dashboard.
  * **Refactoring:** **Vijay G** optimized the utility functions in `core/utils.py` to handle large datasets more efficiently.

* **2025-11-26:**
  * **Map Visualization:** **Saidul** successfully integrated Open Source GeoJSON files to resolve region mismatch issues in the Map Module.
  * **Trend Analysis:** **Rakshitha** implemented the "Peak Hour Traffic" analysis to identify high-risk time windows.

* **2025-11-25:**
  * **Performance Tuning:** **Darsana** and **Saniya** worked on optimizing the filter logic, reducing the dashboard load time by 40%.
  * **Advanced Plots:** **Sanjana** added the "Severity Heatmap" to visualize accident intensity by location.

* **2025-11-22:**
  * **Fake Data Engine:** **Saniya** and **Poojitha** enhanced the `data_generator.py` to produce realistic synthetic violations for stress testing.
  * **Bug Fixes:** **Anshu** resolved a critical merge conflict that was affecting the deployment pipeline.

* **2025-11-20:**
  * **Numerical Analysis:** **Mrunalini** deployed the "Numerical Analysis" page, adding descriptive statistics and data quality checks.
  * **Error Handling:** **Saidul** fixed the `pyarrow.lib.ArrowInvalid` serialization error in the dataframe viewer.
  * **Data Validation:** **Saniya** added strict type checking for the CSV loader to reject malformed files earlier in the pipeline.
  * **Documentation:** **Rakshitha** updated the inline docstrings for all new utility functions.

* **2025-11-18:**
  * **UI Polish:** **Ishwari** and **Harika** refactored the HTML/CSS components to ensure a responsive design on mobile devices.
  * **Page Routing:** **Poojitha** streamlined the Sidebar navigation for better user experience.
  * **Accessibility:** **Rakshitha** audited the color contrast ratios of the charts to ensure they met WCAG standards.
  * **Performance:** **Vijay G** implemented memoization for the sidebar data loader to prevent reloading on every interaction.

* **2025-11-16:**
  * **Data Visualization:** **Sanjana** and **Ishwari** launched the initial "Visualize Data" page with Bar and Pie charts for vehicle distribution.
  * **HTML Debugging:** **Harika** fixed table rendering issues with assistance from AI debugging tools.
  * **Chart Styling:** **Darsana** applied a custom color palette to the Matplotlib figures to match the platform theme.

* **2025-11-13:**
  * **Sidebar Integration:** **Poojitha** finalized the multi-page sidebar structure, enabling seamless switching between 5 different modules.
  * **Asset Management:** **Mrunalini** organized the static assets (images, CSS) and established the project folder structure.

* **2025-11-09:**
  * **Data Upload Feature:** **Divija** implemented the CSV file uploader with validation for required columns.
  * **Data Cleaning:** **Vijay G** wrote the utility scripts to clean null values and standardize date formats.
  * **Unit Tests:** **Darsana** added initial unit tests for the data loader to ensure file compatibility.

* **2025-11-04:**
  * **Git Workflow:** **Anshu** established the Git structure and resolved initial merge conflicts for the team of 13.
  * **Repo Initialization:** **Saidul** set up the repository, virtual environment, and `app.py` skeleton.
  * **Environment Config:** **Rakshitha** created the `pyproject.toml` and `requirements.txt` to manage dependencies.

* **2025-11-01:**
  * **Project Kickoff:** Team **CollisionX India** assembled. **Saidul** (Lead) defined the architecture and assigned initial modules to:
    * **Development:** Ishwari, Harika, Divija, Amith, Sanjana, Darsana, Poojitha, Saniya, Vijay, Rakshitha.
    * **UI/UX:** Mrunalini.
    * **Version Control:** Anshu.

---

## 👥 Authors / Team CollisionX India

The dedicated team behind the **Smart Traffic Violation Pattern Detector Dashboard**.

| Team Member | Role / Key Contribution |
| :--- | :--- |
| **Saidul Ali Mallick** | **Team Lead & Lead Developer**. Initialized Main Repo, handled Architecture, Documentation, and **Map Visualization**. |
| **Anshu Gupta** | **Developer & Git Specialist**. Managed Shared Repository, defined Branching Strategy, handled Merges, and **assisted with Frontend integration**. |
| **Mrunalini P** | **Developer, UI/UX & Branding**. Created "CollisionX India" platform identity, Logo, and **Key Frontend Developer** for core UI pages. |
| **Ishwari Deshmukh** | **Frontend Developer & Analyst**. Built visualization pages and handled Streamlit layout components. |
| **Harika Sayani** | **Developer**. Contributed to page structure, HTML representation, and About page. |
| **Divija V** | **Developer, Analyst & UI/UX**. Implemented Data Upload, Graphical Representations, Visualization Page UI, and file handling logic. |
| **Amith Shaji George** | **Developer, Analyst & QA Tester**. Solved complex backend issues and contributed to dashboard logic. |
| **Sanjana Gowrishetty** | **Developer & Analyst**. Contributed to visual representation and plotting logic. |
| **Darsana R** | **Developer, Analyst & UI/UX**. Contributed to plotting modules, **Frontend UI components**, and dashboard integration. |
| **Poojitha Borra** | **Developer & Analyst**. Assisted with page routing and debugging. |
| **Saniya Mahek** | **Developer & Analyst**. Worked on data validation and filters. |
| **Vijay Gudla** | **Developer & Analyst**. Contributed to backend utility functions. |
| **Rakshitha P** | **Developer & QA Tester**. Assisted with testing and documentation. |
| **Mounika Pinnika** | **QA Tester**. Validated data integrity and handled cross-browser testing. |
| **Mounika Sunkari** | **QA Tester**. Assisted in test case execution and product verification. |

> **Acknowledgment:** We leveraged AI tools (Claude & Gemini) primarily for **complex debugging** where Saidul & Anshu led the analysis to resolve deep technical issues.

---
