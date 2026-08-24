from src.spark_session import create_spark_context
from src.ingestion import read_transection_file
def main():
    sc=create_spark_context
    try:
        file_path="data/raw/transactions_2026_08_21.csv"
        raw_rdd=read_transection_file(
            sc,
            file_path
        )
        print("Transection file loaded sucessfully")
    finally:
        sc.stop()

if __name__=="__main__":
    main()