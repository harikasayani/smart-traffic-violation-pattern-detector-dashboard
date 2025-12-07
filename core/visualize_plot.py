import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import matplotlib.ticker as mtick

# This module handles plots for the Visualization Page (02_Visualize_Data.py)

def plot_speed_exceeded_vs_weather(df):
    """
    Plots Average Speed Exceeded vs Weather Condition.
    """
    # Create new feature
    df['Speed_Exceeded'] = df['Recorded_Speed'] - df['Speed_Limit']

    fig, ax = plt.subplots(figsize=(16,9))

    # Compute mean speed exceeded and sort
    avg_speed = df.groupby('Weather_Condition')['Speed_Exceeded'].mean().sort_values(ascending=False)

    # Barplot
    sns.barplot(
        x=avg_speed.index,
        y=avg_speed.values,
        hue=avg_speed.index,
        palette='viridis',
        ax=ax
    )

    # Add value labels on bars
    for i, v in enumerate(avg_speed.values):
        ax.text(i, v + 0.5, f"{v:.1f}", ha='center', fontsize=10, fontweight='bold')

    # Titles and labels
    ax.set_title("Average Speed Exceeded vs Weather Condition", fontsize=16, fontweight='bold')
    ax.set_xlabel("Weather Condition", fontsize=14)
    ax.set_ylabel("Average Speed Exceeded (km/h)", fontsize=14)

    plt.xticks(rotation=45)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    return fig

def plot_avg_fine_by_violation_type(df):
    """
    Plots Average Fine Amount by Violation Type (Scatter Plot).
    """
    fig, ax = plt.subplots(figsize=(16,9))

    # Compute average fine amount by violation type
    avg_fines = df.groupby('Violation_Type')['Fine_Amount'].mean().sort_values(ascending=False)

    # Scatter plot
    ax.scatter(avg_fines.index, avg_fines.values, s=120, color='red')

    # Add value labels for each point
    for i, v in enumerate(avg_fines.values):
        ax.text(i, v + 5, f"{v:.0f}", ha='center', fontsize=10, fontweight='bold')

    # Titles and labels
    ax.set_title("Average Fine Amount by Violation Type (Scatter Plot)", fontsize=16, fontweight='bold')
    ax.set_xlabel("Violation Type", fontsize=14)
    ax.set_ylabel("Average Fine Amount (₹)", fontsize=14)

    plt.xticks(rotation=90)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    return fig

def plot_bar_or_count(df, x_col, y_col):
    """
    Generates a bar plot or count plot based on the Y-axis selection.
    """
    fig, ax = plt.subplots(figsize=(16,9))

    if y_col == 'Count':
        # Create a count plot using seaborn
        sns.countplot(x=x_col, data=df, ax=ax, order=df[x_col].value_counts().index)
        ax.set_title(f"Count of {x_col}")
        ax.set_ylabel("Count")
    else:
        # Create a bar plot of the mean using seaborn
        sns.barplot(x=x_col, y=y_col, data=df, ax=ax, estimator=lambda x: x.mean())
        ax.set_title(f"Mean of {y_col} by {x_col}")
        ax.set_ylabel(f"Mean {y_col}")

    ax.set_xlabel(x_col)
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig

def plot_correlation_heatmap(df, numerical_cols):
    """
    Plots a correlation heatmap for numerical columns.
    """
    corr_matrix = df[numerical_cols].corr()

    # Plotting the heatmap
    fig = plt.figure(figsize=(16, 9))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5,  fmt=".2f")
    plt.xticks(rotation=45)
    
    return fig


# ---------------------------------------------------------
# TEAM PLOTS - INTEGRATED FUNCTIONS
# ---------------------------------------------------------

# --- MONIKA'S PLOTS ---

def plot_top_5_locations_violation(df):
    """
    Monika: Top 5 Locations that have highest violation.
    """
    fig = plt.figure(figsize=(16,9))
    Location_Count=df['Location'].value_counts().head(5)
    sns.barplot(x=Location_Count.index,y=Location_Count.values)
    plt.title("Top 5 Locations that Have Violation", fontsize=16, fontweight='bold')
    plt.xlabel("Location")
    plt.ylabel("Count")
    plt.close() # Close to prevent display side effect, we return fig
    return fig

def plot_vehicle_type_vs_violation_type(df):
    """
    Monika: Vehicle type vs Violation Type.
    """
    fig = plt.figure(figsize=(16,9))
    sns.countplot(data=df, x='Violation_Type',hue='Vehicle_Type')
    plt.title('Vehicle Type vs Violation Type')
    plt.xlabel('Violation Type')
    plt.ylabel('Number of Violations')
    plt.legend(title='Vehicle Type')
    plt.tight_layout()
    plt.close()
    return fig


