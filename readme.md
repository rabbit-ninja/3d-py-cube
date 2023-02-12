# 3D Cube Example

## Working Demo

![alt text](working-demo.gif)

## Introduction

This repository contains a simple 3D cube example using pygame and OpenGL. It includes two installation scripts for Linux (pre-run.sh) and Windows (pre-run.bat) and the main code is in the file named `3d.py`.

## Requirements

- Pygame
- PyOpenGL

## Installation

### Linux

- Run the pre-run.sh file to install the required packages.
```sh
sh ./pre-run.sh
```

### Windows

- Run the pre-run.bat file to install the required packages.
```powershell
start pre-run.bat
```

## Usage

- Run the `3d.py` file to see the 3D cube in action.


## Controls

- Press 1 to rotate the cube along the x-axis by 1 degree.
- Press 2 to rotate the cube along the y-axis by 1 degree.
- Press 3 to rotate the cube along the z-axis by 1 degree.
- Press 4 to rotate the cube along the -x-axis by 1 degree.
- Press 5 to rotate the cube along the -y-axis by 1 degree.
- Press 6 to rotate the cube along the -z-axis by 1 degree.

## Code Overview

The `3d.py` file contains the following code:

- Import required libraries (pygame and OpenGL)
- Define vertices for a cube
- Define edges connecting the vertices
- Function to draw the cube using defined vertices and edges
- Function to draw a grid
- Main function to initialize and run the 3D cube example

The `pre-run.sh` and `pre-run.bat` files contain the installation scripts for Linux and Windows respectively.

## Conclusion

This simple 3D cube example is a great starting point for anyone looking to get started with pygame and OpenGL. The code is well commented, easy to understand, and can be easily modified to fit your needs.
