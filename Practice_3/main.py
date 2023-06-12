
""" Method 1 """
import services_pb2
# type from service 1
print(services_pb2.SumRequest)

# type from service 2
print(services_pb2.ReadFileRequest)





# """ Method 2 """
# # Very important to change the current working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# protobufs_path = os.path.abspath("../protobufs")
# sys.path.append(protobufs_path)

# services_pb2, services_pb2_grpc = grpc.protos_and_services(
#     "services.proto"
# )

# # type from service 1
# print(services_pb2.SumRequest)

# # # type from service 2
# print(services_pb2.ReadFileRequest)

