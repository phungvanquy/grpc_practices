PROTO_DIR = protobufs
OUT_DIR_SERVICE = .
PROTO_FILE_SERVICE = $(PROTO_DIR)/services.proto $(PROTO_DIR)/service1.proto $(PROTO_DIR)/service2.proto

compile: $(PROTO_FILE_SERVICE)
	python 	-m grpc_tools.protoc \
			-I=protobufs \
			--grpc_python_out=$(OUT_DIR_SERVICE) \
			--python_out=$(OUT_DIR_SERVICE) \
			$(PROTO_FILE_SERVICE) 

clean:
	rm -rf service*.py 
