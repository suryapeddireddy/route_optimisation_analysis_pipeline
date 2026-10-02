import pandas as pd
import numpy as np
import os


def generate_messy_fleet_data():
    print("Generating 50,000+ rows of messy fleet logs...")
    np.random.seed(42)

    # 1. Generate base data matrix
    num_records = 52000
    timestamps = pd.date_range(start="2026-09-01", periods=num_records, freq="10s")

    data = {
        "Log_ID": [f"LOG_{i:06d}" for i in range(num_records)],
        "Timestamp": timestamps.strftime("%Y-%m-%d %H:%M:%S"),
        "Vehicle_ID": np.random.choice(
            ["TRUCK_A", "TRUCK_B", "TRUCK_C", "TRUCK_D", "TRUCK_E"], size=num_records
        ),
        "Route_Code": np.random.choice(
            ["RT_101", "RT_102", "RT_103", "RT_104", "RT_105"], size=num_records
        ),
        "Transit_Time_Mins": np.random.normal(loc=42, scale=12, size=num_records).round(
            2
        ),
        "Fuel_Liters": np.random.normal(loc=25, scale=6, size=num_records).round(2),
        "Status": np.random.choice(
            ["Completed", "Delayed", "Completed", "Completed"], size=num_records
        ),
    }

    df = pd.DataFrame(data)

    # 2. Inject intentional messy data/bugs for the ATS project defense
    # Inject missing timestamps (approx 1% nulls)
    df.loc[df.sample(frac=0.01).index, "Timestamp"] = np.nan

    # Inject impossible negative values for transit times
    df.loc[df.sample(n=15).index, "Transit_Time_Mins"] = -99.0

    # Inject duplicate log rows
    df = pd.concat([df, df.sample(n=500)], ignore_index=True)

    # 3. Save to raw folder
    os.makedirs("data/raw", exist_ok=True)
    output_path = "data/raw/raw_fleet_telemetry.csv"
    df.to_csv(output_path, index=False)
    print(f"Done! Saved messy dataset to: {output_path} (Total rows: {len(df)})")


if __name__ == "__main__":
    generate_messy_fleet_data()
