# 📘 PROJECT_BLUEPRINT_4.md: Agile Project Documentation

**Project Name:** Smart Traffic Violation Pattern Detector Dashboard  
**Platform Name:** CollisionX India  
**Role:** Agile Project Manager & Technical Team Lead  
**Team Size:** 15 Developers (Interns)  
**Duration:** 2 Months (Oct 2025 - Dec 2025, 4 Sprints)  
**Tools:** Python, Streamlit, Pandas, Matplotlib, Folium  

---

## 1. 📋 Product Backlog

This backlog tracks the internship progress from Training to Product Delivery.

| Planned Sprint | Actual Sprint | US ID | User Story Description | MOSCOW | Dependency | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sprint 1 | Sprint 1 | US-00 | As a team, we need to **collaborate on a Shared Learning Repo** to practice Python/Pandas. | Must Have | None | All Team | Done |
| Sprint 2 | Sprint 2 | US-01 | As a lead, I want to **initialize the Main Project Repo** with a 7-branch strategy. | Must Have | None | Saidul (Lead) | Done |
| Sprint 2 | Sprint 2 | US-02 | As a user, I want a **Data Upload Page** to load traffic CSVs. | Must Have | US-01 | Divija | Done |
| Sprint 2 | Sprint 2 | US-03 | As a system, I need **Feature-Branch workflows** (6-7 branches) to manage 15 devs. | Must Have | None | Anshu | Done |
| Sprint 3 | Sprint 3 | US-08 | As a user, I want **Home & About Pages** for project info. | Must Have | US-01 | Ishwari | Done |
| Sprint 3 | Sprint 3 | US-04 | As a user, I want distinct **Visualization Pages** for different insights. | Must Have | US-02 | Divija | Done |
| Sprint 3 | Sprint 3 | US-05 | As a user, I want **Visual Plots** (Bar/Pie) for traffic trends. | Must Have | US-04 | Harika | Done |
| Sprint 3 | Sprint 3 | US-06 | As a user, I want **Scatter & Bar Plots** for variable correlation. | Must Have | US-04 | Poojitha | Done |
| Sprint 3 | Sprint 3 | US-07 | As a user, I want **Donut Charts** for violation composition. | Should Have | US-04 | Anshu | Done |
| Sprint 3 | Sprint 3 | US-08 | As a user, I want **Risk & Heatmap Plots** for severity analysis. | Must Have | US-04 | Divija | Done |
| Sprint 4 | Sprint 4 | US-09 | As a brand, I want a custom **Logo and Platform Identity (CollisionX India)**. | Should Have | None | Mrunalini | Done |
| Sprint 4 | Sprint 4 | US-10 | As a user, I want a **Map Visualization** using specific GeoJSONs for accurate regions. | Must Have | US-02 | Saidul | Done |

---

## 2. 🏃 Sprint Backlog

Detailed task tracking per Sprint (14-day duration).

### **Sprint 1 (Oct 17 - Oct 30): Foundation & Learning**

| US ID | Task ID | Task Description | Task Start Date | Task Completion Date | Team Member | Activity | Status | Original Estimate (Hrs) | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | D14 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US-00 | T-101 | **Python/Pandas Learning** | Oct 17 | Oct 23 | All | Learning | Done | 6 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-00 | T-102 | **VS Code Env Deployment** | Oct 17 | Oct 18 | Anshu | Setup | Done | 4 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-00 | T-103 | **Git Basics Workshop** | Oct 24 | Oct 26 | Saidul | Training | Done | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 |
| US-00 | T-104 | **Shared Repo Collab** | Oct 27 | Oct 29 | All | Coding | Done | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 1 |
| US-00 | T-105 | **Project Ideation** | Oct 30 | Oct 30 | Saidul | Planning | Done | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |

### **Sprint 2 (Oct 31 - Nov 13): Setup & Data Pipeline**

| US ID | Task ID | Task Description | Task Start Date | Task Completion Date | Team Member | Activity | Status | Original Estimate (Hrs) | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | D14 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US-01 | T-201 | **Main Repo Initialization** | Oct 31 | Nov 02 | Saidul | Dev/Ops | Done | 5 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-03 | T-202 | **Branch Protection Rules** | Nov 01 | Nov 03 | Anshu | Config | Done | 4 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-02 | T-203 | **Data Upload Page** | Nov 04 | Nov 07 | Divija | Dev | Done | 6 | 0 | 0 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-02 | T-204 | **CSV Encoding Fixes** | Nov 08 | Nov 10 | Divija | Bugfix | Done | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| US-04 | T-205 | **Data Utility Scripts** | Nov 10 | Nov 13 | Vijay | Dev | Done | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 0 |

### **Sprint 3 (Nov 14 - Nov 27): Visualization & Dashboard**

