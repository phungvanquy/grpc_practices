#!/bin/bash

# python -m grpc_tools.protoc \
#         -I ./services/protobufs \
#         --python_out=./services/service2 \
#         --grpc_python_out=./services/service2 \ 
#         ./services/protobufs/service2.proto


python -m grpc_tools.protoc \
-I=./services/protobufs \
--grpc_python_out=./services/service1 \
--python_out=./services/service1 \
./services/protobufs/service1.proto
        

# python -m grpc_tools.protoc -I ../protobufs --python_out=dir1 --grpc_python_out=dir1 ../protobufs/recommendations.proto

# python -m grpc_tools.protoc -I ../protobufs --python_out=dir2 --grpc_python_out=dir2 ../protobufs/recommendations.proto