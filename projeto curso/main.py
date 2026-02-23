import flet as ft



class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Quarto:
    def __init__(self, numero, tipo, preco):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponivel = True

class Reserva:
    def __init__(self, cliente, quarto, entrada, saida):
        self.cliente = cliente
        self.quarto = quarto
        self.entrada = entrada
        self.saida = saida

class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def reservar_quarto(self, cliente, numero, entrada, saida):
        for quarto in self.quartos:
            if quarto.numero == numero and quarto.disponivel:
                reserva = Reserva(cliente, quarto, entrada, saida)
                self.reservas.append(reserva)
                quarto.disponivel = False
                return "Reserva realizada!"
        return "Quarto indisponível."




def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos"
    hotel = Hotel("Refúgio dos Sonhos")

    
    hotel.quartos.append(Quarto(101, "Standard", 200))
    hotel.quartos.append(Quarto(102, "Luxo", 350))

    nome = ft.TextField(label="Nome")
    email = ft.TextField(label="Email")
    quarto = ft.TextField(label="Número do quarto")
    entrada = ft.TextField(label="Data entrada")
    saida = ft.TextField(label="Data saída")

    resultado = ft.Text()

    def reservar(e):
        cliente = Cliente(nome.value, email.value)
        hotel.adicionar_cliente(cliente)

        msg = hotel.reservar_quarto(
            cliente,
            int(quarto.value),
            entrada.value,
            saida.value
        )

        resultado.value = msg
        page.update()

    page.add(
        ft.Text("Sistema Refúgio dos Sonhos", size=25),
        nome,
        email,
        quarto,
        entrada,
        saida,
        ft.ElevatedButton("Reservar", on_click=reservar),
        resultado
    )

ft.app(target=main)