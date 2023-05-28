# 2023-05-25
#  query = """
#  SELECT collection_name, nft_collateral_contract as address, AVG(apr) as mean, APPROX_QUANTILES(apr, 2)[OFFSET(1)] as median, STDDEV(apr) as std, COUNT(*) as count, SUM(usd_value) as borrow_volume
#  FROM `nftfi_loan_data.nftfi_loan_data`
#  WHERE date >= TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH)) AND apr <= 200
#  GROUP BY collection_name
#  HAVING count >= 20
#  """
#
#  Group the collection names and addresses in groups amongst which they are statistically similar.
#  Explain the reasoning. Perform plots with plotly if needed. Make sure to return the resulting clustering in a table format, add the loan count, dollar volume
#  corresponding to that collection, as well as mean, median and standard deviation of the APR corresponding to that collection_name.
#  The capacity to explain and interpret the results is very important. Have a preference for simple data science tools like box plots with ranges,
#  rather than complex ones. Make sure that the chosen moment which is used for clustering, for instance the mean, makes sense e.g. that there are enough loans in that
#  collection_name sample or that the standard deviation is not too big.
# I would like five clusters, one for median APR in the 0% to 10% range, then 20% to 30%, 30% to 50%, 50% to 70%, then 80% and above.
#
#  Return the table containing the name, address of that collection, as well as the loan count, dollar volume, mean APR, median APR, standard deviation of APR and of course the cluster number to which it belongs to. In the legend of the plot, keep the cluster numbers from 1 to 5 ordered.

from google.cloud import bigquery
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Define query
query = """
 SELECT collection_name, nft_collateral_contract as address, AVG(apr) as mean, APPROX_QUANTILES(apr, 2)[OFFSET(1)] as median, STDDEV(apr) as std, COUNT(*) as count, SUM(usd_value) as borrow_volume
 FROM `nftfi_loan_data.nftfi_loan_data`
 WHERE date >= TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 3 MONTH)) AND apr <= 200
 GROUP BY collection_name, address
 HAVING count >= 20
 """

# Execute query and convert results to pandas dataframe
df = bigquery_client.query(query).to_dataframe()

# Define clusters based on median APR range
df['cluster'] = pd.cut(df['median'], bins=[-0.1, 10, 30, 50, 70, 200], labels=[1, 2, 3, 4, 5])

# Create table with name, address, loan count, dollar volume, mean APR, median APR, standard deviation of APR, and cluster number
table = df[['collection_name', 'address', 'count', 'borrow_volume', 'mean', 'median', 'std', 'cluster']].sort_values(by='median')

# Create box plot to visualize clusters
fig = px.box(table, x='cluster', y='median', color='cluster', labels={'cluster': 'Cluster Number', 'median': 'Median APR'})
fig.update_layout(title='Clustering of Collections Based on Median APR', legend_title='Cluster Number')

# Display table and plot
st.write(table)
st.plotly_chart(fig)