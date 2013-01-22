#!/usr/bin/python3
# -*- coding: utf8 -*-
# vim: set ts=4 sws=4 sw=4:
import sys
import os

class FileParser:
	def __init__(self):
		self.dic = dict()

	def parseTerm(self, term):
		termInfo = term.rpartition("/")
		surface = termInfo[0]
		pos = termInfo[2]
		self.addDic(pos, surface)

	def parseEojeol(self, eojeol):
		for term in eojeol.split(self.separator):
			self.parseTerm(term)

	def parseLine(self, line):
		fields = line.split("\t")
		if len(fields) != 3:
			return
		self.parseEojeol(fields[2])	

	def parse(self, fileName):
		file = open(fileName, mode='r', encoding='UTF-16LE')
		textStart = False
		for line in file:
			stripedLine = line.strip()
			if stripedLine == "<text>":
				textStart = True

			if textStart == True:
				self.parseLine(stripedLine)

	def addDic(self, pos, surface):
		if pos in self.dic:
			self.dic[pos].add(surface)
		else:
			self.dic[pos] = set()
			self.dic[pos].add(surface)
	
	def getDic(self):
		return self.dic
	
	def setSeparator(self, separator):
		self.separator = separator

def main():
	fileParser = FileParser() 

	files = sys.argv
	print("input...")
	directory = "corpus/talk"
	for file in os.listdir(directory):
		fileParser.setSeparator("+")
		print(file)
		fileParser.parse(directory+"/"+file)
	directory = "corpus/write"
	for file in os.listdir(directory):
		fileParser.setSeparator(" + ")
		print(file)
		fileParser.parse(directory+"/"+file)
	dic = fileParser.getDic()
	print("output...")
	for pos, surfaces in dic.items():
		print(pos)
		outFile = open("corpus_dic/" + pos, mode="w", encoding="UTF-8")
		for surface in sorted(surfaces):
			outFile.write(surface + "\n")
		outFile.close()

if __name__ == "__main__":
	main()
