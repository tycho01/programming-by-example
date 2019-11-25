from typing import List, Dict, Tuple, Union
import sys

import itertools
import numpy as np
from functools import total_ordering
import tools_pbe as tls
import tokens as tk

def atom_search(String: str, node_s: str, node_t: str, counters: Dict[str, int], s_num: int, last_idx: int) -> Tuple[List[Union[tls.ConstStr, tls.SubStr]], Dict[str, int]]:
	"""Return a tuple of every atom satisfying the relationship between two nodes, and counters of token types"""
	Atomlist = ["SubStr", "ConstStr"]
	Atoms = list()
	for atom in Atomlist:
		if atom == "SubStr":
			flag = False
			try:
				isdecimal = node_s.isdecimal()
			except:
				isdecimal = 0
			try:
				_isalpha = tk.isalpha(node_s)
			except:
				_isalpha = 0
			if isdecimal:
				func = tls.SubStr(String, "NumTok", counters["NumTok"])
				counters["NumTok"] += 1
				if func.get_value() == node_t:
					Atoms.append(func)
			if _isalpha:
				func = tls.SubStr(String, "AlphaTok", counters["AlphaTok"])
				counters["AlphaTok"] += 1
				if func.get_value() == node_t:
					Atoms.append(func)
			if s_num == 0 and node_s == node_t:
				func = tls.SubStr(String, "StartTok", 0)
				if func.get_value() == node_t:
					Atoms.append(func)
			if s_num == last_idx and node_s == node_t:
				func = tls.SubStr(String, "EndTok", 0)
				if func.get_value() == node_t:
					Atoms.append(func)
		elif atom == "ConstStr":
			if s_num == 0:
				func = tls.ConstStr(node_t)
				Atoms.append(func)
		else:
			print("atom_search did not match with any constructor.")
			return -1
	return Atoms, counters

def Make_all_combination(edges: List[List[Tuple[int, int]]], atoms: List[List[Union[tls.ConstStr, tls.SubStr]]]) -> Tuple[List[List[Tuple[int, int]]], List[List[Union[tls.ConstStr, tls.SubStr]]]]:
	"""return all combinations of edges and atoms"""
	xis = list(itertools.product(*edges))
	Ws = list(itertools.product(*atoms))
	return xis, Ws

def Make_edge_atom_for_each_eta_t(_input: str, eta_s: List[Union[str, int]], eta_t: List[Union[str, int]]) -> Tuple[List[List[Tuple[int, int]]], List[List[Union[tls.ConstStr, tls.SubStr]]]]:
	"""return edges and atoms for each eta a"""
	edges_for_each_eta_t = list()
	atoms_for_each_eta_t = list()
	last_idx = len(eta_s) - 1

	for i, node_t in enumerate(eta_t):
		nest_edges, nest_atoms = list(), list()
		counters = {"NumTok": 0, "AlphaTok": 0}
		for j, node_s in enumerate(eta_s):
			atoms, counters = atom_search(_input, node_s, node_t, counters, j, last_idx)
			if atoms != -1:
				for k in range(0, len(atoms)):
					nest_edges.append((j, i))
				nest_atoms.extend(atoms)
		edges_for_each_eta_t.append(nest_edges)
		atoms_for_each_eta_t.append(nest_atoms)

	return edges_for_each_eta_t, atoms_for_each_eta_t

def GENERATE(_input: str, _output: str) -> List[tls.DAG]:
	"""Make corresponding DAGs for each input / output pair"""
	eta_s = tls.Makenode(_input, [])
	eta_t = tls.Makenode(_output, [])
	eta = [eta_s, eta_t]

	edges, atoms = Make_edge_atom_for_each_eta_t(_input, eta_s, eta_t)
	xis, Ws = Make_all_combination(edges, atoms)

	data_structures = list()
	for xi, W in zip(xis, Ws):
		data_structure = tls.DAG(eta, eta_s, eta_t, xi, W)
		data_structures.append(data_structure)
		#print("estimated_output: ",data_structure.estimated_output())
	return data_structures
