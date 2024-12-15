# Programación Tradicional
def ingresar_temperaturas():
    temperaturas = []
    print("Ingresa las temperaturas diarias de la semana:")
    for i in range(7):
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
temperaturas = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas)
print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")


