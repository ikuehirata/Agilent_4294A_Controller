# Agilent_4294A_Controller
Agilent 4294A Precision Impedance Analyzer controller by PyVISA.  

### Requirement ###
+ Python 2.x
+ NumPy
+ PyVISA

### Usage ###
Run the program with output file name as an argument.  
    ``python Z-phi.py output.csv``
Customize setups accordingly. Commands can be found at [Agilent 4294A Precision Impedance Analyzer
Programming Manual](http://literature.cdn.keysight.com/litweb/pdf/04294-90061.pdf?id=1000002213-1:epsg:man).  


### What this does ###
1. Setups connection to Agilent 4294A Precision Impedance Analyzer at GPIB0::17
(Check l. 23 for GPIB address setting)  
2. Setups sweep parameters in ll. 25-41
3. Performs SINGLE sweep (waiting time for sweep is customized by ``sleepdelay``)
4. Saves x-value, Trace A, Trace B in a single file.
5. Sets back sweep mode to CONTINUOUS, then gives a beep

-----
# Updates  
2016 Jan 21 Version 1.01 uploaded (minor revision)  
2015 Dec 11 Version 1.00 uploaded  
