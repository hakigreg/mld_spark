# 08 — Next iterations

Try these one at a time after the baseline exercise. They are suggestions, not implemented or verified paths in this lab.

1. **Add a row** to `data/sales.csv` with a new category. This teaches how an aggregate creates a new group; observe an extra row in the table.
2. **Add a `filter`** before `groupBy` in `lab.py`, for example keep `amount >= 15`. This teaches a narrow transformation before the shuffle; predict and observe changed totals.
3. **Replace the final `show()` with a Parquet write** to a writable mounted output directory. This teaches that writes are actions and Spark outputs a directory of part files; inspect the files and rerun behavior.
4. **Run a longer job with the Web UI enabled.** This teaches how jobs, stages, and tasks appear while the application is active; inspect the plan and shuffle metrics at port 4040 before the job exits.
5. **Read two small tables and join them** before grouping. This teaches join keys and additional data movement; compare `explain()` output and the final totals.
