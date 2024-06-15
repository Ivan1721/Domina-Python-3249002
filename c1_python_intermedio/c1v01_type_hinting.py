# convertir pyhton en tipado estatico
from typing import Union

def calular_perimetro_cuadrado_1(lado: int) -> int:
    return 4 * lado


def calular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    return 4 * lado
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
print(calular_perimetro_cuadrado(lado=5.1))

print(calular_perimetro_cuadrado_1(lado = 5.5))

# 