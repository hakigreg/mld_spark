# 02 — Tutorial

## 1. Understand the job before running it

The input, `data/sales.csv`, contains six sales in three categories. `lab.py` reads it with an explicit schema, groups rows by `category`, sums `amount`, and sorts category names. The expected totals are books 20, games 50, and music 20. The grouping is the important step: each output row depends on multiple input rows, so Spark must bring values with the same category together. See [DataFrames and SQL](https://spark.apache.org/docs/4.3.0/sql-programming-guide.html).

The Python process is the driver. The `spark-submit` command in `Makefile` starts Spark in `local[2]` mode within a temporary Docker container. Local mode lets you practice the same DataFrame API used on clusters while keeping setup to one machine. The six-row data set is intentionally small; running a local Spark job here teaches behavior, not throughput.

## 2. Set up and run

Start Docker Engine/Desktop. From the repository root, run:

```sh
make setup
make run
```

`make setup` pulls the pinned official Spark image. `make run` mounts this folder read-only into the container and launches `/opt/spark/bin/spark-submit --master 'local[2]' /workspace/lab.py` with two local worker threads. The container disappears on exit. The job needs no running service afterward.

Startup messages can vary. Find the `TOTAL AMOUNT BY CATEGORY:` table:

```text
+--------+------------+
|category|total_amount|
+--------+------------+
|books   |20          |
|games   |50          |
|music   |20          |
+--------+------------+
```

Before that table, `explain()` prints a physical plan. Look for `Exchange`; Spark plans to redistribute rows around the group or sort. The exact operators and stage IDs can change between versions. The table is produced by `show()`, an action. `groupBy`, `agg`, and `orderBy` merely define the computation before it executes. See the [quick start](https://spark.apache.org/docs/4.3.0/quick-start.html) and [performance tuning guide](https://spark.apache.org/docs/4.3.0/sql-performance-tuning.html).

## 3. Change one input and predict the result

Open `data/sales.csv` in an editor. Change the row `3,games,30` to `3,games,40`. Predict the result before rerunning: the games total should become 60, while the others should remain 20. Run:

```sh
make run
```

Observe `games | 60`. The previous run did not leave a live DataFrame or cached result: this new application reads the changed CSV and computes the grouping again when `show()` runs. Change the row back to `3,games,30` to restore the baseline. The physical plan should still have the same broad shape because the operation did not change, only a value did.

If the command fails before the table appears, check that Docker is running and that the image pull completed. If Spark reports that `data/sales.csv` is missing, run `make run` from the project root because the Makefile mounts that directory. If `amount` contains non-integer text, restore a valid integer and rerun. These troubleshooting steps describe expected behavior; they are not additional verified lab paths.

## 4. Connect the exercise to real Spark work

An actual batch pipeline may read Parquet files or a table, filter and join millions of records, group them, and write a partitioned result. The same distinction between transformations and actions applies. A physical plan and Spark's Web UI help diagnose expensive scans, shuffles, skew, and repeated work. Streaming jobs can use a related DataFrame style, but require streaming sources, sinks, and checkpointing; this lab does not run one. See [Web UI](https://spark.apache.org/docs/4.3.0/web-ui.html) and [Structured Streaming](https://spark.apache.org/docs/4.3.0/streaming/getting-started.html).
