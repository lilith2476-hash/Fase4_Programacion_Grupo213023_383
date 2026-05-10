from cliente import Cliente
from reserva import Reserva
from logger import registrar_evento, registrar_error

from servicios.sala import ReservaSala
from servicios.equipos import AlquilerEquipo
from servicios.asesoria import Asesoria


print("=== SISTEMA SOFTWARE FJ ===")


try:

    cliente1 = Cliente("Liliana", "lili@gmail.com")

    servicio1 = ReservaSala(
        "Sala VIP",
        50000,
        3
    )

    reserva1 = Reserva(cliente1, servicio1)

    total = reserva1.procesar()

    print("Reserva exitosa")
    print("Costo:", total)

    registrar_evento("Reserva realizada")

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


try:

    cliente2 = Cliente("", "correo@gmail.com")

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


try:

    cliente3 = Cliente(
        "Carlos",
        "correo_invalido"
    )

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


finally:
    print("Sistema finalizado correctamente")
    