from google.protobuf.json_format import MessageToDict  # , MessageToJson
from py_libra.utils.rpc_client import RPCClient
from py_libra.protos.get_with_proof_pb2 import (
    UpdateToLatestLedgerRequest,
    RequestItem,
    GetTransactionsRequest,
)
from py_libra.protos.transaction_pb2 import RawTransaction


def get_raw_transactions(rpc: RPCClient, version: int = 0, limit: int = 10):
    txn_request = GetTransactionsRequest(
        start_version=version,
        limit=limit,
        fetch_events=True,
    )
    item = RequestItem(get_transactions_request=txn_request)
    request = UpdateToLatestLedgerRequest(
        client_known_version=0,
        requested_items=[item],
    )

    response = rpc.stub.UpdateToLatestLedger(request)
    return response


def message_to_dict(message):
    return MessageToDict(message)


def get_transactions_as_dict(
    rpc: RPCClient, version: int = 0, limit: int = 10
) -> dict:
    response = get_raw_transactions(rpc, version, limit)
    transaction_res = response.response_items[0]
    raw = transaction_res.get_transactions_response.txn_list_with_proof
    res = {}
    res['events_for_versions'] = events_for_versions_parser(
        raw.events_for_versions)
    res['first_transaction_version'] = first_transaction_version_parser(
        raw.first_transaction_version)
    res['transactions'] = transaction_parser(raw.transactions)
    res['proof_of_first_transaction'] = proof_of_transaction_parser(
        raw.proof_of_first_transaction)
    res['proof_of_last_transaction'] = proof_of_transaction_parser(
        raw.proof_of_last_transaction)
    res['infos'] = infos_parser(raw.infos)
    return res


def infos_parser(infos):
    res = []
    for info in infos:
        temp = {}
        temp['event_root_hash'] = bytes.hex(info.event_root_hash)
        temp['gas_used'] = info.gas_used
        temp['signed_transaction_hash'] = bytes.hex(
            info.signed_transaction_hash)
        temp['state_root_hash'] = bytes.hex(info.state_root_hash)
        res.append(temp)
    return res


def proof_of_transaction_parser(proof_of_transaction):
    res = {}
    res['bitmap'] = proof_of_transaction.bitmap
    res['non_default_siblings'] = []
    for siblings in proof_of_transaction.non_default_siblings:
        res['non_default_siblings'].append(bytes.hex(siblings))
    return res


def first_transaction_version_parser(first_transaction_version):
    res = {}
    res['value'] = first_transaction_version.value
    return res


def events_for_versions_parser(events_for_versions):
    events_for_versions_list = events_for_versions.events_for_version
    res = {}
    events = []
    for event_for_version in events_for_versions_list:
        for event in event_for_version.events:
            temp = {}
            temp['access_path'] = {}
            temp['access_path']['address'] = bytes.hex(
                event.access_path.address)
            temp['access_path']['path'] = bytes.hex(event.access_path.path)
            temp['event_data'] = bytes.hex(event.event_data)
            temp['sequence_number'] = event.sequence_number
            events.append(temp)
    res['events'] = events
    return res


def transaction_parser(transactions):
    transaction_list = []
    for transaction in transactions:
        temp = {}
        temp['sender_public_key'] = bytes.hex(transaction.sender_public_key)
        temp['sender_signature'] = bytes.hex(transaction.sender_signature)
        temp['raw_twn_bytes'] = raw_txn_bytes_parser(transaction)
        transaction_list.append(temp)
    return transaction_list


def raw_txn_bytes_parser(transaction):
    temp = {}
    rawT = RawTransaction()
    rawT.ParseFromString(transaction.raw_txn_bytes)
    temp['sender_adress'] = bytes.hex(rawT.sender_account)
    temp['gas_unit_price'] = rawT.gas_unit_price
    temp['max_gas_amount'] = rawT.max_gas_amount
    temp['expiration_time'] = rawT.expiration_time
    temp['sequence_number'] = rawT.sequence_number
    temp['reciever'] = bytes.hex(rawT.program.arguments[0].data)
    # Apparently amount of transation : conversion ???
    temp['amount'] = int(bytes.hex(rawT.program.arguments[1].data), 16)
    # Libra Code : What is it ??
    temp['code'] = bytes.hex(rawT.program.code)
    return temp
