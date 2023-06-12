from concurrent import futures
import grpc
import json
import os
import sys

# Very important to change the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
protobufs_path = os.path.abspath("../protobufs")
sys.path.append(protobufs_path)


service2_pb2, service2_pb2_grpc = grpc.protos_and_services(
    "service2.proto"
)

ReadFileRequest = service2_pb2.ReadFileRequest
ReadFileResponse = service2_pb2.ReadFileResponse

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