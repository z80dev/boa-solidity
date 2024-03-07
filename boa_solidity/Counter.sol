// SPDX-License-Identifier: MIT

pragma solidity >=0.8.7 <0.9.0;

contract Counter {
    uint256 public count;

    constructor(uint256 _count) {
        count = _count;
    }

    function increment() public {
        count += 1;
    }

}
