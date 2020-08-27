ndarray = [['N', 'N', 'N'], ['N', 'N', 'N'], ['N', 'N', 'N']]

PLAYER_X = 'X'
PLAYER_O = 'O'
DEFAULT_MARKER = 'N'

length = len(ndarray);
current_player = input('Select a user(X or O): ')

idx_position = {
    '1': '0,0',
    '2': '0,1',
    '3': '0,2',
    '4': '1,0',
    '5': '1,1',
    '6': '1,2',
    '7': '2,0',
    '8': '2,1',
    '9': '2,2'
}

def display(nd):
    for i in range(len(nd)):
        print(nd[i])
        
def check_full():
    for i in range(length):
        if (ndarray[i][0] == DEFAULT_MARKER or ndarray[i][1] == DEFAULT_MARKER or ndarray[i][2] == DEFAULT_MARKER):
            return False
    return True

def check_spot_empty(r, c):
    return ndarray[r][c] == DEFAULT_MARKER

def toggle_player():
    global current_player
    if current_player == PLAYER_X:
        current_player = PLAYER_O
    else:
        current_player = PLAYER_X


def play(inp):
    if not check_full():
        inp1, inp2 = inp.split(',')
        inp1, inp2 = int(inp1), int(inp2)
        if check_spot_empty(inp1, inp2):
            ndarray[inp1][inp2] = current_player
            toggle_player()

def user_input():
    print('User %s to play' % current_player)
    return input('Input(1-9): ')

def game_won():
    for i in range(length):
        if ((ndarray[i][0] == ndarray[i][1]) and ndarray[i][1] == ndarray[i][2]) and ndarray[i][0] != DEFAULT_MARKER:
            return True
        if ((ndarray[0][i] == ndarray[1][i]) and ndarray[1][i] == ndarray[2][i]) and ndarray[0][i] != DEFAULT_MARKER:
            return True
    if (ndarray[0][0] == ndarray[1][1] and ndarray[1][1] == ndarray[2][2]) and ndarray[2][2] != DEFAULT_MARKER:
        return True
    if (ndarray[2][0] == ndarray[1][1] and ndarray[1][1] == ndarray[0][2]) and ndarray[0][2] != DEFAULT_MARKER:
        return True
    return False
        
        
def main():
    global current_player
    user_readable = [[1,2,3], [4,5,6], [7,8,9]]
    assert current_player == PLAYER_X or current_player == PLAYER_O, 'User must be X or O'
    print('Use the numbers 1-9 as shown below to select position')
    display(user_readable)
    print('#################### START #######################')
    while(True):
        display(ndarray)
        if game_won():
            toggle_player()
            print('User %s won. GAME OVER!!' % current_player)
            break
        if not check_full():
            choice = user_input()
            play(idx_position[choice])
        else:
            break
    print('#################### END #######################')

if __name__ == '__main__':
    main()

