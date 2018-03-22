# Name: Ryan Han
# Login: rhan

# ---------------------------------------------------------------------- 
# Part 1: Pitfalls
# ---------------------------------------------------------------------- 
'''
Problem 1
1) A raw string value cannot be passed as an argument. Also, the argument 'lst' 
is used as a list in the body of the code; thus, lst should not be in quotes 
2) A docstring has 3 beginning apostrophes and 3 ending apostrophes
3) After the keyword if is a comparison statement and not an assignment. Thus,
'if lst == []:' is correct rather than 'if lst = []:'
4) The if and else statements and their respective bodies should be aligned;
they are not which will cause an error upon compilation
5) The end of the while condition does not have a colon after it

Problem 2
1) isPalindrome takes no arguments yet word is passed as an argument
2) ps is a list and thus the operator += cannot be used on it. Instead, the
code should be ps.append(word)
3) The variable words needs to be defined before a value is assigned to it
4) lst == lst.reverse() will not work because lst.reverse() does not return 
anything; thus a list is being compared to nothing so the value of the 
comparison will always be false
5) isPalindrome is called as if there is a return type but isPalindrome 
returns nothing
6) The original intention is to return a list of palindromes; however, by
writing palindromes.append(ps), each ps list is being appended to palindromes
so palindromes, by the end of the function, is a list of lists of palidnromes.

Problem 3
1) The function name gives no indication of what it will do
2) The argument name gives no indication of what it is
3) Docstrings should have 3 single quotes on either side
4) Space before and after the equal sign: j = 0, j = i[0]...
5) Space before and after double equal sign: len(i) == 2
6) Space before an after multiplication sign (before and after operators)
7) Unecessary space after multiplication sign and before i[1][0]
8) The body of the else statement is not indented correctly and should
be lined up to the body of the if statement
9) Space before and after operators like '+' and '-' and '+='
'''

# ---------------------------------------------------------------------- 
# Part 2: Simple functions.
# ---------------------------------------------------------------------- 

import random, sys, math

#
# Problem 2.1
#

def draw_box(n):
    '''
    Return a string which, if printed, would draw a box on the terminal.  The
    exterior of the box should be made from '+' '-' and '|' characters.  The
    interior will have dimensions nxn and the characters will be one of the
    characters 'x', 'y', 'o', or '.', which will occur in order (even between
    lines).  There is a blank line before and after the box contents in the
    returned string.

    Examples:

    >>> print(draw_box(1))

    +-+
    |x|
    +-+

    >>> print(draw_box(2))

    +--+
    |xy|
    |o.|
    +--+

    >>> print(draw_box(3))

    +---+
    |xyo|
    |.xy|
    |o.x|
    +---+

    >>> print(draw_box(4))

    +----+
    |xyo.|
    |xyo.|
    |xyo.|
    |xyo.|
    +----+

    >>> print(draw_box(5))

    +-----+
    |xyo.x|
    |yo.xy|
    |o.xyo|
    |.xyo.|
    |xyo.x|
    +-----+

    >>> print(draw_box(10))

    +----------+
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    |xyo.xyo.xy|
    |o.xyo.xyo.|
    +----------+

    Arguments:
      n -- a positive integer representing the side length of the box.

    Return value: none.
    '''
    assert n > 0
    charList = list(int(math.ceil(n * n / 4.0)) * 'xyo.')
    command = '\n+'
    for a in range(n):
        command += '-'
    command += '+'
    for b in range(n):
        command += '\n|'
        for c in range(n):
            command += str(charList.pop(0))
        command += '|'
    command += '\n+'
    for d in range(n):
        command += '-'  
    command += '+\n'
    return command
        
def test_draw_box():
    print(draw_box(1))
    print(draw_box(2))
    print(draw_box(3))
    print(draw_box(4))
    print(draw_box(5))
    print(draw_box(10))

#
# Problem 2.2
#

def roll():
    '''
    Roll two six-sided dice and return their result.
    Arguments: none
    Return value: the result (an integer between 2 and 12).
    '''
    return random.randint(1, 6) + random.randint(1, 6)

