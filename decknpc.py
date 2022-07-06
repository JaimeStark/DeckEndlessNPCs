#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decknpc.py

Created by Jaime Stark on 7/5/2022

This script comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to
redistribute it under certain conditions.
See 'LICENSE.txt' for details.

This script uses trademarks and/or copyrights owned by Paizo Inc.,
used under Paizo's Community Use Policy (paizo.com/communityuse). 
I am expressly prohibited from charging you to use or access this
content.  This script is not published, endorced, or specifically
approved by Paizo.  For more information about Paizo Inc. and
Paizo products, visit paizo.com.

DESCRIPTION
DeckEndlessNPCs is a script for digitally generating an NPC based on
Paizo's Deck of Endless NPCs
(https://paizo.com/products/btq02d82?Pathfinder-Deck-of-Endless-NPCs).

To use this script, you must own a digital copy of the Deck of
Endless NPCs.  The script generates an image of four cards overlapped
according to the rules of the Deck of Endless NPCs for generating
an NPC.

Place the folder containing the digital copy of the Deck of Endless
NPCs in JPEG format (.jpg), as downloaded from Paizo, in the same
folder as the decknpc.py file. By default, this folder is named 
"PathfinderDeckOfEndlessNPCsDownload-JPGs." If the folder has a
different name or path, add as argument to script execution.

USAGE
python3 decknpc.py [CARD JPG FOLDER]
"""

from PIL import Image
import random
import os
import sys

def getConcatImage(path, imgs):
    im1 = Image.open(path + "/" + imgs[1])
    im2 = Image.open(path + "/" + imgs[2])
    im3 = Image.open(path + "/" + imgs[3])
    im4 = Image.open(path + "/" + imgs[0])
    im5 = im3.crop((150, 140, 365, 242))
    concat = Image.new('RGBA', (im1.width + im1.width - (im1.width - 304), im1.height + im1.height - (im1.height-130) + im5.height))
    concat.paste(im1, (0, 0))
    concat.paste(im2, (304, 0))
    concat.paste(im3, (148, 130))
    concat.paste(im4, (148, 0))
    concat.paste(im5, (298,502))
    return concat

def drawCards(path):
    facecards = []
    bottomcards = []
    files = sorted(os.listdir(path))
    for i in os.listdir(path):
        if i[-4:] == ".jpg":
            if "Rules" in i:
                continue
            else:
                j = i.split('_')
                # print(j)
                if j[1][:-4] == "":
                    facecards.append(i)
                elif int(j[1][:-4]) % 2 == 0:
                    bottomcards.append(i)
                    # print("Bottom Card:", i)
                else:
                    facecards.append(i)
                    # print("Face Card:", i)
    facecard = random.choice(facecards)
    facecard_num = facecard.split("_")
    # print(facecard, facecard_num[1][:-4])
    removedcard = facecard_num[0] + "_" + str(int(facecard_num[1][:-4]) + 1) + ".jpg"
    # print(removedcard)
    bottomcards.remove(removedcard)
    bottomcard1 = random.choice(bottomcards)
    bottomcards.remove(bottomcard1)
    bottomcard2 = random.choice(bottomcards)
    bottomcards.remove(bottomcard2)
    bottomcard3 = random.choice(bottomcards)
    return(facecard, bottomcard1, bottomcard2, bottomcard3)



if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    path = 'PathfinderDeckOfEndlessNPCsDownload-JPGs'

if not os.path.isdir(path):
    print("Path to JPG images folder does not exist")
else:
    image = getConcatImage(path, drawCards(path))
    # print(image.size)
    image.show()