import pandas as pd

df = pd.read_csv('lab_1/ForeignGifts_edu.csv',low_memory=False)

uvadf = df[df['Institution Name'] == 'University of Virginia']

uvaCountryGiftAmounts = uvadf.groupby('Country of Giftor')['Foreign Gift Amount'].agg(['sum', 'count', 'mean', 'median']).sort_values('sum', ascending=False)
print(uvaCountryGiftAmounts, '\n')

uvaGiftTypeAmount = uvadf.groupby("Gift Type")["Foreign Gift Amount"].agg(["count", "sum", "mean", "median"]).sort_values("sum", ascending=False)
print(uvaGiftTypeAmount, '\n')

uvaMarketShare = uvadf["Foreign Gift Amount"].sum() / df["Foreign Gift Amount"].sum() * 100
print(f"UVA's market share: {uvaMarketShare:.2f}%")

peerInstitutions = ['Harvard University', 'Stanford University', 'Yale University', 'Massachusetts Institute of Technology', 'Duke University', 'Princeton University']

peerUVAData = df[df["Institution Name"].isin(["University of Virginia"] + peerInstitutions)].groupby("Institution Name")["Foreign Gift Amount"].agg(["count", "sum", "mean", "median"]).sort_values("sum", ascending=False)
print(peerUVAData, '\n')

peerData = df[df["Institution Name"].isin(peerInstitutions)].groupby("Country of Giftor")["Foreign Gift Amount"].agg(["count", "sum", "mean", "median"]).sort_values("sum", ascending=False)
print(peerData, '\n')

marketData = df.groupby("Country of Giftor")["Foreign Gift Amount"].agg(["count", "sum", "mean", "median"]).sort_values("sum", ascending=False)
print(marketData, '\n')