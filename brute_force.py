# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:40:19 2021

@author: aubin
"""

message = "RMACQADMVCRIQDCRIQDIQVKC"

liste_text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_num = range(26)

def num_to_text(a):
    liste_tex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return liste_tex[a]

def text_to_num(g):
    liste_tex = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return liste_tex.index(g)

for j in list_num:
    message_final = ""
    for i in message.lower().strip():
        message_final = message_final + num_to_text((text_to_num(i)+j)%26)
    print(message_final," => ",j)