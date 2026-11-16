# 06 — Best practices

These practices apply to common Spark batch and streaming work. The lab uses only the ones needed for its small batch job. See the [SQL/DataFrames guide](https://spark.apache.org/docs/4.3.0/sql-programming-guide.html), [performance tuning](https://spark.apache.org/docs/4.3.0/sql-performance-tuning.html), and [Structured Streaming guide](https://spark.apache.org/docs/4.3.0/streaming/getting-started.html).

## Use structured operations and deliberate schemas

For tabular data, prefer DataFrame or SQL expressions such as `filter`, `groupBy`, and `sum`. Spark sees column types and operations and can optimize the plan. The lab declares `amount` as an integer, so `sum` is numeric and its expected result is clear. With real data, establish a schema contract and decide how to handle malformed records; CSV schema assignment alone is not a complete validation strategy. Use RDDs when you genuinely need their lower-level control, not by default for ordinary tables.

## Check the plan and measure before tuning

Call `explain()` or inspect the SQL and Stages tabs in the Web UI to see scans, exchanges, joins, and task counts. A `groupBy` may shuffle data; a join may move a large table. Tune based on observed costs, not a fixed set of magic settings. The lab prints a plan and invites you to find `Exchange`. For real jobs, compare input size, shuffle bytes, task duration, and skew before changing `spark.sql.shuffle.partitions` or repartitioning data.

## Keep data distributed until the result is small

Use distributed filters and aggregates before bringing data to the driver. `show()` is appropriate here because the output has only three rows. In production, a large `collect()` can exhaust driver memory even when executors handle the source data. If the result is large, write it to storage instead of returning all rows to Python.

## Choose useful storage and partitioning

CSV is transparent for this exercise. For repeated large analytical reads, columnar formats such as Parquet often reduce I/O and provide typed columns. Partition output by fields that meaningfully narrow reads, but avoid creating huge numbers of tiny files. A partition is also a unit of Spark work: too few partitions underuse resources, while too many add scheduling and small-file overhead. Start with defaults and adjust after measuring a real workload.

## Reuse computation only when it is reused

Caching can help when the same expensive intermediate DataFrame feeds several actions. It consumes executor memory and must itself be materialized, so cache only when repeated work justifies it; unpersist when finished. This lab runs one `show()` action and therefore does not cache anything.

## Design outputs and recovery deliberately

Real pipelines should write to a known destination and make reruns predictable. Define whether a run appends, replaces, or merges data, and check for duplicate or partial results. For Structured Streaming, configure a durable checkpoint and a compatible sink so progress can recover after failures. This lab has no persistent output or streaming query; its only result is the displayed table.