def craps(verbose):
    '''
    Play one round of craps.

    Arguments: 
      verbose: print out the progress of the game while playing

    Return value: 
      True if the player wins, else False
    '''
    
    initialRoll = roll()
    if initialRoll == 7 or initialRoll == 11:
        if verbose:
            print('You rolled {}. You win!'.format(initialRoll))
        return True
    elif initialRoll == 2 or initialRoll == 3 or initialRoll == 12:
        if verbose:
            print('You rolled {}. You lose!'.format(initialRoll))
        return False      
    else:
        if verbose:
            print('Your point is: {}'.format(initialRoll))
        newRoll = 0
        while True:
            newRoll = roll()
            if verbose:
                print('You rolled {}'.format(newRoll))            
            if newRoll == 7 or newRoll == initialRoll:
                break
        if newRoll == 7:
            if verbose:
                print('You missed your point!  You lose!')
            return False
        elif newRoll == initialRoll:
            if verbose:
                print('You hit your point!  You win!')
            return True

def craps_edge(n):
    '''
    Estimate and return the house edge for craps.
    See https://wizardofodds.com/games/craps/appendix/1/ for an
    analytical derivation.  The result is 1 41/99 % or 1.4141... %.

    Argument: n: the number of rounds played (>= 0)
    Return value: the house edge in percent
    '''
    assert n >= 0
    wins = 0.0
    for i in range(n):
        result = craps(False)
        if result:
            wins += 1
    pwin = wins / n
    plose = (n - wins) / n
    edge = -(pwin - plose) * 100
    return edge

#
# Problem 2.3
#

def remove_indices(lst, indices):
    '''
    Return a copy of a list with the elements at the given indices removed.
    Valid negative indices (between -1 and -(length of list)+1) can be used.
    Out-of-bound indices are ignored.

    Argument:
      lst -- the input list
      indices -- a list of integers representing locations in the list to remove

    Return value:
      The new list.  The old list is not altered in any way.
    '''
    indexList = []
    newList = []
    for index in indices:
        if index < 0:
            index += len(lst)
        if index in range(len(lst)):
            indexList.append(index)
    for i, element in enumerate(lst):
        if i not in indexList:
            newList.append(element)
    return newList



def get_bet_info(bets, cwins):
    '''
    Select the next bet information for a gambling system.

    Arguments:
      bets  -- the list of bets set by the gambling system
      cwins -- the consecutive wins (0, 1) previously

    Result:
      a two tuple containing:
      -- the bet amount;
      -- the indices of the 'bets' array where the bet amount was taken from
    '''
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0
    assert cwins in [0, 1, 2]
    
    sum = 0    
    if cwins == 0:
        sum = bets[0]
        return (sum, [0])
    elif cwins == 1:
        if len(bets) == 1:
            sum = bets[0]
            return (sum, [0])
        else:
            sum = bets[0] + bets[-1]
            return (sum, [0, -1])
    else:
        if len(bets) < 3:
            for i, element in enumerate(bets):
                sum += element
            return (sum, list(range(len(bets))))
        else:
            sum += bets[0] + bets[1] + bets[-1]
            return (sum, [0, 1, -1])
        

def make_one_bet(bankroll, bets, cwins, next_is_win):
    '''
    Play a gambling system for a single bet.

    Arguments:
      bankroll    -- the player's money
      bets        -- the list of bets set by the gambling system
      cwins       -- the consecutive wins previously
      next_is_win -- the next result of the game being played

    Result:
       A tuple consisting of:
       1) the updated bankroll
       2) the updated bets list
       3) the updated consecutive wins (max 2)
    '''

    assert bankroll >= 0
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0
    assert cwins in [0, 1, 2]
    assert next_is_win in [True, False]
    
    (betAmount, indices) = get_bet_info(bets, cwins)
    if bankroll < betAmount:
        return (bankroll, [], 0)
    else:
        if next_is_win:
            bankroll += betAmount
            bets = remove_indices(bets, indices)
            cwins += 1
        else:
            bankroll -= betAmount
            bets.append(betAmount)
            cwins = 0
    if cwins > 2:
        cwins = 2
    return (bankroll, bets, cwins)

#
# Test code supplied to students.
#

def random_bool():
    '''Return a random True/False value.'''
    return random.choice([True, False])

