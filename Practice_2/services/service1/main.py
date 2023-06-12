from concurrent import futures
import grpc
import os
import sys


# Very important to change the current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
protobufs_path = os.path.abspath("../protobufs")
sys.path.append(protobufs_path)


service1_pb2, service1_pb2_grpc = grpc.protos_and_services(
    "service1.proto"
)

SumRequest = service1_pb2.SumRequest
SumResponse = service1_pb2.SumResponse

class Service1(service1_pb2_grpc.Services1Servicer):
    def Sum(self, request, context):
        result = request.arg1 + request.arg2
        print(request)
        return SumResponse(result=result)
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service1_pb2_grpc.add_Services1Servicer_to_server(
        Service1(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()