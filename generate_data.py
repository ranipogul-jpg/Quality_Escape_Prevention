import pandas as pd
import numpy as np
from pathlib import Path

def generate_factory_data(samples=10000):
    np.random.seed(42)
    
    # 93% Normal products (0), 7% Defective products (1)
    is_defective = np.random.choice([0, 1], size=samples, p=[0.93, 0.07])
    
    # Categorical features
    shifts = np.random.choice(['Morning', 'Evening', 'Night'], size=samples)
    machine_ids = np.random.choice(['Machine_A', 'Machine_B', 'Machine_C'], size=samples)
    
    # Simulate factory sensor readings with realistic correlations to defects
    temperature = np.random.normal(70, 5, samples) + (is_defective * 9)
    pressure = np.random.normal(1.2, 0.1, samples) + (is_defective * 0.4)
    vibration = np.random.normal(15, 2, samples) + (is_defective * 5)
    speed = np.random.normal(100, 10, samples) - (is_defective * 18)
    tool_wear = np.random.uniform(0, 100, samples) + (is_defective * 25)
    humidity = np.random.normal(45, 5, samples)
    power = np.random.normal(50, 8, samples) + (is_defective * 12)
    
    # Build the DataFrame using your exact requested feature names
    df = pd.DataFrame({
        'Temperature': temperature,
        'Pressure': pressure,
        'Vibration': vibration,
        'Speed': speed,
        'ToolWear': tool_wear,
        'Humidity': humidity,
        'Power': power,
        'Shift': shifts,
        'MachineID': machine_ids,
        'Defect': is_defective
    })
    
    # Intentionally insert a few missing values in temperature and pressure for preprocessing tests
    df.loc[df.sample(frac=0.01).index, 'Temperature'] = np.nan
    df.loc[df.sample(frac=0.01).index, 'Pressure'] = np.nan
    
    # Automatically create the 'data/raw' folder if it doesn't exist and save as CSV
    output_path = Path("data/raw/factory_data.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"Success! Dataset created and saved as a CSV file at: {output_path}")

if __name__ == "__main__":
    generate_factory_data()