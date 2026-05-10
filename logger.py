import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar_evento(mensaje):
    logging.info(mensaje)

def registrar_error(error):
    logging.error(error)
