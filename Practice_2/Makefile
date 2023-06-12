PROTO_DIR = services/protobufs
OUT_DIR_SERVICE_1 = services/service1
OUT_DIR_SERVICE_2 = services/service2
PROTO_FILE_SERVICE_1 = $(PROTO_DIR)/service1.proto
PROTO_FILE_SERVICE_2 = $(PROTO_DIR)/service2.proto
MODE = main

service1: $(PROTO_FILE_SERVICE_1)
	python 	-m grpc_tools.protoc \
			-I=$(PROTO_DIR) \
			--grpc_python_out=$(OUT_DIR_SERVICE_1) \
			--python_out=$(OUT_DIR_SERVICE_1) \
			$(PROTO_FILE_SERVICE_1)

service2: $(PROTO_FILE_SERVICE_2)
	python 	-m grpc_tools.protoc \
			-I=$(PROTO_DIR) \
			--grpc_python_out=$(OUT_DIR_SERVICE_2) \
			--python_out=$(OUT_DIR_SERVICE_2) \
			$(PROTO_FILE_SERVICE_2)

for_client:
	cp $(OUT_DIR_SERVICE_1)/service* client/
	cp $(OUT_DIR_SERVICE_2)/service* client/

all: service1 service2 for_client

clean:
	rm -rf $(OUT_DIR_SERVICE_1)/service* 
	rm -rf $(OUT_DIR_SERVICE_2)/service* 
	rm -rf client/service* 


run_service_1:
	python ./services/service1/main.py

run_service_2:
	python ./services/service2/main.py

run_client:
	python client/main.py

run_test:
	python services/service1/test.py