| US ID | Task ID | Task Description | Task Start Date | Task Completion Date | Team Member | Activity | Status | Original Estimate (Hrs) | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | D14 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US-04 | T-301 | **Viz Page Architecture** | Nov 14 | Nov 18 | Ishwari | Design | Done | 6 | 1 | 1 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-07 | T-302 | **Sidebar Navigation Fix** | Nov 17 | Nov 18 | Poojitha| Refactor | Done | 4 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-05 | T-303 | **Basic Bar/Pie Charts** | Nov 16 | Nov 19 | Sanjana | Dev | Done | 6 | 0 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-06 | T-304 | **Heatmap Implementation** | Nov 22 | Nov 24 | Saniya | Dev | Done | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| US-08 | T-305 | **Home & About Pages** | Nov 23 | Nov 27 | Ishwari | Dev | Done | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 1 | 0 |

### **Sprint 4 (Nov 28 - Dec 11): Advanced Features & Finalization**

| US ID | Task ID | Task Description | Task Start Date | Task Completion Date | Team Member | Activity | Status | Original Estimate (Hrs) | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | D11 | D12 | D13 | D14 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US-09 | T-401 | **Logo & Identity Design** | Nov 28 | Nov 30 | Mrunalini| Design | Done | 4 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| US-10 | T-402 | **GeoJSON Map Implementation**| Dec 01 | Dec 06 | Saidul | Dev | Done | 6 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| US-10 | T-403 | **Map Validation & Fixes** | Dec 06 | Dec 08 | Saidul | Testing | Done | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 0 |
| US-11 | T-404 | **Cross-Browser QA** | Dec 07 | Dec 10 | Mounika | QA | Done | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 0 | 0 |
| US-12 | T-405 | **Final Documentation** | Dec 09 | Dec 11 | Saidul | Doc | Done | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 2 |

---

## 3. 🗣️ Stand-up Meeting Log

Daily syncing, focusing on "CollisionX India" platform blockers.

| Sprint | Date | Impediments / Blockers | Action Taken |
| :--- | :--- | :--- | :--- |
| **Sp 1** | Day 2 (Oct 18) | **Planning:** Initial project planning. | **Decision:** Concluded to build a **Python-heavy** project to maximize learning (avoiding simple no-code tools). |
| **Sp 1** | Day 6 (Oct 22) | **Info:** Reviewing the overall Project Structure. | **Action:** Walkthrough of the folder structure (`core/`, `pages/`) so everyone understands the flow. |
| **Sp 2** | Day 16 (Nov 01) | **Planning:** Graphic Plots strategy. | **Decision:** Decided which specific libraries (Matplotlib/Seaborn) to use for which insights. |
| **Sp 2** | Day 23 (Nov 08) | **Blocker:** Team Confusion on Architecture. | **Action:** "Clean-the-air" meeting to resolve doubts about where to put logic vs UI code. |
| **Sp 3** | Day 30 (Nov 15) | **Issue:** Frequent merge conflicts overriding code updates. | **Action:** Anshu enforced "Branch Protection Rules" requiring PR reviews before merge. |
| **Sp 3** | Day 37 (Nov 22) | **Demo:** Teammates proposed new features (Home/About/KYD). | **Action:** Accepted proposals: Ishwari assigned Home/About, Mrunalini assigned 'Know Your Data' (Numerical Analysis). |
| **Sp 4** | Day 44 (Nov 29) | **Review:** UI Consistency Check (HTML/CSS). | **Action:** Mrunalini & Ishwari established global CSS variables to fix table rendering issues. |
| **Sp 4** | Day 51 (Dec 06) | **Review:** Final Draft Demonstration. | **Action:** Reviewed the nearly-finished product; requested minor preference-based UI tweaks before freezing code. |
| **Sp 4** | Day 56 (Dec 11) | **Prep:** Presentation & Live Demo planning. | **Action:** Assigned roles for the final presentation: who speaks on Architecture, who does Live Demo, etc. |

---

## 4. 🔄 Retrospection

Reflecting on the "CollisionX India" team performance.

