# NAO Robot Movement Programs

This repository contains programs for the NAO robots to move, which were used for an experiment at work. 
The programs utilize the `qi` library for interacting with the NAO robots and the `pybullet` library for simulating their movements.




## Dependencies

The following libraries are required to run the programs:

- `qi`: A library for interacting with NAO robots.
- `pybullet`: A physics simulation library.


## Usage

To run the programs, use the following commands:

1. Ensure that your NAO robot is powered on and connected to the same network as your computer.

2. Run the desired script. For example, to run the `move_forward.py` script:

    ```sh
    python move_forward.py
    ```

### Example Scripts

- `helloworld.py`: Script to check the connection with NAO
- `naoturn.py`: Script to make the NAO robot turn.
- `naowalk.py`: Script to make the NAO robot wave its hand.

Each script contains comments and documentation to explain its functionality and how to customize it for your needs.

