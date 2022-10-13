from math import pi
import matplotlib.pyplot as plt
import numpy as np

print("-----------------------------")	

a = 100         # Raio inicial
b = 8/(2*pi)    # passo do raio por radianos (quanto que o raio aumenta para cada 1 rad de giro)
                # isso fica legal por assim: x/2Pi, porque seria um aumento de x para cada volta (2Pi)

ti = 0          # angulo inicial em rads
tf = 999        # angulo final em rads
t = 0.01        # passo do ângulo em rads
Sd = 9000      # Comprimento Desejado
S = 0           # Comprimento atual
tk = 0          # Angulo final encontrado

# Equação da integral definida pontual
def f(x):
    return (((a+b*x)**2)+b**2)**(1/2)*t

# Iterage para cada variação de t (grau) até achar o comprimento
for x in np.arange(ti, tf, t):
    S += f(x)
    tk = x
    if S >= Sd: break

print("Ângulo final: " + str(round(tk, 1)) + " rad ("+ str(round(tk * (180/pi), 1)) + "°)")
print("Voltas: " + str(round(tk / (2*pi), 2)) + " voltas")
print("Diâmetro Interno: " + str(round(a * 2, 1)) + " mm")
print("Diâmetro Externo: " + str(round(2*(a+b*(tk-ti)), 1)) + " mm")
print("-----------------------------")	