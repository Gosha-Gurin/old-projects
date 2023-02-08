import numpy as np
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style




def MOVE(IN, ARRAY):
    ALF = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
    y1 = ALF.get(IN[0])
    x1 = 8 - int(IN[1])
    y2 = ALF.get(IN[3])
    x2 = 8 - int(IN[4])
    n = [x1, y1, x2, y2]
    return n

BGR= Back.WHITE
SRA = Style.RESET_ALL

FC = '\033[34m'
FR = '\033[31m'
FRC = '\033[39m'



DACK = np.array([[FR+'R'+FRC,FR+'N'+FRC,FR+'B'+FRC,FR+'Q'+FRC,FR+'K'+FRC,FR+'B'+FRC,FR+'N'+FRC,FR+'R'+FRC],
                 [FR+'P'+FRC,FR+'P'+FRC,FR+'P'+FRC,FR+'P'+FRC,FR+'P'+FRC,FR+'P'+FRC,FR+'P'+FRC,FR+'P'+FRC],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [FC+'P'+FRC,FC+'P'+FRC,FC+'P'+FRC,FC+'P'+FRC,FC+'P'+FRC,FC+'P'+FRC,FC+'P'+FRC,FC+'P'+FRC],
                 [FC+'R'+FRC,FC+'N'+FRC,FC+'B'+FRC,FC+'Q'+FRC,FC+'K'+FRC,FC+'B'+FRC,FC+'N'+FRC,FC+'R'+FRC]])

PLAY = None
MOVE_1 = None
MOVE_2 = None


while True:
    first =      ' /-------------------------------\\'
    second =     '8| '+DACK[0, 0]+' |'+BGR+' '+DACK[0, 1]+' '+SRA+'| '+DACK[0, 2]+' |'+BGR+' '+DACK[0, 3]+' '+SRA+'| '+DACK[0, 4]+' |'+BGR+' '+DACK[0, 5]+' '+SRA+'| '+DACK[0, 6]+' |'+BGR+' '+DACK[0, 7]+' '+SRA+'|'
    third =      ' |-------------------------------|'
    fourth =     '7|'+BGR+' '+DACK[1, 0]+' '+SRA+'| '+DACK[1, 1]+' |'+BGR+' '+DACK[1, 2]+' '+SRA+'| '+DACK[1, 3]+' |'+BGR+' '+DACK[1, 4]+' '+SRA+'| '+DACK[1, 5]+' |'+BGR+' '+DACK[1, 6]+' '+SRA+'| '+DACK[1, 7]+' |'
    fifth =      ' |-------------------------------|'
    sixth =      '6| '+DACK[2, 0]+' |'+BGR+' '+DACK[2, 1]+' '+SRA+'| '+DACK[2, 2]+' |'+BGR+' '+DACK[2, 3]+' '+SRA+'| '+DACK[2, 4]+' |'+BGR+' '+DACK[2, 5]+' '+SRA+'| '+DACK[2, 6]+' |'+BGR+' '+DACK[2, 7]+' '+SRA+'|'
    seventh =    ' |-------------------------------|'
    eighth =     '5|'+BGR+' '+DACK[3, 0]+' '+SRA+'| '+DACK[3, 1]+' |'+BGR+' '+DACK[3, 2]+' '+SRA+'| '+DACK[3, 3]+' |'+BGR+' '+DACK[3, 4]+' '+SRA+'| '+DACK[3, 5]+' |'+BGR+' '+DACK[3, 6]+' '+SRA+'| '+DACK[3, 7]+' |'
    ninth =      ' |-------------------------------|'
    tenth =      '4| '+DACK[4, 0]+' |'+BGR+' '+DACK[4, 1]+' '+SRA+'| '+DACK[4, 2]+' |'+BGR+' '+DACK[4, 3]+' '+SRA+'| '+DACK[4, 4]+' |'+BGR+' '+DACK[4, 5]+' '+SRA+'| '+DACK[4, 6]+' |'+BGR+' '+DACK[4, 7]+' '+SRA+'|'
    eleventh =   ' |-------------------------------|'
    twelfth =    '3|'+BGR+' '+DACK[5, 0]+' '+SRA+'| '+DACK[5, 1]+' |'+BGR+' '+DACK[5, 2]+' '+SRA+'| '+DACK[5, 3]+' |'+BGR+' '+DACK[5, 4]+' '+SRA+'| '+DACK[5, 5]+' |'+BGR+' '+DACK[5, 6]+' '+SRA+'| '+DACK[5, 7]+' |'
    thirteenth = ' |-------------------------------|'
    fourteenth = '2| '+DACK[6, 0]+' |'+BGR+' '+DACK[6, 1]+' '+SRA+'| '+DACK[6, 2]+' |'+BGR+' '+DACK[6, 3]+' '+SRA+'| '+DACK[6, 4]+' |'+BGR+' '+DACK[6, 5]+' '+SRA+'| '+DACK[6, 6]+' |'+BGR+' '+DACK[6, 7]+' '+SRA+'|'
    fifteenth =  ' |-------------------------------|'
    sixteenth =  '1|'+BGR+' '+DACK[7, 0]+' '+SRA+'| '+DACK[7, 1]+' |'+BGR+' '+DACK[7, 2]+' '+SRA+'| '+DACK[7, 3]+' |'+BGR+' '+DACK[7, 4]+' '+SRA+'| '+DACK[7, 5]+' |'+BGR+' '+DACK[7, 6]+' '+SRA+'| '+DACK[7, 7]+' |'
    seventeen =  ' \\-------------------------------/'
    numbers =    '   A   B   C   D   E   F   G   H   '
    print(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeen, numbers, sep='\n')
    PLAY = input()
    if PLAY != 'stop':
        if DACK[MOVE(PLAY, DACK)[2], MOVE(PLAY, DACK)[3]] == ' ':
            DACK[MOVE(PLAY, DACK)[0], MOVE(PLAY, DACK)[1]], DACK[MOVE(PLAY, DACK)[2], MOVE(PLAY, DACK)[3]] = DACK[MOVE(PLAY, DACK)[2], MOVE(PLAY, DACK)[3]], DACK[MOVE(PLAY, DACK)[0], MOVE(PLAY, DACK)[1]]
        else:
            DACK[MOVE(PLAY, DACK)[2], MOVE(PLAY, DACK)[3]] = DACK[MOVE(PLAY, DACK)[0], MOVE(PLAY, DACK)[1]]
            DACK[MOVE(PLAY, DACK)[0], MOVE(PLAY, DACK)[1]] = ' '
    else:
        break
