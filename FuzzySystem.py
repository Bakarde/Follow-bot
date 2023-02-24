import math
from FuzzyTypes import *
from FuzzySet import *
import numpy as np

def rule_base_linear(y): #x je ctr_x a y je povrsina BB-a
	
	conclusions = []

	bb_rules = [BB.XS.value, BB.S.value, BB.M.value, BB.L.value, BB.XL.value]
	conc_rules = [LV.XL.value, LV.L.value, LV.M.value, LV.S.value, LV.XS.value]

	for B,C in zip(bb_rules, conc_rules):

		b = B.valueAt(y) #singleton vrijednost

		#trazimo minimum jer ce taj minimum biti gornja granica zakljucka
		minimum = b

		uni = uniform(minimum) #radimo uniform jer ce to biti max vrijednost za pripadnost zakljucku

		#zakljucak je zadehAnd uniformnog skupa i C gdje C predstavlja neizraziti skup angular velocity-ja
		zakljucak = zadehAnd(C, uni)

		conclusions.append(zakljucak)
	
	c1 = conclusions[0]
	for c in conclusions[1:]:
		c1 = zadehOr(c1,c)
	return c1
	

def rule_base_angular(x,y): #x je ctr_x a y je povrsina BB-a
	
	conclusions = []
	
	#ova dva polja ce se pokretati u for petlji jer pravila imaju ponavljajuca svojstva
	side_rules = [Side.LL.value,Side.LL.value, Side.LL.value,Side.LL.value,Side.LL.value,
			Side.L.value,Side.L.value,Side.L.value,Side.L.value,Side.L.value,
			Side.M.value, Side.M.value,Side.M.value,Side.M.value,Side.M.value,
			Side.R.value, Side.R.value, Side.R.value, Side.R.value, Side.R.value,
			Side.RR.value, Side.RR.value, Side.RR.value, Side.RR.value, Side.RR.value] 
	bb_rules = [BB.XS.value,BB.S.value,BB.M.value,BB.L.value,BB.XL.value,
			BB.XS.value, BB.S.value, BB.M.value, BB.L.value, BB.XL.value,
			BB.XS.value, BB.S.value,BB.M.value, BB.L.value, BB.XL.value,
			BB.XS.value, BB.S.value,BB.M.value, BB.L.value, BB.XL.value,
			BB.XS.value, BB.S.value,BB.M.value, BB.L.value, BB.XL.value]
	conc_rules = [AV.XXS.value,AV.XS.value,AV.XS.value,AV.S.value,AV.S.value,
			AV.XS.value, AV.XS.value, AV.S.value, AV.S.value, AV.M.value,
			AV.M.value, AV.M.value, AV.M.value, AV.M.value, AV.M.value,
			AV.XL.value, AV.XL.value, AV.L.value, AV.L.value, AV.M.value,
			AV.XXL.value, AV.XL.value,AV.XL.value, AV.L.value, AV.L.value ]
	for A,B,C in zip(side_rules, bb_rules, conc_rules):

		a = A.valueAt(x) #singleton vrijednost
		b = B.valueAt(y) #singleton vrijednost

		#trazimo minimum jer ce taj minimum biti gornja granica zakljucka
		minimum = 0.0
		
		if(a > b): minimum = b
		else: minimum = a


		uni = uniform(minimum) #radimo uniform jer ce to biti max vrijednost za pripadnost zakljucku

		#zakljucak je zadehAnd uniformnog skupa i C gdje C predstavlja neizraziti skup angular velocity-ja
		zakljucak = zadehAnd(C, uni)

		conclusions.append(zakljucak)
	
	c1 = conclusions[0]
	for c in conclusions[1:]:
		c1 = zadehOr(c1,c)
	return c1

def conclude_angular(fs):
	
	brojnik = 0.0
	nazivnik = 0.0
	(low,high) = AV.domain.value

	for x in np.arange(low,high,0.01):
		brojnik += fs.valueAt(x) * x
		nazivnik += fs.valueAt(x)
	
	if(nazivnik == 0.0): return 0.0
	else: return brojnik/nazivnik

def conclude_linear(fs):
	
	brojnik = 0.0
	nazivnik = 0.0
	(low,high) = LV.domain.value

	for x in np.arange(low,high,0.01):
		brojnik += fs.valueAt(x) * x
		nazivnik += fs.valueAt(x)
	
	if(nazivnik == 0.0): return 0.0
	else: return brojnik/nazivnik
