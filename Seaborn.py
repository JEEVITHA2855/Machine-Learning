Seaborn – Statistical Data Visualization

1️⃣ What is Seaborn?

Built on top of Matplotlib.
Integrated with Pandas.
Specially made for statistical plots.
Less code → prettier graphs.

👉 Import it:

import seaborn as sns
import matplotlib.pyplot as plt

2️⃣ Themes & Styles

Seaborn has built-in themes that instantly upgrade your plots.

sns.set_style("whitegrid")   # options: darkgrid, whitegrid, dark, white, ticks
sns.set_palette("pastel")    # colors: deep, muted, bright, pastel, dark, colorblind

3️⃣ Core Plot Types
🔹 1. Distribution Plots

Hist + KDE (smoothed curve)

data = sns.load_dataset("tips")
sns.histplot(data["total_bill"], bins=30, kde=True)
plt.show()


✔️ Shows how values are distributed.

🔹 2. Scatter Plots
sns.scatterplot(x="total_bill", y="tip", data=data, hue="sex", style="time")
plt.show()


✔️ Great for relationships between 2 variables.

🔹 3. Line Plot
sns.lineplot(x="size", y="total_bill", data=data, hue="sex")
plt.show()


✔️ Trends over continuous variables.

🔹 4. Bar Plot
sns.barplot(x="sex", y="tip", data=data, estimator=sum)
plt.show()


✔️ Compares categories (with aggregation like mean or sum).

🔹 5. Count Plot
sns.countplot(x="day", data=data)
plt.show()


✔️ Counts occurrences of categories.

🔹 6. Box Plot
sns.boxplot(x="day", y="total_bill", data=data, hue="sex")
plt.show()


✔️ Shows spread + outliers.

🔹 7. Violin Plot
sns.violinplot(x="day", y="total_bill", data=data, hue="sex", split=True)
plt.show()


✔️ Like boxplot but also shows distribution density.

🔹 8. Pair Plot
sns.pairplot(data, hue="sex")
plt.show()


✔️ Plots all pairwise relationships in dataset.

🔹 9. Heatmap (Correlation Matrix)
corr = data.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()


✔️ Visualizes correlations (great in EDA).

4️⃣ Customization

Colors

sns.histplot(data["tip"], color="red")
Titles (needs Matplotlib)
plt.title("Tip Distribution")
Figure size
plt.figure(figsize=(8,5))

5️⃣ Datasets in Seaborn

Seaborn comes with sample datasets for practice:

import seaborn as sns
print(sns.get_dataset_names())   # list all
tips = sns.load_dataset("tips")  # load "tips" dataset

6️⃣ When to Use What?

Histogram → Distribution of single variable
Scatter → Relationship between 2 variables
Line → Trend over time
Bar → Compare category averages
Count → Category frequency
Box/Violin → Spread + outliers
Pairplot → Explore all variables
Heatmap → Correlations
