import time

rooms = {
    'Comienzo': {'habitaciones': ['1'], 'items':[]},
    '1': {'habitaciones': ['Comienzo', '2'], 'items':[]},
    '2': {'habitaciones': ['1', "3", "4"], 'items':[]},
    '3': {'habitaciones': ["2"], 'items':["trampa"]},
    '4': {'habitaciones': ['2', '5', "6"], 'items': []},
    '5': {'habitaciones': ['4'], 'items':["llave"]},
    "6": {"habitaciones": ["4", "7"], "items":["trampa2"]},
    "7": {"habitaciones": ["6", "10", "8"], "items":[]},
    "8": {"habitaciones": ["9", "7"], "items":["llave"]},
    "9": {"habitaciones": ["8"], "items":[]},
    "10": {"habitaciones": ["7", "11"], "items":[]},
    "11": {"habitaciones": ["10", "12"], "items":[]},
    "12": {"habitaciones": ["11", "Salida"],  "items":[]}
    }

room = 'Comienzo'
key = False
while True:
    print('============================')
    print('Estás en una habitación', room)
    for near_room in rooms[room]['habitaciones']:
        print('Puedes ir a', near_room)
    new_room = input('¿Qué habitación eliges?')
    if new_room not in rooms[room]['habitaciones']:
        print('¡Esta habitación no existe!')
        time.sleep(2)
        continue

    if new_room == 'Salida' and not key:
        print('¡No tienes una llave!')
        time.sleep(2)
        continue
    
    if new_room == 'Salida':
        print('¡Usted gana!')
        time.sleep(2)
        break
    
    room = new_room
    if 'llave' in rooms[room]['items']:
        key = True
        print('¡Encontraste una llave!')
        rooms[room]['items'].remove('llave')
        time.sleep(2)
        
    if 'trampa' in rooms[room]['items']:
        key = True
        print('¡Haz caido en una trampa, mejor suerte la proxima vez!')
        rooms[room]['items'].remove('trampa')
        break
    
    if 'trampa2' in rooms[room]['items']:
        key = True
        respuesta = int(input("¡haz caido en arenas movedisas! ¿Que haces? 1=Moverte violentamente para intentar salir / 2= mantener la calma e intentar salir tranquilamente"))
        if respuesta == 2:
            print("¡Haz conseguido escapar!")
        elif respuesta == 1:
            print("¡Te han tragado las arenamas movedisas, más suerte la proxima vez!")
            break
        rooms[room]['items'].remove('trampa2')
        time.sleep(3)