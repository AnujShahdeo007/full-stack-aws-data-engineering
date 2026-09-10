RDD E-Commerce Project - Raw Files

1. transactions_2026_08_21.csv - 25,000 transaction rows
2. transactions_2026_08_22.csv - 25,000 transaction rows
3. transactions_2026_08_23.csv - 25,000 transaction rows
   Total transaction rows: 75,000

4. customer_master.csv - 5,000 customer records
5. product_master.csv - 25 product records
6. payment_method_reference.csv - payment method reference/SLA data

The transaction files intentionally contain a small number of dirty records:
- missing city
- missing payment method
- UNKNOWN status
- amount mismatch
- missing customer_id
- zero quantity

These are included so the project can implement realistic validation,
reject handling, auditing, and production-style RDD transformations.
