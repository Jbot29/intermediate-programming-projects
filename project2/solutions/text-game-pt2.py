



#commands, look <direction>, take <object>, go <direction>, help, debug

def debug(state,o):
    print "Debug Info:",state
    
def show_help(state,o):
    print "Help"

def look(state,direction):
    print state['current_room'][direction]
    if direction in state['current_room']:
        if type(state['current_room'][direction]) == type({}):
            print state['current_room'][direction]['desc']
        else:
            print state['current_room'][direction][0]['desc']
            
    else:
        print "Where do you want to look?"

def go(state,direction):
    if direction in state['current_room']:
        if type(state['current_room'][direction]) == type({}):
            state['current_room'] = state['current_room'][direction]
        else:
            print state['current_room'][direction][0]['desc']
    else:
        print "Where do you want to look?"
    
COMMANDS = {"help":show_help,
            "debug":debug,
            "look":look,
            "go":go,}


#obstacles are an array of items, if there is only one item you can go into the room,
#otherwise it is an obstacle.
#how to debug map

def create_map():
    main_room = {'type':'room'}
    
    second_room = {'type':'room','desc':'You see a doorway to a very dark room'}
    second_room['north'] = {'type':'key','desc':"You see a shiny key lying on the floor"}
    main_room["north"] = second_room

    main_room["east"] = {"type":"wall","desc":"Here hangs an ugly painting of some old dude"}
    main_room["west"] = {"type":"object","desc":"You see a large candle flickering bright"}
    main_room["south"] = [{"type":"obstacle","desc":"You see a large locked door"},{'type':'outside'}]
    return main_room

    
def play_game():
    state = {'current_room':create_map(),
             'inventory':[]}
    
    while state['current_room']['type'] != 'outside':
        command = raw_input("Command:").split(' ')

        #maybe use optional parameters.
        if len(command) == 1: command.append("")
        print command
        if command[0] in COMMANDS:
            COMMANDS[command[0]](state,command[1])

