# Solar Energy Development Analysis

Explore the current solar development status quo in the United States

The raw data is from national solar radiation database(https://developer.nrel.gov/). It has extensive raw data for the past 20 years, which includes the temperature, solar irradiation, wind speed, location and so on. Each feature is in its own dataset and each one is as large as 70GB. 

## Geo Difference for Global Horizontal Irradiance(GHI).ipynb

Analysis to find out how solar radiation changes across the same year at different places. Taking 4 cities as a sample: NYC, Seattle, San Diego and Miami. The solar irradiation changes a lot for all of the cities throughout the year, which makes a lot of sense as we are in the north hemisphere, and will get more sunshine in the summer.  We can see distinctively that San Diego and Miami has overall better solar irradiation, however, the difference is more severe in the winter/spring time.

## Time Difference for Global Horizontal Irradiance(GHI).ipynb

Analysis to find out how the solar irradiation difference will look like at the different time in the same location. Taking NYS as a sample, pick the hottest time in the year of 2017 and 2007, and find out the difference is more or less evenly distributed across the state.

## Open Distributed PV Project in US.ipynb

The data source is from Berkeley Lab (https://emp.lbl.gov/tracking-the-sun). Download the data from the zip file. 

From prior analysis, Arizona and California has similar solar energy resource. For the currently installed distributed solar projects, California has the most projects, as much as 700,000. Followed by Arizona, where it has 100,000. But Arizona has the total biggest system size, as much as 1.4GW, which is twice the size of that in California, where it has 0.7GW. That’s why Arizona average solar system size is 14 times larger than California’s. 

Thus probably developing solar projects in Arizonais better choice over California.
