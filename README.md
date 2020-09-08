# How has the COVID-19 pandemic impacted Capital Bikeshare ridership?

The COVID-19 pandemic has had huge effects on American society.
One unforseen impact is the rate of bike ridership throughout the country (and the world!): 
Some bike shops are even having a hard time keeping up with demand. 
(Read about it in the NYT: https://www.nytimes.com/2020/05/18/nyregion/bike-shortage-coronavirus.html)

How have these effects impacted shared bike ridership, like the Capital Bikeshare system in the Washington DC area?

First, let's take a look of COVID-19 rates in the DC-MD-VA area (DC and suburbs of DC).
This data  was collected at the state level from the following websites:
 - DC: https://coronavirus.dc.gov/page/coronavirus-data
 - VA: https://data.virginia.gov/Government/VDH-COVID-19-PublicUseDataset-Cases/bre9-aqqr
 - MD: https://coronavirus.maryland.gov/datasets/mdcovid19-master-zip-code-cases
 
NameCensus (https://namecensus.com/igapo/zip_codes/metropolitan-areas/metro-zip/Washington%20(DC-MD-VA)1.html) defines the counties in the DC-Metropolitan area.
The data below has been filtered to only include DC and the MD and VA suburbs.

![new_covid_cases](https://github.com/mathyjokes/Cabi_COVID/blob/master/new_cases_dmv.png)
As the image shows, new COVID cases have remained relatively steady following a surge in May and June.

And now, onto shared bike ridership. Shared bikes have become a popular way of getting around DC as users rent the bikes to go short distances.
Capital Bikeshare publishes their data at at: https://s3.amazonaws.com/capitalbikeshare-data/index.html

A look at the past few years of Capital Bikeshare data shows the general increase in ridership.
Members (individuals who buy yearly subscriptions) take more trips than casual members.

![ridership_2018_2020](https://github.com/mathyjokes/Cabi_COVID/blob/master/cabi_ridership_per_memtype.png)

Since April 2020, however, this trend has reversed dramaticallly. DC issued a stay-at-home order beginning April 1, 2020, and Capital Bikeshare members took this seriously.
It is possible that many of the rides taken by these members (like the rides taken by mysef!) are used to get to work.
In the COVID-19 stay-at-home world, however, these rides are not happening.

![ridership_2020](https://github.com/mathyjokes/Cabi_COVID/blob/master/cabi_ridership_per_memtype_2020.png)

In fact, member and casual ridership since April 2020 has been highly correlated.
Looking at Capital Bikeshare rides over time, by year, shows an even starker picture of the impacts.
(Note that data from July and August 2019 was corrupted and not processed - to be fixed in a later iteration!)
While normal ridership follows seasonal patterns (higher in the summer, lower in the winter), 2020 bucks this trend.

![monthly_ridership](https://github.com/mathyjokes/Cabi_COVID/blob/master/ridership_per_month_comparison.png)

As DC continues to reopen, it appears that people are cautiously using Capital Bikeshare to move to their socially-distant activities.
Only time will tell if many of these casual riders become members of the Capital Bikeshare system later on!
