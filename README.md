# light-parser
A Python script that takes a (lowercase alphabetic) string and parses the string into [Arduino](http://arduino.cc) formatted data for output to a minimum 8 x 5 LED dot matrix module, flashed one letter at a time. For use with MAX7219 and MAX7221 display drivers and the [LedControl library.](https://github.com/wayoda/LedControl) 

How to use
----------
```
$ python main.py
```
1. Input your string. Only lowercase Latin alphabetic characters are supported at this time.
2. Copy and paste the whole output into a blank file in the Arduino IDE.
3. Initialize your program with the LedControl library according to [their documentation.](http://wayoda.github.io/LedControl/pages/software)
4. Compile and upload your code to Arduino.

Warnings
--------
The letters are **not pretty**. If you have better ideas for more elegant letters, open a pull request for the binary letters. Each 8-bit value covers one 8-LED row or column of your display; letters are currently max 5 rows tall.

At the moment, if you type a word with repeated letters you'll have to manually delete the duplicate binary code from ```BinaryDict```.

Acknowledgements
----------------
This code was inspired by Elegoo's tutorial for the LED dot matrix parser, which can be found [here](http://www.elegoo.com/download/), under "Elegoo UNO R3 The Most Complete Starter Kit" (please be warned that the file containing the tutorial is 500+ MB).







