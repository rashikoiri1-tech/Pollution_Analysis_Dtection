import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pollution dataset
pollution_data = {
    1: {"Category": "Air", "Pollution_Index": [70, 82, 91, 78, 67, 45, 99],
        "Quality_Score": [30, 18, 9, 8, 56, 34, 16]},
    2: {"Category": "Water", "Pollution_Index": [55, 67, 75, 78, 65, 45, 89],
        "Quality_Score": [45, 33, 25, 7, 13, 9, 14]},
    3: {"Category": "Noise", "Pollution_Index": [65, 78, 88, 78, 44, 76, 99],
        "Quality_Score": [35, 22, 12, 5, 13, 5, 10]},
    4: {"Category": "Soil", "Pollution_Index": [50, 60, 68, 78, 56, 66, 98],
        "Quality_Score": [50, 40, 32, 34, 42, 30, 20]}
}

def detect_pollution(choice):
    match choice:
        case 1: return "Air Pollution Detected: High PM levels and harmful gases."
        case 2: return "Water Pollution Detected: Chemical, plastic, and microbial impurities."
        case 3: return "Noise Pollution Detected: High decibel levels harmful to hearing."
        case 4: return "Soil Pollution Detected: Toxic chemicals and heavy metals present."
        case _: return "Invalid input. Please choose 1 to 4."

# User menu
print("Choose Pollution Type:")
print("1 - Air Pollution")
print("2 - Water Pollution")
print("3 - Noise Pollution")
print("4 - Soil Pollution")

try:
    choice = int(input("Enter your choice (1/2/3/4): "))
except ValueError:
    print("Please enter a number 1-4")
    exit()

# Detection message
print(detect_pollution(choice))

# Continue only if valid choice
if choice in pollution_data:
    data = pollution_data[choice]
    category = data["Category"]

    df = pd.DataFrame({
        "Pollution_Index": data["Pollution_Index"],
        "Quality_Score": data["Quality_Score"]
    })

    print(f"\nShowing detailed analysis for {category} Pollution...\n")
    print(df.describe()) # Bonus: show stats

    # Set style
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)

    # Create 2x2 subplot for all graphs
    fig, axes = plt.subplots(2, 2)
    fig.suptitle(f'{category} Pollution Analysis Dashboard', fontsize=16, fontweight='bold')

    # 1. Pie Chart
    axes[0,0].pie(df["Pollution_Index"], labels=[f"S{i+1}" for i in range(len(df))],
                  autopct="%1.1f%%", startangle=90)
    axes[0,0].set_title("Pollution Index Distribution")

    # 2. Bar Graph
    axes[0,1].bar([f"S{i+1}" for i in range(len(df))], df["Pollution_Index"], color='crimson')
    axes[0,1].set_title("Pollution Index Levels")
    axes[0,1].set_xlabel("Samples")
    axes[0,1].set_ylabel("Pollution Index")

    # 3. Scatter Plot
    axes[1,0].scatter(df["Pollution_Index"], df["Quality_Score"], c='green', s=100)
    axes[1,0].set_title("Index vs Quality Score")
    axes[1,0].set_xlabel("Pollution Index")
    axes[1,0].set_ylabel("Quality Score")

    # 4. Correlation Heatmap
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=axes[1,1])
    axes[1,1].set_title("Correlation Matrix")

    plt.tight_layout()
    plt.show()

    # Key insight
    correlation = df["Pollution_Index"].corr(df["Quality_Score"])
    print(f"\nKey Insight: Correlation between Pollution Index and Quality Score = {correlation:.2f}")
    if correlation < -0.5:
        print("Strong negative correlation: As pollution increases, quality drops sharply.")

else:
    print("Exiting. Run again with valid choice.")