def one_round(bankroll, bets, verbose):
    '''
    Play a gambling system for a single round.
    Halt if either the desired amount of money is made, or if
    the player's bankroll hits zero.  Return the final bankroll.

    Arguments:
      bankroll    -- the player's money
      bets        -- the list of bets set by the gambling system
      verbose     -- if True, print out debugging information

    Return value: total profit (negative if there was a loss)
    '''

    assert bankroll >= 0
    assert len(bets) > 0
    for bet in bets:
        assert bet > 0

    orig_bankroll = bankroll
    cwins = 0

    if verbose:
        print('bankroll: {}, bets: {}, cwins: {}'.format(bankroll, bets,
            cwins))

    while True:
        # Test the gambling system on craps.
        #result = craps(False)
        # Alternatively, test it on a random uniformly-distributed boolean 
        # result (like flipping heads or tails).
        result = random_bool()
        if verbose:
            print('result: {}'.format(result))
        (bankroll, bets, cwins) = make_one_bet(bankroll, bets, cwins, result)
        if verbose:
            print('bankroll: {}, bets: {}, cwins: {}'.format(bankroll, bets,
                cwins))
        if bets == []:
            break
    profit = bankroll - orig_bankroll
    return profit

def run_gambling_system(verbose):
    '''
    Run multiple iterations of the gambling system,
    carrying on the bankroll from one iteration to the next.
    '''

    niters = 1000
    bankroll = 700
    orig_bankroll = bankroll
    for _ in range(niters):
        bets = [10, 10, 15]
        profit = one_round(bankroll, bets, verbose)
        if verbose:
            print('PROFIT: {}\n'.format(profit))
        bankroll += profit
        if verbose:
            print('BANKROLL: {}'.format(bankroll))
        if bankroll <= 0:
            break
    total_profit = bankroll - orig_bankroll
    if verbose:
        print('TOTAL PROFIT: {}'.format(total_profit))
    return total_profit

def run_gambling_system_multiple_times(n, verbose):
    '''
    Run multiple independent iterations of the gambling system,
    estimating and printing the average profit.
    '''

    total_profit = 0
    for _ in range(n):
        net_profit = run_gambling_system(verbose)
        if verbose:
            print(net_profit)
        total_profit += net_profit
    avg_profit = total_profit / n
    print('AVERAGE PROFIT: {}'.format(avg_profit))

# Example of use:
# run_gambling_system_multiple_times(10000, False)

# ---------------------------------------------------------------------- 
# Miniproject: 2048 game.
# ---------------------------------------------------------------------- 

#
# Problem 3.1
#

def make_board():
    '''
    Create a game board in its initial state.
    The board is a dictionary mapping (row, column) coordinates 
    (zero-indexed) to integers which are all powers of two (2, 4, ...).
    Exactly two locations are filled.
    Each contains either 2 or 4, with an 80% probability of it being 2.

    Arguments: none
    Return value: the board
    '''
    
    board = {}
    locations = []
    for i in range(4):
        for j in range(4):
            locations.append((i, j))
    random.shuffle(locations)
    
    for i in range(2):
        randNum = random.random()
        if randNum < 0.8:
            randNum = 2
        else:
            randNum = 4
        board[locations[i]] = randNum
    
    return board

#
# Problem 3.2
#

def get_row(board, row_n):
    '''
    Return a row of the board as a list of integers.
    Arguments:
      board -- the game board
      row_n -- the row number

    Return value: the row
    '''
    assert 0 <= row_n < 4
    
    lst = [0, 0, 0, 0]
    for r, c in list(board.keys()):
        if r == row_n:
            lst[c] = board[(r, c)]
    return lst

def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''

    assert 0 <= col_n < 4
    lst = [0, 0, 0, 0]
    for r, c in list(board.keys()):
        if c == col_n:
            lst[r] = board[(r, c)]
    return lst

def put_row(board, row, row_n):
    '''
    Given a row as a list of integers, put the row values into the board.

    Arguments:
      board -- the game board
      row   -- the row (a list of integers)
      row_n -- the row number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= row_n < 4
    assert len(row) == 4
    
    for c, num in enumerate(row):
        if num == 0:
            if (row_n, c) in list(board.keys()):
                del board[(row_n, c)]
        else:
            board[(row_n, c)] = num
    

def put_column(board, col, col_n):
    '''
    Given a column as a list of integers, put the column values into the board.

    Arguments:
      board -- the game board
      col   -- the column (a list of integers)
      col_n -- the column number

    Return value: none; the board is updated in-place.
    '''

    assert 0 <= col_n < 4
    assert len(col) == 4
    
    for r, num in enumerate(col):
        if num == 0:
            if (r, col_n) in list(board.keys()):
                del board[(r, col_n)]
        else:
            board[(r, col_n)] = num    

#
# Problem 3.3
#

def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    2048 game.

    Argument: numbers -- a list of 4 numbers
    Return value: the list after moving the numbers to the left.
    '''

    assert len(numbers) == 4
    
    lst1 = []
    lst2 = []
    i = 1
    for num in numbers:
        if num != 0:
            lst1.append(num)
    while len(lst1) < 4:
        lst1.append(0)
    while i < 4:
        if lst1[i] == lst1[i - 1]:
            lst2.append(2 * lst1[i])
            i += 2
        else:
            lst2.append(lst1[i - 1])
            i += 1
    if i == 4:
        lst2.append(lst1[3])
    while len(lst2) < 4:
        lst2.append(0)
    return lst2     

