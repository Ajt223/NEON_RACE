# NEON RACE

## 1. El juego

NEON RACE es una carrera simulada en consola. El jugador elige entre dos modalidades:

- **Local:** una pista de 2 carriles. Se mueve con `A` (izquierda) y `D` (derecha). Si choca con un obstáculo sin escudo, la partida termina. El escudo y la velocidad duran un número determinado de turnos y cada 60 turnos se otorga una bonificación de 1000 puntos.
- **Multijugador:** una pista de 4 carriles para dos jugadores en el mismo equipo de cómputo. El jugador 1 usa `A`/`D` y el jugador 2 usa `J`/`L` (sustitutos de las flechas en esta versión de consola). Los choques descuentan 600 puntos y la carrera finaliza a los 120 turnos; al terminar se compara el puntaje para definir ganador o empate.

Las teclas no asignadas se ignoran y no modifican el carril, y tampoco es posible salirse de los límites de la pista.

## 2. Integrantes

| Integrante | Rol | Aporte principal |
| --- | --- | --- |
| [Michael Cadena] | Análisis y requisitos | Definición de requisitos funcionales (RF-10, fin de partida, puntajes). |
| [Agustin Jara | Diseño | Diagrama de la Fase 2 y flujo de los modos de juego. |
| [Jácome Falconí David] | Implementación y pruebas | Código de `menu.py`, `local.py` y `multijugador.py`; validaciones. |

## 3. Cómo ejecutarlo

1. Instalar Python 3 (no se necesitan paquetes adicionales).
2. Abrir la carpeta `NEON_RACE` en Visual Studio Code.
3. Ejecutar **solamente** `menu.py`:
   ```bash
   python menu.py
   ```
4. Responder `1` si la computadora cumple los requisitos mínimos (o `2` para salir).
5. Elegir `1` para Local, `2` para Multijugador o `3` para salir.
6. Al terminar una partida, el programa regresa automáticamente al menú.

**Controles**

| Modo | Jugador | Teclas |
| --- | --- | --- |
| Local | Jugador 1 | `A` / `D` |
| Multijugador | Jugador 1 | `A` / `D` |
| Multijugador | Jugador 2 | `J` / `L` |

**Consideraciones:** cada vuelta del ciclo representa un turno lógico, no un segundo real. El movimiento de los jugadores es por turnos (primero el jugador 1 y después el jugador 2), no simultáneo ni en red. La variable `velocidad` se contabiliza pero aún no altera la rapidez real del juego, y el ítem de limpieza solo muestra un mensaje porque esta versión no almacena una lista de obstáculos.

## 4. Link del video
https://drive.google.com/file/d/1Ou8gRZFXeYNb16KYJG_q_IyeHY7Vzfq8/view?usp=sharing

## 5. Créditos

- **Código de terceros:** no se utilizó código externo; los tres módulos fueron escritos para este proyecto.
- **Librerías:** Python 3 y el módulo estándar `random` (incluido en la biblioteca estándar de Python, sin instalación adicional).
- **Recursos visuales:** ninguno; la interfaz es únicamente de texto en consola.
- **Referencias:** documento *Fase 1 – Análisis y Requisitos de NEON RACE* y la guía de lógica de la Fase 2.

## 6. Uso de IA

Se utilizó la IA de **Claude** como apoyo durante el desarrollo:

- **Para el código de la lógica:** nos ayudó a depurar los errores y a entender cómo pasar las variables de los diagramas al código.
