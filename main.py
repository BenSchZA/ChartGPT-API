
from analytics_bot_langchain.data.bigquery_pipeline import clean_csv_files_and_save_to_bigquery, Datatype
from analytics_bot_langchain.data.dune.execute_query import run_query

tables_id = {
        "nft_lending_aggregated_borrow": 1205836,
        "nft_lending_aggregated_repay": 1227068,
        "dex": 2421110,
}


def query_dune_api_and_save_dataset_to_bq(table_name: str, query_id: int, datatype: Datatype):
    # run_query(file_name=table_name, datatype=datatype, query_id=query_id)
    clean_csv_files_and_save_to_bigquery(table_name=table_name, datatype=datatype)


table_name = "nft_lending_aggregated_repay"
datatype = Datatype.nftfi

# table_name = "dex"
# datatype = Datatype.dex

query_dune_api_and_save_dataset_to_bq(table_name=table_name, query_id=tables_id[table_name], datatype=datatype)


