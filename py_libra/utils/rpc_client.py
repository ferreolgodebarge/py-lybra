import grpc

from py_libra.protos.admission_control_pb2_grpc import AdmissionControlStub


class RPCClient(object):
    def __init__(self, host: str = "localhost", port: int = 80):
        self.channel = grpc.insecure_channel(host + ':' + str(port))
        self.stub = AdmissionControlStub(self.channel)
