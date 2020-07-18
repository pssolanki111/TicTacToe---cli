import pprint as pp


def drawBoard(board):
    print('\n\n')
    print(' ' + board['tl'] + ' | ' + board['tm'] + ' | ' + board['tr'])
    print('============')
    print(' ' + board['ml'] + ' | ' + board['mm'] + ' | ' + board['mr'])
    print('============')
    print(' ' + board['bl'] + ' | ' + board['bm'] + ' | ' + board['br'])
    print('\n\n')


def mainGame():
    for p in [1, 2, 3, 4, 5]:
        while 1:
            inp = input('\nPLAYER 1 ( \'' + uType + '\' ) - Type Your move\t')

            if inp == '':
                print('\nAre kuchh likhna bhi hota h Enter press krne s pehle. waapas likho')
                continue
            elif inp in conDetails.keys():
                if tttBoard[inp] == ' ':
                    break
                else:
                    print('\nSorry the move has been already played.. Try another..')
                    continue
            else:
                print('\nInvalid move input. Check the list of available moves above.'
                      '\nOnly lowercase letters expected. Please try again..')
                continue

        tttBoard[inp] = uType
        drawBoard(tttBoard)

        if p >= 3:
            if tttBoard['tl'] == tttBoard['tm'] == tttBoard['tr'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['tm'] == tttBoard['tr'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['ml'] == tttBoard['mm'] == tttBoard['mr'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['ml'] == tttBoard['mm'] == tttBoard['mr'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['bl'] == tttBoard['bm'] == tttBoard['br'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['bl'] == tttBoard['bm'] == tttBoard['br'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['ml'] == tttBoard['bl'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['ml'] == tttBoard['bl'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tm'] == tttBoard['mm'] == tttBoard['bm'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tm'] == tttBoard['mm'] == tttBoard['bm'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mr'] == tttBoard['br'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mr'] == tttBoard['br'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['mm'] == tttBoard['br'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['mm'] == tttBoard['br'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mm'] == tttBoard['bl'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mm'] == tttBoard['bl'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            else:
                pass

        while 1:
            inp = input('\nPLAYER 2 ( \'' + uType2 + '\' ) - Type Your move\t')

            if inp == '':
                print('\nAre kuchh likhna bhi hota h Enter press krne s pehle. waapas likho')
                continue
            elif inp in conDetails.keys():
                if tttBoard[inp] == ' ':
                    break
                else:
                    print('\nSorry the move has been already played.. Try another..')
                    continue
            else:
                print('\nInvalid move input.  Check the list of available\
             moves above. Only lowercase letters expected. Please try again..')
                continue

        tttBoard[inp] = uType2
        drawBoard(tttBoard)

        if p >= 3:
            if tttBoard['tl'] == tttBoard['tm'] == tttBoard['tr'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['tm'] == tttBoard['tr'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['ml'] == tttBoard['mm'] == tttBoard['mr'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['ml'] == tttBoard['mm'] == tttBoard['mr'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['bl'] == tttBoard['bm'] == tttBoard['br'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['bl'] == tttBoard['bm'] == tttBoard['br'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['ml'] == tttBoard['bl'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['ml'] == tttBoard['bl'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tm'] == tttBoard['mm'] == tttBoard['bm'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tm'] == tttBoard['mm'] == tttBoard['bm'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mr'] == tttBoard['br'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mr'] == tttBoard['br'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['mm'] == tttBoard['br'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tl'] == tttBoard['mm'] == tttBoard['br'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mm'] == tttBoard['bl'] == uType:
                print('\nCongratulations! PLAYER 1 has WON..')
                break
            elif tttBoard['tr'] == tttBoard['mm'] == tttBoard['bl'] == uType2:
                print('\nCongratulations! PLAYER 2 has WON..')
                break
            else:
                pass

        if p == 5:
            print('Game Draw!')
            break


print('\nWelcome to the game - Tic Tac Toe..(Multi player)\
 \nPlease make a selection below for PLAYER 1..')

while 1:
    utp = input('\nAre you an \'X\' Person or a \'0\' Person ( Type only either X or 0 )\t')

    if utp == '':
        print('\nAre kuchh likhna bhi hota h enter press krne se pehle..waapas likho')
        continue
    elif (utp != 'X') and (utp != 'x') and (utp != '0'):
        print('\nInvalid input. Only \'X\' or \'0\' expected. Please try again..')
        continue
    else:
        break

if (utp == 'x') or (utp == 'X'):
    uType = 'X'
    uType2 = '0'
else:
    uType = '0'
    uType2 = 'X'

print('\nExcellent choice.\nHave a look below on the supported inputs(or moves)\
 for playing the game\n')

conDetails = {'tl': 'Top Left', 'tm': 'Top Mid', 'tr': 'Top Right',
              'ml': 'Mid Left', 'mm': 'Mid Mid', 'mr': 'Mid Right',
              'bl': 'Bottom Left', 'bm': 'Bottom Mid', 'br': 'Bottom Right'}

pp.pprint(conDetails)
print('\nPlz note that ONLY SMALL CASE LETTERS ARE EXPECTED')
print('\nPLAYER 1 => \'' + uType + '\' || PLAYER 2 => \'' + uType2 + '\'')

tttBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ', 'ml': ' ', 'mm': ' ',
            'mr': ' ', 'bl': ' ', 'bm': ' ', 'br': ' '}

drawBoard(tttBoard)

mainGame()

while 1:
    playChoice = input('\nWanna play again( yes/ no)?\t')
    if (playChoice == 'y') or (playChoice.lower() == 'yes') or (playChoice == 'Y'):
        print('\nHERE WE GO AGAIN...\n')
        tttBoard = {'tl': ' ', 'tm': ' ', 'tr': ' ', 'ml': ' ', 'mm': ' ',
                    'mr': ' ', 'bl': ' ', 'bm': ' ', 'br': ' '}

        drawBoard(tttBoard)
        mainGame()

    elif (playChoice == 'n') or (playChoice.lower() == 'no') or (playChoice == 'N'):
        break
    else:
        print('\nInvalid input! please type either yes/no..')
        continue

print('\nTHANKS FOR PLAYING THE GAME...HAVE A GOOD DAY :)\n')
