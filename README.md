# Locust Rendimiento
Se hizo la prueba de rendimento a una pagina del BN

Para ejecutar la prueba en modo UI:
```python
locust -f locustfile.py --host=https://outlook.office.com
```


Para ejecutar la prueba en modo headless:
```python
locust -f locustfile.py --host=https://outlook.office.com --headless -u 1500 -r 0.208 --stop-timeout 10 --csv=resultado_prueba
```
