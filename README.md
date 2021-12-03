# Advent of Code 2021

Here are my tries at solving Advent of Code 2021 in Python

## How to use this repo?

Look at my solutions if you want.

## new_day.py

If you want to generate a skeleton for a new day's problem, use the `./new_day.py n` where `n` is the number of the day you want to generate the skeleton for.

This will generate a basic skeleton for the problem of day `n`:

``` sh
dayn/
  dayn.py
  test_dayn.py
```

The `dayn.py` file will contain three functions: 

* `read_input` - a function responsible for reading the problem input (expected to live in the file "input" in the same directory)
* `part1` - a function that takes the input from `read_input` and is expected to return the solution to the second part of today's problem
* `part2` - a function that takes the input from `read_input` and is expected to return the solution to the second part of today's problem

**NOTE:** This script will fail if you try to generate a skeleton for an already existing day.
