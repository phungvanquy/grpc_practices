# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service1_pb2 as service1__pb2


class Services1Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sum = channel.unary_unary(
                '/Services1/Sum',
                request_serializer=service1__pb2.SumRequest.SerializeToString,
                response_deserializer=service1__pb2.SumResponse.FromString,
                )
        self.Sub = channel.unary_unary(
                '/Services1/Sub',
                request_serializer=service1__pb2.SubRequest.SerializeToString,
                response_deserializer=service1__pb2.SubResponse.FromString,
                )
        self.Div = channel.unary_unary(
                '/Services1/Div',
                request_serializer=service1__pb2.DivRequest.SerializeToString,
                response_deserializer=service1__pb2.DivResponse.FromString,
                )
        self.Mul = channel.unary_unary(
                '/Services1/Mul',
                request_serializer=service1__pb2.MulRequest.SerializeToString,
                response_deserializer=service1__pb2.MulResponse.FromString,
                )


class Services1Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def Sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sub(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Div(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Mul(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Services1Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=service1__pb2.SumRequest.FromString,
                    response_serializer=service1__pb2.SumResponse.SerializeToString,
            ),
            'Sub': grpc.unary_unary_rpc_method_handler(
                    servicer.Sub,
                    request_deserializer=service1__pb2.SubRequest.FromString,
                    response_serializer=service1__pb2.SubResponse.SerializeToString,
            ),
            'Div': grpc.unary_unary_rpc_method_handler(
                    servicer.Div,
                    request_deserializer=service1__pb2.DivRequest.FromString,
                    response_serializer=service1__pb2.DivResponse.SerializeToString,
            ),
            'Mul': grpc.unary_unary_rpc_method_handler(
                    servicer.Mul,
                    request_deserializer=service1__pb2.MulRequest.FromString,
                    response_serializer=service1__pb2.MulResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Services1', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Services1(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Services1/Sum',
            service1__pb2.SumRequest.SerializeToString,
            service1__pb2.SumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sub(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Services1/Sub',
            service1__pb2.SubRequest.SerializeToString,
            service1__pb2.SubResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Div(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Services1/Div',
            service1__pb2.DivRequest.SerializeToString,
            service1__pb2.DivResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Mul(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Services1/Mul',
            service1__pb2.MulRequest.SerializeToString,
            service1__pb2.MulResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)