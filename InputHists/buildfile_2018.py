import ROOT
from ROOT import *
import os
from array import array
import math
from math import *
import sys
import glob
import csv
import ctypes
from ctypes import *
import XRootD
from pyxrootd import client
import numpy as np

#from future import division

class Build:
	def __init__(self, name, bfile1, bfile2, bfile3, bfile4, dfile1, sfile10, sfile20, sfile25, sfile50, sfile75, sfile100, sfile125, sfile150):
		gROOT.SetBatch(True)

		#Output Files
	        ofile = ROOT.TFile(name + ".root", "RECREATE")
	        ofile.cd()


		#background files
		self.f = TFile.Open(dfile1, "READ")
		self.f.ls();

		self.Data_p7_w = self.f.Get("jet_pt_soft_pass_wide8_wide")
		self.Data_f7_w = self.f.Get("jet_pt_soft_fail_wide8_wide")
		self.Data_p1 = self.f.Get("pass_soft")
		self.Data_f1 = self.f.Get("fail_soft")
		

		self.g = TFile(bfile1, "READ")
		self.TTBar_p7_w = self.g.Get("jet_pt_soft_pass_wide8_wide")
		self.TTBar_f7_w = self.g.Get("jet_pt_soft_fail_wide8_wide")
		
		self.TTBar_p1 = self.g.Get("pass_soft")	
		self.TTBar_f1 = self.g.Get("fail_soft")	
		
		self.TTBar_p7_w_puUp = self.g.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.TTBar_f7_w_puUp = self.g.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.TTBar_p1_puUp = self.g.Get("pass_soft_puUp")	
		self.TTBar_f1_puUp = self.g.Get("fail_soft_puUp")	
		
		self.TTBar_p7_w_puDown = self.g.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.TTBar_f7_w_puDown = self.g.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.TTBar_p1_puDown = self.g.Get("pass_soft_puDown")	
		self.TTBar_f1_puDown = self.g.Get("fail_soft_puDown")	
		
		self.TTBar_p7_w_jerUp = self.g.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.TTBar_f7_w_jerUp = self.g.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.TTBar_p1_jerUp = self.g.Get("pass_soft_jerUp")	
		self.TTBar_f1_jerUp = self.g.Get("fail_soft_jerUp")	
		
		self.TTBar_p7_w_jerDown = self.g.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.TTBar_f7_w_jerDown = self.g.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.TTBar_p1_jerDown = self.g.Get("pass_soft_jerDown")	
		self.TTBar_f1_jerDown = self.g.Get("fail_soft_jerDown")	
		
		self.TTBar_p7_w_jesUp = self.g.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.TTBar_f7_w_jesUp = self.g.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.TTBar_p1_jesUp = self.g.Get("pass_soft_jesUp")	
		self.TTBar_f1_jesUp = self.g.Get("fail_soft_jesUp")	
		
		self.TTBar_p7_w_jesDown = self.g.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.TTBar_f7_w_jesDown = self.g.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.TTBar_p1_jesDown = self.g.Get("pass_soft_jesDown")	
		self.TTBar_f1_jesDown = self.g.Get("fail_soft_jesDown")	
		
		self.h = TFile(bfile2, "READ")
		self.WGamma_p7_w = self.h.Get("jet_pt_soft_pass_wide8_wide")
		self.WGamma_f7_w = self.h.Get("jet_pt_soft_fail_wide8_wide")
		
		self.WGamma_p1 = self.h.Get("pass_soft")	
		self.WGamma_f1 = self.h.Get("fail_soft")	
		
		self.WGamma_p7_w_puUp = self.h.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.WGamma_f7_w_puUp = self.h.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.WGamma_p1_puUp = self.h.Get("pass_soft_puUp")	
		self.WGamma_f1_puUp = self.h.Get("fail_soft_puUp")	
		
		self.WGamma_p7_w_puDown = self.h.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.WGamma_f7_w_puDown = self.h.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.WGamma_p1_puDown = self.h.Get("pass_soft_puDown")	
		self.WGamma_f1_puDown = self.h.Get("fail_soft_puDown")	
		
		self.WGamma_p7_w_jerUp = self.h.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.WGamma_f7_w_jerUp = self.h.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.WGamma_p1_jerUp = self.h.Get("pass_soft_jerUp")	
		self.WGamma_f1_jerUp = self.h.Get("fail_soft_jerUp")	
		
		self.WGamma_p7_w_jerDown = self.h.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.WGamma_f7_w_jerDown = self.h.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.WGamma_p1_jerDown = self.h.Get("pass_soft_jerDown")	
		self.WGamma_f1_jerDown = self.h.Get("fail_soft_jerDown")	
		
		self.WGamma_p7_w_jesUp = self.h.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.WGamma_f7_w_jesUp = self.h.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.WGamma_p1_jesUp = self.h.Get("pass_soft_jesUp")	
		self.WGamma_f1_jesUp = self.h.Get("fail_soft_jesUp")	
		
		self.WGamma_p7_w_jesDown = self.h.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.WGamma_f7_w_jesDown = self.h.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.WGamma_p1_jesDown = self.h.Get("pass_soft_jesDown")	
		self.WGamma_f1_jesDown = self.h.Get("fail_soft_jesDown")	
		
		self.j = TFile(bfile3, "READ")
		self.ZGamma_p7_w = self.j.Get("jet_pt_soft_pass_wide8_wide")
		self.ZGamma_f7_w = self.j.Get("jet_pt_soft_fail_wide8_wide")
		
		self.ZGamma_p1 = self.j.Get("pass_soft")	
		self.ZGamma_f1 = self.j.Get("fail_soft")	
		
		self.ZGamma_p7_w_puUp = self.j.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.ZGamma_f7_w_puUp = self.j.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.ZGamma_p1_puUp = self.j.Get("pass_soft_puUp")	
		self.ZGamma_f1_puUp = self.j.Get("fail_soft_puUp")	
		
		self.ZGamma_p7_w_puDown = self.j.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.ZGamma_f7_w_puDown = self.j.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.ZGamma_p1_puDown = self.j.Get("pass_soft_puDown")	
		self.ZGamma_f1_puDown = self.j.Get("fail_soft_puDown")	
		
		self.ZGamma_p7_w_jerUp = self.j.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.ZGamma_f7_w_jerUp = self.j.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.ZGamma_p1_jerUp = self.j.Get("pass_soft_jerUp")	
		self.ZGamma_f1_jerUp = self.j.Get("fail_soft_jerUp")	
		
		self.ZGamma_p7_w_jerDown = self.j.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.ZGamma_f7_w_jerDown = self.j.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.ZGamma_p1_jerDown = self.j.Get("pass_soft_jerDown")	
		self.ZGamma_f1_jerDown = self.j.Get("fail_soft_jerDown")	
		
		self.ZGamma_p7_w_jesUp = self.j.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.ZGamma_f7_w_jesUp = self.j.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.ZGamma_p1_jesUp = self.j.Get("pass_soft_jesUp")	
		self.ZGamma_f1_jesUp = self.j.Get("fail_soft_jesUp")	
		
		self.ZGamma_p7_w_jesDown = self.j.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.ZGamma_f7_w_jesDown = self.j.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.ZGamma_p1_jesDown = self.j.Get("pass_soft_jesDown")	
		self.ZGamma_f1_jesDown = self.j.Get("fail_soft_jesDown")	
		
		self.k = TFile(bfile4, "READ")
		self.GJ_p7_w = self.k.Get("jet_pt_soft_pass_wide8_wide")
		self.GJ_f7_w = self.k.Get("jet_pt_soft_fail_wide8_wide")
		
		self.GJ_p1 = self.k.Get("pass_soft")	
		self.GJ_f1 = self.k.Get("fail_soft")	
		
		self.GJ_p7_w_puUp = self.k.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.GJ_f7_w_puUp = self.k.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.GJ_p1_puUp = self.k.Get("pass_soft_puUp")	
		self.GJ_f1_puUp = self.k.Get("fail_soft_puUp")	
		
		self.GJ_p7_w_puDown = self.k.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.GJ_f7_w_puDown = self.k.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.GJ_p1_puDown = self.k.Get("pass_soft_puDown")	
		self.GJ_f1_puDown = self.k.Get("fail_soft_puDown")	
		
		self.GJ_p7_w_jerUp = self.k.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.GJ_f7_w_jerUp = self.k.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.GJ_p1_jerUp = self.k.Get("pass_soft_jerUp")	
		self.GJ_f1_jerUp = self.k.Get("fail_soft_jerUp")	
		
		self.GJ_p7_w_jerDown = self.k.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.GJ_f7_w_jerDown = self.k.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.GJ_p1_jerDown = self.k.Get("pass_soft_jerDown")	
		self.GJ_f1_jerDown = self.k.Get("fail_soft_jerDown")	
		
		self.GJ_p7_w_jesUp = self.k.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.GJ_f7_w_jesUp = self.k.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.GJ_p1_jesUp = self.k.Get("pass_soft_jesUp")	
		self.GJ_f1_jesUp = self.k.Get("fail_soft_jesUp")	
		
		self.GJ_p7_w_jesDown = self.k.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.GJ_f7_w_jesDown = self.k.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.GJ_p1_jesDown = self.k.Get("pass_soft_jesDown")	
		self.GJ_f1_jesDown = self.k.Get("fail_soft_jesDown")	

		self.s10 = TFile(sfile10, "READ")
		self.Sig10_p7_w = self.s10.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig10_f7_w = self.s10.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig10_p1 = self.s10.Get("pass_soft")	
		self.Sig10_f1 = self.s10.Get("fail_soft")	
		
		self.Sig10_p7_w_puUp = self.s10.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig10_f7_w_puUp = self.s10.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig10_p1_puUp = self.s10.Get("pass_soft_puUp")	
		self.Sig10_f1_puUp = self.s10.Get("fail_soft_puUp")	
		
		self.Sig10_p7_w_puDown = self.s10.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig10_f7_w_puDown = self.s10.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig10_p1_puDown = self.s10.Get("pass_soft_puDown")	
		self.Sig10_f1_puDown = self.s10.Get("fail_soft_puDown")	
		
		self.Sig10_p7_w_jerUp = self.s10.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig10_f7_w_jerUp = self.s10.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig10_p1_jerUp = self.s10.Get("pass_soft_jerUp")	
		self.Sig10_f1_jerUp = self.s10.Get("fail_soft_jerUp")	
		
		self.Sig10_p7_w_jerDown = self.s10.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig10_f7_w_jerDown = self.s10.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig10_p1_jerDown = self.s10.Get("pass_soft_jerDown")	
		self.Sig10_f1_jerDown = self.s10.Get("fail_soft_jerDown")	
		
		self.Sig10_p7_w_jesUp = self.s10.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig10_f7_w_jesUp = self.s10.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig10_p1_jesUp = self.s10.Get("pass_soft_jesUp")	
		self.Sig10_f1_jesUp = self.s10.Get("fail_soft_jesUp")	
		
		self.Sig10_p7_w_jesDown = self.s10.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig10_f7_w_jesDown = self.s10.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig10_p1_jesDown = self.s10.Get("pass_soft_jesDown")	
		self.Sig10_f1_jesDown = self.s10.Get("fail_soft_jesDown")	

		self.s20 = TFile(sfile20, "READ")
		self.Sig20_p7_w = self.s20.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig20_f7_w = self.s20.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig20_p1 = self.s20.Get("pass_soft")	
		self.Sig20_f1 = self.s20.Get("fail_soft")	
		
		self.Sig20_p7_w_puUp = self.s20.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig20_f7_w_puUp = self.s20.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig20_p1_puUp = self.s20.Get("pass_soft_puUp")	
		self.Sig20_f1_puUp = self.s20.Get("fail_soft_puUp")	
		
		self.Sig20_p7_w_puDown = self.s20.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig20_f7_w_puDown = self.s20.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig20_p1_puDown = self.s20.Get("pass_soft_puDown")	
		self.Sig20_f1_puDown = self.s20.Get("fail_soft_puDown")	
		
		self.Sig20_p7_w_jerUp = self.s20.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig20_f7_w_jerUp = self.s20.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig20_p1_jerUp = self.s20.Get("pass_soft_jerUp")	
		self.Sig20_f1_jerUp = self.s20.Get("fail_soft_jerUp")	
		
		self.Sig20_p7_w_jerDown = self.s20.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig20_f7_w_jerDown = self.s20.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig20_p1_jerDown = self.s20.Get("pass_soft_jerDown")	
		self.Sig20_f1_jerDown = self.s20.Get("fail_soft_jerDown")	
		
		self.Sig20_p7_w_jesUp = self.s20.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig20_f7_w_jesUp = self.s20.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig20_p1_jesUp = self.s20.Get("pass_soft_jesUp")	
		self.Sig20_f1_jesUp = self.s20.Get("fail_soft_jesUp")	
		
		self.Sig20_p7_w_jesDown = self.s20.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig20_f7_w_jesDown = self.s20.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig20_p1_jesDown = self.s20.Get("pass_soft_jesDown")	
		self.Sig20_f1_jesDown = self.s20.Get("fail_soft_jesDown")	


		self.s25 = TFile(sfile25, "READ")
		self.Sig25_p7_w = self.s25.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig25_f7_w = self.s25.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig25_p1 = self.s25.Get("pass_soft")	
		self.Sig25_f1 = self.s25.Get("fail_soft")	
		
		self.Sig25_p7_w_puUp = self.s25.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig25_f7_w_puUp = self.s25.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig25_p1_puUp = self.s25.Get("pass_soft_puUp")	
		self.Sig25_f1_puUp = self.s25.Get("fail_soft_puUp")	
		
		self.Sig25_p7_w_puDown = self.s25.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig25_f7_w_puDown = self.s25.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig25_p1_puDown = self.s25.Get("pass_soft_puDown")	
		self.Sig25_f1_puDown = self.s25.Get("fail_soft_puDown")	
		
		self.Sig25_p7_w_jerUp = self.s25.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig25_f7_w_jerUp = self.s25.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig25_p1_jerUp = self.s25.Get("pass_soft_jerUp")	
		self.Sig25_f1_jerUp = self.s25.Get("fail_soft_jerUp")	
		
		self.Sig25_p7_w_jerDown = self.s25.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig25_f7_w_jerDown = self.s25.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig25_p1_jerDown = self.s25.Get("pass_soft_jerDown")	
		self.Sig25_f1_jerDown = self.s25.Get("fail_soft_jerDown")	
		
		self.Sig25_p7_w_jesUp = self.s25.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig25_f7_w_jesUp = self.s25.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig25_p1_jesUp = self.s25.Get("pass_soft_jesUp")	
		self.Sig25_f1_jesUp = self.s25.Get("fail_soft_jesUp")	
		
		self.Sig25_p7_w_jesDown = self.s25.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig25_f7_w_jesDown = self.s25.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig25_p1_jesDown = self.s25.Get("pass_soft_jesDown")	
		self.Sig25_f1_jesDown = self.s25.Get("fail_soft_jesDown")	

		self.s50 = TFile(sfile50, "READ")
		self.Sig50_p7_w = self.s50.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig50_f7_w = self.s50.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig50_p1 = self.s50.Get("pass_soft")	
		self.Sig50_f1 = self.s50.Get("fail_soft")	
		
		self.Sig50_p7_w_puUp = self.s50.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig50_f7_w_puUp = self.s50.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig50_p1_puUp = self.s50.Get("pass_soft_puUp")	
		self.Sig50_f1_puUp = self.s50.Get("fail_soft_puUp")	
		
		self.Sig50_p7_w_puDown = self.s50.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig50_f7_w_puDown = self.s50.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig50_p1_puDown = self.s50.Get("pass_soft_puDown")	
		self.Sig50_f1_puDown = self.s50.Get("fail_soft_puDown")	
		
		self.Sig50_p7_w_jerUp = self.s50.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig50_f7_w_jerUp = self.s50.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig50_p1_jerUp = self.s50.Get("pass_soft_jerUp")	
		self.Sig50_f1_jerUp = self.s50.Get("fail_soft_jerUp")	
		
		self.Sig50_p7_w_jerDown = self.s50.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig50_f7_w_jerDown = self.s50.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig50_p1_jerDown = self.s50.Get("pass_soft_jerDown")	
		self.Sig50_f1_jerDown = self.s50.Get("fail_soft_jerDown")	
		
		self.Sig50_p7_w_jesUp = self.s50.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig50_f7_w_jesUp = self.s50.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig50_p1_jesUp = self.s50.Get("pass_soft_jesUp")	
		self.Sig50_f1_jesUp = self.s50.Get("fail_soft_jesUp")	
		
		self.Sig50_p7_w_jesDown = self.s50.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig50_f7_w_jesDown = self.s50.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig50_p1_jesDown = self.s50.Get("pass_soft_jesDown")	
		self.Sig50_f1_jesDown = self.s50.Get("fail_soft_jesDown")	

		self.s75 = TFile(sfile75, "READ")
		self.Sig75_p7_w = self.s75.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig75_f7_w = self.s75.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig75_p1 = self.s75.Get("pass_soft")	
		self.Sig75_f1 = self.s75.Get("fail_soft")	
		
		self.Sig75_p7_w_puUp = self.s75.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig75_f7_w_puUp = self.s75.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig75_p1_puUp = self.s75.Get("pass_soft_puUp")	
		self.Sig75_f1_puUp = self.s75.Get("fail_soft_puUp")	
		
		self.Sig75_p7_w_puDown = self.s75.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig75_f7_w_puDown = self.s75.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig75_p1_puDown = self.s75.Get("pass_soft_puDown")	
		self.Sig75_f1_puDown = self.s75.Get("fail_soft_puDown")	
		
		self.Sig75_p7_w_jerUp = self.s75.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig75_f7_w_jerUp = self.s75.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig75_p1_jerUp = self.s75.Get("pass_soft_jerUp")	
		self.Sig75_f1_jerUp = self.s75.Get("fail_soft_jerUp")	
		
		self.Sig75_p7_w_jerDown = self.s75.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig75_f7_w_jerDown = self.s75.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig75_p1_jerDown = self.s75.Get("pass_soft_jerDown")	
		self.Sig75_f1_jerDown = self.s75.Get("fail_soft_jerDown")	
		
		self.Sig75_p7_w_jesUp = self.s75.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig75_f7_w_jesUp = self.s75.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig75_p1_jesUp = self.s75.Get("pass_soft_jesUp")	
		self.Sig75_f1_jesUp = self.s75.Get("fail_soft_jesUp")	
		
		self.Sig75_p7_w_jesDown = self.s75.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig75_f7_w_jesDown = self.s75.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig75_p1_jesDown = self.s75.Get("pass_soft_jesDown")	
		self.Sig75_f1_jesDown = self.s75.Get("fail_soft_jesDown")	

		self.s100 = TFile(sfile100, "READ")
		self.Sig100_p7_w = self.s100.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig100_f7_w = self.s100.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig100_p1 = self.s100.Get("pass_soft")	
		self.Sig100_f1 = self.s100.Get("fail_soft")	
		
		self.Sig100_p7_w_puUp = self.s100.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig100_f7_w_puUp = self.s100.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig100_p1_puUp = self.s100.Get("pass_soft_puUp")	
		self.Sig100_f1_puUp = self.s100.Get("fail_soft_puUp")	
		
		self.Sig100_p7_w_puDown = self.s100.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig100_f7_w_puDown = self.s100.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig100_p1_puDown = self.s100.Get("pass_soft_puDown")	
		self.Sig100_f1_puDown = self.s100.Get("fail_soft_puDown")	
		
		self.Sig100_p7_w_jerUp = self.s100.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig100_f7_w_jerUp = self.s100.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig100_p1_jerUp = self.s100.Get("pass_soft_jerUp")	
		self.Sig100_f1_jerUp = self.s100.Get("fail_soft_jerUp")	
		
		self.Sig100_p7_w_jerDown = self.s100.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig100_f7_w_jerDown = self.s100.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig100_p1_jerDown = self.s100.Get("pass_soft_jerDown")	
		self.Sig100_f1_jerDown = self.s100.Get("fail_soft_jerDown")	
		
		self.Sig100_p7_w_jesUp = self.s100.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig100_f7_w_jesUp = self.s100.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig100_p1_jesUp = self.s100.Get("pass_soft_jesUp")	
		self.Sig100_f1_jesUp = self.s100.Get("fail_soft_jesUp")	
		
		self.Sig100_p7_w_jesDown = self.s100.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig100_f7_w_jesDown = self.s100.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig100_p1_jesDown = self.s100.Get("pass_soft_jesDown")	
		self.Sig100_f1_jesDown = self.s100.Get("fail_soft_jesDown")	

		self.s125 = TFile(sfile125, "READ")
		self.Sig125_p7_w = self.s125.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig125_f7_w = self.s125.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig125_p1 = self.s125.Get("pass_soft")	
		self.Sig125_f1 = self.s125.Get("fail_soft")	
		
		self.Sig125_p7_w_puUp = self.s125.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig125_f7_w_puUp = self.s125.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig125_p1_puUp = self.s125.Get("pass_soft_puUp")	
		self.Sig125_f1_puUp = self.s125.Get("fail_soft_puUp")	
		
		self.Sig125_p7_w_puDown = self.s125.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig125_f7_w_puDown = self.s125.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig125_p1_puDown = self.s125.Get("pass_soft_puDown")	
		self.Sig125_f1_puDown = self.s125.Get("fail_soft_puDown")	
		
		self.Sig125_p7_w_jerUp = self.s125.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig125_f7_w_jerUp = self.s125.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig125_p1_jerUp = self.s125.Get("pass_soft_jerUp")	
		self.Sig125_f1_jerUp = self.s125.Get("fail_soft_jerUp")	
		
		self.Sig125_p7_w_jerDown = self.s125.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig125_f7_w_jerDown = self.s125.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig125_p1_jerDown = self.s125.Get("pass_soft_jerDown")	
		self.Sig125_f1_jerDown = self.s125.Get("fail_soft_jerDown")	
		
		self.Sig125_p7_w_jesUp = self.s125.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig125_f7_w_jesUp = self.s125.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig125_p1_jesUp = self.s125.Get("pass_soft_jesUp")	
		self.Sig125_f1_jesUp = self.s125.Get("fail_soft_jesUp")	
		
		self.Sig125_p7_w_jesDown = self.s125.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig125_f7_w_jesDown = self.s125.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig125_p1_jesDown = self.s125.Get("pass_soft_jesDown")	
		self.Sig125_f1_jesDown = self.s125.Get("fail_soft_jesDown")	

		self.s150 = TFile(sfile150, "READ")
		self.Sig150_p7_w = self.s150.Get("jet_pt_soft_pass_wide8_wide")
		self.Sig150_f7_w = self.s150.Get("jet_pt_soft_fail_wide8_wide")
		
		self.Sig150_p1 = self.s150.Get("pass_soft")	
		self.Sig150_f1 = self.s150.Get("fail_soft")	
		
		self.Sig150_p7_w_puUp = self.s150.Get("jet_pt_soft_pass_wide8_wide_puUp")
		self.Sig150_f7_w_puUp = self.s150.Get("jet_pt_soft_fail_wide8_wide_puUp")
		self.Sig150_p1_puUp = self.s150.Get("pass_soft_puUp")	
		self.Sig150_f1_puUp = self.s150.Get("fail_soft_puUp")	
		
		self.Sig150_p7_w_puDown = self.s150.Get("jet_pt_soft_pass_wide8_wide_puDown")
		self.Sig150_f7_w_puDown = self.s150.Get("jet_pt_soft_fail_wide8_wide_puDown")
		self.Sig150_p1_puDown = self.s150.Get("pass_soft_puDown")	
		self.Sig150_f1_puDown = self.s150.Get("fail_soft_puDown")	
		
		self.Sig150_p7_w_jerUp = self.s150.Get("jet_pt_soft_pass_wide8_wide_jerUp")
		self.Sig150_f7_w_jerUp = self.s150.Get("jet_pt_soft_fail_wide8_wide_jerUp")
		self.Sig150_p1_jerUp = self.s150.Get("pass_soft_jerUp")	
		self.Sig150_f1_jerUp = self.s150.Get("fail_soft_jerUp")	
		
		self.Sig150_p7_w_jerDown = self.s150.Get("jet_pt_soft_pass_wide8_wide_jerDown")
		self.Sig150_f7_w_jerDown = self.s150.Get("jet_pt_soft_fail_wide8_wide_jerDown")
		self.Sig150_p1_jerDown = self.s150.Get("pass_soft_jerDown")	
		self.Sig150_f1_jerDown = self.s150.Get("fail_soft_jerDown")	
		
		self.Sig150_p7_w_jesUp = self.s150.Get("jet_pt_soft_pass_wide8_wide_jesUp")
		self.Sig150_f7_w_jesUp = self.s150.Get("jet_pt_soft_fail_wide8_wide_jesUp")
		self.Sig150_p1_jesUp = self.s150.Get("pass_soft_jesUp")	
		self.Sig150_f1_jesUp = self.s150.Get("fail_soft_jesUp")	
		
		self.Sig150_p7_w_jesDown = self.s150.Get("jet_pt_soft_pass_wide8_wide_jesDown")
		self.Sig150_f7_w_jesDown = self.s150.Get("jet_pt_soft_fail_wide8_wide_jesDown")
		self.Sig150_p1_jesDown = self.s150.Get("pass_soft_jesDown")	
		self.Sig150_f1_jesDown = self.s150.Get("fail_soft_jesDown")	
	
		#currently using 10% of data
		self.TTBar_p7_w.Scale(.1)
		self.TTBar_f7_w.Scale(.1)
		self.TTBar_p1.Scale(.1)
		self.TTBar_f1.Scale(.1)

		self.TTBar_p7_w_puUp.Scale(.1)
		self.TTBar_f7_w_puUp.Scale(.1)
		self.TTBar_p1_puUp.Scale(.1)
		self.TTBar_f1_puUp.Scale(.1)

		self.TTBar_p7_w_puDown.Scale(.1)
		self.TTBar_f7_w_puDown.Scale(.1)
		self.TTBar_p1_puDown.Scale(.1)
		self.TTBar_f1_puDown.Scale(.1)

		self.TTBar_p7_w_jerUp.Scale(.1)
		self.TTBar_f7_w_jerUp.Scale(.1)
		self.TTBar_p1_jerUp.Scale(.1)
		self.TTBar_f1_jerUp.Scale(.1)

		self.TTBar_p7_w_jerDown.Scale(.1)
		self.TTBar_f7_w_jerDown.Scale(.1)
		self.TTBar_p1_jerDown.Scale(.1)
		self.TTBar_f1_jerDown.Scale(.1)
		
		self.TTBar_p7_w_jesUp.Scale(.1)
		self.TTBar_f7_w_jesUp.Scale(.1)
		self.TTBar_p1_jesUp.Scale(.1)
		self.TTBar_f1_jesUp.Scale(.1)

		self.TTBar_p7_w_jesDown.Scale(.1)
		self.TTBar_f7_w_jesDown.Scale(.1)
		self.TTBar_p1_jesDown.Scale(.1)
		self.TTBar_f1_jesDown.Scale(.1)


		self.WGamma_p7_w.Scale(.1)
		self.WGamma_f7_w.Scale(.1)
		
		self.WGamma_p7_w_puUp.Scale(.1)
		self.WGamma_f7_w_puUp.Scale(.1)
		self.WGamma_p1_puUp.Scale(.1)
		self.WGamma_f1_puUp.Scale(.1)

		self.WGamma_p7_w_puDown.Scale(.1)
		self.WGamma_f7_w_puDown.Scale(.1)
		self.WGamma_p1_puDown.Scale(.1)
		self.WGamma_f1_puDown.Scale(.1)

		self.WGamma_p7_w_jerUp.Scale(.1)
		self.WGamma_f7_w_jerUp.Scale(.1)
		self.WGamma_p1_jerUp.Scale(.1)
		self.WGamma_f1_jerUp.Scale(.1)

		self.WGamma_p7_w_jerDown.Scale(.1)
		self.WGamma_f7_w_jerDown.Scale(.1)
		self.WGamma_p1_jerDown.Scale(.1)
		self.WGamma_f1_jerDown.Scale(.1)
		
		self.WGamma_p7_w_jesUp.Scale(.1)
		self.WGamma_f7_w_jesUp.Scale(.1)
		self.WGamma_p1_jesUp.Scale(.1)
		self.WGamma_f1_jesUp.Scale(.1)

		self.WGamma_p7_w_jesDown.Scale(.1)
		self.WGamma_f7_w_jesDown.Scale(.1)
		self.WGamma_p1_jesDown.Scale(.1)
		self.WGamma_f1_jesDown.Scale(.1)

		self.ZGamma_p7_w.Scale(.1)
		self.ZGamma_f7_w.Scale(.1)
		
		self.ZGamma_p7_w_puUp.Scale(.1)
		self.ZGamma_f7_w_puUp.Scale(.1)
		self.ZGamma_p1_puUp.Scale(.1)
		self.ZGamma_f1_puUp.Scale(.1)

		self.ZGamma_p7_w_puDown.Scale(.1)
		self.ZGamma_f7_w_puDown.Scale(.1)
		self.ZGamma_p1_puDown.Scale(.1)
		self.ZGamma_f1_puDown.Scale(.1)

		self.ZGamma_p7_w_jerUp.Scale(.1)
		self.ZGamma_f7_w_jerUp.Scale(.1)
		self.ZGamma_p1_jerUp.Scale(.1)
		self.ZGamma_f1_jerUp.Scale(.1)

		self.ZGamma_p7_w_jerDown.Scale(.1)
		self.ZGamma_f7_w_jerDown.Scale(.1)
		self.ZGamma_p1_jerDown.Scale(.1)
		self.ZGamma_f1_jerDown.Scale(.1)
		
		self.ZGamma_p7_w_jesUp.Scale(.1)
		self.ZGamma_f7_w_jesUp.Scale(.1)
		self.ZGamma_p1_jesUp.Scale(.1)
		self.ZGamma_f1_jesUp.Scale(.1)

		self.ZGamma_p7_w_jesDown.Scale(.1)
		self.ZGamma_f7_w_jesDown.Scale(.1)
		self.ZGamma_p1_jesDown.Scale(.1)
		self.ZGamma_f1_jesDown.Scale(.1)

		self.GJ_p7_w.Scale(.1)
		self.GJ_f7_w.Scale(.1)
		
		self.GJ_p7_w_puUp.Scale(.1)
		self.GJ_f7_w_puUp.Scale(.1)
		self.GJ_p1_puUp.Scale(.1)
		self.GJ_f1_puUp.Scale(.1)

		self.GJ_p7_w_puDown.Scale(.1)
		self.GJ_f7_w_puDown.Scale(.1)
		self.GJ_p1_puDown.Scale(.1)
		self.GJ_f1_puDown.Scale(.1)

		self.GJ_p7_w_jerUp.Scale(.1)
		self.GJ_f7_w_jerUp.Scale(.1)
		self.GJ_p1_jerUp.Scale(.1)
		self.GJ_f1_jerUp.Scale(.1)

		self.GJ_p7_w_jerDown.Scale(.1)
		self.GJ_f7_w_jerDown.Scale(.1)
		self.GJ_p1_jerDown.Scale(.1)
		self.GJ_f1_jerDown.Scale(.1)
		
		self.GJ_p7_w_jesUp.Scale(.1)
		self.GJ_f7_w_jesUp.Scale(.1)
		self.GJ_p1_jesUp.Scale(.1)
		self.GJ_f1_jesUp.Scale(.1)

		self.GJ_p7_w_jesDown.Scale(.1)
		self.GJ_f7_w_jesDown.Scale(.1)
		self.GJ_p1_jesDown.Scale(.1)
		self.GJ_f1_jesDown.Scale(.1)

		self.Sig10_p7_w.Scale(.1)
		self.Sig10_f7_w.Scale(.1)

		self.Sig10_p7_w_puUp.Scale(.1)
		self.Sig10_f7_w_puUp.Scale(.1)
		self.Sig10_p1_puUp.Scale(.1)
		self.Sig10_f1_puUp.Scale(.1)

		self.Sig10_p7_w_puDown.Scale(.1)
		self.Sig10_f7_w_puDown.Scale(.1)
		self.Sig10_p1_puDown.Scale(.1)
		self.Sig10_f1_puDown.Scale(.1)

		self.Sig10_p7_w_jerUp.Scale(.1)
		self.Sig10_f7_w_jerUp.Scale(.1)
		self.Sig10_p1_jerUp.Scale(.1)
		self.Sig10_f1_jerUp.Scale(.1)

		self.Sig10_p7_w_jerDown.Scale(.1)
		self.Sig10_f7_w_jerDown.Scale(.1)
		self.Sig10_p1_jerDown.Scale(.1)
		self.Sig10_f1_jerDown.Scale(.1)
		
		self.Sig10_p7_w_jesUp.Scale(.1)
		self.Sig10_f7_w_jesUp.Scale(.1)
		self.Sig10_p1_jesUp.Scale(.1)
		self.Sig10_f1_jesUp.Scale(.1)

		self.Sig10_p7_w_jesDown.Scale(.1)
		self.Sig10_f7_w_jesDown.Scale(.1)
		self.Sig10_p1_jesDown.Scale(.1)
		self.Sig10_f1_jesDown.Scale(.1)

		self.Sig20_p7_w.Scale(.1)
		self.Sig20_f7_w.Scale(.1)

		self.Sig20_p7_w_puUp.Scale(.1)
		self.Sig20_f7_w_puUp.Scale(.1)
		self.Sig20_p1_puUp.Scale(.1)
		self.Sig20_f1_puUp.Scale(.1)

		self.Sig20_p7_w_puDown.Scale(.1)
		self.Sig20_f7_w_puDown.Scale(.1)
		self.Sig20_p1_puDown.Scale(.1)
		self.Sig20_f1_puDown.Scale(.1)

		self.Sig20_p7_w_jerUp.Scale(.1)
		self.Sig20_f7_w_jerUp.Scale(.1)
		self.Sig20_p1_jerUp.Scale(.1)
		self.Sig20_f1_jerUp.Scale(.1)

		self.Sig20_p7_w_jerDown.Scale(.1)
		self.Sig20_f7_w_jerDown.Scale(.1)
		self.Sig20_p1_jerDown.Scale(.1)
		self.Sig20_f1_jerDown.Scale(.1)
		
		self.Sig20_p7_w_jesUp.Scale(.1)
		self.Sig20_f7_w_jesUp.Scale(.1)
		self.Sig20_p1_jesUp.Scale(.1)
		self.Sig20_f1_jesUp.Scale(.1)

		self.Sig20_p7_w_jesDown.Scale(.1)
		self.Sig20_f7_w_jesDown.Scale(.1)
		self.Sig20_p1_jesDown.Scale(.1)
		self.Sig20_f1_jesDown.Scale(.1)


		self.Sig25_p7_w.Scale(.1)
		self.Sig25_f7_w.Scale(.1)

		self.Sig25_p7_w_puUp.Scale(.1)
		self.Sig25_f7_w_puUp.Scale(.1)
		self.Sig25_p1_puUp.Scale(.1)
		self.Sig25_f1_puUp.Scale(.1)

		self.Sig25_p7_w_puDown.Scale(.1)
		self.Sig25_f7_w_puDown.Scale(.1)
		self.Sig25_p1_puDown.Scale(.1)
		self.Sig25_f1_puDown.Scale(.1)

		self.Sig25_p7_w_jerUp.Scale(.1)
		self.Sig25_f7_w_jerUp.Scale(.1)
		self.Sig25_p1_jerUp.Scale(.1)
		self.Sig25_f1_jerUp.Scale(.1)

		self.Sig25_p7_w_jerDown.Scale(.1)
		self.Sig25_f7_w_jerDown.Scale(.1)
		self.Sig25_p1_jerDown.Scale(.1)
		self.Sig25_f1_jerDown.Scale(.1)
		
		self.Sig25_p7_w_jesUp.Scale(.1)
		self.Sig25_f7_w_jesUp.Scale(.1)
		self.Sig25_p1_jesUp.Scale(.1)
		self.Sig25_f1_jesUp.Scale(.1)

		self.Sig25_p7_w_jesDown.Scale(.1)
		self.Sig25_f7_w_jesDown.Scale(.1)
		self.Sig25_p1_jesDown.Scale(.1)
		self.Sig25_f1_jesDown.Scale(.1)
		
		self.Sig50_p7_w.Scale(.1)
		self.Sig50_f7_w.Scale(.1)

		self.Sig50_p7_w_puUp.Scale(.1)
		self.Sig50_f7_w_puUp.Scale(.1)
		self.Sig50_p1_puUp.Scale(.1)
		self.Sig50_f1_puUp.Scale(.1)

		self.Sig50_p7_w_puDown.Scale(.1)
		self.Sig50_f7_w_puDown.Scale(.1)
		self.Sig50_p1_puDown.Scale(.1)
		self.Sig50_f1_puDown.Scale(.1)

		self.Sig50_p7_w_jerUp.Scale(.1)
		self.Sig50_f7_w_jerUp.Scale(.1)
		self.Sig50_p1_jerUp.Scale(.1)
		self.Sig50_f1_jerUp.Scale(.1)

		self.Sig50_p7_w_jerDown.Scale(.1)
		self.Sig50_f7_w_jerDown.Scale(.1)
		self.Sig50_p1_jerDown.Scale(.1)
		self.Sig50_f1_jerDown.Scale(.1)
		
		self.Sig50_p7_w_jesUp.Scale(.1)
		self.Sig50_f7_w_jesUp.Scale(.1)
		self.Sig50_p1_jesUp.Scale(.1)
		self.Sig50_f1_jesUp.Scale(.1)

		self.Sig50_p7_w_jesDown.Scale(.1)
		self.Sig50_f7_w_jesDown.Scale(.1)
		self.Sig50_p1_jesDown.Scale(.1)
		self.Sig50_f1_jesDown.Scale(.1)

		self.Sig75_p7_w.Scale(.1)
		self.Sig75_f7_w.Scale(.1)

		self.Sig75_p7_w_puUp.Scale(.1)
		self.Sig75_f7_w_puUp.Scale(.1)
		self.Sig75_p1_puUp.Scale(.1)
		self.Sig75_f1_puUp.Scale(.1)

		self.Sig75_p7_w_puDown.Scale(.1)
		self.Sig75_f7_w_puDown.Scale(.1)
		self.Sig75_p1_puDown.Scale(.1)
		self.Sig75_f1_puDown.Scale(.1)

		self.Sig75_p7_w_jerUp.Scale(.1)
		self.Sig75_f7_w_jerUp.Scale(.1)
		self.Sig75_p1_jerUp.Scale(.1)
		self.Sig75_f1_jerUp.Scale(.1)

		self.Sig75_p7_w_jerDown.Scale(.1)
		self.Sig75_f7_w_jerDown.Scale(.1)
		self.Sig75_p1_jerDown.Scale(.1)
		self.Sig75_f1_jerDown.Scale(.1)
		
		self.Sig75_p7_w_jesUp.Scale(.1)
		self.Sig75_f7_w_jesUp.Scale(.1)
		self.Sig75_p1_jesUp.Scale(.1)
		self.Sig75_f1_jesUp.Scale(.1)

		self.Sig75_p7_w_jesDown.Scale(.1)
		self.Sig75_f7_w_jesDown.Scale(.1)
		self.Sig75_p1_jesDown.Scale(.1)
		self.Sig75_f1_jesDown.Scale(.1)

		self.Sig100_p7_w.Scale(.1)
		self.Sig100_f7_w.Scale(.1)

		self.Sig100_p7_w_puUp.Scale(.1)
		self.Sig100_f7_w_puUp.Scale(.1)
		self.Sig100_p1_puUp.Scale(.1)
		self.Sig100_f1_puUp.Scale(.1)

		self.Sig100_p7_w_puDown.Scale(.1)
		self.Sig100_f7_w_puDown.Scale(.1)
		self.Sig100_p1_puDown.Scale(.1)
		self.Sig100_f1_puDown.Scale(.1)

		self.Sig100_p7_w_jerUp.Scale(.1)
		self.Sig100_f7_w_jerUp.Scale(.1)
		self.Sig100_p1_jerUp.Scale(.1)
		self.Sig100_f1_jerUp.Scale(.1)

		self.Sig100_p7_w_jerDown.Scale(.1)
		self.Sig100_f7_w_jerDown.Scale(.1)
		self.Sig100_p1_jerDown.Scale(.1)
		self.Sig100_f1_jerDown.Scale(.1)
		
		self.Sig100_p7_w_jesUp.Scale(.1)
		self.Sig100_f7_w_jesUp.Scale(.1)
		self.Sig100_p1_jesUp.Scale(.1)
		self.Sig100_f1_jesUp.Scale(.1)

		self.Sig100_p7_w_jesDown.Scale(.1)
		self.Sig100_f7_w_jesDown.Scale(.1)
		self.Sig100_p1_jesDown.Scale(.1)
		self.Sig100_f1_jesDown.Scale(.1)

		self.Sig125_p7_w.Scale(.1)
		self.Sig125_f7_w.Scale(.1)

		self.Sig125_p7_w_puUp.Scale(.1)
		self.Sig125_f7_w_puUp.Scale(.1)
		self.Sig125_p1_puUp.Scale(.1)
		self.Sig125_f1_puUp.Scale(.1)

		self.Sig125_p7_w_puDown.Scale(.1)
		self.Sig125_f7_w_puDown.Scale(.1)
		self.Sig125_p1_puDown.Scale(.1)
		self.Sig125_f1_puDown.Scale(.1)

		self.Sig125_p7_w_jerUp.Scale(.1)
		self.Sig125_f7_w_jerUp.Scale(.1)
		self.Sig125_p1_jerUp.Scale(.1)
		self.Sig125_f1_jerUp.Scale(.1)

		self.Sig125_p7_w_jerDown.Scale(.1)
		self.Sig125_f7_w_jerDown.Scale(.1)
		self.Sig125_p1_jerDown.Scale(.1)
		self.Sig125_f1_jerDown.Scale(.1)
		
		self.Sig125_p7_w_jesUp.Scale(.1)
		self.Sig125_f7_w_jesUp.Scale(.1)
		self.Sig125_p1_jesUp.Scale(.1)
		self.Sig125_f1_jesUp.Scale(.1)

		self.Sig125_p7_w_jesDown.Scale(.1)
		self.Sig125_f7_w_jesDown.Scale(.1)
		self.Sig125_p1_jesDown.Scale(.1)
		self.Sig125_f1_jesDown.Scale(.1)

		self.Sig150_p7_w.Scale(.1)
		self.Sig150_f7_w.Scale(.1)

		self.Sig150_p7_w_puUp.Scale(.1)
		self.Sig150_f7_w_puUp.Scale(.1)
		self.Sig150_p1_puUp.Scale(.1)
		self.Sig150_f1_puUp.Scale(.1)

		self.Sig150_p7_w_puDown.Scale(.1)
		self.Sig150_f7_w_puDown.Scale(.1)
		self.Sig150_p1_puDown.Scale(.1)
		self.Sig150_f1_puDown.Scale(.1)

		self.Sig150_p7_w_jerUp.Scale(.1)
		self.Sig150_f7_w_jerUp.Scale(.1)
		self.Sig150_p1_jerUp.Scale(.1)
		self.Sig150_f1_jerUp.Scale(.1)

		self.Sig150_p7_w_jerDown.Scale(.1)
		self.Sig150_f7_w_jerDown.Scale(.1)
		self.Sig150_p1_jerDown.Scale(.1)
		self.Sig150_f1_jerDown.Scale(.1)
		
		self.Sig150_p7_w_jesUp.Scale(.1)
		self.Sig150_f7_w_jesUp.Scale(.1)
		self.Sig150_p1_jesUp.Scale(.1)
		self.Sig150_f1_jesUp.Scale(.1)

		self.Sig150_p7_w_jesDown.Scale(.1)
		self.Sig150_f7_w_jesDown.Scale(.1)
		self.Sig150_p1_jesDown.Scale(.1)
		self.Sig150_f1_jesDown.Scale(.1)

	
		
		ofile.WriteObject(self.Data_p7_w, "Data_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Data_f7_w, "Data_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Data_p1, "Data_pass_soft")
		ofile.WriteObject(self.Data_f1, "Data_fail_soft")
		
		
		ofile.WriteObject(self.TTBar_p7_w, "TTBar_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.TTBar_f7_w, "TTBar_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.TTBar_p1, "TTBar_pass_soft")
		ofile.WriteObject(self.TTBar_f1, "TTBar_fail_soft")
		
		ofile.WriteObject(self.TTBar_p7_w_puUp, "TTBar_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.TTBar_f7_w_puUp, "TTBar_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.TTBar_p1_puUp, "TTBar_pass_soft_puUp")
		ofile.WriteObject(self.TTBar_f1_puUp, "TTBar_fail_soft_puUp")

		ofile.WriteObject(self.TTBar_p7_w_puDown, "TTBar_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.TTBar_f7_w_puDown, "TTBar_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.TTBar_p1_puDown, "TTBar_pass_soft_puDown")
		ofile.WriteObject(self.TTBar_f1_puDown, "TTBar_fail_soft_puDown")
		
		ofile.WriteObject(self.TTBar_p7_w_jerUp, "TTBar_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.TTBar_f7_w_jerUp, "TTBar_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.TTBar_p1_jerUp, "TTBar_pass_soft_jerUp")
		ofile.WriteObject(self.TTBar_f1_jerUp, "TTBar_fail_soft_jerUp")

		ofile.WriteObject(self.TTBar_p7_w_jerDown, "TTBar_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.TTBar_f7_w_jerDown, "TTBar_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.TTBar_p1_jerDown, "TTBar_pass_soft_jerDown")
		ofile.WriteObject(self.TTBar_f1_jerDown, "TTBar_fail_soft_jerDown")
		
		ofile.WriteObject(self.TTBar_p7_w_jesUp, "TTBar_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.TTBar_f7_w_jesUp, "TTBar_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.TTBar_p1_jesUp, "TTBar_pass_soft_jesUp")
		ofile.WriteObject(self.TTBar_f1_jesUp, "TTBar_fail_soft_jesUp")

		ofile.WriteObject(self.TTBar_p7_w_jesDown, "TTBar_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.TTBar_f7_w_jesDown, "TTBar_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.TTBar_p1_jesDown, "TTBar_pass_soft_jesDown")
		ofile.WriteObject(self.TTBar_f1_jesDown, "TTBar_fail_soft_jesDown")


		ofile.WriteObject(self.WGamma_p7_w, "WGamma_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.WGamma_f7_w, "WGamma_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.WGamma_p1, "WGamma_pass_soft")
		ofile.WriteObject(self.WGamma_f1, "WGamma_fail_soft")
		
		ofile.WriteObject(self.WGamma_p7_w_puUp, "WGamma_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.WGamma_f7_w_puUp, "WGamma_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.WGamma_p1_puUp, "WGamma_pass_soft_puUp")
		ofile.WriteObject(self.WGamma_f1_puUp, "WGamma_fail_soft_puUp")

		ofile.WriteObject(self.WGamma_p7_w_puDown, "WGamma_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.WGamma_f7_w_puDown, "WGamma_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.WGamma_p1_puDown, "WGamma_pass_soft_puDown")
		ofile.WriteObject(self.WGamma_f1_puDown, "WGamma_fail_soft_puDown")
		
		ofile.WriteObject(self.WGamma_p7_w_jerUp, "WGamma_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.WGamma_f7_w_jerUp, "WGamma_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.WGamma_p1_jerUp, "WGamma_pass_soft_jerUp")
		ofile.WriteObject(self.WGamma_f1_jerUp, "WGamma_fail_soft_jerUp")

		ofile.WriteObject(self.WGamma_p7_w_jerDown, "WGamma_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.WGamma_f7_w_jerDown, "WGamma_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.WGamma_p1_jerDown, "WGamma_pass_soft_jerDown")
		ofile.WriteObject(self.WGamma_f1_jerDown, "WGamma_fail_soft_jerDown")
		
		ofile.WriteObject(self.WGamma_p7_w_jesUp, "WGamma_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.WGamma_f7_w_jesUp, "WGamma_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.WGamma_p1_jesUp, "WGamma_pass_soft_jesUp")
		ofile.WriteObject(self.WGamma_f1_jesUp, "WGamma_fail_soft_jesUp")

		ofile.WriteObject(self.WGamma_p7_w_jesDown, "WGamma_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.WGamma_f7_w_jesDown, "WGamma_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.WGamma_p1_jesDown, "WGamma_pass_soft_jesDown")
		ofile.WriteObject(self.WGamma_f1_jesDown, "WGamma_fail_soft_jesDown")



		ofile.WriteObject(self.ZGamma_p7_w, "ZGamma_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.ZGamma_f7_w, "ZGamma_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.ZGamma_p1, "ZGamma_pass_soft")
		ofile.WriteObject(self.ZGamma_f1, "ZGamma_fail_soft")
		
		ofile.WriteObject(self.ZGamma_p7_w_puUp, "ZGamma_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.ZGamma_f7_w_puUp, "ZGamma_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.ZGamma_p1_puUp, "ZGamma_pass_soft_puUp")
		ofile.WriteObject(self.ZGamma_f1_puUp, "ZGamma_fail_soft_puUp")

		ofile.WriteObject(self.ZGamma_p7_w_puDown, "ZGamma_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.ZGamma_f7_w_puDown, "ZGamma_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.ZGamma_p1_puDown, "ZGamma_pass_soft_puDown")
		ofile.WriteObject(self.ZGamma_f1_puDown, "ZGamma_fail_soft_puDown")
		
		ofile.WriteObject(self.ZGamma_p7_w_jerUp, "ZGamma_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.ZGamma_f7_w_jerUp, "ZGamma_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.ZGamma_p1_jerUp, "ZGamma_pass_soft_jerUp")
		ofile.WriteObject(self.ZGamma_f1_jerUp, "ZGamma_fail_soft_jerUp")

		ofile.WriteObject(self.ZGamma_p7_w_jerDown, "ZGamma_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.ZGamma_f7_w_jerDown, "ZGamma_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.ZGamma_p1_jerDown, "ZGamma_pass_soft_jerDown")
		ofile.WriteObject(self.ZGamma_f1_jerDown, "ZGamma_fail_soft_jerDown")
		
		ofile.WriteObject(self.ZGamma_p7_w_jesUp, "ZGamma_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.ZGamma_f7_w_jesUp, "ZGamma_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.ZGamma_p1_jesUp, "ZGamma_pass_soft_jesUp")
		ofile.WriteObject(self.ZGamma_f1_jesUp, "ZGamma_fail_soft_jesUp")

		ofile.WriteObject(self.ZGamma_p7_w_jesDown, "ZGamma_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.ZGamma_f7_w_jesDown, "ZGamma_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.ZGamma_p1_jesDown, "ZGamma_pass_soft_jesDown")
		ofile.WriteObject(self.ZGamma_f1_jesDown, "ZGamma_fail_soft_jesDown")



		ofile.WriteObject(self.GJ_p7_w, "GJ_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.GJ_f7_w, "GJ_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.GJ_p1, "GJ_pass_soft")
		ofile.WriteObject(self.GJ_f1, "GJ_fail_soft")
		
		ofile.WriteObject(self.GJ_p7_w_puUp, "GJ_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.GJ_f7_w_puUp, "GJ_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.GJ_p1_puUp, "GJ_pass_soft_puUp")
		ofile.WriteObject(self.GJ_f1_puUp, "GJ_fail_soft_puUp")

		ofile.WriteObject(self.GJ_p7_w_puDown, "GJ_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.GJ_f7_w_puDown, "GJ_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.GJ_p1_puDown, "GJ_pass_soft_puDown")
		ofile.WriteObject(self.GJ_f1_puDown, "GJ_fail_soft_puDown")
		
		ofile.WriteObject(self.GJ_p7_w_jerUp, "GJ_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.GJ_f7_w_jerUp, "GJ_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.GJ_p1_jerUp, "GJ_pass_soft_jerUp")
		ofile.WriteObject(self.GJ_f1_jerUp, "GJ_fail_soft_jerUp")

		ofile.WriteObject(self.GJ_p7_w_jerDown, "GJ_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.GJ_f7_w_jerDown, "GJ_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.GJ_p1_jerDown, "GJ_pass_soft_jerDown")
		ofile.WriteObject(self.GJ_f1_jerDown, "GJ_fail_soft_jerDown")
		
		ofile.WriteObject(self.GJ_p7_w_jesUp, "GJ_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.GJ_f7_w_jesUp, "GJ_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.GJ_p1_jesUp, "GJ_pass_soft_jesUp")
		ofile.WriteObject(self.GJ_f1_jesUp, "GJ_fail_soft_jesUp")

		ofile.WriteObject(self.GJ_p7_w_jesDown, "GJ_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.GJ_f7_w_jesDown, "GJ_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.GJ_p1_jesDown, "GJ_pass_soft_jesDown")
		ofile.WriteObject(self.GJ_f1_jesDown, "GJ_fail_soft_jesDown")

		ofile.WriteObject(self.Sig10_p7_w, "Sig10_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig10_f7_w, "Sig10_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig10_p1, "Sig10_pass_soft")
		ofile.WriteObject(self.Sig10_f1, "Sig10_fail_soft")
		
		ofile.WriteObject(self.Sig10_p7_w_puUp, "Sig10_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig10_f7_w_puUp, "Sig10_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig10_p1_puUp, "Sig10_pass_soft_puUp")
		ofile.WriteObject(self.Sig10_f1_puUp, "Sig10_fail_soft_puUp")

		ofile.WriteObject(self.Sig10_p7_w_puDown, "Sig10_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig10_f7_w_puDown, "Sig10_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig10_p1_puDown, "Sig10_pass_soft_puDown")
		ofile.WriteObject(self.Sig10_f1_puDown, "Sig10_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig10_p7_w_jerUp, "Sig10_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig10_f7_w_jerUp, "Sig10_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig10_p1_jerUp, "Sig10_pass_soft_jerUp")
		ofile.WriteObject(self.Sig10_f1_jerUp, "Sig10_fail_soft_jerUp")

		ofile.WriteObject(self.Sig10_p7_w_jerDown, "Sig10_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig10_f7_w_jerDown, "Sig10_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig10_p1_jerDown, "Sig10_pass_soft_jerDown")
		ofile.WriteObject(self.Sig10_f1_jerDown, "Sig10_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig10_p7_w_jesUp, "Sig10_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig10_f7_w_jesUp, "Sig10_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig10_p1_jesUp, "Sig10_pass_soft_jesUp")
		ofile.WriteObject(self.Sig10_f1_jesUp, "Sig10_fail_soft_jesUp")

		ofile.WriteObject(self.Sig10_p7_w_jesDown, "Sig10_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig10_f7_w_jesDown, "Sig10_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig10_p1_jesDown, "Sig10_pass_soft_jesDown")
		ofile.WriteObject(self.Sig10_f1_jesDown, "Sig10_fail_soft_jesDown")

		ofile.WriteObject(self.Sig20_p7_w, "Sig20_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig20_f7_w, "Sig20_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig20_p1, "Sig20_pass_soft")
		ofile.WriteObject(self.Sig20_f1, "Sig20_fail_soft")
		
		ofile.WriteObject(self.Sig20_p7_w_puUp, "Sig20_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig20_f7_w_puUp, "Sig20_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig20_p1_puUp, "Sig20_pass_soft_puUp")
		ofile.WriteObject(self.Sig20_f1_puUp, "Sig20_fail_soft_puUp")

		ofile.WriteObject(self.Sig20_p7_w_puDown, "Sig20_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig20_f7_w_puDown, "Sig20_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig20_p1_puDown, "Sig20_pass_soft_puDown")
		ofile.WriteObject(self.Sig20_f1_puDown, "Sig20_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig20_p7_w_jerUp, "Sig20_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig20_f7_w_jerUp, "Sig20_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig20_p1_jerUp, "Sig20_pass_soft_jerUp")
		ofile.WriteObject(self.Sig20_f1_jerUp, "Sig20_fail_soft_jerUp")

		ofile.WriteObject(self.Sig20_p7_w_jerDown, "Sig20_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig20_f7_w_jerDown, "Sig20_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig20_p1_jerDown, "Sig20_pass_soft_jerDown")
		ofile.WriteObject(self.Sig20_f1_jerDown, "Sig20_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig20_p7_w_jesUp, "Sig20_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig20_f7_w_jesUp, "Sig20_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig20_p1_jesUp, "Sig20_pass_soft_jesUp")
		ofile.WriteObject(self.Sig20_f1_jesUp, "Sig20_fail_soft_jesUp")

		ofile.WriteObject(self.Sig20_p7_w_jesDown, "Sig20_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig20_f7_w_jesDown, "Sig20_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig20_p1_jesDown, "Sig20_pass_soft_jesDown")
		ofile.WriteObject(self.Sig20_f1_jesDown, "Sig20_fail_soft_jesDown")
		
		ofile.WriteObject(self.Sig25_p7_w, "Sig25_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig25_f7_w, "Sig25_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig25_p1, "Sig25_pass_soft")
		ofile.WriteObject(self.Sig25_f1, "Sig25_fail_soft")
		
		ofile.WriteObject(self.Sig25_p7_w_puUp, "Sig25_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig25_f7_w_puUp, "Sig25_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig25_p1_puUp, "Sig25_pass_soft_puUp")
		ofile.WriteObject(self.Sig25_f1_puUp, "Sig25_fail_soft_puUp")

		ofile.WriteObject(self.Sig25_p7_w_puDown, "Sig25_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig25_f7_w_puDown, "Sig25_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig25_p1_puDown, "Sig25_pass_soft_puDown")
		ofile.WriteObject(self.Sig25_f1_puDown, "Sig25_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig25_p7_w_jerUp, "Sig25_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig25_f7_w_jerUp, "Sig25_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig25_p1_jerUp, "Sig25_pass_soft_jerUp")
		ofile.WriteObject(self.Sig25_f1_jerUp, "Sig25_fail_soft_jerUp")

		ofile.WriteObject(self.Sig25_p7_w_jerDown, "Sig25_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig25_f7_w_jerDown, "Sig25_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig25_p1_jerDown, "Sig25_pass_soft_jerDown")
		ofile.WriteObject(self.Sig25_f1_jerDown, "Sig25_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig25_p7_w_jesUp, "Sig25_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig25_f7_w_jesUp, "Sig25_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig25_p1_jesUp, "Sig25_pass_soft_jesUp")
		ofile.WriteObject(self.Sig25_f1_jesUp, "Sig25_fail_soft_jesUp")

		ofile.WriteObject(self.Sig25_p7_w_jesDown, "Sig25_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig25_f7_w_jesDown, "Sig25_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig25_p1_jesDown, "Sig25_pass_soft_jesDown")
		ofile.WriteObject(self.Sig25_f1_jesDown, "Sig25_fail_soft_jesDown")
		

		ofile.WriteObject(self.Sig50_p7_w, "Sig50_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig50_f7_w, "Sig50_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig50_p1, "Sig50_pass_soft")
		ofile.WriteObject(self.Sig50_f1, "Sig50_fail_soft")
		
		ofile.WriteObject(self.Sig50_p7_w_puUp, "Sig50_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig50_f7_w_puUp, "Sig50_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig50_p1_puUp, "Sig50_pass_soft_puUp")
		ofile.WriteObject(self.Sig50_f1_puUp, "Sig50_fail_soft_puUp")

		ofile.WriteObject(self.Sig50_p7_w_puDown, "Sig50_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig50_f7_w_puDown, "Sig50_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig50_p1_puDown, "Sig50_pass_soft_puDown")
		ofile.WriteObject(self.Sig50_f1_puDown, "Sig50_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig50_p7_w_jerUp, "Sig50_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig50_f7_w_jerUp, "Sig50_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig50_p1_jerUp, "Sig50_pass_soft_jerUp")
		ofile.WriteObject(self.Sig50_f1_jerUp, "Sig50_fail_soft_jerUp")

		ofile.WriteObject(self.Sig50_p7_w_jerDown, "Sig50_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig50_f7_w_jerDown, "Sig50_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig50_p1_jerDown, "Sig50_pass_soft_jerDown")
		ofile.WriteObject(self.Sig50_f1_jerDown, "Sig50_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig50_p7_w_jesUp, "Sig50_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig50_f7_w_jesUp, "Sig50_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig50_p1_jesUp, "Sig50_pass_soft_jesUp")
		ofile.WriteObject(self.Sig50_f1_jesUp, "Sig50_fail_soft_jesUp")

		ofile.WriteObject(self.Sig50_p7_w_jesDown, "Sig50_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig50_f7_w_jesDown, "Sig50_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig50_p1_jesDown, "Sig50_pass_soft_jesDown")
		ofile.WriteObject(self.Sig50_f1_jesDown, "Sig50_fail_soft_jesDown")

		
		ofile.WriteObject(self.Sig75_p7_w, "Sig75_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig75_f7_w, "Sig75_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig75_p1, "Sig75_pass_soft")
		ofile.WriteObject(self.Sig75_f1, "Sig75_fail_soft")
		
		ofile.WriteObject(self.Sig75_p7_w_puUp, "Sig75_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig75_f7_w_puUp, "Sig75_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig75_p1_puUp, "Sig75_pass_soft_puUp")
		ofile.WriteObject(self.Sig75_f1_puUp, "Sig75_fail_soft_puUp")

		ofile.WriteObject(self.Sig75_p7_w_puDown, "Sig75_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig75_f7_w_puDown, "Sig75_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig75_p1_puDown, "Sig75_pass_soft_puDown")
		ofile.WriteObject(self.Sig75_f1_puDown, "Sig75_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig75_p7_w_jerUp, "Sig75_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig75_f7_w_jerUp, "Sig75_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig75_p1_jerUp, "Sig75_pass_soft_jerUp")
		ofile.WriteObject(self.Sig75_f1_jerUp, "Sig75_fail_soft_jerUp")

		ofile.WriteObject(self.Sig75_p7_w_jerDown, "Sig75_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig75_f7_w_jerDown, "Sig75_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig75_p1_jerDown, "Sig75_pass_soft_jerDown")
		ofile.WriteObject(self.Sig75_f1_jerDown, "Sig75_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig75_p7_w_jesUp, "Sig75_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig75_f7_w_jesUp, "Sig75_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig75_p1_jesUp, "Sig75_pass_soft_jesUp")
		ofile.WriteObject(self.Sig75_f1_jesUp, "Sig75_fail_soft_jesUp")

		ofile.WriteObject(self.Sig75_p7_w_jesDown, "Sig75_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig75_f7_w_jesDown, "Sig75_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig75_p1_jesDown, "Sig75_pass_soft_jesDown")
		ofile.WriteObject(self.Sig75_f1_jesDown, "Sig75_fail_soft_jesDown")
		

		
		ofile.WriteObject(self.Sig100_p7_w, "Sig100_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig100_f7_w, "Sig100_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig100_p1, "Sig100_pass_soft")
		ofile.WriteObject(self.Sig100_f1, "Sig100_fail_soft")
		
		ofile.WriteObject(self.Sig100_p7_w_puUp, "Sig100_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig100_f7_w_puUp, "Sig100_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig100_p1_puUp, "Sig100_pass_soft_puUp")
		ofile.WriteObject(self.Sig100_f1_puUp, "Sig100_fail_soft_puUp")

		ofile.WriteObject(self.Sig100_p7_w_puDown, "Sig100_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig100_f7_w_puDown, "Sig100_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig100_p1_puDown, "Sig100_pass_soft_puDown")
		ofile.WriteObject(self.Sig100_f1_puDown, "Sig100_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig100_p7_w_jerUp, "Sig100_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig100_f7_w_jerUp, "Sig100_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig100_p1_jerUp, "Sig100_pass_soft_jerUp")
		ofile.WriteObject(self.Sig100_f1_jerUp, "Sig100_fail_soft_jerUp")

		ofile.WriteObject(self.Sig100_p7_w_jerDown, "Sig100_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig100_f7_w_jerDown, "Sig100_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig100_p1_jerDown, "Sig100_pass_soft_jerDown")
		ofile.WriteObject(self.Sig100_f1_jerDown, "Sig100_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig100_p7_w_jesUp, "Sig100_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig100_f7_w_jesUp, "Sig100_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig100_p1_jesUp, "Sig100_pass_soft_jesUp")
		ofile.WriteObject(self.Sig100_f1_jesUp, "Sig100_fail_soft_jesUp")

		ofile.WriteObject(self.Sig100_p7_w_jesDown, "Sig100_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig100_f7_w_jesDown, "Sig100_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig100_p1_jesDown, "Sig100_pass_soft_jesDown")
		ofile.WriteObject(self.Sig100_f1_jesDown, "Sig100_fail_soft_jesDown")
		
		
		ofile.WriteObject(self.Sig125_p7_w, "Sig125_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig125_f7_w, "Sig125_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig125_p1, "Sig125_pass_soft")
		ofile.WriteObject(self.Sig125_f1, "Sig125_fail_soft")
		
		ofile.WriteObject(self.Sig125_p7_w_puUp, "Sig125_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig125_f7_w_puUp, "Sig125_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig125_p1_puUp, "Sig125_pass_soft_puUp")
		ofile.WriteObject(self.Sig125_f1_puUp, "Sig125_fail_soft_puUp")

		ofile.WriteObject(self.Sig125_p7_w_puDown, "Sig125_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig125_f7_w_puDown, "Sig125_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig125_p1_puDown, "Sig125_pass_soft_puDown")
		ofile.WriteObject(self.Sig125_f1_puDown, "Sig125_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig125_p7_w_jerUp, "Sig125_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig125_f7_w_jerUp, "Sig125_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig125_p1_jerUp, "Sig125_pass_soft_jerUp")
		ofile.WriteObject(self.Sig125_f1_jerUp, "Sig125_fail_soft_jerUp")

		ofile.WriteObject(self.Sig125_p7_w_jerDown, "Sig125_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig125_f7_w_jerDown, "Sig125_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig125_p1_jerDown, "Sig125_pass_soft_jerDown")
		ofile.WriteObject(self.Sig125_f1_jerDown, "Sig125_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig125_p7_w_jesUp, "Sig125_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig125_f7_w_jesUp, "Sig125_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig125_p1_jesUp, "Sig125_pass_soft_jesUp")
		ofile.WriteObject(self.Sig125_f1_jesUp, "Sig125_fail_soft_jesUp")

		ofile.WriteObject(self.Sig125_p7_w_jesDown, "Sig125_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig125_f7_w_jesDown, "Sig125_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig125_p1_jesDown, "Sig125_pass_soft_jesDown")
		ofile.WriteObject(self.Sig125_f1_jesDown, "Sig125_fail_soft_jesDown")
		

		
		ofile.WriteObject(self.Sig150_p7_w, "Sig150_pass_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig150_f7_w, "Sig150_fail_jet_pt_soft_wide8")
		ofile.WriteObject(self.Sig150_p1, "Sig150_pass_soft")
		ofile.WriteObject(self.Sig150_f1, "Sig150_fail_soft")
		
		ofile.WriteObject(self.Sig150_p7_w_puUp, "Sig150_pass_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig150_f7_w_puUp, "Sig150_fail_jet_pt_soft_wide8_puUp")
		ofile.WriteObject(self.Sig150_p1_puUp, "Sig150_pass_soft_puUp")
		ofile.WriteObject(self.Sig150_f1_puUp, "Sig150_fail_soft_puUp")

		ofile.WriteObject(self.Sig150_p7_w_puDown, "Sig150_pass_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig150_f7_w_puDown, "Sig150_fail_jet_pt_soft_wide8_puDown")
		ofile.WriteObject(self.Sig150_p1_puDown, "Sig150_pass_soft_puDown")
		ofile.WriteObject(self.Sig150_f1_puDown, "Sig150_fail_soft_puDown")
		
		ofile.WriteObject(self.Sig150_p7_w_jerUp, "Sig150_pass_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig150_f7_w_jerUp, "Sig150_fail_jet_pt_soft_wide8_jerUp")
		ofile.WriteObject(self.Sig150_p1_jerUp, "Sig150_pass_soft_jerUp")
		ofile.WriteObject(self.Sig150_f1_jerUp, "Sig150_fail_soft_jerUp")

		ofile.WriteObject(self.Sig150_p7_w_jerDown, "Sig150_pass_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig150_f7_w_jerDown, "Sig150_fail_jet_pt_soft_wide8_jerDown")
		ofile.WriteObject(self.Sig150_p1_jerDown, "Sig150_pass_soft_jerDown")
		ofile.WriteObject(self.Sig150_f1_jerDown, "Sig150_fail_soft_jerDown")
		
		ofile.WriteObject(self.Sig150_p7_w_jesUp, "Sig150_pass_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig150_f7_w_jesUp, "Sig150_fail_jet_pt_soft_wide8_jesUp")
		ofile.WriteObject(self.Sig150_p1_jesUp, "Sig150_pass_soft_jesUp")
		ofile.WriteObject(self.Sig150_f1_jesUp, "Sig150_fail_soft_jesUp")

		ofile.WriteObject(self.Sig150_p7_w_jesDown, "Sig150_pass_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig150_f7_w_jesDown, "Sig150_fail_jet_pt_soft_wide8_jesDown")
		ofile.WriteObject(self.Sig150_p1_jesDown, "Sig150_pass_soft_jesDown")
		ofile.WriteObject(self.Sig150_f1_jesDown, "Sig150_fail_soft_jesDown")


                ofile.Write()
