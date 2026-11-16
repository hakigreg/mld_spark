# 03 — Use cases

Spark is useful when processing is large, parallel, or shared across a data platform. This lab's tiny CSV represents the shape of a batch aggregation, but scale is the reason most teams choose Spark. See the [Spark overview](https://spark.apache.org/docs/4.3.0/) and [SQL/DataFrames guide](https://spark.apache.org/docs/4.3.0/sql-programming-guide.html).

## Batch analytics and ETL

A retailer can read transaction files, clean invalid rows, join product information, and produce daily revenue by category. DataFrames provide one API for reading, filtering, joining, aggregating, and writing. Spark can schedule work over many partitions, so it fits data too large for a single process. The costs are startup, cluster resources, and shuffles for joins or grouping; for a small daily CSV, a database query or local script may be simpler. The lab implements only the final grouping shape, with no cleaning, join, or output table.

## Large SQL queries and lakehouse processing

An analyst can query tables stored in files such as Parquet and combine them with SQL or DataFrame operations. Spark can use schema and statistics to optimize scans and joins. File layout, partitioning, and table formats matter: thousands of small files or an unsuitable join can dominate runtime. The lab shows schema and a physical plan, but reads CSV and does not create a lakehouse table. See [SQL performance tuning](https://spark.apache.org/docs/4.3.0/sql-performance-tuning.html).

## Event streams

A service can count events by time window or enrich them as they arrive. Structured Streaming expresses an incremental query with DataFrame-like operations and uses checkpoints and suitable sinks to recover progress. It fits sustained streams where state, fault tolerance, and integration with data sources matter. It also adds operational complexity and latency considerations; a one-off batch job is easier when live updates are unnecessary. The lab is batch only, so rerunning it rereads the whole CSV. See [Structured Streaming getting started](https://spark.apache.org/docs/4.3.0/streaming/getting-started.html).

## Feature preparation and machine learning

A data science team can clean and join large training datasets, create features, and use MLlib pipelines for some distributed learning tasks. Spark is especially useful for preparing data before training when raw inputs do not fit comfortably on one machine. Not every algorithm benefits from distributed execution, and model training may use other specialized frameworks after feature extraction. The lab's typed columns and aggregation are simple feature-engineering building blocks, but it trains no model. See the [MLlib guide](https://spark.apache.org/docs/4.3.0/ml-guide.html).

## Log and observability analysis

An operations team can read many log files, parse fields, group errors by service, and investigate trends over time. Spark handles large file collections and parallel transformations well. It is less suitable for very low-latency point lookups than an indexed search system. The lab's group-by is analogous to an error count by service, but it has no log parser or search interface.

Across these examples, start by asking whether the dataset and workflow justify Spark's coordination and data-movement costs. The core read → transform → action pattern is transferable; the surrounding storage, reliability, and operations choices depend on the use case.
