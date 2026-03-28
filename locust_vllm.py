from locust import HttpUser, task, between

class VLLMUser(HttpUser):
    host = "http://10.106.25.110"
    wait_time = between(1, 2)

    @task
    def generate(self):
        self.client.post("/v1/completions", json={
            "model": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            "prompt": "What is machine learning?",
            "max_tokens": 100
        }, timeout=120)
