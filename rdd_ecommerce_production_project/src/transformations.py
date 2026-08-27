def format_parsing_rejects(record):
    status=record[0]
    row_record=record[1]
    error_reason=record[2]
    return (
        "PARSING",
        row_record,
        error_reason

    )

def format_validation_rejects(record):
    status=record[0]
    row_record=record[1]
    error_reason=record[2]

    return (
        "VALIDATION",
        row_record,
        error_reason

    )
