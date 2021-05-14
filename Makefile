clean:
	rm result.json
	rm -f image/*
start:
	bash -c "source venv/bin/activate"
	scrapy crawl renrenche -o result.json -s FEED_EXPORT_ENCODING=UTF-8 -s