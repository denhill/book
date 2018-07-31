
# // tag::imports[]
from graphframes import *
# // end::imports[]

# // tag::load-graph-frame[]
v = spark.read.csv("data/sw-nodes.csv", header=True)
e = spark.read.csv("data/sw-relationships.csv", header=True)
g = GraphFrame(v, e)
# // end::load-graph-frame[]

# // tag::scc[]
from pyspark.sql import functions as F

result = g.stronglyConnectedComponents(maxIter=10)
result.sort("component") \
    .groupby("component") \
    .agg(F.collect_list("id")) \
    .show(truncate=False)
# // end::scc[]