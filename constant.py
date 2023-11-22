from locust import HttpUser, task, constant

class MyUser(HttpUser):
    wait_time = constant(1)  # Set the constant wait time (1 second in this example)

    @task
    def my_task(self):
        self.client.get("/")  # Replace with your actual endpoint




