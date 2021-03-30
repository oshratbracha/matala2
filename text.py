# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:22:31 2021

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
    word=str('')
    times=1
    for line in text:
        word=line.strip('\n')
        break
    
    for line in text: 
        line=line.strip('\n')
        words=line.split()
        for mila in words:
            check=revword(mila)
            if check==word:
                times=times+1
    return(times)

print(countword())