#!/usr/bin/env python3

import gs1
import sys
import subprocess


def main():

    for i in range(500,3501,500):
        requested_inputs = i
        gs1.main(i)

    sys.stdout = open("data.txt", "w")



    #I couldn't get gnuplot to work 
    #subprocess.call(['/usr/bin/gnuplot -persist model.gpt'])
    


main()
