import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression

# Read the updated data from a CSV file
updated_df = pd.read_csv('llm-mmlu.csv')

# Convert the 'Release Date' into a datetime object assuming the year is 2020+
updated_df['Release Date'] = updated_df['Release Date'].apply(lambda x: datetime.strptime('20' + x.split('-')[1] + '-' + x.split('-')[0], '%Y-%b'))

# Separate the updated dataframe into open and closed
updated_df_open = updated_df[updated_df['Model Type'].str.lower() == 'open']
updated_df_closed = updated_df[updated_df['Model Type'].str.lower() == 'closed']

# Define the linear_regression_dates function
def linear_regression_dates(df):
    X = mdates.date2num(df['Release Date']).reshape(-1, 1)
    y = df['MMLU Score'].values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_[0][0], model.intercept_[0]

# Perform linear regression for the average score lines on the updated data
slope_open_updated, intercept_open_updated = linear_regression_dates(updated_df_open)
slope_closed_updated, intercept_closed_updated = linear_regression_dates(updated_df_closed)

# Generate date range for plotting
start_date = min(updated_df['Release Date'])
end_date = max(updated_df['Release Date'])
date_range = pd.date_range(start=start_date, end=end_date, freq='MS')

# Apply the regression parameters to the date range for plotting for the updated data
line_open_updated = slope_open_updated * mdates.date2num(date_range) + intercept_open_updated
line_closed_updated = slope_closed_updated * mdates.date2num(date_range) + intercept_closed_updated

# Replot with linear regression lines for averages using the updated data
plt.figure(figsize=(12,8))

# Plot updated open models
for index, row in updated_df_open.iterrows():
    plt.scatter(row['Release Date'], row['MMLU Score'], color='green')
    plt.text(row['Release Date'], row['MMLU Score'] + 0.5, f"{row['Model']} ({row['Organization']})", fontsize=8, ha='center', va='bottom')

# Plot updated closed models
for index, row in updated_df_closed.iterrows():
    plt.scatter(row['Release Date'], row['MMLU Score'], color='red')
    plt.text(row['Release Date'], row['MMLU Score'] + 0.5, f"{row['Model']} ({row['Organization']})", fontsize=8, ha='center', va='bottom')

# Plot regression lines for updated data
plt.plot(date_range, line_open_updated, color='green', linestyle='--', label='Open Models')
plt.plot(date_range, line_closed_updated, color='red', linestyle='--', label='Closed Models')

# Formatting the date axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=4))
plt.gcf().autofmt_xdate() # Rotation

plt.title('MMLU Score of AI Models Over Time with Trend Lines', fontsize=16, fontweight='bold')
plt.xlabel('Release Date')
plt.ylabel('MMLU Score')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure and show the plot with updated data
trend_graph_updated_path = 'mmlu_score_graph.png'
plt.savefig(trend_graph_updated_path)
#plt.show()
