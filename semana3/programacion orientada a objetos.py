# Programación Orientada a Objetos (POO)
class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.__dia = dia
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

class ClimaSemanal:
    def __init__(self):
        self.__dias = []

    def agregar_dia(self, dia, temperatura):
        dia_clima = ClimaDiario(dia, temperatura)
        self.__dias.append(dia_clima)

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.__dias)
        return total / len(self.__dias) if self.__dias else 0

# Programa principal
clima_semanal = ClimaSemanal()
print("Ingresa las temperaturas diarias de la semana:")
for i in range(7):
    temp = float(input(f"Día {i + 1}: "))
    clima_semanal.agregar_dia(f"Día {i + 1}", temp)

promedio = clima_semanal.calcular_promedio()
print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")
