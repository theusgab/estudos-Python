# VARIÁVEIS, CONSTANTES E COMPLEXIDADES DE CÓDIGO

"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (Ruim)
    <- Contagem de complexidade (Ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)


if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_passou_radar_1 and vel_carro_pass_radar_1:
    print('carro multado em radar 1')