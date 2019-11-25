"""extract desired tokens from a string"""
from typing import List
import sys
import re

alphaReg = re.compile(r'^[a-zA-Z]+$')
def isalpha(s: str) -> bool:
    return alphaReg.match(s) is not None

def NumTok(string: str) -> List[str]:
	node = re.findall(r"[0-9]+" , string)
	return node

def AlphaTok(string: str) -> List[str]:
	node = re.findall(r"[a-zA-Z]+" , string)
	return node

def SpaceTok(string: str) -> List[str]:
	node = [" "]
	return node

def PeriodTok(string: str) -> List[str]:
	node = ["."]
	return node

def CommaTok(string: str) -> List[str]:
	node = [","]
	return node

def LeftParenthesisTok(string: str) -> List[str]:
	node = ["("]
	return node

def RightParenthesisTok(string: str) -> List[str]:
	node = [")"]
	return node

def DQuoteTok(string: str) -> List[str]:
	node = ["\""]
	return node

def SQuoteTok(string: str) -> List[str]:
	node = ["'"]
	return node

def HyphenTok(string: str) -> List[str]:
	node = ["-"]
	return node

def UBarTok(string: str) -> List[str]:
	node = ["_"]
	return node

def SlashTok(string: str) -> List[str]:
	node = ["/"]
	return node

def StartTok(string: str) -> List[str]:
	node = string[0]
	return node

def EndTok(string: str) -> List[str]:
	node = string[-1]
	return node

def EOFTok(string: str) -> List[str]:
	node = [""]
	return node

def NoneTok(string: str) -> List[str]:
	node = [None]
	return node

def MatchTok(string: str) -> List[str]:
	node = [string]
	return node
