"""
This script processes two datasets: shopping queries and product details. 

It performs the following steps:
1. Loads `shopping_queries_dataset_examples.parquet` and `shopping_queries_dataset_products.parquet`.
2. Merges them on `product_locale` and `product_id`.
3. Filters the data for three specific queries and the ESCI label "E".
4. Keeps relevant columns: `query`, `query_id`, `product_id`, `product_locale`, `product_title`, `product_description`, `product_bullet_point`, `product_brand`, `product_color`, and `esci_label`.
5. Saves the filtered dataset as a CSV file.

Output:
- A CSV file containing the filtered data.
"""


import pandas as pd


df_examples = pd.read_parquet('../data/shopping_queries_dataset_examples.parquet')
df_products = pd.read_parquet('../data/shopping_queries_dataset_products.parquet')

# Merge datasets
df_example_products = pd.merge(
    df_examples,
    df_products,
    how="left",
    left_on=["product_locale", "product_id"],
    right_on=["product_locale", "product_id"],
)

# Get the shape of df_example_products
print("Shape of df_example_products:", df_example_products.shape)

# Get unique values in esci_label column
unique_esci_labels = df_example_products["esci_label"].unique()
print("Unique values in esci_label column:", unique_esci_labels)


#Filter for the three queries and ESCI label "E"
queries = [
    "aa batteries 100 pack",
    "kodak photo paper 8.5 x 11 glossy",
    "dewalt 8v max cordless screwdriver kit, gyroscopic",
]


df_example_products["query_lower"] = df_example_products["query"].str.lower()

# Filter for queries (case-insensitive) and ESCI label "E"
df_filtered = df_example_products[
    (df_example_products["query_lower"].isin(queries)) & (df_example_products["esci_label"] == "E")
]

# Keep only the necessary columns
columns_to_keep = [
    "query", "query_id", "product_id",
    "product_title", "product_description", "product_bullet_point",
    "product_brand", "product_color", "esci_label"
]

df_final = df_filtered[columns_to_keep]

output_path = "../data/filtered_shopping_queries.csv"
df_final.to_csv(output_path, index=False)

print(f"CSV file saved at: {output_path}")
