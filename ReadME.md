### Locust Load Testing Script
## Overview
This script provides a user-friendly interface for configuring and running Locust tests with various load patterns. Users can simulate different scenarios to test the performance of their systems by specifying the number of users, run time, spawn rate, load type, and host.

## Usage
Clone the Repository
git clone https://github.com/Harshitha199819/Locust/

## Run the Script:
python locust-all.py
Enter User Inputs:
Example:
python3 locust-all.py 
Please enter the number of users: 50
Please enter the run time in seconds: 300
Please enter the spawn rate: 2
Please enter the type of load (1-constant, 2-step-up, 3-ramp, 4-spike, 5-randomize): 1
Please enter the host (in the format http(s)://<IP>:<port>): http://localhost:8000

## Review Results:

The script dynamically constructs and executes Locust commands based on the specified load type. Locust test results will be displayed, and users can monitor the progress in the Locust web interface.
Load Types
1. Constant Load
Runs Locust with a constant number of users and spawn rate for the specified run time.

2. Step-Up Load
Runs Locust with a step-up pattern, gradually increasing the number of users during the test.

3. Ramp Load
Runs Locust with a ramp-up pattern, gradually increasing the load over the specified run time.

4. Spike Load
Runs Locust with a spike in the number of users.

5. Randomized Load
Randomly selects one of the four load types (constant, step-up, ramp, or spike) and runs the corresponding Locust command.

Important Notes
Ensure that the paths and filenames used in the script accurately correspond to your Locust scripts.
Exercise caution when using user inputs in commands to prevent potential security risks. Validate and sanitize user inputs before using them in command construction.
License
This project is licensed under the MIT License.

Acknowledgments
Locust - An open-source load testing tool.
Feel free to customize this template based on your specific project details and add any additional sections that you think would be helpful for users.





