
#command functions
def debug(state,o):
    print "Debug Info:",state
    
def show_help(state,o):
    print "Commands:look <direction>, take <object>, go <direction>, help, debug"

def look(state,direction):
    if direction in state['current_room']:
        print state['current_room'][direction]['desc']
    else:
        print "Not too much to look at."

def go(state,direction):
    if direction in state['current_room']:
        if state['current_room'][direction]['type'] == 'door':
            if 'key' in state['inventory']:
                state['current_room'] = None
            else:
                print "You need a key for that door"
        else:
            state['current_room'] = state['current_room'][direction]
    else:
        print "Walking through walls is a skill not yet aquired."

def take(state, name):
    if 'objects' in state['current_room'] and name in state['current_room']['objects']: 
        state['inventory'].append(name)
        state['current_room']['objects'].remove(name) 

        
COMMANDS = {"help":show_help,
            "debug":debug,
            "look":look,
            "go":go,
            'take':take}


#map building functions

def create_room(desc,objects):
    return {'type':'room',
            'desc':desc,
            'objects':objects}

def create_door(desc):
    return {"type":"door","desc":desc}
    
def create_map():

    main_room = create_room('You find yourself in a large candle lit room',[])
    second_room = create_room('Another dark room',[])
    third_room = create_room('Another smaller dark room',['key'])

    
    third_room['north'] = {'type':'object','desc':"You see a shiny key lying on the floor"}
    third_room['west'] = second_room
    
    second_room['east'] = third_room
    second_room['south'] = main_room
    
    main_room["north"] = second_room
    main_room["south"] = create_door("You see a large locked door")
    
    return main_room

    
def play_game():
    state = {'current_room':create_map(),
             'inventory':[]}
    last_room = None
    
    while state['current_room']:
        if last_room != state['current_room']:
            print "Current room:",state['current_room']['desc']
            last_room = state['current_room']

        command = raw_input("Command:").split(' ')
        command.append("") # add dummy value for commands that don't take a parameter

        if command[0] in COMMANDS:
            COMMANDS[command[0]](state,command[1])



    print "You did it!"
