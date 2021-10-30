#%% Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% Initial Conditions 

prob_gain = 0.60
prob_loss = 1 - prob_gain

gain_mean_return = 100
loss_mean_return = 100

#%% Single Simultaion

num_trades = 5000
start_equity = 10000
capital_over_time = [start_equity]


for i in range(num_trades):
    if np.random.rand() < prob_gain:
        capital_over_time += [capital_over_time[-1] + gain_mean_return]
    else:
        capital_over_time += [capital_over_time[-1] - loss_mean_return]
        
plt.plot(capital_over_time);
        

#%% Multiple Simulation

prob_gain = 0.60
prob_loss = 1 - prob_gain

gain_mean_return = 100
loss_mean_return = 100

num_simulations = 100
np_simulations = np.array([])

for j in range(num_simulations):
    num_trades = 1000
    start_equity = 10000
    capital_over_time = [start_equity]
    
    for i in range(num_trades):
        if np.random.rand() < prob_gain:
            capital_over_time += [capital_over_time[-1]+gain_mean_return]
        else:
            capital_over_time += [capital_over_time[-1]-loss_mean_return]
            
    np_simulations = np.array(capital_over_time) if len(np_simulations) == 0 else np.vstack([np_simulations, np.array(capital_over_time)])


fig, ax = plt.subplots(figsize=(20,8))
for i in range(num_simulations):
    ax.plot(np_simulations.transpose()[:, i])

# %%
