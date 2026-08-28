def format_parsing_rejects(record,run_id,source_file):
    row_record=record[1]
    error_reason=record[2]
    return (
        run_id,
        source_file,
        "PARSING",
        "UNKNOWN",
        row_record,
        error_reason

    )

def format_validation_rejects(record,run_id,source_file):
    row_record=record[1]
    error_reason=record[2]
    transaction_id=row_record[0]

    return (
        run_id,
        source_file,
        "VALIDATION",
        transaction_id,
        row_record,
        error_reason

    )
