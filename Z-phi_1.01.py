# -*- coding: utf-8 -*-

import visa
import numpy as np
import winsound
import sys
from datetime import datetime as dt
import locale
from time import sleep

# seconds to wait for sweep to complete
sweepdelay = 5

def main():
        if len(sys.argv) < 1:
                print 'input file name to save'
                return 0
        else:
                fname = sys.argv[1]

        # open instrument
        rm = visa.ResourceManager()
        pia = rm.open_resource('GPIB0::17::INSTR')

        # setup measurement parameters
        # Z-phi measurement
        pia.write('MEAS IMPH') 

        # oscillator mode to votage 0.1 V
        pia.write('POWMOD')
        pia.write('POWE 0.1')

        # DC bias 0
        pia.write('DCO 0')

        # sweep start and stop
        pia.write('SWPP FREQ')
        pia.write('SWPT LOG')
        pia.write('STAR 40')
        pia.write('STOP 110E6')
        pia.write('POIN 101')

        # run single sweep, wait for sweep to finish
        pia.write('SING')
        sleep(sweepdelay)
        
        # frequency array
        freq = np.array(pia.query_ascii_values('OUTPSWPRM?'))

        # set trace A as active trace and write data
        pia.write('TRAC A')
        traca = np.array(pia.query_ascii_values('OUTPDTRC?'))

        # same for B
        pia.write('TRAC B')
        tracb = np.array(pia.query_ascii_values('OUTPDTRC?'))

        # save data
        head = """data file made from Agilent 4294A Precision Impedance Analyzer by impedance-read.py
URL: https://github.com/ikuehirata/Agilent_4294A_Controller

Data file created at %s
Meas. Parameter = %s
Adapter = %s
Sweep Type = %s	
Number of Points = %s	
Point Delay Time = %s	
Sweep Delay Time =%s
Osc Level = %s
Osc Mode = %s
DC Bias = %s
BW = %s
Sweep Averaging = %s	
Point Averaging = %s
Sweep Parameter = %s

Param1\tTrace A (Re)\tTrace A (Im)\tTrace B (Re)\tTrace B (Im)"""%
        (dt.now().strftime("%Y-%m-%d %H:%M:%S"),
        pia.query('MEAS?').strip('\n'), pia.query('E4TP?').strip('\n'),
        pia.query('SWPT?').strip('\n'), pia.query('POIN?').strip('\n'),
             pia.query('PDELT?').strip('\n'), pia.query('SDELT?').strip('\n'),
             pia.query('POWE?').strip('\n'), pia.query('POWMOD?').strip('\n'),
             pia.query('DCO?').strip('\n'), pia.query('BWFACT?').strip('\n'),
             pia.query('AVER?').strip('\n'), pia.query('PAVER?').strip('\n'),
             pia.query('SWPP?').strip('\n'))
        np.savetxt(fname, zip(freq, traca[::2], traca[1::2], tracb[::2], tracb[1::2]), delimiter='\t', header=head)

        # set sweep mode to continuous
        pia.write('CONT')

        # beep
        winsound.Beep(2500,500)

main()
