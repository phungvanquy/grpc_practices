import grpc

import sys
sys.path.append("./services/protobufs")
service1_pb2, service1_pb2_grpc = grpc.protos_and_services(
    "service1.proto"
)

service2_pb2, service2_pb2_grpc = grpc.protos_and_services(
    "service2.proto"
)

SumRequest = service1_pb2.SumRequest
SumResponse = service1_pb2.SumResponse
ReadFileRequest = service2_pb2.ReadFileRequest
ReadFileResponse = service2_pb2.ReadFileResponse
Services1Stub = service1_pb2_grpc.Services1Stub
Services2Stub = service2_pb2_grpc.Services2Stub

service1_host = "localhost"
service2_host = "localhost"
service1_channel = grpc.insecure_channel(f"{service1_host}:50051")
service2_channel = grpc.insecure_channel(f"{service2_host}:50052")


service1_client = Services1Stub(service1_channel)
service2_client = Services2Stub(service2_channel)


for i in range(100):
    """ Read data (x, y) from file """
    # data = service2_client.ReadFile(ReadFileRequest(filename="services/service2/data.json"))
    data = service2_client.ReadFile(ReadFileRequest(filename="data.json"))
    print(data)
    x = data.x
    y = data.y

    """ Perfrom calculation """
    request = SumRequest(arg1=x, arg2=y)
    result = service1_client.Sum(request)
    print("Sum of x and y: ",result.result)



