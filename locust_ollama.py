from locust import HttpUser, task, between

class OllamaUser(HttpUser):
    host = "http://10.101.238.82"
    wait_time = between(1, 2)

    @task
    def generate(self):
        self.client.post("/api/generate", json={
            "model": "tinyllama",
            "prompt": "What is machine learning?",
            "stream": False,
            "options": {"num_predict": 100}
        }, timeout=120)
