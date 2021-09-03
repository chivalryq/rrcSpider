clean:
	rm result.json
	rm -f ./image/*
start:
	mkdir -p image/
	bash -c "source venv/bin/activate"
	scrapy crawl renrenche -o result.json -s FEED_EXPORT_ENCODING=UTF-8
gen_sql:
	bash -c "source venv/bin/activate"
	python3 sql/sql_generator.py > sql.txt