| SL # | Sprint # | Sprint start date | Sprint end date | Team member name | Start Doing | Stop Doing | Continue Doing | Action taken |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Sprint 2 | Oct 27 | Nov 09 | Anshu | Grouping PRs by Feature Branch (UI, Data, Core). | Allowing direct commits to Main. | Managing the shared repository protections. | Enforced Branch Protection Rules requiring reviews. |
| 2 | Sprint 2 | Oct 27 | Nov 09 | Divija | checking file encoding (UTF-8 vs Latin-1). | Assuming all CSVs are clean. | Writing robust data loader tests. | Added `try-except` block for encoding errors in `utils.py`. |
| 3 | Sprint 3 | Nov 10 | Nov 23 | Saidul | Leveraging **Gemini/Claude** for tricky Pandas debugging. | Writing custom CSS without checking Streamlit support. | guiding the 15-member team on architecture. | Scheduled AI-debugging sessions for complex errors. |
| 4 | Sprint 3 | Nov 10 | Nov 23 | Mrunalini | Creating assets (Logo) earlier in the sprint. | Using hardcoded paths. | improving UI aesthetics. | Established `assets/` folder standard for all images. |
| 5 | Sprint 3 | Nov 10 | Nov 23 | Ishwari | Testing dashboard on Window resizing. | Designing only for maximized Desktop view. | Explicitly defining `width` parameter (fixing deprecation issue). | Resolved layout breaks by manually setting chart width. |
| 6 | Sprint 3 | Nov 10 | Nov 23 | Poojitha | Using relative path keys for navigation. | Hardcoding page filenames in links. | Modularizing the Sidebar code. | Refactored `sidebar.py` to be robust against file renaming. |
| 7 | Sprint 4 | Nov 24 | Dec 07 | Saidul | Validating GeoJSON files before implementation. | Ignoring projection errors. | searching for open-source resources. | Implemented specific GeoJSON validation step in `map_plot.py`. |
| 8 | Sprint 4 | Nov 24 | Dec 07 | All | Using standard Variable names (Data Variables). | Hardcoding column names in pages. | collaborating on plotting logic. | Refactored all page hardcoding to usage of `data_variables.py`. |
| 9 | Sprint 4 | Nov 24 | Dec 07 | Mounika P | Cross-browser testing (Chrome/Edge/Firefox). | Waiting for DEV completion to start QA. | Logging defects in the shared Tracker. | Identified 2 critical UI bugs (BUG-03, BUG-05) before final demo. |

---

## 5. 🐛 Defect Tracker

| Sl No | Submitted By | Submitted Date | Description | Detected Sprint | Assigned To | Type Of Defect | Action Taken | Action Taken Date | Status(Open/Closed) | Remarks |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BUG-01 | Anshu | Nov 02 | **Merge Conflict:** Logic overwrites in `app.py`. | Sprint 2 | Anshu | Process | Restricted main branch; enforced 7-branch workflow. | Nov 03 | Closed | Process Updated |
| BUG-02 | Divija | Nov 05 | **Encoding Error:** CSVs with special chars failing. | Sprint 2 | Divija | Data | Added `latin-1` fallback in `utils.py`. | Nov 06 | Closed | Critical Fix |
| BUG-03 | Mounika P | Nov 18 | **Visuals:** Bar charts overlapping. | Sprint 3 | Sanjana | UI | Adjusted figure size and rotation using Matplotlib params. | Nov 19 | Closed | Verified |
| BUG-04 | Darsana | Nov 20 | **Analysis:** Complex filters causing slow load. | Sprint 3 | Darsana | Perf | Optimization assistance from AI tools (Claude). | Nov 21 | Closed | Optimized |
| BUG-05 | Mounika P | Nov 22 | **UI Glitch:** Sidebar overlapping text. | Sprint 3 | Ishwari | UI | Applied custom CSS media queries. | Nov 23 | Closed | Verified |
| BUG-06 | Saidul | Dec 01 | **Map Visibility:** Map not loading for certain States. | Sprint 4 | Saidul | Data | Swapped broken GeoJSON with valid Open Source files. | Dec 02 | Closed | Fixed |

---

## 6. 🧪 Unit Test Plan

| Sl No | Test Case Name | Test Procedure | Condition to be Tested | Expected Result | Actual Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | **GeoJSON Validity** | Load map with new GeoJSON file. | `map_plot.py` check. | Map renders without polygon errors. | Matches Expected |
| TC-02 | **Logo Rendering** | Check Sidebar logo display. | `sidebar.py` render. | "CollisionX India" logo appears correctly. | Matches Expected |
| TC-03 | **Git Workflow** | Merge 'UI-Feature' Branch to Main. | Conflict resolution. | Clean merge due to branch alignment. | Matches Expected |
| TC-04 | **Variable Consistency** | Check column names across pages. | `data_variables.py` usage. | All pages use unified constants. | Matches Expected |
| TC-05 | **Error Handling: Invalid File** | Upload a `.txt` or `.exe` file instead of CSV. | `09_Upload_Dataset.py` validator. | System rejects file with "Invalid format" error. | Matches Expected |
| TC-06 | **Error Handling: Schema Check** | Upload CSV with missing columns. | `app.py` Schema Validation. | "Missing Columns" warning displayed; App prevents crash. | Matches Expected |

---

> **Acknowledgment:** We leveraged AI tools (Claude & Gemini) primarily for **complex debugging** where Saidul & Anshu led the analysis to resolve deep technical issues. We, everyone have worked together collaboratively to resolve the issues and give a successful from to this project.
