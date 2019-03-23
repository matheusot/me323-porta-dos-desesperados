#!/usr/bin/env python
# coding: utf-8

import random
import copy

def getTotal():
    return total

def getTroca():
    return troca/total * 100

def getNaoTroca():
    return naoTroca/total * 100

def getPlotDataTroca():
    return plotDataTroca

def getPlotDataNaoTroca():
    return plotDataNaoTroca

def getResult():
    print("Troca: " + str(troca/total * 100) + "%")
    print("Não Troca: " + str(naoTroca/total * 100) + "%")
    return '';

total = 10000
portas = ["A", "B", "C"]
troca = 0
naoTroca = 0
plotDataTroca = [ [],[] ]
plotDataNaoTroca = [ [],[] ]

for i in range(1, total):
    premio = random.choice(portas)
    escolhida = random.choice(portas)
    livres = list(filter(lambda x: x != premio or x != escolhida, copy.deepcopy(portas)))
    apresentador = random.choice(livres)
    trocada = list(filter(lambda x: x != escolhida or x != apresentador, copy.deepcopy(portas)))
    if (escolhida == premio):
        naoTroca += 1
        plotDataNaoTroca[1].append(round(naoTroca/i, 4))
        plotDataNaoTroca[0].append(i);
    else:
        troca += 1
        plotDataTroca[1].append(round(troca/i, 4))
        plotDataTroca[0].append(i);
