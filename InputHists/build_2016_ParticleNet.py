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

from buildfile_2016 import *

#from future import division

if __name__ == "__main__":
	print("Starting Run")
	bfile1 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/TTBar_UL_nano_2016_merged.root"
	bfile2 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/WGamma_UL_nano_2016_merged.root"
	bfile3 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/ZGamma_UL_nano_2016_merged.root"
	bfile4 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/GJ_UL_2016.root"

	bfile5 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/TTBar_UL_nano_2016_merged.root"
	bfile6 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/WGamma_UL_nano_2016_merged.root"
	bfile7 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/ZGamma_UL_nano_2016_merged.root"
	bfile8 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/GJ_UL_2016.root"

	
	dfile1 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/Data_UL_2016.root" 
	
	dfile2 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/Data_UL_2016.root" 
	

	#Signal Files
	sfile10 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M10_UL_nano_2016_merged.root"
	sfile20 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M20_UL_nano_2016_merged.root"
	sfile25 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M25_UL_nano_2016_merged.root"
	sfile50 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M50_UL_nano_2016_merged.root"
	sfile75 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M75_UL_nano_2016_merged.root"
	sfile100 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M100_UL_nano_2016_merged.root"
	sfile125 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M125_UL_nano_2016_merged.root"
	sfile150 = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016/NanoTool_UL_ParticleNet/M150_UL_nano_2016_merged.root"

	sfile10_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M10_UL_nano_2016_merged.root"
	sfile20_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M20_UL_nano_2016_merged.root"
	sfile25_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M25_UL_nano_2016_merged.root"
	sfile50_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M50_UL_nano_2016_merged.root"
	sfile75_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M75_UL_nano_2016_merged.root"
	sfile100_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M100_UL_nano_2016_merged.root"
	sfile125_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M125_UL_nano_2016_merged.root"
	sfile150_APV = "/home/akobert/CMSSW_11_1_0_pre7/src/RData/2016APV/NanoTool_UL_ParticleNet/M150_UL_nano_2016_merged.root"
	
	name = "FitHist_2016_ParticleNet"
	RData = Build(name, bfile1, bfile2, bfile3, bfile4, bfile5, bfile6, bfile7, bfile8, dfile1, dfile2, sfile10, sfile20, sfile25, sfile50, sfile75, sfile100, sfile125, sfile150, sfile10_APV, sfile20_APV, sfile25_APV, sfile50_APV, sfile75_APV, sfile100_APV, sfile125_APV, sfile150_APV)
	print("FitHist Finished")
