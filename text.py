# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:06:46 2021

@author: oshra
"""

def revword(wo):
      rev=str('')
      index = len(wo)
      while index > 0: 
          rev += wo[index - 1] # save the value of str[index-1] in reverseString
          index = index - 1
      return(rev.lower())


def countword():
    text=open('text.txt','r')
    lines=list()
    word=str('')
    times=1
    for line in text:
        lines.append(line)
        if line is lines[0]:
            word=str(lines[0]).lower()
        else:
            for mila in line.split(): 
                check=revword(mila)
                check=check+'\n'
                if check==word:
                    times=times+1
    return(times)

print(countword())
