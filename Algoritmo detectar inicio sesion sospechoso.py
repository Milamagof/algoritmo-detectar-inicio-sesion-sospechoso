"""Se ejecuta cada momento en que
un nuevo usuario inicia sesión y verifica si ese usuario ha tenido
tres o más intentos fallidos de inicio de sesión """

# Abrir, leer y split el archivo de texto

with open("usuarios_inicio_sesion.txt", "r", encoding="utf8") as archivo:
    archivo_texto = archivo.read()
usernames = archivo_texto.split()


# Contar los intentos fallidos de inicio de sesión de un usuario

def login_check(login_list, usuario_actual):
    if usuario_actual in login_list:
        counter = 0
        for i in login_list:
            if i == usuario_actual:
                counter = counter + 1

        if counter >= 3:
            return "Haz hecho 3 o más intentos de inicio de sesión.Tu cuenta ha sido bloqueada"
        else:
            return "Estás logueado"
    else:
        return "Usuario inexistente"


print(login_check(usernames, "López"))
