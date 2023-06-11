from concurrent import futures
import grpc
import service2_pb2_grpc
import json

from service2_pb2 import (
    ReadFileRequest, 
    ReadFileResponse,
)

class Service2(service2_pb2_grpc.Services2Servicer):
    def ReadFile(self, request, context):
        with open(request.filename,'r') as f:
            data = json.load(f) 
        response = ReadFileResponse(x = data["x"], y = data["y"])
        return response



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service2_pb2_grpc.add_Services2Servicer_to_server(
        Service2(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()