# El archivo client.py permitirá que el Jugador 2 se conecte al servidor mediante sockets UDP. Su función principal es enviar las acciones
#  y movimientos del jugador al servidor, así como recibir las actualizaciones del estado de la partida, incluyendo posiciones, puntuaciones
#  y eventos del juego. De esta manera, el cliente podrá participar en la carrera y visualizar su progreso mientras el servidor centraliza
# la mayor parte del procesamiento.

# Justificación de uso socket UDP: Se utilizará el protocolo UDP porque permite enviar y recibir información con poca sobrecarga y baja latencia,
#  algo conveniente para un videojuego que necesita respuestas rápidas, idealmente inferiores a un segundo. Sin embargo, estamos conscientes de que
#  UDP no garantiza que todos los paquetes lleguen ni que lo hagan en orden, por lo que consideramos esta limitación y solicitamos al profesor la autorización
#  para utilizar este protocolo o cambiarlo por sockets Tcp.
