# rrcSpider
spider for renrenche

Run method:
1. run `make start` to collect data
2. run `make gen_sql` to generate sql. **Will drop existing data.**

Get data for process:

1. make sure be in venv
2. pip install -r requirements.txt
3. python3 sql/process.sql

Compile .proto file:

    python -m grpc_tools.protoc --python_out=./service  --grpc_python_out=./service ./service/service.proto -I ./service/
