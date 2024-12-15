class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def __str__(self):
        return f"{self.dia}: {self.temperatura}°C"

class ClimaSemanal:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia, temperatura):
        self.dias.append(ClimaDiario(dia, temperatura))

    def calcular_promedio(self):
        if not self.dias:
            return 0
        total = sum(dia.temperatura for dia in self.dias)
        return total / len(self.dias)

    def mostrar_temperaturas(self):
        for dia in self.dias:
            print(dia)

# Programa principal
def main():
    clima_semanal = ClimaSemanal()
    temperaturas = [22.5, 24.0, 21.8, 23.4, 22.0, 20.5, 25.2]  # Ejemplo de temperaturas
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia, temp in zip(dias_semana, temperaturas):
        clima_semanal.agregar_dia(dia, temp)

    print("Temperaturas de la semana:")
    clima_semanal.mostrar_temperaturas()

    promedio = clima_semanal.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
