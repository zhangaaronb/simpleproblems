import pandas as pd


def find_closest_sales(n_closest, sales_df, property_lat, property_lon):
    lats = sales_df.loc[:, 'lat']
    lons = sales_df.loc[:, 'long']
    dists_sq = (lats - property_lat) ** 2 + (lons - property_lon) ** 2
    closest_indices = dists_sq.nsmallest(n_closest).index
    return sales_df.loc[closest_indices, :]


'''
The runtime is linear in the number of rows of sales_df, as long as n_closest is constant (such as 10).
This runtime is the best possible, because it is necessary to read every row of sales_df.

If sales_df were constant and we wanted to improve the amortized runtime over multiple queries,
we could use a nearest neighbors data structure such as a k-d tree.
(A k-d tree also supports modifications between queries.)
'''


sales_df = pd.read_csv('sales.csv')
print(find_closest_sales(10, sales_df, 47.5112, -122.257))
