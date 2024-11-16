import textwrap

import boa
import boa_solidity
import pytest

@pytest.fixture(scope="module")
def solidity_source():
    return textwrap.dedent("""
    // SPDX-License-Identifier: UNLICENSED
    pragma solidity ^0.8.18;
    contract Test {
        uint256 public value = 123;
    }
    """)


def test_loads_partial(solidity_source):
    deployer = boa.loads_partial_solc(solidity_source, name="Test")
    test_contract = deployer.deploy()
    assert test_contract.value() == 123


