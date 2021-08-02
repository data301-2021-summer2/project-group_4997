df = (
    pd.read_csv('../../data/raw/AirQualityUCI.csv', sep=";")
    .drop(columns=["Unnamed: 15","Unnamed: 16"])
    .rename(columns={"CO(GT)":"CO", "PT08.S1(CO)": "Tin Oxide", "NMHC(GT)": "Avg. Benzene", "PT08.S2(NMHC)": "Titania", "NOx(GT)": "Avg. NO in ppb", "PT08.S3(NOx)": "Tungsten Oxide", 
                     "NO2(GT)": "NO2", "PT08.S4(NO2)": "Hr Avg. Tungsten Oxide", "PT08.S5(O3)": "Indium Oxide"})
    .dropna().reset_index(drop=True)
    .loc[:, ["Tin Oxide", "Titania", "Tungsten Oxide", "Indium Oxide", "T"]]
)

