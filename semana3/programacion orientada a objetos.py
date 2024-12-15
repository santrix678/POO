def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
temperaturas = [22.5, 24.0, 21.8, 23.4, 22.0, 20.5, 25.2]  # Ejemplo de temperaturas de la semana
promedio = calcular_promedio(temperaturas)

print("Temperaturas de la semana:")
print(f"Lunes: {temperaturas[0]}°C, Martes: {temperaturas[1]}°C, Miércoles: {temperaturas[2]}°C, "
      f"Jueves: {temperaturas[3]}°C, Viernes: {temperaturas[4]}°C, Sábado: {temperaturas[5]}°C, Domingo: {temperaturas[6]}°C")
print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")
