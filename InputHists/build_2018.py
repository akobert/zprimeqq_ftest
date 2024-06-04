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

from buildfile_2018 import *

#from future import division

if __name__ == "__main__":
	print("Starting Run")
	bfile1 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/TTBar_UL_nano_merged_10.root"
	bfile2 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/WGamma_UL_nano_merged_10.root"
	bfile3 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/ZGamma_UL_nano_merged_10.root"
	bfile4 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/GJ_UL_10.root"
	
	dfile1 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/Data_UL_10.root" 

	#Signal Files
	sfile10 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M10_UL_nano_merged_10.root"
	sfile20 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M20_UL_nano_merged_10.root"
	sfile25 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M25_UL_nano_merged_10.root"
	sfile50 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M50_UL_nano_merged_10.root"
	sfile75 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M75_UL_nano_merged_10.root"
	sfile100 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M100_UL_nano_merged_10.root"
	sfile125 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M125_UL_nano_merged_10.root"
	sfile150 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/M150_UL_nano_merged_10.root"
	
	name = "FitHist_2018"
	RData = Build(name, bfile1, bfile2, bfile3, bfile4, dfile1, sfile10, sfile20, sfile25, sfile50, sfile75, sfile100, sfile125, sfile150)
	print("FitHist Finished")
