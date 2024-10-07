import boa
import solcx
from .soldeployer import SolDeployer
from pathlib import Path

def load_partial_solc(filename: str, compiler_args = {}, contract_name = None) -> SolDeployer:
    if contract_name is None:
        contract_name = Path(filename).stem
    compiled_src = solcx.compile_files([filename], output_values=["abi", "bin"], **compiler_args)
    abi = compiled_src[f"{filename}:{contract_name}"]["abi"]
    bytecode = compiled_src[f"{filename}:{contract_name}"]["bin"]
    bytecode = bytes.fromhex(bytecode)
    return SolDeployer(abi, bytecode, filename=filename)

def loads_partial_solc(
    source_code: str,
    name: str = None,
    filename: str | Path | None = None,
    compiler_args: dict = None,
) -> SolDeployer:
    name = name or "SolidityContract"
    filename = filename or "<unknown>"

    compiler_args = compiler_args or {}

    # Compile the Solidity source code
    compiled_src = solcx.compile_source(
        source_code,
        output_values=["abi", "bin"],
        **compiler_args
    )

    # Extract the ABI and bytecode
    contract_key = f"<stdin>:{name}"
    if contract_key not in compiled_src:
        raise ValueError(f"Contract {name} not found in compiled source")

    abi = compiled_src[contract_key]["abi"]
    bytecode = compiled_src[contract_key]["bin"]
    bytecode = bytes.fromhex(bytecode)

    return SolDeployer(abi, bytecode, filename=filename)

boa.load_partial_solc = load_partial_solc
boa.loads_partial_solc = loads_partial_solc