#
# Problem 3.4
#

def make_move(board, cmd):
    '''
    Make a move on a board given a movement command.
    Movement commands include:

      'w' -- move numbers upward
      's' -- move numbers downward
      'a' -- move numbers to the left
      'd' -- move numbers to the right

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    assert cmd in ['w', 'a', 's', 'd']

    if cmd == 'w':
        for c in range(4):
            column = get_column(board, c)
            column = make_move_on_list(column)
            put_column(board, column, c)
    elif cmd == 's':
        for c in range(4):
            column = get_column(board, c)
            column.reverse()
            column = make_move_on_list(column)
            column.reverse()
            put_column(board, column, c)
    elif cmd == 'a':
        for r in range(4):
            row = get_row(board, r)
            row = make_move_on_list(row)
            put_row(board, row, r)
    elif cmd == 'd': 
        for r in range(4):
            row = get_row(board, r)
            row.reverse()
            row = make_move_on_list(row)
            row.reverse()
            put_row(board, row, r)

#
# Problem 3.5
#

def game_over(board):
    '''
    Make a move on a board given a movement command.  If the board has changed,
    then add a new number (2 or 4, 90% probability it's a 2) on a
    randomly-chosen empty square on the board.  This function assumes that a 
    move can be made on the board.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''
    counter = 0
    for (r, c) in list(board.keys()):
        counter += 1
    if counter != 16:
        return False
    else:
        copyBoard = board.copy()
        cmds = ['a', 's', 'd', 'w']
        for cmd in cmds:
            make_move(copyBoard, cmd)
            if board != copyBoard:
                return False
    return True

#
# Problem 3.6
#

def update(board, cmd):
    '''
    Make a move on a board given a movement command.  If the board
    has changed, then add a new number (2 or 4, 90% probability it's 
    a 2) on a randomly-chosen empty square on the board.  
    If there are no empty squares, the game is over, so return False.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''
    copyBoard = board.copy()
    make_move(board, cmd)
    emptyCells = []
    if copyBoard != board:
        for r in range(4):
            for c in range(4):
                if (r, c) not in list(board.keys()):
                    emptyCells.append((r,c))
        randNum = random.random()
        if randNum < 0.9:
            randNum = 2
        else:
            randNum = 4
        board[random.choice(emptyCells)] = randNum  

### Supplied to students:

def display(board):
    '''
    Display the board on the terminal in a human-readable form.

    Arguments:
      board  -- the game board

    Return value: none
    '''

    s1 = '+------+------+------+------+'
    s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

    print(s1)
    for row in range(4):
        c0 = str(board.get((row, 0), ''))
        c1 = str(board.get((row, 1), ''))
        c2 = str(board.get((row, 2), ''))
        c3 = str(board.get((row, 3), ''))
        print(s2.format(c0, c1, c2, c3))
        print(s1)

def play_game():
    '''
    Play a game interactively.  Stop when the board is completely full
    and no moves can be made.

    Arguments: none
    Return value: none
    '''

    b = make_board()
    display(b)
    while True:
        move = input('Enter move: ')
        if move not in ['w', 'a', 's', 'd', 'q']:
            print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
            print('Try again.')
            continue
        if move == 'q':  # quit
            return
        update(b, move)
        if not b:
            print('Game over!')
            break
        display(b)

#
# Useful for testing:
#

def list_to_board(lst):
    '''
    Convert a length-16 list into a board.
    '''
    board = {}
    k = 0
    for i in range(4):
        for j in range(4):
            if lst[k] != 0:
                board[(i, j)] = lst[k]
            k += 1
    return board 

def random_game():
    '''Play a random game.'''
    board = make_board()
    display(board)
    while True:
        print()
        move = random.choice('wasd')
        update(board, move)
        display(board)
        if game_over(board):
            break