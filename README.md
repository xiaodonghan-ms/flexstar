
# Welcome to Flexstar

## Project Introduction

This project aims to address the challenges of analyzing logs within a cloud computing framework, specifically focusing 
on DevOps and operational tasks. Users can download specific log files from their virtual machines and utilize this 
project to analyze these logs, identify issues, and troubleshoot problems effectively.

The project is designed to support various plugins, allowing users to easily integrate and expand functionality. As long 
as the necessary plugin is available, users can enhance the system, fostering a collaborative environment for module 
development. Currently, I am working on a module for analyzing Linux logs, which will be more versatile than traditional 
vmagent logs. The goal is to create a tool that everyone can contribute to, enabling us to extend its capabilities to 
analyze logs from other services, such as AKS.

This initiative not only simplifies log analysis but also encourages community involvement, making it a valuable resource 
for users seeking to improve their operational efficiency.

All Python submodules within the module folder can be executed independently from the main module. Each submodule can 
operate with or without a graphical user interface (GUI). Additionally, the main module has the capability to run each 
submodule as a subprocess, providing flexibility and enhancing modularity in execution.

## Installation

1. Clone the repository:<br>
 git clone https://github.com/xiaodonghan-ms/flexstar

2. Navigate to the project directory:<br>
 cd flexstar

3. Install the required packages:<br>
 pip install -r requirements.txt

4. Goto Flexstar folder and run it:<br>
 cd Flexstar<br>
 python flexstar.py

That's it! You should now be able to run the project.

![image](https://github.com/user-attachments/assets/8632ddc2-86fc-446f-919f-23398e2f4419)
