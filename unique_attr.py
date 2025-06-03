import pandas as pd
import numpy as np

file_path = "./ow2_season_01_FINAL_heroes_stats__2023-05-06.csv"
df = pd.read_csv(file_path)

def get_common_attr(df):
    df = df[df['Skill Tier'] == 'All']
    return_dict = {}
    for hero in df['Hero'].unique():
        return_dict[hero] = []

    for col in df.columns:
        if df[col].notnull().sum() == 1:
            idx = df[df[col].notnull()].index[0]
            hero = df.loc[idx, 'Hero']
            return_dict[hero].append(col)

    return return_dict

common_attr = get_common_attr(df)
for i in common_attr:
    print(i, ":", common_attr[i])
# print(common_attr)

corr_dict = {}
for i, hero in enumerate(df['Hero'].unique()):
    hero_df = df.iloc[i * 8 : i * 8 + 8]
    hero_df = hero_df.fillna(hero_df.mean(numeric_only=True))
    corr = 0
    for attr in common_attr[hero]:
        if(np.isnan(np.corrcoef(hero_df['Win Rate, %'], hero_df[attr])[0, 1])):
            continue
        corr += np.abs(np.corrcoef(hero_df['Win Rate, %'], hero_df[attr])[0, 1])
    corr /= len(common_attr[hero])
    corr_dict[hero] = corr
        
sorting_corr = dict(sorted(corr_dict.items(), key=lambda x: x[1], reverse=True))

# for hero in sorting_corr:
#     print(hero, ':', sorting_corr[hero])