import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(df_path):
    # Read data using pandas
    df = pd.read_csv(df_path)
    # Convert duration from milliseconds to seconds
    df["duration_s"] = df["duration_ms"] / 1000
    # Drop the original 'duration_ms' column
    df = df.drop("duration_ms", axis=1)
    # print(df.head())
    return df


def calc_stats(df):
    numerical_columns = [
        "popularity",
        "duration_s",
        "explicit",
        "danceability",
        "energy",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "time_signature",
    ]

    # Initialize dict to store stats
    stats_dict = {"column": [], "mean": [], "median": [], "std_dev": []}

    # Calculate stats for each column
    for col in numerical_columns:
        mean_value = round(df[col].mean(), 2)
        median_value = round(df[col].median(), 2)
        std_dev_value = round(df[col].std(), 2)

        # Store results to dict
        stats_dict["column"].append(col)
        stats_dict["mean"].append(mean_value)
        stats_dict["median"].append(median_value)
        stats_dict["std_dev"].append(std_dev_value)

    # Convert dict to pandas DataFrame
    stats_df = pd.DataFrame(stats_dict)

    # Save DataFrame as an image
    fig, ax = plt.subplots(figsize=(12, len(stats_df) * 0.4))
    ax.axis("tight")
    ax.axis("off")
    # Create table
    table = ax.table(
        cellText=stats_df.values,
        colLabels=stats_df.columns,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(16)
    table.scale(1.5, 2.5)

    # Save table image to folder
    fig.savefig("resources/stats_df.png", bbox_inches="tight", dpi=300)
    plt.close()
    print(stats_df)
    print('Stats saved to resources/stats_df.png')
    return stats_df


def create_viz(df, save):
    plt.figure(figsize=(8, 4))

    # First subplot: histogram of duration
    plt.subplot(1, 2, 1)
    sns.histplot(df["duration_s"], bins=100, kde=True)
    plt.title("Distribution of Track Duration")
    plt.xlabel("Duration (in seconds)")
    plt.xlim(0, 800)
    plt.ylabel("Frequency")
    plt.grid(True)

    # Second subplot: scatterplot of loudness vs energy
    plt.subplot(1, 2, 2)
    sns.scatterplot(x="loudness", y="energy", data=df, s=20, alpha=0.3)
    plt.title("Song's Energy vs Volume")
    plt.xlabel("Loudness (in dB)")
    plt.ylabel("Energy")
    plt.grid(True)

    # Save and output
    plt.tight_layout()
    if save:
        plt.savefig("resources/plot.png", dpi=300, bbox_inches="tight")
    else:
        plt.show()

def create_viz_tempo(df, save):
    plt.figure(figsize=(5, 3))
    sns.histplot(df['tempo'], bins=10, kde=True, edgecolor='black')
    plt.title('Distribution of Tempo')
    plt.xlabel('Tempo')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Save and output
    plt.tight_layout()
    if save:
        plt.savefig("resources/plot_tempo.png", dpi=300, bbox_inches="tight")
    else:
        plt.show()
