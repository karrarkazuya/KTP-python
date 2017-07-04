#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:14:44 2017

@author: Karrar (karrar.kazuya@gmail.com)
Version: 1.0
Disc: A text processing class
"""

 
class KTP(object):
    percent = 0
    arlist = ["؟",",","."]
    enlist = [" a ", " is ", " an ", " and ", " the ", " of ", " in ", ".", ",", "?", "!"]

    @classmethod
    def main(cls, args):
        print "KTP!"
        
       
        
        
    # 
    # 	The Description of this method is to find out in percent how much what you are looking for exists in a string
    # 	,"text" is the line of string to search in
    # 	,"search" is the letter to search for
    # 	the value returned by this method is the number in percent of how much what you are looking for exists in the text, if returns from 0 to 100 depends how the percent, It will also return 0 if you pass a null value
    # 	
    
    @classmethod
    def Search(cls, text, search):
        if text == None or search == None:
            return 0
        temp = ""
        temptext = ""
        temp2 = ""
        tempsearch = ""
        added = False
        #  1# check if it is same text
        temptext = text.lower()
        tempsearch = search.lower()
        if temptext == tempsearch:
            return 100
        #  2# check if it got the whole part of the search
        if tempsearch in temptext:
            return 90
        #  3# Handling the "..." words
        while KTP.howManyLetter(search, "\"") > 0:
            temp = KTP.cropFromTo(search, "\"", "\"", False)
            if temp == None:
                break
            if temp not in text:
                return 0
            else:
                search = search.replace("\"" + temp + "\"", "")
                if not added:
                    KTP.AddToPercent(50)
                    added = True
                    
         #  4# removing unwanted spaces
        text = text+" "
        search = search+" "
        while "  " in text:
            text = text.replace("  ", " ")
        
        try:
            k = text.index(" ")
        except:
            k = -0
            
        if k == 0:
            text = text.replace(" ", "",1)
        try:
            z = search.index(" ")
        except:
            z = -0
        if z == 0:
            search = search.replace(" ", "",1)
        
        #  5# Handling the -... words
        while KTP.howManyLetter(search, "-") > 0:
            temp = KTP.cropFromTo(search, "-", " ", False)
            if temp == None:
                break
            if temp in text:
                return 0
            search = search.replace("-" + temp + " ", "")
        
        #  6# removing every useless or not needed words
        text = text.lower()
        search = search.lower()
        text = KTP.replaceAll(text, cls.arlist, " ")
        text = KTP.replaceAll(text, cls.enlist, " ")
        
       
        #  7# converting both strings to lists
        temptext = text + " "
        tempsearch = search + " "
        w = KTP.ConverToList(temptext)
        s = KTP.ConverToList(tempsearch)
        #  8# checking for similarities
        num = 0
        x = 0
        i = 0
        while x < len(s):
            while i < len(w):
                num = KTP.checkMistake(w[i], s[x]) / len(s)
                if num > 0:
                    KTP.AddToPercent(num)
                i += 1
            x += 1
        return cls.percent

    @classmethod
    def checkMistake(cls, f1, f2):
        val = 0
        val2 = 0
        num = 0
        if len(f2) < len(f1):
            val2 = len(f2)
        else:
            val2 = len(f1)
        if val2 == 1:
            return 20
        num = 100 / val2
        i = 0
        while i < val2:
            if f1[i] == f2[i]:
                val = val + num
            i += 1
        if val < 60:
            return 0
        return val

    @classmethod
    def AddToPercent(cls, num):
        if cls.percent != 100:
            cls.percent = cls.percent + num
        while cls.percent > 100:
            cls.percent = cls.percent - 1

    # 
    # 	The Description of this method is to find out how many a letter exists in a string
    # 	,"text" is the line of string to search in
    # 	,"letter" is the letter to search for
    # 	the value returned by this method is the number of how many a letter exist in the text, if returns 0 it means there is no such letter in the text, It will also return 0 if you pass a null value
    # 	
    @classmethod
    def howManyLetter(cls, text, letter):
        if text == None or letter == None:
            return 0
        exist = 0
        charat = ""
        i = 0
        while i < len(text):
            charat = text[i]
            if charat == letter:
                exist = exist + 1
            i += 1
        return exist

    # 
    # 	The Description of this method is to find out how many a word exists in a string
    # 	,"text" is the line of string to search in
    # 	,"word" is the word to search for
    # 	the value returned by this method is the number of how many a word exist in the text, if returns 0 it means there is no such letter in the text, It will also return 0 if you pass a null value
    # 	
    @classmethod
    def howManyWord(cls, text, word):
        if text == None or word == None:
            return 0
        exist = 0
        while word in text:
            text = text.replace(word, "",1)
            exist = exist + 1
        return exist

   

    # 
    # 	The Description of this method is to crop a part of a string from long string, "text" is the text to 
    # 	crop from,"from" is the start point, "to" is the end point "leavesides" is a boolean value if it is false then it will crop without sides else it will crop with sides
    # 	the value returned by this method is the cropped part of the string after from the start point till end point, It will also return null if you pass a null value
    # 	
    @classmethod
    def cropFromTo(cls, text, from_, to, leavesides):
        if text == None or from_ == None or to == None:
            return None
        realfrom = from_
        realto = to
        if from_ == to:
            text = text.replace(from_, "%%>>%%ww",1)
            text = text.replace(to, "%%>>%%MM",1)
            from_ = "%%>>%%ww"
            to = "%%>>%%MM"
        
        f1 = 0
        t1 = 0
        try:
            f1 = text.index(from_)
        except:
            f1 = 0
            
        try:
            t1 = text.index(to)
        except:
            t1 = 0
        
            
        if from_ in text and to in text:
            while f1 > t1:
                text = text.replace(to, "",1)
                try:
                    f1 = text.index(from_)
                except:
                    break
                try:
                    t1 = text.index(to)
                except:
                    break
            if f1 < t1:
                if not leavesides:
                    return text[text.index(from_) + len(from_):text.index(to)]
                else:
                    return text[text.index(from_):text.index(to)] + to
        return None

    # 
    # 	The Description of this method is to crop a part of a string from long string, "text" is the text to 
    # 	crop from,"from" is the start point, "to" is the end point.
    # 	the value returned by this method is the cropped part of the string after from the start point till end point, It will also return null if you pass a null value
    # 	
    @classmethod
    def cropFromTo1(cls, text, from_, to):
        if text == None or to == None:
            return None
        if to in text:
            if 0 != text.index(to):
                return text[from_:text.index(to)]
        return None

    # 
    # 	The Description of this method is to crop a part of a string from long string, "text" is the text to 
    # 	crop from,"from" is the start point, "to" is the end point.
    # 	the value returned by this method is the cropped part of the string after from the start point till end point, It will also return null if you pass a null value
    # 	
    @classmethod
    def cropFromTo3(cls, text, from_, to):
        if text == None:
            return None
        if 2 > len(text):
            if from_ < to:
                return text[from_:to]
        return None

    # 
    # 	The Description of this method is to crop a part of a string from long string, "text" is the text to 
    # 	crop from,"from" is the start point, "to" is the end point.
    # 	the value returned by this method is the cropped part of the string after from the start point till end point, It will also return null if you pass a null value
    # 	
    @classmethod
    def cropFromTo2(cls, text, from_, to):
        if text == None or from_ == None:
            return None
        if from_ in text:
            if to > text.index(from_):
                return text[text.index(from_):to]
        return None

    # 
    # 	The Description of this method is to remove any digit from a string, "text" is the text to 
    # 	remove digits from.
    # 	the value returned by this method is the string after removing the digits from, It will also return null if you pass a null value
    # 	
    
    @classmethod
    def getOnlyString(cls, text):
        if text == None:
            return None
        lasttext = ""
        i = 0
        while i < len(text):
            if not text[i].isdigit():
                lasttext = lasttext + text[i]
            i += 1
        return lasttext

    # 
    # 	The Description of this method is to remove any digit from a string, "text" is the text to 
    # 	remove digits from.
    # 	the value returned by this method is the string after removing the digits from, It will also return null if you pass a null value
    # 	
    @classmethod
    def getOnlyDigit(cls, text):
        if text == None:
            return None
        lasttext = ""
        i = 0
        while i < len(text):
            if text[i].isdigit():
                lasttext = lasttext + text[i]
            i += 1
        return lasttext

    # 
    # 	The Description of this method is to remove every word in string based on a String[], "text" is the text to 
    # 	remove words from, search is the String[] containing the words
    # 	the value returned by this method is the string after removing the words from, It will also return null if you pass a null value
    # 	
    @classmethod
    def removeAll(cls, text, search):
        if text == None or search == None:
            return None
        lasttext = ""
        i = 0
        while i < len(search):
            text = text.replace(search[i].__str__(), "")
            i += 1
        return text

    # replace each word in list from string
    @classmethod
    def replaceAll(cls, text, search, replacement):
        if text == None or search == None or replacement == None:
            return None
        lasttext = ""
        i = 0
        while i < len(search):
            text = text.replace(search[i].__str__(), replacement)
            i += 1
        return text

   
    
    # converts each word in string to list
    @classmethod
    def ConverToList(cls, text):
        if text == None:
            return None
        temptext = ""
        text = text + " "
        list_ = []
        while "  " in text:
            text = text.replace("  ", " ")
        if text.index(" ") == 0:
            text = text.replace(" ", "",1)
        while " " in text:
            temptext = KTP.cropFromTo1(text, 0, " ")
            text = text.replace(temptext + " ", "")
            list_.append(temptext)
        return list_


if __name__ == '__main__':
    import sys
    #KTP.main(sys.argv)
    print KTP.Search("hello everybody  it going","haloo")
