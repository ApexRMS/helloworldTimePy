from osgeo import gdal

# Load SyncroSim python package
import pysyncrosim as ps

# Load numpy and pandas
import numpy as np
import pandas as pd

# Get the SyncroSim Scenario that is currently running
my_scenario = ps.Scenario()

# Load Run Control Datasheet to set timesteps
run_settings = my_scenario.datasheets(name="helloworldTimePy_RunControl")

# Set timesteps
timesteps = np.array(range(run_settings.MinimumTimestep.item(),
                           run_settings.MaximumTimestep.item() + 1))

# Load Scenario's input Datasheet from SyncroSim Library into DataFrame
my_input_dataframe = my_scenario.datasheets(name="helloworldTimePy_InputDatasheet")

# Extract model inputs from Input DataFrame
m = my_input_dataframe.m.item()
b = my_input_dataframe.b.item()

# Perform calculations
y = m * timesteps + b

# Put output values into new pandas DataFrame
my_output_dataframe = pd.DataFrame({"Timestep": timesteps, "y": y})

# Save the output DataFrame to the Scenario output Datasheet
my_scenario.save_datasheet(name="helloworldTimePy_OutputDatasheet",
                          data=my_output_dataframe)