import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

# This module handles plots for the Dashboard (Home Page)

# =============================== Dashboard Overview Plots =============================================
# ----- Amit's Plots -----
def plot_violation_type_percentage_pie(df):
    """
    Plots the percentage of traffic violation types as a pie chart.
    """
    sns.set_theme(style='darkgrid')
    violation_counts = df['Violation_Type'].value_counts()
    
    fig, ax = plt.subplots(figsize=(16, 9))
    wedges, texts, autotexts = ax.pie(
        violation_counts,
        autopct='%1.1f%%',
        colors=sns.color_palette('pastel'),
        wedgeprops={'edgecolor': 'black'},
        pctdistance=0.85
    )
    plt.setp(autotexts, size=20, weight="bold")
    ax.legend(
        wedges, 
        violation_counts.index,
        title="Violation Types",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        title_fontsize=20,
        fontsize=25,
    )
    ax.set_title("Percentage of Traffic Violation Types", fontsize=20, fontweight='bold')
    ax.axis('equal')
    plt.tight_layout()
    return fig

# =================================================================================
def plot_fines_based_on_violation_type(summary):
    """
    Plots the fines based on violation type (Paid vs Unpaid).
    """
    fig, ax = plt.subplots(figsize=(16, 9))
    summary.plot(
        kind='bar',
        stacked=True,
        color=['#FF6B6B', '#4ECDC4'],     # Paid, Unpaid
        edgecolor='black', 
        linewidth=1.5,
        fontsize=20,
        ax=ax
    )
    ax.set_title('Fines Based on Violation Type', fontweight='bold', fontsize=20)
    ax.set_xlabel('Violation Type', fontweight='bold', fontsize=20)
    ax.set_ylabel('Total Fine Amount (₹)',fontweight='bold', fontsize=20)
    plt.xticks(rotation=20)
    plt.yticks(rotation=20)

    # Format Color Bar values, Y-axis values
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
    
    # Calculate totals for percentage calculation
    totals = summary.sum(axis=1)
    
    # Show Paid / Unpaid inside bars with Percentage
    for c in ax.containers:
        # Create custom labels with value and percentage
        labels = []
        for i, v in enumerate(c):
            height = v.get_height()
            if height > 0:
                percentage = (height / totals.iloc[i]) * 100
                labels.append(f'{percentage:.1f}%')
            else:
                labels.append('')
        ax.bar_label(c, labels=labels, label_type='center', fontsize=10, color='black', rotation=0, fontweight='bold')

    totals = summary.sum(axis=1)
    for idx, total in enumerate(totals):
        ax.text(
            idx,
            summary.iloc[idx].sum() + (max(totals) * 0.02),
            f'{total:,.0f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold', color='black'
        )
    
    plt.tight_layout()

    ax.legend(
        title="Status", 
        bbox_to_anchor=(1, 1.05), 
        loc="upper right", 
        ncol=2,
        title_fontsize=20,
        fontsize=20,
    )
    return fig

# =================================================================================
def plot_violations_by_location(location_based_violations):
    sns.set_theme(style='white')
    
    # 1. Create subplots to have better control over the object
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # 2. Plot the pie
    wedges, texts, autotexts = ax.pie(
        location_based_violations['No of Violations'],
        autopct='%1.1f%%',
        colors=sns.color_palette('pastel'),
        wedgeprops={'edgecolor': 'black'},
        pctdistance=0.85,
    )
    
    # 3. Handle Text Styling
    plt.setp(autotexts, size=20, weight="bold")
    
    # 4. Create a legend on the side to utilize the 16:9 width
    ax.legend(
        wedges, 
        location_based_violations['Location'],
        title="Locations",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1), # This pushes the legend outside to the right
        title_fontsize=20,
        fontsize=25,
    )
    
    ax.set_title("Violations by Location", fontsize=20, fontweight='bold')
    
    # 5. Enforce circular shape
    ax.axis('equal')
    
    # 6. Adjust layout to make room for the legend
    plt.tight_layout()
    
    return fig
# =================================================================================
# ---- Anshu's Plots ----
def plot_license_validity_by_gender(df):

    """
    Anshu: License Validity by Gender.
    """
    validity_gender = df.groupby(['License_Validity', 'Driver_Gender']).size().unstack(fill_value=0)
    
    fig, ax = plt.subplots(figsize=(16, 9))
    validity_gender.plot(
        kind='bar', 
        ax=ax,
        edgecolor='black', 
        linewidth=1.5,
        fontsize=20,
    )

    ax.set_title("Number of License Validities by Gender", fontsize=20, fontweight='bold')
    ax.set_xlabel("License Status", fontsize=20, fontweight='bold')
    ax.set_ylabel("Count", fontsize=20, fontweight='bold')
    ax.legend(title="Driver Gender", fontsize=20)
    plt.xticks(rotation=20)
    plt.yticks(rotation=20)
    plt.tight_layout()
    return fig



