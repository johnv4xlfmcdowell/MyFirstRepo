#1uarda una contraseña como password. Crea un sistema de seguridad donde el ordenador muestra un mensaje 'Ordenador bloqueado. Contraseña incorrecta.' si el usuario falla la contraseña. 
#En caso contrario, que muestre por pantalla 'Bienvenid@...'.

def bienvenido():
    print("Bienvenido...")

def bloqueado():
    print('Bloqueando pc...')

#
#hecer que el sistema pida contreaseña y usuario desde un archivo
# encriptar el archivo para que solo el servidor pueda validarlo (ufff)

passw = '1234'


def contraseña(passw,pass_inp):
    intentos = 3
    while intentos < 4 :
        print(f'Contraseña incorrecta: {intentos} intentos restantes')
        print('Intentelo de nuevo:')
        intentos = intentos-1
        pass_inp = input()
        if intentos == 0:
            bloqueado()
            break
        elif passw != pass_inp:
            continue
        elif passw == pass_inp:
            bienvenido()
            break
        
    


print('Bienvenido, ingrese su contraseña:')
pass_inp = input()
if pass_inp != passw:
    contraseña(passw,pass_inp)
else:
    bienvenido()

input()