#   # T0000001,C02286,P012,Cooking Oil,Grocery,3,937,2811,NETBANKING,FAILED,2026-08-21 03:30:47,Kolkata

def parse_transaction(row):
    try:

        fields=row.split(",")
        if len(fields) !=12:
            return (
                "INVALID",
                row,
                f"Expected_12_COLUMNS_FOUND_{len(fields)}"
            )
        transaction_id=fields[0].strip()
        customer_id=fields[1].strip()
        product_id=fields[2].strip()
        product_name=fields[3].strip()
        category=fields[4].strip()

        quantity=int(fields[5])
        unit_price=float(fields[6])
        amount=float(fields[7])

        payment_method=fields[8].strip()
        status=fields[9].strip()
        transaction_timestamp=fields[10].strip()
        city=fields[11].strip()

        parsad_records=(
            transaction_id,
            customer_id,
            product_id,
            product_name,
            category,
            quantity,
            unit_price,
            amount,
            payment_method,
            status,
            transaction_timestamp,
            city
        )

        return (
            "VALID",
            parsad_records,
            None
        )

    except ValueError as error:
        return (
            "INVALID",
            row,
            f"TYPE_CONVERSAION_ERROR:{str(error)}"
        )

    except Exception as error:
        return (
            "INVALID",
            row,
            f"UNEXPECTED_PARSING_ERROR:{str(error)}"
        )
    
