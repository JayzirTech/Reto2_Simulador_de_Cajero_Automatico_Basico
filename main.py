# Enunciado del proyecto

# Un banco necesita un programa sencillo en consola que simule operaciones básicas de un cajero automático.
# El sistema no debe manejar múltiples cuentas ni acumuladores complejos. Solo debe trabajar con un saldo inicial fijo.

# Reglas del sistema
# Inicio
# El programa debe:
# • Definir un saldo inicial de $1000.
# • Preguntar cuántas operaciones desea realizar el usuario.

# Por cada operación
# El sistema debe mostrar el siguiente menú:
# 1 → Consultar saldo
# 2 → Retirar dinero
# 3 → Depositar dinero
# El usuario debe elegir una opción.

# Reglas de cada opción
# Opción 1: Consultar saldo
# • Mostrar el saldo actual.

# Opción 2: Retirar dinero
# • Pedir el monto a retirar.
# • Si el monto es mayor que el saldo → mostrar "Fondos insuficientes".
# • Si el monto es menor o igual al saldo → permitir el retiro y mostrar el nuevo saldo.
# • Si el monto es negativo → pedir nuevamente el monto hasta que sea válido.

# Opción 3: Depositar dinero
# • Pedir el monto a depositar.
# • Si el monto es negativo → pedir nuevamente el monto.
# • Si es válido → sumarlo al saldo y mostrar el nuevo saldo.

# Validación de opción
# Si el usuario elige una opción distinta de 1, 2 o 3:
# • Mostrar mensaje: "Opción inválida"

# Finalización
# Cuando se completen todas las operaciones indicadas al inicio:
# • Mostrar mensaje: "Gracias por usar el cajero automático" 