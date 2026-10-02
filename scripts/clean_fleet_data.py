import pandas as pd
import numpy as np
import os


def clean_pipeline():
    print("Starting data cleaning pipeline...")
    raw_path = "data/raw/raw_fleet_telemetry.csv"
    processed_dir = "data/processed"

    # 1. Load the messy data
    if not os.path.exists(raw_path):
        print(f"Error: {raw_path} not found. Run generate_fleet_data.py first!")
        return

    df = pd.read_csv(raw_path)
    initial_count = len(df)
    print(f"Loaded {initial_count} raw rows.")

    # 2. Drop duplicate log entries
    df = df.drop_duplicates(subset=["Log_ID"])
    after_dupes = len(df)
    print(f"Removed {initial_count - after_dupes} duplicate rows.")

    # 3. Handle missing data variables (Drop rows with missing timestamps)
    df = df.dropna(subset=["Timestamp"])
    after_nulls = len(df)
    print(f"Removed {after_dupes - after_nulls} rows due to missing timestamps.")

    # 4. Fix anomalous outliers (Replace negative transit times with the median value)
    median_transit = df.loc[df["Transit_Time_Mins"] > 0, "Transit_Time_Mins"].median()
    df.loc[df["Transit_Time_Mins"] < 0, "Transit_Time_Mins"] = median_transit
    print(
        f"Fixed negative transit time anomalies using median replacement ({median_transit} mins)."
    )

    # 5. Format dates properly
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    # 6. Save the clean analysis-ready dataset
    os.makedirs(processed_dir, exist_ok=True)
    clean_path = os.path.join(processed_dir, "clean_fleet_telemetry.csv")
    df.to_csv(clean_path, index=False)

    final_count = len(df)
    integrity_margin = (final_count / initial_count) * 100
    print(f"Done! Cleaned data saved to: {clean_path}")
    print(
        f"Final usable rows: {final_count} | Data Integrity Margin: {integrity_margin:.2f}%"
    )


if __name__ == "__main__":
    clean_pipeline()
