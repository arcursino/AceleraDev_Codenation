.PHONY: start

start: 
	docker build -t codenation .
	docker run -p 8888:8888 -v $(shell pwd):/notebooks codenation