# --- AMITH'S PLOTS ---

def plot_violation_type_percentage(df):
    """
    Amith: Percentage of traffic violation types.
    """
    violation_counts = df['Violation_Type'].value_counts()
    fig = plt.figure(figsize=(16, 9))
    plt.pie(
        violation_counts,
        labels=violation_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title('Percentage of Traffic Violation Types')
    plt.axis('equal')
    plt.close()
    return fig

def plot_fines_per_year(df):
    """
    Amith: Total fines per year.
    """
    df = df.copy() # Avoid modifying original
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Year'] = df['Date'].dt.year
        fines_per_year = df.groupby('Year')['Fine_Amount'].sum()
        
        fig = plt.figure(figsize=(16, 9))
        plt.plot(fines_per_year.index, fines_per_year.values, marker='o')
        plt.grid(True, which='both', linestyle='--', linewidth=0.9, alpha=0.9)
        plt.title("Total Fines Per Year")
        plt.xlabel("Year")
        plt.ylabel("Total Fine Amount")
        plt.close()
        return fig
    else:
        return None


# --- HARIKA'S PLOTS ---

def plot_repeat_offenders(df):
    """
    Harika: Previous Violations per Record.
    """
    fig = plt.figure(figsize=(16, 9))
    colors = ['pink','skyblue','green','grey']
    if 'Previous_Violations' in df.columns:
        violations = df[df['Previous_Violations']>3].head(10)
        if not violations.empty:
            bars = plt.barh(violations.get('Violation_ID', range(len(violations))), violations['Previous_Violations'], color=colors)
            plt.title('Previous Violations per Record (Records with > 3 violations)')
            plt.xlabel('Number of Previous Violations')
            plt.ylabel('Record / Violation ID')
            plt.tight_layout()
            # Legend might fail if Violation_ID is simple index, skip logic for simplicity or keep basic
        else:
            plt.text(0.5, 0.5, "No records with > 3 previous violations", ha='center')
    plt.close()
    return fig

def plot_violation_by_location_pie(df):
    """
    Harika: Percentage of Traffic Violations by Location.
    """
    sns.set_theme(style='darkgrid')
    
    # Pre-process data: limit to top 10 + others
    location_counts = df["Location"].value_counts()
    if len(location_counts) > 10:
        top_n = location_counts.head(10)
        others_count = location_counts.iloc[10:].sum()
        if others_count > 0:
            top_n['Others'] = others_count
        location_counts = top_n

    fig, ax = plt.subplots(figsize=(16, 9))
    
    wedges, texts, autotexts = ax.pie(
        location_counts,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("pastel"),
        wedgeprops={'edgecolor': 'black'},
        pctdistance=0.85
    )
    
    # Style the percentage text
    plt.setp(autotexts, size=10, weight="bold")
    
    # Add external legend
    ax.legend(
        wedges, 
        location_counts.index,
        title="Locations",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        title_fontsize=12,
        fontsize=10
    )
    
    ax.set_title("Percentage of Traffic Violations by Location", fontsize=16, fontweight='bold')
    ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()
    plt.close() # Close to prevent display side-effects
    return fig


# --- DARSANA'S PLOTS ---

def plot_speeding_vs_road_condition(df):
    """
    Darsana: Speeding vs. Road Condition.
    """
    df = df.copy()
    if 'Recorded_Speed' in df.columns and 'Speed_Limit' in df.columns:
        df['Speeding'] = df['Recorded_Speed'] - df['Speed_Limit']
        speed_df = df[df['Speeding'] > 0]
        
        avg_speeding = speed_df.groupby('Road_Condition')['Speeding'].mean().reset_index()
        
        fig = plt.figure(figsize=(16,9))
        sns.barplot(
            data=avg_speeding,
            y='Road_Condition',
            x='Speeding',
            orient='h',
            palette='magma',
            hue='Road_Condition'
        )
        plt.title("Average Speeding Across Different Road Conditions")
        plt.xlabel("Average Speeding (km/h)")
        plt.ylabel("Road Condition")
        plt.close()
        return fig
    return None

def plot_fines_vs_weather_severity(df):
    """
    Darsana: Fines vs. Weather.
    """
    fig = plt.figure(figsize=(16,9))
    df_severity = df.groupby('Weather_Condition')['Fine_Amount'].mean().sort_values()
    
    sns.barplot(
        x=df_severity.values,
        y=df_severity.index,
        orient='h',
        hue=df_severity.index,
        palette='coolwarm'
    )
    plt.xlabel("Average Fine Amount (Severity)")
    plt.ylabel("Weather Condition")
    plt.title("Weather Condition vs Severity (Higher Fine = More Severe Violation)")
    plt.tight_layout()
    plt.close()
    return fig


# --- MRUNALINI'S PLOTS ---

def plot_severity_heatmap_by_location(df):
    """
    Mrunalini: Average Severity Score by Location and Violation Type.
    """
    df = df.copy()
    
    def calc_severity_score(row):
        severity = 0
        # Fine Amount
        if pd.notnull(row.get('Fine_Amount')):
            severity += row['Fine_Amount'] / 1000
        # Penalty Points
        if pd.notnull(row.get('Penalty_Points')):
            severity += row['Penalty_Points'] 
        # Speed Violation
        if pd.notnull(row.get('Recorded_Speed')) and pd.notnull(row.get('Speed_Limit')):
            overspeed = row['Recorded_Speed'] - row['Speed_Limit']
            if overspeed > 0:
                severity += overspeed /10
        # Alcohol Level
        if pd.notnull(row.get('Alcohol_Level')):
            severity += row['Alcohol_Level'] * 10
        # Helmet / Seatbelt
        if row.get('Helmet_Worn') == 'No':
            severity += 10
        if row.get('Seatbelt_Worn') == 'No':
            severity += 10
        # Traffic Light
        if row.get('Traffic_Light_Status') == 'Red':
            severity += 15
        # Previous Violations
        if pd.notnull(row.get('Previous_Violations')):
            severity += row['Previous_Violations'] * 1.5
        return severity

    df['Violation_Severity_Score'] = df.apply(calc_severity_score, axis=1)
    
    location_heatmap = df.pivot_table(
        values='Violation_Severity_Score',
        index='Location',
        columns='Violation_Type',
        aggfunc='mean'
    )

    fig = plt.figure(figsize=(16,9))
    sns.heatmap(location_heatmap, cmap='coolwarm', annot=True, fmt=".1f")
    plt.title("Average Severity Score by Location and Violation Type")
    plt.tight_layout()
    plt.close()
    return fig


# --- POOJITHA'S PLOTS ---

def plot_speed_exceeded_vs_weather_2(df):
    """
    Poojitha: Average Speed Exceeded vs Weather Condition.
    """
    df = df.copy()
    if 'Recorded_Speed' in df.columns and 'Speed_Limit' in df.columns:
        df['Speed_Exceeded'] = df['Recorded_Speed'] - df['Speed_Limit']
        fig = plt.figure(figsize=(16,9))
        avg_speed = df.groupby('Weather_Condition')['Speed_Exceeded'].mean().sort_values(ascending=False)
        sns.barplot(
            x=avg_speed.index,
            y=avg_speed.values,
            palette='viridis',
            hue=avg_speed.index
        )
        for i, v in enumerate(avg_speed.values):
            plt.text(i, v + 0.5, f"{v:.1f}", ha='center', fontsize=10, fontweight='bold')
        
        plt.title("Average Speed Exceeded vs Weather Condition", fontsize=16, fontweight='bold')
        plt.xlabel("Weather Condition", fontsize=14)
        plt.ylabel("Average Speed Exceeded (km/h)", fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.close()
        return fig
    return None

def plot_avg_fine_by_violation_type_2(df):
    """
    Poojitha: Average Fine Amount by Violation Type.
    """
    fig = plt.figure(figsize=(16,9))
    avg_fines = df.groupby('Violation_Type')['Fine_Amount'].mean().sort_values(ascending=False)
    plt.scatter(avg_fines.index, avg_fines.values, s=120, color='red')
    for i, v in enumerate(avg_fines.values):
        plt.text(i, v + 5, f"{v:.0f}", ha='center', fontsize=10, fontweight='bold')
    
    plt.title("Average Fine Amount by Violation Type (Scatter Plot)", fontsize=16, fontweight='bold')
    plt.xlabel("Violation Type", fontsize=14)
    plt.ylabel("Average Fine Amount (₹)", fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.close()
    return fig


# --- RAKSHITHA'S PLOTS ---

def plot_peak_hour_traffic(df):
    """
    Rakshitha: Peak Hour Traffic Violations.
    """
    df = df.copy()
    if 'Time' in df.columns:
        # Assuming format HH:MM or similar, pd.to_datetime should handle
        try:
            df['hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.hour
            # Fallback if format is just HH:MM
            if df['hour'].isnull().any():
                 df['hour'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.hour
            
            # If still issues, simple split (robust fallback)
            if df['hour'].isnull().all():
                 df['hour'] = df['Time'].astype(str).str.split(':').str[0].astype(float) # convert to float first
        except:
             return None

        hour_counts = df['hour'].value_counts().sort_index()
        fig = plt.figure(figsize=(16,9)) 
        sns.lineplot(x=hour_counts.index, y=hour_counts.values, marker="o", linewidth=2)
        plt.title("Peak Hour Traffic Violations", fontsize=14)
        plt.xlabel("Hour of the Day (0–23)")
        plt.ylabel("Number of Violations")
        plt.xticks(range(0, 24))
        plt.tight_layout()
        plt.close()
        return fig
    return None

def plot_violation_by_road_condition(df):
    """
    Rakshitha: Violation Distribution by Road Condition.
    """
    sns.set_theme(style='darkgrid')
    road_counts = df['Road_Condition'].value_counts()
    
    fig, ax = plt.subplots(figsize=(16, 9))
    
    wedges, texts, autotexts = ax.pie(
        road_counts,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("pastel"),
        wedgeprops={'edgecolor': 'black'},
        pctdistance=0.85
    )
    
    # Style the percentage text
    plt.setp(autotexts, size=10, weight="bold")
    
    # Add external legend
    ax.legend(
        wedges, 
        road_counts.index,
        title="Road Conditions",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        title_fontsize=12,
        fontsize=10
    )

    ax.set_title("Violation Distribution by Road Condition", fontsize=16, fontweight='bold')
    ax.axis('equal')
    plt.tight_layout()
    plt.close()
    return fig


# --- SANIYA'S PLOTS ---

def plot_weather_impact_heatmap(df):
    """
    Saniya: Impact of Weather conditions on Traffic Violations - Heat Map.
    """
    pivot = df.pivot_table(
        index="Violation_Type",
        columns="Weather_Condition",
        values="Violation_ID", # Assuming count
        aggfunc="count",
        fill_value=0
    )
    fig = plt.figure(figsize=(16,9))
    ax = sns.heatmap(
        pivot, 
        annot=True, 
        fmt="d", 
        cmap="YlGnBu",   
        cbar=True        
    )
    plt.title("Impact of Weather Conditions on Traffic Violations")
    plt.xlabel("Weather Condition")
    plt.ylabel("Violation Type")
    plt.tight_layout()
    plt.close()
    return fig

def plot_driver_risk_by_age(df):
    """
    Saniya: Average Driver Risk Level By Age group - Line Graph.
    """
    df = df.copy()
    bins = [0, 25, 35, 45, 60, 100]
    labels = ["18-25", "26-35", "36-45", "46-60", "60+"]
    df["Age_Group"] = pd.cut(df["Driver_Age"], bins=bins, labels=labels, include_lowest=True)
    
    df['Alcohol_Flag'] = (df['Breathalyzer_Result'] == "Positive").astype(int)
    df["Risk_Level"] = df["Previous_Violations"] + df["Alcohol_Flag"]

    risk_by_age = df.groupby("Age_Group", observed=False)["Risk_Level"].mean().reset_index()
    risk_by_age = risk_by_age.sort_values("Age_Group")

    fig = plt.figure(figsize=(16,9))
    sns.set_style("whitegrid")
    
    plt.plot(
        risk_by_age["Age_Group"],
        risk_by_age["Risk_Level"],
        marker="o",
        markersize=10,
        linewidth=2,
        color="#D43F6A"
    )
    for i, row in risk_by_age.iterrows():
        plt.text(
            row["Age_Group"],
            row["Risk_Level"] + 0.02,
            f"{row['Risk_Level']:.2f}",
            ha="center",
            fontsize=10,
            weight="bold"
        )
    plt.title("Average Driver Risk Level by Age Group ", fontsize=14, weight="bold")
    plt.xlabel("Age Group")
    plt.ylabel("Average Risk Level")
    plt.tight_layout()
    plt.close()
    return fig


# --- SANJANA'S PLOTS ---

def plot_vehicle_risk_countplot(df):
    """
    Sanjana: Vehicle-Type Based Risk.
    """
    vehicle_counts = df['Vehicle_Type'].value_counts().index
    fig = plt.figure(figsize=(16,9))
    sns.countplot(
        y=df['Vehicle_Type'],
        order=vehicle_counts,
        palette='coolwarm',
        hue=df['Vehicle_Type']
    )
    plt.title('Vehicle-Type Based Risk')
    plt.xlabel('Vehicle Count')
    plt.ylabel('Vehicle Type')
    plt.tight_layout()
    plt.close()
    return fig

def plot_age_alcohol_heatmap(df):
    """
    Sanjana: Age group vs alcohol test.
    """
    df = df.copy()
    bins = [0, 25, 35, 45, 60, 100]
    labels = ["18-25", "26-35", "36-45", "46-60", "60+"]
    
    max_alcohol = df['Alcohol_Level'].max()
    # Handle case where max might be low
    upper = max(0.251, max_alcohol)
    
    ranges = [0, 0.03, 0.08, 0.15, 0.25, upper]
    safelevels = ['Safe', 'Mild', 'Risky', 'High Risk', 'Dangerous']
    
    # Needs handling duplicates or exact edges if bins not unique, but usually ok
    # If duplicates in ranges (e.g. max is 0.0), cut will fail.
    # Simple check:
    ranges = sorted(list(set(ranges)))
    if len(ranges) - 1 != len(safelevels): 
        # Fallback if ranges merged
        return None

    df["Age_Group"] = pd.cut(df["Driver_Age"], bins=bins, labels=labels, include_lowest=True)
    df["Alcohol_Range"] = pd.cut(df["Alcohol_Level"], bins=ranges, labels=safelevels, include_lowest=True)
    
    heatmap_data = pd.crosstab(df['Age_Group'], df['Alcohol_Range'])
    
    fig = plt.figure(figsize=(16,9))
    sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="Reds")
    plt.title("Age Group vs Alcohol Test Result Heatmap")
    plt.xlabel("Alcohol Test Result")
    plt.ylabel("Age Group")
    plt.tight_layout()
    plt.close()
    return fig


# --- ISHWARI'S PLOTS ---

def plot_fine_vs_vehicle_pie(df):
    """
    Ishwari: Fine Paid vs Vehicle Type.
    """
    fine_data = df.groupby('Vehicle_Type')['Fine_Amount'].sum()
    fig = plt.figure(figsize=(16, 9))
    plt.pie(
        fine_data.values,
        labels=fine_data.index,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title("Fine Paid vs Vehicle Type", fontsize=18)
    plt.axis('equal')
    plt.close()
    return fig

def plot_avg_fine_location_line(df):
    """
    Ishwari: Average fine per location.
    """
    fine_location = df.groupby('Location')['Fine_Amount'].mean().reset_index()
    fig = plt.figure(figsize=(16,9))
    plt.plot(
        fine_location['Location'],
        fine_location['Fine_Amount'],
        marker='o'
    )
    plt.title("Average Fine Amount vs Location")
    plt.xlabel("Location")
    plt.ylabel("Average Fine Amount")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.close()
    return fig

# ---- Anshu's Plots ----

def plot_license_validity_by_gender(df):
    """
    Anshu: License Validity by Gender.
    """
    validity_gender = df.groupby(['License_Validity', 'Driver_Gender']).size().unstack(fill_value=0)
    
    fig, ax = plt.subplots(figsize=(16,9))
    validity_gender.plot(kind='bar', ax=ax)

    ax.set_title("Number of License Validities by Gender")
    ax.set_xlabel("License Status")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    ax.legend(title="Driver Gender")
    plt.tight_layout()
    return fig

def plot_fine_amount_distribution_vs_weather(df):
    """
    Anshu: Fine Amount Distribution Across Different Weather Conditions (Violin Plot).
    """
    plt.figure(figsize=(16, 9))
    sns.violinplot(data=df, x='Weather_Condition', y='Fine_Amount', inner='box')
    
    plt.title("Fine Amount Distribution Across Different Weather Conditions")
    plt.xlabel("Weather Condition")
    plt.ylabel("Fine Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

def plot_violation_types_vs_weather_heatmap(df):
    """
    Anshu: Violation Types Across Different Weather Conditions (Heatmap).
    """
    plt.figure(figsize=(16, 9))
    heatmap_violation = pd.crosstab(df['Weather_Condition'], df['Violation_Type'])
    
    sns.heatmap(heatmap_violation, annot=True, cmap="YlOrRd", fmt='d')
    
    plt.title("Violation Types Across Different Weather Conditions")
    plt.xlabel("Violation Type")
    plt.ylabel("Weather Condition")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()
