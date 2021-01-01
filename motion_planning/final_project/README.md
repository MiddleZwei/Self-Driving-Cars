## Motion Planner for a self-driving vehicle

| Task                        | Goal                                                                                               | Implementation                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Behaviour Planning Logic    | Handle a stop sign                                                                                 | State machine that transitions between :<br> <br>1) follow a lane<br>2) decelerate to the stop sign<br>3) stay stopped<br>4) follow a lane when a stop sign |
| Path Generation             | Generate a path with optimization                                                                  | Spiral path                                                                                                                                                 |
| Static Collision Checking   | Check for collision on the generated path                                                          | Circle-based collision checker                                                                                                                              |
| Path Selection              | Choose a path without collisions                                                                   | Penalizing term                                                                                                                                             |
| Velocity Profile Generation | Have a velocity planner for stop sign,<br> lead dynamic obstacles and nominal<br> lane maintenance | Physics functions                                                                                                                                           |

#### Prerequisites
Windows 10, Powershell, Python 3.6

#### Setup
1. Create a virtual environment and install dependencies from [requirements.txt](requirements.txt)
2. Download `CarlaSimulator.zip` from https://www.coursera.org/learn/motion-planning-self-driving-cars/ and place CarlaSimulator folder into the parent folder.

#### Execution in PowerShell
```shell script
.\execute.sh  # this copies necessary files into CARLA Simulator and runs both simulator and Python client
```

#### Cleanup in PowerShell
```shell script
.\cleanup.sh  # this undo's execute.ps1
```