import pandas as pd

csv_path = "cities.csv"
cities_df = pd.read_csv(csv_path)

cities_df.to_html('output.html', index=False)
