SPARK_IMAGE := spark:4.3.0-scala2.13-java17-python3-ubuntu

.PHONY: setup run

setup:
	docker pull $(SPARK_IMAGE)

run:
	docker run --rm -e SPARK_LOCAL_IP=127.0.0.1 \
		-v "$(CURDIR):/workspace:ro" -w /workspace $(SPARK_IMAGE) \
		/opt/spark/bin/spark-submit --master 'local[2]' \
		--conf spark.ui.enabled=false /workspace/lab.py
