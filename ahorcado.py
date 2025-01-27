import random


class juegoAhorcado:

    """
    .. include:: MARKDOWN.md
    Esta clase sirve dasdas
    """
    estados = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    salvado = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    categorias = ''
    respuestas1 = ('PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON '
                  'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA ').split()
    respuestas2 = ('DUDA KOVACIC MODRIC MOLDOVAN TAH AKE').split()
    respuestas3 = ('GUFFYACOCHE BMW MERCEDES FORD PORSCHEDEAMALLAH SUBARUDEIVAN ASIERNOTIENECOCHE').split()


    numero_aleatorio = random.randint(1, 3)

    if numero_aleatorio == 1:
        respuestas = respuestas1
        categorias = 'FRUTAS'
    elif numero_aleatorio == 2:
        respuestas = respuestas2
        categorias = 'FUTBOL'
    else:
        respuestas = respuestas3
        categorias = 'MARCAS COCHE'


    def jugar(self, nombre):
        """

        :param nombre:
        :return:
        """
        letrasIncorrectas = []
        letrasCorrectas = []
        secreto = random.choice(self.respuestas)

        while True:
            self.dibujar(letrasIncorrectas, letrasCorrectas, secreto)

            guardarLetras = self.dimeLetra(letrasIncorrectas + letrasCorrectas , secreto)

            if guardarLetras in secreto:

                letrasCorrectas.append(guardarLetras)

                acierto = True
                for siguienteLetra in secreto:
                    if siguienteLetra not in letrasCorrectas:
                        acierto = False
                        break
                if acierto:
                    print(self.salvado[0], '\n''¡Bien hecho! la palabra secreta es :', secreto, '\n' 'Has ganado!' , nombre)
                    break
            else:
                letrasIncorrectas.append(guardarLetras)


                if len(letrasIncorrectas) == len(self.estados) - 1:
                    self.dibujar(letrasIncorrectas, letrasCorrectas, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break





    def dibujar(self, listaDibujo, letraCorrecta, secreto):
        """

        :param listaDibujo:
        :param letraCorrecta:
        :param secreto:
        :return:
        """
        contador = 6
        print(self.estados[len(listaDibujo)])
        print('La categoría es: ', self.categorias)
        print()
        print('Letras incorrectas: ', end='')
        for letra in listaDibujo:
            print(letra, end=' ')
            contador -=1

        if len(listaDibujo) == 0 and 0 == len(listaDibujo):
            print('No hay letras incorrectas.')
        if len(listaDibujo) == len(listaDibujo) + 1:
            print('Letras diferentes.')
        if len(listaDibujo) == len(listaDibujo) + 2:
            print('No coinciden.')
        print()

        espacio = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in letraCorrecta:
                espacio[i] = secreto[i]

        print(' '.join(espacio))
        print(f"Intentos : {contador}")

    def dimeLetra(self, letraRepetida , secreto):
        """

        :param letraRepetida:
        :param secreto:
        :return:
        """
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if adivina == "TERMINAR":
                print(secreto)
                print("Que lastima pero adios.")
                print(f" {self.estados[6]} ")
                quit()
            elif len(adivina) != 1:
                print('Introduce una única letra.')

            elif adivina in letraRepetida:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina


if __name__ == '__main__':
    nombre = input("Dime tu nombre")
    juego1 = juegoAhorcado()
    juego1.jugar(nombre)
