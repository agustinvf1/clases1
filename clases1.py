class Informe:
    def __init__(self, titulo: str, autor: str, contenido: str, codigo_seguridad: int = 0):
        self._titulo = titulo
        self._autor = autor
        self._contenido = contenido
        self.__codigo_seguridad = codigo_seguridad
        self._confirmado = False


    @property
    def codigo_seguridad(self) -> int:
        return self.__codigo_seguridad


    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not self._confirmado:
            self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        if not self._confirmado:
            self._autor = valor

    @property
    def contenido(self):
        return self._contenido

    @property
    def confirmado(self):
        return self._confirmado

    def esConfidencial(self) -> bool:
        return self.__codigo_seguridad != 0

    def agregarContenido(self, frase: str) -> bool:
        if self._confirmado:
            return False
        if frase:
            self._contenido += " " + frase
            return True
        return False


    def eliminarContenido(self, frase: str) -> bool:
        if self._confirmado:
            return False
        if frase in self._contenido:
            self._contenido = self._contenido.replace(frase, "").strip()

            self._contenido = " ".join(self._contenido.split())
            return True
        return False

    def mostrarDetalle(self, codigo: int = 0) -> None:
        print(f"Titulo: {self._titulo}")
        print(f"Autor: {self._autor}")

        if self.esConfidencial():
            if codigo == self.__codigo_seguridad:
                print(f"Contenido: {self._contenido}")
            else:
                print("Contenido:[Se requiere codigo de seguridad]")
        else:
            print(f"Contenido: {self._contenido}")

        print(f"Confirmado: {self._confirmado}")

    def confirmarInforme(self) -> None:
        self._confirmado = True
