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

from buildfile_2017 import *

#from future import division

if __name__ == "__main__":
	print("Starting Run")
	bfile1 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/TTBar_UL_nano_2017_merged.root"
	bfile2 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/WGamma_UL_nano_2017_merged.root"
	bfile3 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/ZGamma_UL_nano_2017_merged.root"
	bfile4 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/GJ_UL_2017.root"
	
	dfile1 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/Data_UL_2017.root" 
	
	

	#Signal Files
	sfile10 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M10_UL_nano_2017_merged.root"
	sfile20 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M20_UL_nano_2017_merged.root"
	sfile25 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M25_UL_nano_2017_merged.root"
	sfile50 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M50_UL_nano_2017_merged.root"
	sfile75 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M75_UL_nano_2017_merged.root"
	sfile100 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M100_UL_nano_2017_merged.root"
	sfile125 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M125_UL_nano_2017_merged.root"
	sfile150 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2017/NanoTool_UL_ParticleNet/M150_UL_nano_2017_merged.root"
	
	name = "FitHist_2017_ParticleNet"
	RData = Build(name, bfile1, bfile2, bfile3, bfile4, dfile1, sfile10, sfile20, sfile25, sfile50, sfile75, sfile100, sfile125, sfile150)
	print("FitHist Finished")
