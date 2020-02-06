#!/usr/bin/env python3

import sys
from elasticsearch import Elasticsearch

es_host = sys.argv[1]
es_port = sys.argv[2]
index_name = sys.argv[3]
json_file = sys.argv[4]

es = Elasticsearch([{'host': es_host, 'port': es_port}])

f = open(json_file)
json_content = f.read()
# Send the data into es
es.bulk(index=index_name, ignore=400, body=json_content)
