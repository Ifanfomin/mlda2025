import pandas as pd

tables = pd.read_html("iris.html")
iris = tables[0]
iris.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
iris.to_csv("iris.csv", index=False)

print(iris.head())
