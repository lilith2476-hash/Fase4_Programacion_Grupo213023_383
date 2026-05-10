from excepciones import ClienteError

class Cliente:

    def __init__(self, nombre, correo):

        if not nombre.strip():
            raise ClienteError("El nombre está vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def mostrar_datos(self):
        return f"{self.__nombre} - {self.__correo}"
