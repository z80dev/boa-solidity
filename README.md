# Boa Solidity

Implements solidity support for `Titanoboa`

## Usage

``` python
import boa
import boa_solidity

sol_deployer = boa.load_partial_solc("Counter.sol")

sol_contract = sol_deployer.deploy()

# or attach to existing contract (useful when forking mainnet state)

sol_contract = sol_deployer.at(<addr>)
```

