def get_partition_record_count(rdd):
    def count_record(partition_index,records):
        count=0
        for record in records:
            count+=1
        yield (partition_index,count)
    return rdd.mapPartitionsWithIndex(count_record)