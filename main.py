import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create folders if not exist
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ---------------------------
# STEP 1: CREATE DATA
# ---------------------------
np.random.seed(42)
n = 200

data = pd.DataFrame({
    "Respondent_ID": range(1, n+1),
    "Region": np.random.choice(["North", "South", "East", "West"], n),
    "Age_Group": np.random.choice(["18-25", "26-35", "36-50"], n),
    "Response": np.random.choice(["Product A", "Product B", "Product C"], n)
})

data.to_csv("data/poll_data.csv", index=False)

print("\nDataset Preview:\n")
print(data.head())

# ---------------------------
# STEP 2: CLEAN DATA
# ---------------------------
data.dropna(inplace=True)

# ---------------------------
# STEP 3: ANALYSIS
# ---------------------------
counts = data["Response"].value_counts()
percentage = (counts / len(data)) * 100

summary = pd.DataFrame({
    "Count": counts,
    "Percentage": percentage
})

print("\nSummary:\n", summary)

# ---------------------------
# STEP 4: REGION ANALYSIS
# ---------------------------
region_analysis = pd.crosstab(data["Region"], data["Response"], normalize='index') * 100

print("\nRegion-wise Analysis:\n", region_analysis)

# ---------------------------
# STEP 5: VISUALIZATION
# ---------------------------

# Bar Chart
plt.figure()
sns.countplot(x="Response", data=data)
plt.title("Response Distribution")
plt.savefig("outputs/bar_chart.png")
plt.show()

# Pie Chart
plt.figure()
counts.plot.pie(autopct='%1.1f%%')
plt.title("Response Share")
plt.savefig("outputs/pie_chart.png")
plt.show()

# Region-wise Chart
region_analysis.plot(kind='bar', stacked=True)
plt.title("Region-wise Preferences")
plt.savefig("outputs/region_chart.png")
plt.show()

# ---------------------------
# STEP 6: INSIGHTS
# ---------------------------
top_product = counts.idxmax()
print(f"\nMost Preferred Product: {top_product}")