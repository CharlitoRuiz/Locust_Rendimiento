from locust import HttpUser, task, constant
import time

TOTAL_REQUESTS = 50000
INTERVAL_SEGUNDOS = 0.012  # 1500 requests en 10 minutos (600 segundos)

class BNUser(HttpUser):
    wait_time = constant(INTERVAL_SEGUNDOS)
    request_count = 0

    @task
    def hacer_request(self):
        if self.request_count >= TOTAL_REQUESTS:
            self.environment.runner.quit()
            return

        self.client.get(
            "/book/ReservasucitaparaMonedaColeccionable@bnficr.onmicrosoft.com/?ismsaljsauthenabled",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
        )
        self.request_count += 1
