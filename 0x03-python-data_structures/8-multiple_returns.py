#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_let = None
    else:
        first_let = sentence[0]
    return length, first_let
