# 05 — GitHub repositories

These repository URLs were checked on 2026-11-13. They are source references, not dependencies cloned by this lab.

- [apache/spark](https://github.com/apache/spark) — Spark's official source repository. Inspect `examples/src/main/python` for runnable Python examples and `python/pyspark/sql` for the API behind DataFrame operations. The examples show patterns beyond this lab, so read their prerequisites before trying them.
- [apache/spark-docker](https://github.com/apache/spark-docker) — Official Dockerfile source for the Spark image family. Inspect its Dockerfiles and README to understand what the container provides and why the lab needs no host Java installation.

For the lab itself, `lab.py` is the shortest example to study first: locate the read, the two transformations, `explain()`, and the `show()` action, then compare those steps with the larger upstream examples.
