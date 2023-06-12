import grpc

from service1_pb2 import SumRequest, SumResponse
from service2_pb2 import ReadFileRequest, ReadFileResponse
from service1_pb2_grpc import Services1Stub
from service2_pb2_grpc import Services2Stub

service1_host = "localhost"
service2_host = "192.168.0.107"
service1_channel = grpc.insecure_channel(f"{service1_host}:50051")
service2_channel = grpc.insecure_channel(f"{service2_host}:50052")


service1_client = Services1Stub(service1_channel)
service2_client = Services2Stub(service2_channel)
for i in range(10):
    """ Read data (x, y) from file """
    data = service2_client.ReadFile(ReadFileRequest(filename="services/service2/data.json"))
    print(data)
    x = data.x
    y = data.y

    """ Perfrom calculation """
    request = SumRequest(arg1=x, arg2=y)
    result = service1_client.Sum(request)
    print("Sum of x and y: ",result.result)


import time
while True:
    time.sleep(1)
