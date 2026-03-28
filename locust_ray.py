from locust import HttpUser, task, between

class RayServeUser(HttpUser):
    host = "http://10.111.54.211"
    wait_time = between(1, 2)

    @task
    def generate(self):
        self.client.post("/generate", json={
            "prompt": "What is machine learning?"
        }, timeout=120)
