// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.20;

import "forge-std/console.sol";

contract Example {
    uint8 a = 255; // 0 -> 255
    uint256 b = 22; // alias: uint

    int8 c = 127; // -128 -> 127
    int256 d = -55; // alias: int256

    uint256 e = type(uint256).max;

    bool myCondition = true;

    enum Choice {
        Up,
        Down,
        Left,
        Right
    }

    // Choice choice = Choice.Up;

    constructor(Choice choice) {
        // overflow
        // a += 1;

        // ignore overflow
        unchecked {
            a += 1;
        }
        console.log(a);

        console.log(e);
        console.logBytes32(bytes32(e));

        console.logInt(type(int256).max);
        console.logInt(type(int256).min);

        if (myCondition) {
            console.log("yay!");
        }

        if (choice == Choice.Up) {
            console.log("up");
        }
        if (choice == Choice.Down) {
            console.log("down");
        }
        if (choice == Choice.Left) {
            console.log("left");
        }
        if (choice == Choice.Right) {
            console.log("right");
        }
    }
}
