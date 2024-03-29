# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import get_with_proof_pb2 as get__with__proof__pb2
import storage_pb2 as storage__pb2


class StorageStub(object):
  """-----------------------------------------------------------------------------
  ---------------- Service definition for storage
  -----------------------------------------------------------------------------
  Write APIs.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SaveTransactions = channel.unary_unary(
        '/storage.Storage/SaveTransactions',
        request_serializer=storage__pb2.SaveTransactionsRequest.SerializeToString,
        response_deserializer=storage__pb2.SaveTransactionsResponse.FromString,
        )
    self.UpdateToLatestLedger = channel.unary_unary(
        '/storage.Storage/UpdateToLatestLedger',
        request_serializer=get__with__proof__pb2.UpdateToLatestLedgerRequest.SerializeToString,
        response_deserializer=get__with__proof__pb2.UpdateToLatestLedgerResponse.FromString,
        )
    self.GetTransactions = channel.unary_unary(
        '/storage.Storage/GetTransactions',
        request_serializer=storage__pb2.GetTransactionsRequest.SerializeToString,
        response_deserializer=storage__pb2.GetTransactionsResponse.FromString,
        )
    self.GetAccountStateWithProofByStateRoot = channel.unary_unary(
        '/storage.Storage/GetAccountStateWithProofByStateRoot',
        request_serializer=storage__pb2.GetAccountStateWithProofByStateRootRequest.SerializeToString,
        response_deserializer=storage__pb2.GetAccountStateWithProofByStateRootResponse.FromString,
        )
    self.GetExecutorStartupInfo = channel.unary_unary(
        '/storage.Storage/GetExecutorStartupInfo',
        request_serializer=storage__pb2.GetExecutorStartupInfoRequest.SerializeToString,
        response_deserializer=storage__pb2.GetExecutorStartupInfoResponse.FromString,
        )


class StorageServicer(object):
  """-----------------------------------------------------------------------------
  ---------------- Service definition for storage
  -----------------------------------------------------------------------------
  Write APIs.
  """

  def SaveTransactions(self, request, context):
    """Persist transactions. Called by Execution when either syncing nodes or
    committing blocks during normal operation.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateToLatestLedger(self, request, context):
    """Read APIs.

    Used to get a piece of data and return the proof of it. If the client
    knows and trusts a ledger info at version v, it should pass v in as the
    client_known_version and we will return the latest ledger info together
    with the proof that it derives from v.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactions(self, request, context):
    """When we receive a request from a peer validator asking a list of
    transactions for state synchronization, this API can be used to serve the
    request. Note that the peer should specify a ledger version and all proofs
    in the response will be relative to this given ledger version.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAccountStateWithProofByStateRoot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExecutorStartupInfo(self, request, context):
    """Returns information needed for Executor to start up.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StorageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SaveTransactions': grpc.unary_unary_rpc_method_handler(
          servicer.SaveTransactions,
          request_deserializer=storage__pb2.SaveTransactionsRequest.FromString,
          response_serializer=storage__pb2.SaveTransactionsResponse.SerializeToString,
      ),
      'UpdateToLatestLedger': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateToLatestLedger,
          request_deserializer=get__with__proof__pb2.UpdateToLatestLedgerRequest.FromString,
          response_serializer=get__with__proof__pb2.UpdateToLatestLedgerResponse.SerializeToString,
      ),
      'GetTransactions': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactions,
          request_deserializer=storage__pb2.GetTransactionsRequest.FromString,
          response_serializer=storage__pb2.GetTransactionsResponse.SerializeToString,
      ),
      'GetAccountStateWithProofByStateRoot': grpc.unary_unary_rpc_method_handler(
          servicer.GetAccountStateWithProofByStateRoot,
          request_deserializer=storage__pb2.GetAccountStateWithProofByStateRootRequest.FromString,
          response_serializer=storage__pb2.GetAccountStateWithProofByStateRootResponse.SerializeToString,
      ),
      'GetExecutorStartupInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetExecutorStartupInfo,
          request_deserializer=storage__pb2.GetExecutorStartupInfoRequest.FromString,
          response_serializer=storage__pb2.GetExecutorStartupInfoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'storage.Storage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
