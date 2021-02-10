#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:40:10 2021

@author: basakulcay
"""

#Assume a file containing a series of integers is named as numbers.txt and exist on the 
#computer’s disk. Write a program that reads all of the numbers stored in the
#file and calculates their total, the count of negative and positive numbers.
# Add also appropriate exception handling properties.

def main():
    outfile=open('numbers.txt','w')
    outfile.write('-20\n')
    outfile.write('900\n')
    outfile.write('100\n')
    outfile.write('500\n')
    outfile.close()
main()



def main2():
    infile=open('numbers.txt','r')
    
    total=0
    neg_count=0
    pos_count=0
    zero_count=0
    
    try:
        for line in infile:
            each=int(line.rstrip('\n'))
            print(each)
            total+=each
            
            if each<0:
                neg_count+=1
            elif each>0:
                pos_count+=1
            else:
                zero_count+=1
            
            
        print('The total is', total)
        print('The number of negative integers is:' ,neg_count)
        print('The number of positive integers is:',pos_count)
        
    except:
        print('error')
    infile.close()

main2()
