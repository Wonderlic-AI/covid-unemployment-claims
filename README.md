### COVID-19 and Unemployment Claims Projections

This project forecasts weekly unemployment claims in the United States as a result of the COVID-19 pandemic using IHME, Census, and Department of Labor unemployment claims data.

The model used is a long short-term memory (LSTM) neural network. This model was trained to predict the next period difference in unemployment claims, and was trained on state-level data for the first 11 weeks of the pandemic, starting with the week ending on February 22nd. Explicitly, the model is told the previous-week change in unemployment claims as well as IHME COVID-19 information from the previous three weeks. Also present in the training data is static state-level information from the Census Bureau Quickfacts data tool, including but not limited to information about population size, population density, demographics, and approximate number of pre-pandemic employers. Implicitly, LSTMs remember information for long periods of time and can draw conclusions about later periods based on information from much earlier periods.

For more information, see our article at: wonderlic.ai/blogs/covid-unemployment/

Data sources:
- IHME: https://covid19.healthdata.org/united-states-of-america
- Department of Labor Unemployment Claims: https://oui.doleta.gov/unemploy/claims_arch.asp
- Census QuickFacts: https://www.census.gov/quickfacts/fact/table/US/PST045219