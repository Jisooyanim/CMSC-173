using Distributions
using Plots
using CSV
using DataFrames
using HypothesisTests

dataset = CSV.read("ex2_data.csv", DataFrame);
X = dataset[!,2];

## Step 1
fig1 = plot()
histogram(X,bins=20)