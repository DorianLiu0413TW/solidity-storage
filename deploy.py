from solcx import compile_standard
import json
from web3 import Web3


with open("./SimpleStorage.sol","r") as file:
    simple_storage_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings":{
            "outputSelection":{
                "*":{"*":['abi','metadata', 'evm.bytecode', 'evm.sourceMap']}
            }
        }  
    },
    solc_version = "0.6.0"
)

with open("compiled_code.json","w") as file:
    json.dump(compiled_sol, file)

#get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

#connecting to ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

chain_id = 5777
my_address = "0xf8c5D33f3e71E2B6614A5139EFEE8b69452De491BALANCE"
private_key = "52bb7886fc0a4fc19852f48a93bb0cdd9f352c88cab52314b91a5f5f421a13da"

#SimpleStorage 
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)