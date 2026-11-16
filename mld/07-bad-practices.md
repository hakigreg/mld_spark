# 07 — Bad practices

These mistakes are common because Spark code can look like ordinary in-memory Python even though execution is distributed. See the [SQL/DataFrames guide](https://spark.apache.org/docs/4.3.0/sql-programming-guide.html), [performance tuning](https://spark.apache.org/docs/4.3.0/sql-performance-tuning.html), and [Web UI guide](https://spark.apache.org/docs/4.3.0/web-ui.html).

## Treating a transformation as an executed result

Writing `sales.groupBy("category").sum("amount")` defines a DataFrame; it does not by itself display computed totals. If you expect a side effect there, you may think the job ran when it did not. Use an explicit action such as `show()` for inspection or `write` for an output. The lab marks that boundary directly.

## Pulling a large dataset into the driver

Calling `collect()` or converting a huge DataFrame to pandas moves all selected rows to one process. That can crash the driver and erase the benefit of distributed processing. Filter and aggregate in Spark first, then collect only a bounded result. The lab uses `show()` on a three-row result; its tiny input cannot reveal the memory failure, but it models a safe inspection pattern.

## Ignoring shuffles, skew, and plan shape

A group or join may redistribute data across tasks. If one key contains most rows, one task can dominate runtime while others finish quickly. Adding more workers does not automatically fix that imbalance. Inspect the plan and Web UI metrics, reduce data before the shuffle when possible, and choose join or partition strategies based on the measured case. The lab's `Exchange` is the small visible version of this concern.

## Guessing types or accepting malformed input silently

An inferred CSV schema can change when sample data changes, and malformed numeric values may be parsed unexpectedly under permissive options. Incorrect types can turn a numeric calculation into an error or incorrect result. Define expected types and validate input quality. The lab declares an explicit schema, but production input validation would need additional checks.

## Caching everything and changing settings blindly

`cache()` consumes memory and may slow a one-use query. Setting a huge or tiny shuffle partition count without measuring can create task overhead or oversized tasks. First run a representative job, inspect its plan and metrics, then tune one bottleneck at a time. The lab keeps defaults and avoids caching because its input is trivial.

## Using Spark where coordination costs outweigh the work

Spark startup, scheduling, and shuffling cost time. A six-row CSV does not need Spark in a real application; this lab uses it so the execution model is visible. For genuinely small local data, a simple script or database query may finish sooner and be easier to operate. Choose Spark when parallel processing or its shared data platform capabilities solve a real problem.
