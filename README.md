# Minimum Lab Deployment: Apache Spark

This lab teaches one Spark fundamental: describe a distributed DataFrame transformation, then run an **action** that computes it. A local Spark job reads six CSV rows, groups them by category, sums the amounts, and prints the result and physical plan.

## Mental model

Your Python program is the **driver**. Spark reads the CSV into a DataFrame whose rows can be split into **partitions**. `groupBy` and `orderBy` describe transformations; they do not produce the displayed table by themselves. `show()` is an action that asks Spark to execute the plan. The plan contains an `Exchange` because grouping or sorting may require a **shuffle**: redistributing rows between tasks. `local[2]` runs two worker threads on one machine, so this demonstrates Spark's programming model without a cluster. The tiny CSV is for learning, not a performance comparison with pandas or a database.

## Prerequisites and setup

- Docker Engine/Desktop running, with a few GB of free disk space for the Spark image.
- `make` and an internet connection for the first image pull.
- No host Java or Python installation is needed.

From the project root:

```sh
make setup
```

This pulls the official Docker Spark image `spark:4.3.0-scala2.13-java17-python3-ubuntu`.

## Run

```sh
make run
```

The job runs in a temporary container, mounts this project read-only, and exits when finished. Look for the physical plan and this table among Spark's startup messages:

```text
+--------+------------+
|category|total_amount|
+--------+------------+
|books   |20          |
|games   |50          |
|music   |20          |
+--------+------------+
```

The physical plan's exact text can vary, but it should contain `Exchange`, showing that Spark planned data movement for the aggregation or sort.

## Exercise: change, predict, observe

1. Open `data/sales.csv` and change the `games` row with `order_id` 3 from `30` to `40`.
2. Predict the new `games` total, then run `make run` again.
3. Observe `games | 60` while `books` and `music` stay at `20`. This shows that Spark rereads the CSV and recomputes the aggregation when `show()` runs.
4. Change that amount back to `30` to restore the starting example.

The container stops automatically after each run. If you interrupt a run, press `Ctrl+C`; `--rm` removes the stopped container. The project contains no persistent Spark service or output volume.

## Files and learning guide

| File | Purpose |
| --- | --- |
| `Makefile` | Versioned image and exact local `spark-submit` command. |
| `lab.py` | DataFrame read, transformation, plan, and action. |
| `data/sales.csv` | Small input for the exercise. |
| [`mld/01-concepts-and-fundamentals.md`](mld/01-concepts-and-fundamentals.md) | Spark's core model and terms. |
| [`mld/02-tutorial.md`](mld/02-tutorial.md) | Guided run and exercise. |
| [`mld/03-use-cases.md`](mld/03-use-cases.md) | Where Spark is useful. |
| [`mld/04-essential-links.md`](mld/04-essential-links.md) | Official documentation. |
| [`mld/05-github-repositories.md`](mld/05-github-repositories.md) | Source and examples. |
| [`mld/06-best-practices.md`](mld/06-best-practices.md) | Sound Spark habits. |
| [`mld/07-bad-practices.md`](mld/07-bad-practices.md) | Common mistakes. |
| [`mld/08-next-iterations.md`](mld/08-next-iterations.md) | Small follow-up experiments. |
