I2CBase
=======


## Install Steps for FT232H Platform

Communicate I2C over USB with a [FT232H chip](http://www.adafruit.com/product/2264).

1. This block requires uses the Adafuit_Python_GPIO package for I2C communication but it requires a [special branch](https://github.com/neutralio/Adafruit_Python_GPIO/tree/htu-python3-v2) that supports python 3.


2. Also required is the libftdi library for communicating with the FT232H chip. Follow the Adafruit [install instructions](https://learn.adafruit.com/adafruit-ft232h-breakout/linux-setup) with two slight modifications.

  1. Replace the step `cmake -DCMAKE_INSTALL_PREFIX="/usr/" ../` with  `cmake -DCMAKE_INSTALL_PREFIX="/usr/" -DPYTHON_EXECUTABLE="/usr/bin/python3.4" ../`.
  2. After the `cmake ...` step and before the `make` step. Modify the file `build/python/ftdi1PYTHON_wrap.c`. In line 3161, replace `PyUnicode_AsUTF8String` with `PyUnicode_AsLatin1String`. Otherwise the library won't work completely with python3. A bug has reported to the libftdi [mailing list](http://www.intra2net.com/en/developer/libftdi/mailinglist.php).


Properties
----------

-   Platform - The Platform used for i2c communction (ex. Raspberry Pi, Edidon, FT232H)

Dependencies
------------

FT232H
-   [**libftdi**](https://learn.adafruit.com/adafruit-ft232h-breakout/linux-setup)
-   [**Adafruit_Python_GPIO**](https://github.com/neutralio/Adafruit_Python_GPIO/tree/htu-python3-v2)

Commands
--------
None

Input
-----
Any list of signals.

Output
------
None
