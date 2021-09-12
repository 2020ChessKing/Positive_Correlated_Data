#   imports
import csv, plotly.express as plotly;

#   code
with open(r"C:\Swarup\WhiteHat Jr\Python\Projects\Correlation\data.csv") as data:
    framed_data = csv.DictReader(data)
    scatter_graph = plotly.scatter(framed_data, x="Coffee in ml", y="sleep in hours")
    scatter_graph.show()

