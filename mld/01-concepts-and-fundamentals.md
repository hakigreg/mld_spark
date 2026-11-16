# 01 — Concepts and fundamentals

## What Spark does

Apache Spark is an engine for processing data with work spread across cores or machines. You write a computation in Python, SQL, Scala, or Java; Spark plans and runs many tasks over pieces of the data. It is most useful when the data or computation is large enough that parallel work and a shared execution engine outweigh setup and data-movement costs. Spark can run on one laptop or on a cluster. It is an execution engine, not a database that stores your source data for you.

This lab runs real Spark on one machine. Six CSV rows are deliberately too small to benefit from parallelism. They make the execution model easy to see.

## Driver, executors, tasks, and partitions

The **driver** runs your application code, creates a `SparkSession`, builds a plan, and coordinates execution. **Executors** run tasks and hold data used during execution. A **task** works on one partition for a stage. A **partition** is one slice of a distributed dataset; its size and placement influence parallelism and data movement. In local mode, these roles exist on one host rather than on separate cluster machines. `local[2]` gives the lab two local worker threads; it does not launch a two-node cluster.

The `SparkSession` is the usual entry point for DataFrame and SQL work. The lab creates one session, reads the CSV, runs one computation, and stops the session. In a cluster, a cluster manager such as Spark Standalone, Kubernetes, or YARN allocates resources for the application. None is needed for this local exercise. See the [Spark overview](https://spark.apache.org/docs/4.3.0/) and [cluster overview](https://spark.apache.org/docs/4.3.0/cluster-overview.html).

## DataFrames, schema, and SQL

A **DataFrame** is a collection of rows with named, typed columns. Spark can read files and other sources into DataFrames, then apply relational operations such as select, filter, join, and aggregate. Spark SQL expresses many of the same operations with SQL text; DataFrame code and SQL use the same underlying engine. Python also has the older, lower-level RDD API. Learn DataFrames first for structured data because schema information helps Spark plan and optimize operations. Python does not expose the statically typed Dataset API used in Scala and Java. See the [SQL and DataFrames guide](https://spark.apache.org/docs/4.3.0/sql-programming-guide.html).

In the lab, `sales` has `order_id` and `amount` as integers and `category` as a string. The explicit schema avoids guessing column types from a tiny file. In real pipelines, validate data against the schema: a malformed CSV value can become null or trigger a parsing behavior that needs deliberate handling.

## Transformations, actions, and lazy execution

A **transformation** defines a new DataFrame from an existing one. The lab's `groupBy(...).agg(...)` and `orderBy(...)` build a computation. An **action** requests a result, such as `show()`, `count()`, `collect()`, or writing to storage. Spark delays most execution until an action, so it can plan the work as a whole. Reading a file can still involve metadata checks before an action; “lazy” does not mean no work at all happens earlier. The lab calls `explain()` to print a plan and `show()` to execute and display the rows. See the [quick start](https://spark.apache.org/docs/4.3.0/quick-start.html).

Spark divides execution into **jobs**, **stages**, and **tasks**. A job is triggered by an action. Stages are separated by operations that require data exchange. Within a stage, tasks process partitions in parallel. The physical plan printed by the lab shows `Exchange` around the aggregation or sort. That is a **shuffle**: Spark repartitions data so rows with the same grouping key can be combined. Spark can partially aggregate before the exchange to reduce the data moved. With six rows, this is observable as a plan, not a performance win. See [performance tuning](https://spark.apache.org/docs/4.3.0/sql-performance-tuning.html) and the [Web UI guide](https://spark.apache.org/docs/4.3.0/web-ui.html).

## Typical workflow and boundaries

A common batch workflow is: read data, define a schema, transform and aggregate, inspect the plan, run an action, and write results. The same DataFrame engine also supports joins, table formats, and Structured Streaming queries. Spark does not automatically make a poor data model or expensive shuffle cheap. A driver has finite memory; sending all rows to it with `collect()` can fail even when the distributed computation fits. Spark startup and coordination have overhead, so a tiny local file is often better handled by simpler tools outside a learning lab.

The lab demonstrates a batch CSV read, DataFrame aggregation, a physical plan, and a local action. It does not demonstrate cluster deployment, production ingestion, fault recovery, streaming, or reliable output storage. Those build on the same concepts but need their own examples and checks.
