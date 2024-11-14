wall_char  = '*'
exit_char  = 'x'
free_char  = ' '
start_char = 'o'
dirs       = {'north':(-1,0),'east':(0,1),'south':(1,0),'west':(0,-1)}

###
### Functions
###

def find_start_pos(maze):
    for i in range(len(maze)):
        if start_char in maze[i]:
            return (i, maze[i].index(start_char))


def find_exit_pos(maze):
    for i in range(len(maze)):
        if exit_char in maze[i]:
            return (i, maze[i].index(exit_char))


def right_dir(dir):
    global dirs
    #print('Enter: right_dir(',dir,')')
    keys=list(dirs.keys())
    ci=keys.index(dir)
    ni=(ci+1)%len(keys)
    return keys[ni]


def left_dir(dir):
    global dirs
    #print('Enter: left_dir(',dir,')')
    keys=list(dirs.keys())
    ci=keys.index(dir)
    ni=(ci-1)%len(keys)
    return keys[ni]


def is_pos_type(maze,pos,type):
    global wall_char
    if maze[pos[0]][pos[1]] == type:
        return True
    else:
        return False


def is_pos_wall(pos):
    global maze
    global wall_char
    if maze[pos[0]][pos[1]] == wall_char:
        return True
    else:
        return False


def is_pos_exit(pos):
    global maze
    global wall_char
    if maze[pos[0]][pos[1]] == exit_char:
        return True
    else:
        return False


def is_pos_free(pos):
    global maze
    global wall_char
    if maze[pos[0]][pos[1]] not in list(wall_char,exit_char):
        return True
    else:
        return False


def pos_ahead(pos,direction):
    global dirs
    return tuple(map(sum, zip(pos, dirs[direction])))


def fill_maze_struct(str):
    maze_rows=str.split('\n')
    maze=[[] for _ in range(len(maze_rows))]
    print(maze)
    for i in range(len(maze_rows)):
        for j in range(len(maze_rows[i])):
            maze[i].append(maze_rows[i][j])
    return maze


def main():
    global maze_string
    print(maze_string)
    maze=fill_maze_struct(maze_string)

    seen = []
    pos_seen = False

    # Start
    sp=find_start_pos(maze)
    cp=sp
    sd='west' # arbitrary
    cd=sd
    ep=find_exit_pos(maze)
    
    # Find wall
    while(True):
        cd=right_dir(cd)
        if is_pos_type(maze,pos_ahead(cp,cd),wall_char):
            break
    print('Current position: ', cp)
    # Turn left to have the wall to our right
    cd=left_dir(cd)
    
    # Follow the wall until we find the exit
    max_steps=500 # Prevent loops if any bugs
    step=0
    while(step <= max_steps):
    
        step = step + 1
        
        # Where are we?
        print('At ', cp, ' facing ', cd)

        # Quit if position already seen
        seen_item=str(cp[0]) + str(cp[1]) + cd
        if seen_item in seen:
            print('Quit since this position has already been visited')
            break
        seen.append(seen_item)
    
        # Turn left until we can advance
        while(is_pos_type(maze,pos_ahead(cp,cd),wall_char)):
            cd=left_dir(cd)
            
        # Step forward
        cp=pos_ahead(cp,cd)
    
        # Are we at the exit?
        if is_pos_type(maze,cp,exit_char):
            print('Found exit at ', cp)
            break
    
        # Make sure that we still have the wall on our right
        rd=right_dir(cd)
        if not is_pos_type(maze,pos_ahead(cp,rd),wall_char):
            cd=rd

###
### MAIN
###

maze_string1 = ('********\n'
               '*      *\n'
               '*    ***\n'
               '*      *\n'
               '*    ox*\n'
               '*  *** *\n'
               '*    * *\n'
               '********')

maze_string2 = ('********\n'
               '*  *   *\n'
               '*    ***\n'
               '*      *\n'
               '*    o *\n'
               '*  x** *\n'
               '*    * *\n'
               '********')

maze_string=maze_string2

main()
