import boa
import solcx
from .soldeployer import SolDeployer
from pathlib import Path

def load_partial_solc(filename: str, compiler_args = None, contract_name = None) -> SolDeployer:
    if contract_name is None:
        contract_name = Path(filename).stem
    compiled_src = solcx.compile_files([filename], output_values=["abi", "bin"])
    abi = compiled_src[f"{filename}:{contract_name}"]["abi"]
    bytecode = compiled_src[f"{filename}:{contract_name}"]["bin"]
    bytecode = bytes.fromhex(bytecode)
    return SolDeployer(abi, bytecode, filename=filename)

boa.load_partial_solc = load_partial_solc
