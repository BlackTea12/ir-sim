# Intelligent-Robot-Simulator2

A python based robot simulator framework for the intelligent robotics navigation and learning

## Prerequisite

Test platform: Ubuntu20.04, windows10

- Python: >= 3.8
    - numpy  
    - matplotlib 
    - cvxpy
    - scipy

## Installation

clone the repository

```
git clone https://github.com/hanruihua/Intelligent-Robot-Simulator2.git
```

install the package (ir_sim2)

```
cd Intelligent-Robot-Simulator2
pip install -e .
```

## Usage

The examples are in the ir-sim2/usage

## To do list

- [x] Basic framework
- [x] Mobile robot movement
- [x] collision check
- [x] gif generation
- [x] multi robots mode (collision)  
- [x] sensor lidar
- [x] env res
- [x] collision check with discrete samples
- [x] omni directional robots
- [x] Add custom robot model
- [x] Add sensor: gps, odometry
- [x] Add noise (diff)
- [ ] line obstacle
- [ ] map obstacle
- [ ] using the mouse to select the circle and polygon obstacles
- [ ] Add the data monitor
- [ ] Add more scenarios (traffic)