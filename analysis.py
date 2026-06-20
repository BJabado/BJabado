import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load dataset
df = pd.read_csv("supermarket.csv")
df.columns = df.columns.str.strip()

# 2. Analytics: Grouping by Category and Sub-Category for Total Sales
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
sub_category_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).reset_index()

# 3. Setting up a high-quality visualization layout
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Chart 1: Sales Distribution by Core Category
axes[0].pie(
    category_sales["Sales"], 
    labels=category_sales["Category"], 
    autopct="%1.1f%%", 
    startangle=140, 
    colors=["#3498db", "#2ecc71", "#e74c3c"]
)
axes[0].set_title("Sales Distribution by Core Category")

# Chart 2: Top 10 Sub-Categories by Total Sales Revenue
# Changed 'Viridis' to lowercase 'viridis' to prevent library crashing
sns.barplot(
    x="Sales", 
    y="Sub-Category", 
    data=sub_category_sales.head(10), 
    ax=axes[1], 
    palette="viridis" 
)
axes[1].set_title("Top 10 Product Sub-Categories by Revenue")
axes[1].set_xlabel("Total Sales Revenue ($)")
axes[1].set_ylabel("Product Sub-Category")

plt.tight_layout()

# Save image for your GitHub repository README
plt.savefig("portfolio_sales_analysis.png", dpi=300)
plt.show()

print("\n--- Project Metrics Calculated Successfully ---")
print(sub_category_sales.head(5).to_string(index=False))