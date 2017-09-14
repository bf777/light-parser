import time
BinaryDict = {'a' : "byte a[5]={B01111110,B10001000,B10001000,B10001000,B01111110};",	'b' : "byte b[5]={B00011100,B00100010,B10100010,B00010010,B01111110};",		'c' : "byte c[5]={B01000010,B01000010,B00111100,B00000000,B00000000};",		'd' : "byte d[5]={B11111110,B00010010,B00100010,B00100010,B00011100};",		'e' : "byte e[5]={B01111010,B01001010,B01001010,B01001010,B00111100};",		'f' : "byte f[5]={B01000000,B01001000,B01001000,B00101000,B00011111};",		'g' : "byte g[5]={B01111110,B10010010,B10010010,B10010010,B11100110};",		'h' : "byte h[5]={B00001110,B00010000,B00010000,B00010000,B11111110};",		'i' : "byte i[5]={B00000000,B00000010,B10111110,B00100010,B00000000};",		'j' : "byte j[5]={B10111100,B00000010,B00000010,B00000010,B00001100};",		'k' : "byte k[5]={B00000001,B01000010,B00100100,B00011000,B11111111};",		'l' : "byte l[5]={B00000000,B00000000,B11111111,B00000000,B00000000};",		'm' : "byte m[5]={B00011111,B00100000,B00011111,B00100000,B00011111};",		'n' : "byte n[5]={B00011110,B00100000,B00100000,B00010000,B00111110};",		'o' : "byte o[5]={B00011100,B00100010,B00100010,B00100010,B00011100};",		'p' : "byte p[5]={B00000000,B01100000,B10010000,B10010000,B11111111};",		'q' : "byte q[5]={B01111111,B01000100,B01000100,B01000100,B00111000};",		'r' : "byte r[5]={B00010000,B00100000,B00100000,B00010000,B00111110};",		's' : "byte s[5]={B01000110,B01001001,B01001001,B01001001,B00110001};",		't' : "byte t[5]={B00100000,B00100000,B01111111,B00100000,B00100000};",		'u' : "byte u[5]={B00111110,B00000100,B00000010,B00000010,B00111100};",		'v' : "byte v[5]={B00110000,B00001100,B00000011,B00001100,B00110000};",		'w' : "byte w[5]={B00011110,B00000001,B00011110,B00000001,B00011110};",		'x' : "byte x[5]={B00010001,B00001010,B00000100,B00001010,B00010001};",		'y' : "byte y[5]={B01111111,B00001001,B00001001,B00001001,B01111001};",		'z' : "byte z[5]={B01100001,B01010001,B01001001,B01000101,B01000011};"} # Use characters at own risk. They're not pretty.

InputString = input("Type your message: ") # Warning! Only takes lower case strings containing Latin alphabetical characters!
InputString.replace(" ", "_")

RowNo = 0
for char in InputString:
  for key in BinaryDict:
    if char == key:
	    print (BinaryDict[key])

time.sleep(0.5) # Needed to print code in correct and clean order
for char in InputString:
  for key in BinaryDict:
    if char == key:
      while RowNo < 5:
        print ("lc.setRow(0,{},{}[{}]);".format(RowNo, char, RowNo))
        RowNo +=1
    if RowNo == 5: # Note that characters are drawn for a 5 x 7 matrix; increasing this WILL NOT increase character scale!
      print("delay(delaytime1);") 
      RowNo = 0
