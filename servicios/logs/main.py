from cliente import Cliente
from reserva import Reserva
from logger import registrar_evento, registrar_error

from servicios.sala import ReservaSala
from servicios.equipos import AlquilerEquipo
from servicios.asesoria import Asesoria


print("=== SISTEMA SOFTWARE FJ ===")


# OPERACIÓN 1
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

    registrar_evento("Reserva 1 realizada")

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 2
try:

    cliente2 = Cliente("", "correo@gmail.com")

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 3
try:

    cliente3 = Cliente(
        "Carlos",
        "correo_invalido"
    )

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 4
try:

    servicio2 = AlquilerEquipo(
        "Computador Gamer",
        80000,
        2
    )

    reserva2 = Reserva(cliente1, servicio2)

    total = reserva2.procesar()

    print("Reserva exitosa")
    print("Costo:", total)

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 5
try:

    servicio3 = Asesoria(
        "Python",
        100000,
        4
    )

    reserva3 = Reserva(cliente1, servicio3)

    total = reserva3.procesar()

    print("Reserva exitosa")
    print("Costo:", total)

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 6
try:

    reserva4 = Reserva(None, servicio1)

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 7
try:

    reserva5 = Reserva(cliente1, None)

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 8
try:

    cliente4 = Cliente(
        "Andrea",
        "andrea@gmail.com"
    )

    servicio4 = ReservaSala(
        "Sala Premium",
        70000,
        5
    )

    reserva6 = Reserva(cliente4, servicio4)

    total = reserva6.procesar()

    print("Reserva exitosa")
    print("Costo:", total)

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 9
try:

    servicio5 = AlquilerEquipo(
        "Proyector",
        30000,
        1
    )

    reserva7 = Reserva(cliente4, servicio5)

    total = reserva7.procesar()

    print("Reserva exitosa")
    print("Costo:", total)

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


# OPERACIÓN 10
try:

    cliente5 = Cliente(
        "",
        "malcorreo"
    )

except Exception as e:

    print("Error:", e)
    registrar_error(str(e))


finally:
    print("Sistema finalizado correctamente")