# ============================== Additional Plots ===================================================
# 1. Gender Distribution
def plot_gender_distribution(gender_distribution):
    """
    Plots the gender distribution of drivers.
    """
    sns.set_theme(style='darkgrid')
    fig, ax = plt.subplots(figsize=(18, 9))
    sns.barplot(
        x=gender_distribution.index, 
        y=gender_distribution.values, 
        hue=gender_distribution.index,
        legend=False,
        palette='viridis', 
        edgecolor='black', 
        linewidth=1.5,
        ax=ax
    )
    ax.set_title('Gender Distribution', fontweight='bold', fontsize=20)
    ax.set_xlabel('Gender', fontweight='bold', fontsize=20)
    ax.set_ylabel('Count', fontweight='bold', fontsize=20)
   
    plt.xticks(rotation=20, fontsize=20)
    plt.yticks(rotation=20, fontsize=20)
    return fig

# 2. Vehicle Type vs Violation Type (Monika's Contribution)
def plot_vehicle_type_vs_violation_type(df):
    """
    Monika: Vehicle type vs Violation Type.
    """
    sns.set_theme(style='darkgrid')
    fig, ax = plt.subplots(figsize=(16, 9))
    sns.countplot(
        data=df, 
        x='Violation_Type',
        hue='Vehicle_Type',
        ax=ax,
        palette='Set2',
        edgecolor='black'
    )
    ax.set_title('Vehicle Type vs Violation Type', fontsize=20, fontweight='bold')
    ax.set_xlabel('Violation Type', fontsize=20, fontweight='bold')
    ax.set_ylabel('Number of Violations', fontsize=20, fontweight='bold')
    ax.legend(title='Vehicle Type', fontsize=18, title_fontsize=20, bbox_to_anchor=(1, 1), loc='upper left')
    plt.xticks(rotation=20, fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    return fig

# 3. Severity Heatmap by Location (Mrunalini's Contribution)
def plot_severity_heatmap_by_location(df):
    """
    Mrunalini: Average Severity Score by Location and Violation Type.
    """
    # Helper to calculate severity (Internal logic kept same)
    def calc_severity_score(row):
        severity = 0
        if pd.notnull(row.get('Fine_Amount')): severity += row['Fine_Amount'] / 1000
        if pd.notnull(row.get('Penalty_Points')): severity += row['Penalty_Points'] 
        if pd.notnull(row.get('Recorded_Speed')) and pd.notnull(row.get('Speed_Limit')):
            if row['Recorded_Speed'] > row['Speed_Limit']:
                severity += (row['Recorded_Speed'] - row['Speed_Limit']) / 10
        if pd.notnull(row.get('Alcohol_Level')): severity += row['Alcohol_Level'] * 10
        if row.get('Helmet_Worn') == 'No': severity += 10
        if row.get('Seatbelt_Worn') == 'No': severity += 10
        if row.get('Traffic_Light_Status') == 'Red': severity += 15
        if pd.notnull(row.get('Previous_Violations')): severity += row['Previous_Violations'] * 1.5
        return severity

    # We need a copy to avoid SettingWithCopyWarning on the original df if modifying
    # But for dashboard summary df is passed, better to just apply
    # Optimizing: Calculate on the fly might be slow for full df, but for dashboard summary (last n days) should be fine.
    
    # We'll use a local copy to be safe
    local_df = df.copy()
    local_df['Violation_Severity_Score'] = local_df.apply(calc_severity_score, axis=1)
    
    location_heatmap = local_df.pivot_table(
        values='Violation_Severity_Score',
        index='Location',
        columns='Violation_Type',
        aggfunc='mean'
    )

    fig, ax = plt.subplots(figsize=(16, 9))
    sns.heatmap(
        location_heatmap, 
        cmap='coolwarm', 
        annot=True, 
        fmt=".1f", 
        ax=ax,
        annot_kws={"size": 12, "weight": "bold"},
        linewidths=1,
        linecolor='black',
    )
    ax.set_title("Average Severity Score by Location and Violation Type", fontsize=20, fontweight='bold')
    ax.set_xlabel('Violation Type', fontsize=20, fontweight='bold')
    ax.set_ylabel('Location', fontsize=20, fontweight='bold')
    plt.xticks(rotation=20, fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    return fig