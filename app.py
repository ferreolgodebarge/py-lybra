from py_libra.utils.rpc_client import RPCClient
from py_libra.transactions import (
    get_transactions_as_dict,
)
from py_libra.utils.converters import dict_to_json

HOST = "ac.testnet.libra.org"
PORT = 80

rpc = RPCClient(host=HOST, port=PORT)

result = get_transactions_as_dict(rpc, version=1, limit=100)

with open('txn.json', 'w') as f:
    f.write(dict_to_json(result))
