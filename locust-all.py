from locust import HttpUser, task, between, constant, constant_pacing, constant_throughput
import os
import random

class MyUser(HttpUser):
    host = "http://localhost:8000"  # Default host, you can replace it with the user input

    def on_start(self):
        # This function is called when a user starts
        pass

    @task
    def my_task(self):
        self.client.get("/")

# Get user inputs
users = int(input("Please enter the number of users: "))
time = input("Please enter the run time in seconds: ")
sr = int(input("Please enter the spawn rate: "))
choice = int(input("Please enter the type of load (1-constant, 2-step-up, 3-ramp, 4-spike, 5-randomize): "))
host = input("Please enter the host (in the format http(s)://<IP>:<port>): ")


# Run Locust with user inputs
if choice==1:
    cmd= f"locust -f constant.py --run-time {time} --users {time} --spawn-rate {sr}"
    os.system(cmd)
if choice==2:
    cmd= f"locust -f your_script_file.py --headless -u {users/2} -r {sr} --stop-time {time/2}"
    cmd= f"locust -f your_script_file.py --headless -u {users} -r {sr} --stop-time {time}"
    os.system(cmd)
if choice==3:
    cmd= f"locust -f constant.py --headless -u {users} -r {sr} -t {time}"
    os.system(cmd)
if choice==4:
    cmd= f"locust -f constant.py --headless -u {users} -r {sr} -t {time} --spawn-rate 10"
    os.system(cmd)
if choice==5:
    choice= random.randint(1,4)
    if choice==1:
        cmd= f"locust -f constant.py --run-time {time} --users {time} --spawn-rate {sr}"
        os.system(cmd)
    if choice==2:
        cmd= f"locust -f your_script_file.py --headless -u {users/2} -r {sr} --stop-time {time/2}"
        cmd= f"locust -f your_script_file.py --headless -u {users} -r {sr} --stop-time {time}"
        os.system(cmd)
    if choice==3:
        cmd= f"locust -f constant.py --headless -u {users} -r {sr} -t {time}"
        os.system(cmd)
    if choice==4:
        cmd= f"locust -f constant.py --headless -u {users} -r {sr} -t {time} --spawn-rate 10"
        os.system(cmd)


