#Declaramos una variable del tipo str, y un input para solicitar datos al usuario.
n_propio = str(input("Ingresa tu nombre: "))
#Utilizamos .capitalize() para convertir la primera letra del str en mayúsculas, ya que en este caso son nombre propios.
n_propio = n_propio.capitalize()
n_mascota = str(input("Ingresa el nombre de tu mascota: "))
n_mascota = n_mascota.capitalize()
n_ciudad = str(input("Ingresa el nombre de tu ciudad: "))
n_ciudad = n_ciudad.capitalize()
n_amigo = str(input("Ingresa el nombre de tu amigo: "))
n_amigo = n_amigo.capitalize()
n_amigo2 = str(input("Ingresa el nombre de otro amigo: "))
n_amigo2 = n_amigo2.capitalize()

#Mostramos en consola la historia, que en este caso es un fragmento de un resúmen del Hobbit xD.
print(f"...La historia cuenta la aventura de {n_propio}, un hobbit que vive en {n_ciudad}. {n_propio} disfruta de una vida pacífica \
y pastoral hasta que su rutina es interrumpida por la aparición sorpresiva de {n_amigo}, el mago. Antes de que {n_propio} pueda \
evitarlo, {n_amigo} entra en su casa, se invita a tomar el té e introduce a un grupo de enanos que van llegando paulatinamente \
y que están liderados por {n_amigo2} Escudo de Roble. Los enanos le cuentan a {n_propio} que van a embarcarse en una aventura para \
recuperar un tesoro perdido que es custodiado por {n_mascota}, el dragón, en la Montaña Solitaria. {n_amigo} ha decidido, muy a pesar \
de {n_propio}, que el hobbit sería una excelente adición al equipo, y que él podría cumplir con el papel del ladrón, ya que los \
hobbits pueden ser muy sigilosos y pasar desapercibidos si se lo proponen. Movido por la curiosidad -algo raro en un hobbit \
-{n_propio} acepta y se suma al grupo....")