import winsound
import time
d = {
   'A' : '.-',
   'B' : '-...',
   'C' : '-.-.',
   'D' : '-..',
   'E' : '.',
   'F' : '..-.',
   'G' : '--.',   
   'H' : '....',
   'I' : '..',
   'J' : '.---',
   'K' : '-.-',
   'L' : '.-..',
   'M' : '--',
   'N' : '-.',
   'O' : '---',
   'P' : '.--.',
   'Q' : '--.-',
   'R' : '.-.',
   'S' : '...',
   'T' : '-',
   'U' : '..-',
   'V' : '...-',
   'W' : '.--',
   'X' : '-..-',
   'Y' : '-.--',
   'Z' : '--..',
   '0' : '-----',
   '1' : '.----',
   '2' : '..---',
   '3' : '...--',
   '4' : '....-',
   '5' : '.....',
   '6' : '-....',
   '7' : '--...',
   '8' : '---..',
   '9' : '----.',
   ' ' : '/'
    }
x = 1
while x != '3':
   print()
   function = int(input(('English to Morse Code [1] Morse Code to English [2] Stop the program [3]\n')))
   if (function == 1):
       sentence = str(input(('Type in what you want to be converted to Morse Code.\n')))
       index = 0
       line = ' '
       while (index < len(sentence)):
           if sentence[index] in d:
               print(d[sentence[index]], end=" ")
               line = line + str(d[sentence[index]])
           
           if (sentence[index].upper() in d):
               print(d[sentence[index].upper()], end=" ")
               line = line + str(d[sentence[index].upper()])
           index = index + 1
       index = 0

       while (index < len(line)):
  
          if line[index] == '.':
              winsound.Beep(5000, 500)
      
          elif line[index] == '-':
              winsound.Beep(1000, 700)
      
          elif line[index] == '/':
              time.sleep(1.5)
          index = index + 1


   if (function == 2):
       morseCode = str(input(('''Type in what you want to be converted to English.
Each letter should be separated by a comma.
There should be no spaces between the Morse Code.
Example: .-..,.-,-.,-.-.,.,.-.,/,....,.-,-.-.,-.-,...\n''')))
       index = 0
       morseCode = morseCode.split(',')
       key_list = list(d.keys())
       val_list = list(d.values())
       while (index < len(morseCode)):
           if morseCode[index] not in d:
               print(key_list[val_list.index(morseCode[index])], end="")
           index = index + 1


   if (function == 3):
       print('Bye!')
       print ('-... -.-- . -.-.--')
       exit()
