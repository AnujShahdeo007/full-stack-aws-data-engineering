from src.spark_session import create_spark_context
from src.ingestion import read_transaction_file,remove_header
from src.partition_utils import get_partition_record_count
from src.parser import parse_transaction


def main():

    sc = create_spark_context()

    try:

        file_path = "data/raw/transactions_2026_08_21.csv"

        raw_rdd = read_transaction_file(
            sc,
            file_path
        )

        header,data_rdd=remove_header(raw_rdd)

        print("Header: ",header)
        print("Records after removing header:",data_rdd.count())

        parsed_rdd=data_rdd.map(parse_transaction)

        valid_parsad_rdd=parsed_rdd.filter(
            lambda record:record[0]=="VALID"
        )
        invalid_parsad_rdd=parsed_rdd.filter(
            lambda record:record[0]=="INVALID"
        )

        valid_transaction_rdd=valid_parsad_rdd.map(lambda record:record[1])

        print("Valid parsed sample")
        for record in valid_transaction_rdd.take(3):
            print(record)

        print("Invalid Parsing samples ")
        for record in invalid_parsad_rdd.take(3):
            print(record)

        # sample_records=parsed_rdd.take(3)
        # print("parsad records: ")
        # for record in sample_records:
        #     print(record)

        # print("Transaction file loaded successfully")
        # first_record = raw_rdd.first()

        # print("First record - HEADER:")
        # print(first_record)
        # T0000001,C02286,P012,Cooking Oil,Grocery,3,937,2811,NETBANKING,FAILED,2026-08-21 03:30:47,Kolkata
        total_records=raw_rdd.count()
        print("Total records including header:",total_records)

        print("Number of partitions",raw_rdd.getNumPartitions())

        partition_count_rdd=get_partition_record_count(raw_rdd)
        partition_count=partition_count_rdd.collect()
        print("Records per partition")

        for partition_index,count in partition_count:
            print(
                f"Partition {partition_index}: {count} records"
            )


    finally:

        sc.stop()


if __name__ == "__main__":
    main()