def read_transection_file(sc,file_path):
    raw_rdd=sc.textFile(file_path)
    return raw_rdd