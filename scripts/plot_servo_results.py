import os
import glob
import pandas as pd
import matplotlib.pyplot as plt


DATASET_DIR = "dataset"
FIGURES_DIR = "figures"


def ensure_output_dir():
    """Create figures directory if it does not exist."""
    os.makedirs(FIGURES_DIR, exist_ok=True)


def load_csv_files():
    """Load all CSV files from dataset directory."""
    pattern = os.path.join(DATASET_DIR, "*.csv")
    files = sorted(glob.glob(pattern))
    return files


def plot_variable(df, x_col, y_col, title, output_path):
    """Generate and save a single plot."""
    plt.figure(figsize=(10, 5))
    plt.plot(df[x_col], df[y_col], linewidth=2)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def plot_multi_variable(df, x_col, y_cols, title, output_path):
    """Generate and save a multi-line plot."""
    plt.figure(figsize=(10, 5))
    for col in y_cols:
        if col in df.columns:
            plt.plot(df[x_col], df[col], linewidth=2, label=col)
    plt.xlabel(x_col)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def process_file(file_path):
    """Read dataset and generate plots."""
    filename = os.path.basename(file_path)
    basename = os.path.splitext(filename)[0]

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return

    required_columns = [
        "time_s",
        "voltage_V",
        "current_A",
        "position_deg",
        "velocity_deg_s",
        "torque_Nm",
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        print(f"Skipping {filename}. Missing columns: {missing}")
        return

    print(f"Processing {filename}...")

    # Individual plots
    plot_variable(
        df,
        "time_s",
        "voltage_V",
        f"Voltage vs Time - {basename}",
        os.path.join(FIGURES_DIR, f"{basename}_voltage.png"),
    )

    plot_variable(
        df,
        "time_s",
        "current_A",
        f"Current vs Time - {basename}",
        os.path.join(FIGURES_DIR, f"{basename}_current.png"),
    )

    plot_variable(
        df,
        "time_s",
        "position_deg",
        f"Position vs Time - {basename}",
        os.path.join(FIGURES_DIR, f"{basename}_position.png"),
    )

    plot_variable(
        df,
        "time_s",
        "velocity_deg_s",
        f"Velocity vs Time - {basename}",
        os.path.join(FIGURES_DIR, f"{basename}_velocity.png"),
    )

    plot_variable(
        df,
        "time_s",
        "torque_Nm",
        f"Torque vs Time - {basename}",
        os.path.join(FIGURES_DIR, f"{basename}_torque.png"),
    )

    # Combined plot
    plot_multi_variable(
        df,
        "time_s",
        ["voltage_V", "current_A", "position_deg", "velocity_deg_s", "torque_Nm"],
        f"Combined Servo Variables - {basename}",
        os.path.join(FIGURES_DIR, f"{basename}_combined.png"),
    )

    print(f"Finished {filename}")


def main():
    """Main execution function."""
    ensure_output_dir()
    files = load_csv_files()

    if not files:
        print("No CSV files found in dataset/ directory.")
        return

    for file_path in files:
        process_file(file_path)

    print("All plots generated successfully.")


if __name__ == "__main__":
    main()
