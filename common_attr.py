import pandas as pd

file_path = "./ow2_season_01_FINAL_heroes_stats__2023-05-06.csv"
df = pd.read_csv(file_path)

hero_dict = df.groupby("Role")["Hero"].unique().to_dict()

return_attr = {}
for role in ["Damage", "Support", "Tank"]:
    heroes = hero_dict[role]
    role_df = df[df["Hero"].isin(heroes)]
    common_attr = []
    value_columns = [col for col in role_df.columns if col != 'Hero' and col != 'Skill Tier' and col != 'Role']
    for col in value_columns:
        if role_df[col].notnull().all():
            common_attr.append(col)
    return_attr[role] = common_attr

return_attr["All"] = list(
    set(return_attr["Damage"]) & set(return_attr["Support"]) & set(return_attr["Tank"])
)

print(return_attr)