import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


def run_eda_bottlenecks():
    print("Running Exploratory Data Analysis (EDA) pipeline...")
    clean_path = "data/processed/clean_fleet_telemetry.csv"

    if not os.path.exists(clean_path):
        print(f"Error: {clean_path} not found. Run clean_fleet_data.py first!")
        return

    # 1. Load clean metrics dataset
    df = pd.read_csv(clean_path)

    # 2. Isolate Route Bottlenecks using NumPy grouping conditions
    # Define a high delay threshold as transit times exceeding 50 minutes
    df["Is_Delayed"] = np.where(df["Transit_Time_Mins"] > 50, 1, 0)

    route_metrics = (
        df.groupby("Route_Code")
        .agg(
            Total_Trips=("Log_ID", "count"),
            Avg_Transit_Time=("Transit_Time_Mins", "mean"),
            Avg_Fuel_Consumed=("Fuel_Liters", "mean"),
            Delay_Incident_Count=("Is_Delayed", "sum"),
        )
        .reset_index()
    )

    # Calculate operational delay rate per route layout
    route_metrics["Delay_Rate_%"] = (
        route_metrics["Delay_Incident_Count"] / route_metrics["Total_Trips"] * 100
    ).round(2)

    print("\n--- Route Operational Performance Summary ---")
    print(route_metrics.to_string(index=False))

    # 3. Save calculated analytical summary data structures for Power BI ingestion
    os.makedirs("data/processed", exist_ok=True)
    summary_out = "data/processed/route_bottleneck_summary.csv"
    route_metrics.to_csv(summary_out, index=False)
    print(f"\nSummary metrics exported for reporting dashboards to: {summary_out}")

    # 4. Generate visual distribution tracking trends using Matplotlib and Seaborn
    print("\nGenerating performance plots...")
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")

    # Plot average transit times by operational route codes
    sns.barplot(
        data=route_metrics, x="Route_Code", y="Avg_Transit_Time", palette="viridis"
    )
    plt.title(
        "Average Transit Time Allocation Across Delivery Routes", fontsize=14, pad=15
    )
    plt.xlabel("Route Code Tag", fontsize=12)
    plt.ylabel("Mean Transit Duration (Mins)", fontsize=12)

    # Save the plot asset
    os.makedirs("reports", exist_ok=True)
    plot_path = "reports/route_transit_performance.png"
    plt.savefig(plot_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Operational data plot successfully generated at: {plot_path}")


if __name__ == "__main__":
    run_eda_bottlenecks()
