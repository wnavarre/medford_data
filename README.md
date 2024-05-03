# Medford_Data Overview

This is some scripts and stuff to help you exploring Medford's assessment data *fast*. 

You'll want to have Docker installed. 

# Dropping in

To drop into the docker container, execute the file `./local_run`after having docker installed. It will take a while the first time. 

## Building something

Go into `intermediate` directory and look at the Makefile!

Stuff in the `output` directory is more likely to be cool and interesting stuff.

In the `intermediate` directory, type `make` followed by the path to the file you want to build. e.g. `make ./intermediate/with_small_apts.pqt`.

## Inspecting the results

Fire up `ipython3` and `import geopandas`. Then you can do `geopandas.read_parquet(<filename>)` in order to create a (geo-)pandas dataframe.

Look into geopandas and pandas dataframes FMI.
