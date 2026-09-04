import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df = pd.read_csv('lab_1/ForeignGifts_edu.csv',low_memory=False)
print(df.head())

print(df["Gift Type"].describe(), '\n')

topCountryMoneyContribution = df.groupby("Country of Giftor")["Foreign Gift Amount"].sum().idxmax()
print(topCountryMoneyContribution, '\n')

topCountryGiftCount = df.groupby("Country of Giftor").size().idxmax()
print(topCountryGiftCount, '\n')

topCountryAverageGift = df.groupby("Country of Giftor")["Foreign Gift Amount"].mean().idxmax()
print(topCountryAverageGift, '\n')

topInstitutionMoneyReceived = df.groupby("Institution Name")["Foreign Gift Amount"].sum().idxmax()
print(topInstitutionMoneyReceived, '\n')

topInstitutionGiftCount = df.groupby("Institution Name").size().idxmax()
print(topInstitutionGiftCount, '\n')

sns.barplot(data=df.groupby("Institution Name").size().reset_index(name="Gift Count").nlargest(20, "Gift Count"), x="Gift Count", y="Institution Name", dodge=False, palette="viridis")

plt.title('Top 20 Institutions by Gift Count')
plt.xlabel('Gift Count')
plt.ylabel('Institution Name')
plt.show()

uniAverage = df.groupby("Institution Name")["Foreign Gift Amount"].sum().mean()
uniMedian = df.groupby("Institution Name")["Foreign Gift Amount"].sum().median()
print(uniAverage, '\n')
print(uniMedian, '\n')
# Reason for the mean being way bigger than the median is that the mean is affected by outliers, while the median is not. 
# In this case, there are some institutions that received very large gifts, which skews the mean upwards. 
# The median, on the other hand, represents the middle value of the data and is less influenced by extreme values.

sns.histplot(data=df.groupby("Institution Name")["Foreign Gift Amount"].sum().reset_index(), x="Foreign Gift Amount", bins=50, kde=True)
plt.axvline(uniAverage, color='red', linestyle='--', linewidth=2, label=f'Mean: ${uniAverage:,.0f}')
plt.axvline(uniMedian, color='green', linestyle='-', linewidth=2, label=f'Median: ${uniMedian:,.0f}')

plt.title('Distribution of Total Foreign Funding per University')
plt.xlabel('Total Funding Received (USD)')
plt.ylabel('Count of Universities')
plt.legend()
plt.show()

largestFlowCountryToInstitution = df.groupby(["Country of Giftor", "Institution Name"])["Foreign Gift Amount"].sum().reset_index().sort_values(by="Foreign Gift Amount", ascending=False).head(1).iloc[0]
print(largestFlowCountryToInstitution, '\n')

giftCrossTab = pd.crosstab(index=df["Country of Giftor"], columns=df["Institution Name"], values=df["Foreign Gift Amount"], aggfunc='sum', dropna=False).fillna(0)
print(giftCrossTab, '\n')

topUSGifters = df.groupby("Country of Giftor")["Foreign Gift Amount"].sum().sort_values(ascending=False).head(10)
print(topUSGifters, '\n')

df = pd.read_csv('lab_1/ForeignGifts_edu.csv',low_memory=False)
df.head()

#giftor = 'Giftor Name'
giftor = 'Country of Giftor'
recipi = 'Institution Name'
flow = 'Foreign Gift Amount'
N = 25

flows = (
    df.groupby([giftor, 
                recipi])
      [flow]
      .sum()
      .nlargest(N)
      .reset_index()
)

labels = (
    flows[giftor].tolist()
    + flows[recipi].tolist()
)

labels = list(dict.fromkeys(labels))

fig = go.Figure(
    go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=flows[giftor]
                        .map(labels.index),
            target=flows[recipi]
                        .map(labels.index),
            value=flows[flow]
        )
    )
)

fig.show()