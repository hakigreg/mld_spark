# 04 — Essential links

These Apache Spark and Docker documentation URLs were checked on 2026-11-13. The Spark guides are pinned to version 4.3.0, matching this lab's image. The PySpark installation page uses `latest`, which was 4.3.0 when checked and may advance later.

- [Spark 4.3.0 overview](https://spark.apache.org/docs/4.3.0/) — Start here for supported runtimes, Spark components, and the documentation map.
- [Quick start](https://spark.apache.org/docs/4.3.0/quick-start.html) — Short examples of creating DataFrames, transformations, actions, and `spark-submit`.
- [Spark SQL and DataFrames guide](https://spark.apache.org/docs/4.3.0/sql-programming-guide.html) — Explains the structured API used in `lab.py` and its relationship to SQL.
- [PySpark installation](https://spark.apache.org/docs/latest/api/python/getting_started/install.html) — Useful if you later run Spark without Docker; lists Python and Java requirements.
- [Performance tuning](https://spark.apache.org/docs/4.3.0/sql-performance-tuning.html) — Introduces shuffle partitions, caching, join choices, and plan-related tuning.
- [Web UI](https://spark.apache.org/docs/4.3.0/web-ui.html) — Shows where to inspect jobs, stages, tasks, SQL plans, and shuffle metrics in a longer-running application.
- [Structured Streaming getting started](https://spark.apache.org/docs/4.3.0/streaming/getting-started.html) — The next starting point for live data; streaming is outside this lab.
- [Official Spark Docker image](https://hub.docker.com/_/spark/) — Describes the image family used by `Makefile` and its available tags.
