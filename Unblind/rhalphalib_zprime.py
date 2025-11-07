from __future__ import print_function, division
import sys
import os
import csv
import rhalphalib as rl
from rhalphalib import AffineMorphTemplate, MorphHistW2
import numpy as np
import scipy.stats
import pickle
import ROOT
from ROOT import *
import json
import pandas as pd
import argparse
import uproot
from array import array
import logging
from rich.logging import RichHandler
from rich.prompt import Confirm
from rich.pretty import pprint
import click
#from common import sys_name_updown, lumi_dict, lumi_correlated_dict_unc, lumi_1718_dict_unc, lumi_dict_unc
import time
start_time=time.time()

from rich.traceback import install
install(show_locals=False)

rl.util.install_roofit_helpers()
# rl.ParametericSample.PreferRooParametricHist = False


np.random.seed(1)
eps=0.001
do_systematics = True # Quick enable or disable non-lumi systematics

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")
    
parser = argparse.ArgumentParser(description="Rhalphalib setup.")
parser.add_argument(
    "--opath", action="store", type=str, required=True, help="Path to store output."
)
parser.add_argument(
    "--ipt", action="store", type=int, required=True, help="TF pt order."
)
parser.add_argument(
    "--irho", action="store", type=int, required=True, help="TF rho order."
)
parser.add_argument(
    "--iptMC", action="store", type=int, required=False, help="MCTF pt order."
)
parser.add_argument(
    "--irhoMC", action="store", type=int, required=False, help="MCTF rho order."
)
parser.add_argument(
    "--tagger",
    action="store",
    type=str,
    required=True,
    help="Tagger name to cut, N2DDT or ParticleNet",
)
parser.add_argument(
    "--pickle",
    action="store",
    type=str,
    required=False,
    help="Path to pickle holding templates.",
)
parser.add_argument(
    "--sigmass",
    action="store",
    type=str,
    required=False,
    default="150",
    help="mass point like 150.",
)
# parser.add_argument("--root_path", action='store', type=str, required=True, help="Path to ROOT holding templates.")
parser.add_argument(
    "--root_file",
    action="store",
    type=str,
    required=True,
    help="Path to ROOT holding templates.",
)
parser.add_argument(
    "--h_sensitivity", action="store_true", help="Just to run sensitivty check for H with toy 150 invfb data."
)
parser.add_argument(
    "--make_prefit_plot", action="store_true", help="Just to run prefit plot."
)
parser.add_argument(
    "--all_signals", action="store_true", help="Run on all signal templates."
)
parser.add_argument(
    "--scale_qcd",
    action="store_true",
    help="Scale QCD MC so its poisson matches true uncs.",
)
parser.add_argument(
    "--qcd_ftest", action="store_true", default=False, help="Run QCD ftest."
)
parser.add_argument(
    "--highbvl", action="store_true", default=False, help="Consider only highbvl."
)
parser.add_argument(
    "--lowbvl", action="store_true", default=False, help="Consider only highbvl."
)
parser.add_argument(
    "--ftest", action="store_true", default=False, help="Run ftest.")
parser.add_argument(
    "--pseudo", action="store_true", default=False, help="Run pseudo data."
)
parser.add_argument("--MCTF", action="store_true", help="Prefit the TF params to MC.")
parser.add_argument(
    "--do_systematics", action="store_true", help="Include systematics."
)
parser.add_argument(
    "--do_systematics_mu", action="store_true", help="Include systematics."
)
# do_systematics = parser.add_mutually_exclusive_group(required=True)
    # pseudo.add_argument("--data", action="store_false", dest="pseudo")
    # pseudo.add_argument("--MC", action="store_true", dest="pseudo")
    # pseudo.add_argument("--toys", action="store_true", dest="toys")
    # parser.add_argument(
    #     "--clipx",
    #     type=str2bool,
    #     default="True",
    #     choices={True, False},
    #     help="Clip x-axis to range of data",
    # )

parser.add_argument("--is_blinded", action="store_true", help="Run on 10pct dataset.")
parser.add_argument("--throwPoisson", action="store_true", help="Throw poisson.")
parser.add_argument(
    "--four_pt_bins", action="store_true", help="Sum the last two pt bins."
)
parser.add_argument("--tworeg", action="store_true", help="Two regs.")
parser.add_argument(
    "--year",
    action="store",
    type=str,
    help="Year to run on : one of 2016APV, 2016, 2017, 2018.",
)
parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
parser.add_argument("--debug", "-vv", action="store_true", help="Debug logging")

args = parser.parse_args()
# Arg processing
log_level = logging.WARNING
if args.verbose:
    log_level = logging.INFO
if args.debug:
    log_level = logging.DEBUG
logging.getLogger("matplotlib").setLevel(logging.WARNING)
logging.basicConfig(
    level=log_level,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
)
log = logging.getLogger("rich")


with open('./sf.json') as f:
    SF = json.load(f)
with open('./lumi.json') as f:
    lumi = json.load(f)

tagger = args.tagger

def badtemp_ma(hvalues, mask=None):
    # Need minimum size & more than 1 non-zero bins           
    tot = np.sum(hvalues[mask])
    
    count_nonzeros = np.sum(hvalues[mask] > 0)
    if (tot < eps) or (count_nonzeros < 2):
        return True
    else:
        return False
def syst_variation(numerator,denominator):
    """
    Get systematic variation relative to nominal (denominator)
    """
    var = np.divide(numerator,denominator)
    var[np.where(numerator==0)] = 1
    var[np.where(denominator==0)] = 1
    return var

def smass(sName):
    if sName in ['ggF','VBF','WH','ZH','ttH']:
        _mass = 125.
    elif sName in ['Wjets','EWKW','ttbar','singlet','VV', 'WGamma', 'TTBar']:
        _mass = 80.379
    elif sName in ['Zjets','Zjetsbb','EWKZ','EWKZbb', 'ZGamma']:
        _mass = 91.
    elif "Sig" in sName:
        _mass = float(sName[3:])
    else:
        raise ValueError("What is {}".format(sName))
    return _mass


def flipSF(SF, SF_unc, yield_pass, yield_fail):
    """
    Return (SF, SF_unc) for a pass/fail scale factor.
    """
    sf = 1 - (yield_pass * (SF - 1) / yield_fail)
    sfup = 1. - (SF_unc * yield_pass/yield_fail)/sf
    sfdown = 1/sfup
    return sf, sfup, sfdown

#with open("xsec.json") as f:
#    xsec_dict = json.load(f)

short_to_long = {
    # "wqq": "WJetsToQQ",
    # "zqq": "ZJetsToQQ",
    "wqq": "wqq",
    "wlnu": "wlnu",
    "tt": "tt",
    "st": "tt",
    "zqq": "zqq",
    "zbb": "zbb",
    "hbb": "hbb",    
    "dy": "dy",
    # "tt": "TTbar",
    # "st": "SingleTop",
    # "wlnu": "WJetsToLNu",
    # "m50": "VectorZPrimeToQQ_M50",
    # "m75": "VectorZPrimeToQQ_M75",
    # "m100": "VectorZPrimeToQQ_M100",
    # "m125": "VectorZPrimeToQQ_M125",
    # "m150": "VectorZPrimeToQQ_M150",
    # "m200": "VectorZPrimeToQQ_M200",
    # "m250": "VectorZPrimeToQQ_M250",
    "m50": "zpqq50",
    "m75": "zpqq75",
    "m100": "zpqq100",
    "m125": "zpqq125",
    "m150": "zpqq150",
    "m200": "zpqq200",
    "m250": "zpqq250",
    "b50": "zpbb50",
    "b75": "zpbb75",
    "b100": "zpbb100",
    "b125": "zpbb125",
    "b150": "zpbb150",
    "b200": "zpbb200",
    "b250": "zpbb250",
    # "m300" : "VectorZPrimeToQQ_M300",
}

sys_types = {
    "JES": "lnN",
    "JER": "lnN",
    "pileup_weight": "lnN",
    "lumi": "lnN",
    "phoID": "lnN",
    "trig": "lnN",
    "pu": "lnN",
    "N2DDT": "lnN",
    "ParticleNet": "lnN",
    "smear": "shape",
    "scale": "shape"
}


# pT Bins for each year
ptbinning = {
    "2016": np.array([200.0, 240.0, 275.0, 330.0, 700.0]),
    "2017": np.array([220.0, 260.0, 300.0, 360.0, 700.0]),
    "2018": np.array([120.0, 160.0, 200.0, 255.0, 700.0])
}



if args.all_signals:
    signals = [
        "Sig10",
        "Sig20",
        "Sig25",
        "Sig50",
        "Sig75",
        "Sig100",
        "Sig125",
        "Sig150",
    ]
else:
    signals = ["Sig" + args.sigmass]

poly_order = (args.ipt, args.irho)


def expo_sample(norm, scale, obs):
    cdf = scipy.stats.expon.cdf(scale=scale, x=obs.binning) * norm
    return (np.diff(cdf), obs.binning, obs.name)


def gaus_sample(norm, loc, scale, obs):
    cdf = scipy.stats.norm.cdf(loc=loc, scale=scale, x=obs.binning) * norm
    return (np.diff(cdf), obs.binning, obs.name)

def plot_mctf(tf_MCtempl, msdbins):
    """
    Plot the MC pass / fail TF as function of (pt,rho) and (pt,msd)
    """
    import matplotlib.pyplot as plt
    
    ofile = ROOT.TFile("TF_Data.root", "RECREATE")
    ofile.cd()

    # arrays for plotting pt vs msd                    
    #pts = np.linspace(0,2000,41)
    pts = np.array([0, 200, 230, 255, 290, 360, 1000, 2000])
    #ptpts, msdpts = np.meshgrid(pts[:-1] + 0.5 * np.diff(pts), msdbins[:-1] + 0.5 * np.diff(msdbins), indexing='ij')
    ptpts, msdpts = np.meshgrid(pts[:-1] + 0.5 * np.diff(pts), msdbins[:-1] + 0.5 * np.diff(msdbins), indexing='ij')
    ptpts_scaled = (ptpts) / (2000.)
    
    rhopts = 2*np.log(msdpts/ptpts)

    rhopts_scaled = (rhopts - (-7.3)) / ((-2.0) - (-7.3))
    validbins = (rhopts_scaled >= 0) & (rhopts_scaled <= 1)

    ptpts = ptpts[validbins]
    msdpts = msdpts[validbins]
    ptpts_scaled = ptpts_scaled[validbins]
    rhopts_scaled = rhopts_scaled[validbins]

    tf_MCtempl_vals = tf_MCtempl(ptpts_scaled, rhopts_scaled, nominal=True)
    df = pd.DataFrame([])
    df['msd'] = msdpts.reshape(-1)
    df['pt'] = ptpts.reshape(-1)
    df['MCTF'] = tf_MCtempl_vals.reshape(-1)
    
    mpt = df.to_numpy()
    
    ROOT.gInterpreter.Declare("Double_t widebins6[9] = {0, 200, 230, 255, 290, 360, 1000, 2000};")
    mpt_TF = TH2F("mpt_TF", "Mass vs. pT Transfer Factor", 7, widebins6, 40, 0, 2000)
    for i in range(0, mpt.shape[0]):
        mpt_TF.Fill(mpt[i][0], mpt[i][1], mpt[i][2])
#       print(mpt[i][2])
    
    ofile.WriteObject(mpt_TF, "mpt_TF")

    fig, ax = plt.subplots()
    h = ax.hist2d(x=df["msd"],y=df["pt"],weights=df["MCTF"], bins=(msdbins,pts))
    plt.xlabel("$m_{sd}$ [GeV]")
    plt.ylabel("$p_{T}$ [GeV]")
    cb = fig.colorbar(h[3],ax=ax)
    cb.set_label("Ratio")
    fig.savefig("MCTF_msdpt_2016_sig25v2.png",bbox="tight")
    plt.clf()

    # arrays for plotting pt vs rho                                          
    rhos = np.linspace(-7.3,-2.0,41)
    #ptpts, rhopts = np.meshgrid(pts[:-1] + 0.5*np.diff(pts), rhos[:-1] + 0.5 * np.diff(rhos), indexing='ij')
    ptpts, rhopts = np.meshgrid(pts[:-1] + 0.5*np.diff(pts), rhos[:-1] + 0.5 * np.diff(rhos), indexing='ij')
    ptpts_scaled = (ptpts) / (2000)
    rhopts_scaled = (rhopts - (-7.3)) / ((-2.0) - (-7.3))
    validbins = (rhopts_scaled >= 0) & (rhopts_scaled <= 1)

    ptpts = ptpts[validbins]
    rhopts = rhopts[validbins]
    ptpts_scaled = ptpts_scaled[validbins]
    rhopts_scaled = rhopts_scaled[validbins]

    tf_MCtempl_vals = tf_MCtempl(ptpts_scaled, rhopts_scaled, nominal=True)

    df = pd.DataFrame([])
    df['rho'] = rhopts.reshape(-1)
    df['pt'] = ptpts.reshape(-1)
    df['MCTF'] = tf_MCtempl_vals.reshape(-1)

    rpt = df.to_numpy()

    rpt_TF = TH2F("rpt_TF", "Rho vs. pT Transfer Factor", 40, -9, 0, 40, 0, 2000)
    for i in range(0, rpt.shape[0]):
        rpt_TF.Fill(rpt[i][0], rpt[i][1], rpt[i][2])

    
    ofile.WriteObject(rpt_TF, "rpt_TF")
    
    
    
    fig, ax = plt.subplots()
    h = ax.hist2d(x=df["rho"],y=df["pt"],weights=df["MCTF"],bins=(rhos,pts))
    plt.xlabel("rho")
    plt.ylabel("$p_{T}$ [GeV]")
    cb = fig.colorbar(h[3],ax=ax)
    cb.set_label("Ratio")
    fig.savefig("MCTF_rhopt_2016_sig25v2.png",bbox="tight")

    return


#root_fn = args.root_file
#root_file = uproot.open(root_fn)
def get_template(sName, passed, ptbin, year, obs, syst, muon=False):
    """
    Read msd template from root file
    """
#    f = ROOT.TFile.Open('FitHist.root')
    f = ROOT.TFile.Open(args.root_file)

    name = 'fail'
    if passed:
        name = 'pass'

    if year == '2018':
        #name = sName+'_'+name+'_'+"jet_pt_soft_wide15_"+str(year)
        name = sName+'_'+name+'_'+"jet_pt_soft_wide15"
    else:
        #name = sName+'_'+name+'_'+"jet_pt_soft_wide11_"+str(year)
        name = sName+'_'+name+'_'+"jet_pt_soft_wide11"

    if syst != 'nominal':
        name += '_'+syst


    h = f.Get(name)
#    print("Template: "+name)
    sumw = []
    sumw2 = []
    #for i in range(1, h.GetNbinsX()+1):
    #for i in range(1, 11):
    for i in range(1, 41):
        sumw += [h.GetBinContent(ptbin, i)]
        sumw2 += [h.GetBinError(ptbin, i)*h.GetBinError(ptbin, i)]

    integral = np.array(sumw).sum()
#    print("For template "+name+" integral is "+str(integral))
    
    return (np.array(sumw), obs.binning, obs.name, np.array(sumw2))

def get_template2(sName, passed, ptbin, year, obs, syst, muon=False):
    """
    Read msd template from root file
    """
#    f = ROOT.TFile.Open('FitHist.root')
    f = ROOT.TFile.Open(args.root_file)

    name = 'fail'
    if passed:
        name = 'pass'

    if year == '2018':
        #name = sName+'_'+name+'_'+"jet_pt_soft_wide15_"+str(year)
        name = sName+'_'+name+'_'+"jet_pt_soft_wide15"
    else:
        #name = sName+'_'+name+'_'+"jet_pt_soft_wide11_"+str(year)
        name = sName+'_'+name+'_'+"jet_pt_soft_wide11"

    h = f.Get(name)
#    print("Template: "+name)
    sumw = []
    sumw2 = []
    #for i in range(1, 41):
    for i in range(1, 41):
        sumw += [h.GetBinContent(ptbin, i)]
        sumw2 += [h.GetBinError(ptbin, i)*h.GetBinError(ptbin, i)]

    integral = np.array(sumw).sum()
 #   print("For template "+name+" integral is "+str(integral))
    
    return (np.array(sumw), obs.binning, obs.name, np.array(sumw2))


def th1_to_numpy(path, label="msd"):
    with uproot.open(path) as file:
        th1d = file[label]
        _hist, _ = th1d.to_numpy()
    return _hist


def shape_to_num(var, nom, clip=1.5):
    nom_rate = np.sum(nom)
    var_rate = np.sum(var)

    if abs(var_rate/nom_rate) > clip:
        var_rate = clip*nom_rate

    if var_rate < 0:
        var_rate = 0

    return var_rate/nom_rate

def num_to_hist(num, title):
    hist = TH1F("hist_conv", title, 40, 0, 200) 

    for i in range(1, num.size+1):
        hist.SetBinContent(i, num[i-1])

    return hist

def passfailSF(isPass, sName, ptbin, year, obs, mask, SF=1, SF_unc=0.1, muon=False):
    """
    Return (SF, SF_unc) for a pass/fail scale factor.
    """
    if isPass:
        return SF, 1. + SF_unc / SF
    else:
        _pass = get_template(sName, 1, ptbin, year, obs=obs, syst='nominal', muon=muon)
        _pass_rate = np.sum(_pass[0] * mask)

        _fail = get_template(sName, 0, ptbin, year, obs=obs, syst='nominal', muon=muon)
        _fail_rate = np.sum(_fail[0] * mask)

        if _fail_rate > 0:
            _sf = 1 + (1 - SF) * _pass_rate / _fail_rate
            _sfunc = 1. - SF_unc * (_pass_rate / _fail_rate)
            return _sf, _sfunc
        else:
            return 1, 1

def test_rhalphabet(tmpdir, sig, throwPoisson=False):
    # Xsection floating params
    tqq_xs = rl.NuisanceParameter('tqq_xs_{}'.format(args.year), 'lnN', 1., 0, 10)
    WG_xs = rl.NuisanceParameter('WG_xs_{}'.format(args.year), 'lnN', 1., 0, 10)
    ZG_xs = rl.NuisanceParameter('ZG_xs_{}'.format(args.year), 'lnN', 1., 0, 10)

    # Systematics
    sys_lumi = rl.NuisanceParameter('CMS_lumi_13TeV_{}'.format(args.year[:4]), 'lnN')
    sys_phoID = rl.NuisanceParameter('CMS_phoID_13TeV_{}'.format(args.year[:4]), 'lnN')
    sys_trig = rl.NuisanceParameter('CMS_trig_13TeV_{}'.format(args.year[:4]), 'lnN') #Trigger Systematic

    sys_dict = {}
    
    sys_dict['jes'] = rl.NuisanceParameter('CMS_scale_j_{}'.format(args.year), 'lnN')
    sys_dict['jer'] = rl.NuisanceParameter('CMS_res_j_{}'.format(args.year), 'lnN')
    
    sys_dict['pu'] = rl.NuisanceParameter('CMS_PU_{}'.format(args.year), 'lnN')

    sys_Tag_eff = rl.NuisanceParameter('CMS_'+str(args.tagger)+'eff_{}'.format(args.year), 'lnN') # N2DDT or ParticleNet Systematic

    sys_smear = rl.NuisanceParameter('CMS_smear_{}'.format(args.year), 'shape')
    sys_scale = rl.NuisanceParameter('CMS_scale_{}'.format(args.year), 'shape')

    # Systematic Tags
    exp_systs = ['pu', 'jes', 'jer']

    # define bins    
    ptbins = ptbinning[args.year]
    npt = len(ptbins) - 1
    msdbins = np.linspace(0, 200, 41)
    msd = rl.Observable('msd', msdbins)

    # here we derive these all at once with 2D array
    ptpts, msdpts = np.meshgrid(ptbins[:-1] + 0.5 * np.diff(ptbins), msdbins[:-1] + 0.5 * np.diff(msdbins), indexing='ij')
    print(ptpts)
    print(msdpts)
    rhopts = 2*np.log(msdpts/ptpts)
    print(rhopts)
    ptscaled = (ptpts - ptbins[0]) / (ptbins[-1] - ptbins[0])
    rhoscaled = (rhopts - (-7.3)) / ((-2.0) - (-7.3))
    validbins = (rhoscaled >= 0) & (rhoscaled <= 1)
    rhoscaled[~validbins] = 1  # we will mask these out later

    fitfailed_GJ = 0
    
    while fitfailed_GJ < 5:
        # Build MC pass+fail model and fit to polynomial
        GJmodel = rl.Model('GJmodel')
        GJpass, GJfail = 0., 0.
        pass_count, fail_count = 0., 0.
    
        
        for ptbin in range(npt):
            failCh = rl.Channel('ptbin%d%s' % (ptbin, 'fail'))
            passCh = rl.Channel('ptbin%d%s' % (ptbin, 'pass'))
            GJmodel.addChannel(failCh)
            GJmodel.addChannel(passCh)

            # GJ templates from file
            failTempl = get_template('GJ', 0, ptbin+2, args.year, obs=msd, syst='nominal') 
            passTempl = get_template('GJ', 1, ptbin+2, args.year, obs=msd, syst='nominal') 
        

            failCh.setObservation(failTempl, read_sumw2=True)
            passCh.setObservation(passTempl, read_sumw2=True)


            GJfail += sum([val for val in failCh.getObservation()[0]])
            fail_count += sum([val for val in failCh.getObservation()[0]])

            print(GJfail)
            print(fail_count)
            GJpass += sum([val for val in passCh.getObservation()[0]])
            pass_count += sum([val for val in passCh.getObservation()[0]])
            print(GJpass)
            print(pass_count)

        GJeff = GJpass / GJfail
        print('Inclusive P/F from Monte Carlo = ' + str(GJeff))

        # initial values

        degsMC = tuple([int(s) for s in [args.ipt, args.irho]])
        _initsMC = np.ones(tuple(n + 1 for n in degsMC))
    
        log.debug(f"Initializing MCTF with n_pt={args.ipt} and n_rho={args.irho}")
        log.debug(_initsMC)
        if fitfailed_GJ == 0:
            tf_MCtempl = rl.BasisPoly(
                f"tf{args.year}_MC_templ",
                degsMC,
                ["pt", "rho"],
                basis="Bernstein",
                init_params=_initsMC,
                limits=(-50, 50),
                coefficient_transform=None,
            )
        else:
            # initial values                                                                 
            print('Initial fit values read from file initial_vals*')
            with open(f'{opath}initial_vals_mc_{args.ipt}{args.irho}.json') as f:
                initial_vals = np.array(json.load(f)['initial_vals'])
            print(initial_vals)
            tf_MCtempl = rl.BasisPoly(
                f"tf{args.year}_MC_templ",
                degsMC,
                ["pt", "rho"],
                basis="Bernstein",
                init_params=initial_vals,
                limits=(-50, 50),
                coefficient_transform=None,
            )
        #tf_MCtempl = rl.BasisPoly('tf_MCtempl', (2, 2), ['pt', 'rho'], basis='Bernstein', init_params=initial_vals, limits=(-100, 100))
        tf_MCtempl_params = GJeff * tf_MCtempl(ptscaled, rhoscaled)
        for ptbin in range(npt):
            failCh = GJmodel['ptbin%dfail' % ptbin]
            passCh = GJmodel['ptbin%dpass' % ptbin]
            failObs = failCh.getObservation()
            passObs = passCh.getObservation()


            print(np.size(failObs))

            if np.any(failObs[0] < 0):
                for i in range(np.size(failObs[0])):
                    if failObs[0][i] < 0:
                       failObs[0][i] = 0
                       failObs[1][i] = 0
            if np.any(passObs[0] < 0):
                for i in range(np.size(passObs[0])):
                    if passObs[0][i] < 0:
                       passObs[0][i] = 0
                       passObs[1][i] = 0


            GJparams = np.array([rl.IndependentParameter('GJparam_ptbin%d_msdbin%d' % (ptbin, i), 0) for i in range(msd.nbins)])
            sigmascale = 10.
            scaledparams = failObs * (1 + sigmascale/np.maximum(1., np.sqrt(failObs)))**GJparams

            fail_GJ = rl.ParametericSample('ptbin%dfail_GJ' % ptbin, rl.Sample.BACKGROUND, msd, scaledparams[0])
            failCh.addSample(fail_GJ)
            pass_GJ = rl.TransferFactorSample('ptbin%dpass_GJ' % ptbin, rl.Sample.BACKGROUND, tf_MCtempl_params[ptbin, :], fail_GJ)
            passCh.addSample(pass_GJ)

            failCh.mask = validbins[ptbin]
            passCh.mask = validbins[ptbin]

        GJfit_ws = ROOT.RooWorkspace('GJfit_ws')

        simpdf, obs = GJmodel.renderRoofit(GJfit_ws)
        GJfit = simpdf.fitTo(obs,
                              ROOT.RooFit.Extended(True),
                              ROOT.RooFit.SumW2Error(True),
                              ROOT.RooFit.Strategy(2),
                              ROOT.RooFit.Offset(True),
                              ROOT.RooFit.Save(),
                              ROOT.RooFit.Minimizer('Minuit2', 'migrad'),
                              ROOT.RooFit.Verbose(0),
                              ROOT.RooFit.PrintLevel(-1),
                              )
        GJfit_ws.add(GJfit)
        _values = [par.value for par in tf_MCtempl.parameters.flatten()]
        _names = [par.name for par in tf_MCtempl.parameters.flatten()]
        for name, value in zip(_names, _values):
            log.debug(f"{name} = {value:.3f}")
        GJfit_ws.writeToFile(os.path.join(str(tmpdir), f"testModel_{GJmodel.name}.root"))

        # Set parameters to fitted values  
        allparams = dict(zip(GJfit.nameArray(), GJfit.valueArray()))
        pvalues = []
        for i, p in enumerate(tf_MCtempl.parameters.reshape(-1)):
            p.value = allparams[p.name]
            print(p.name,p.value)
            pvalues += [p.value]

        if GJfit.status() != 0:
            print('Could not fit GJ')
            fitfailed_GJ += 1
            new_values = np.array(pvalues).reshape(tf_MCtempl.parameters.shape)
            import json
            with open(f"{opath}initial_vals_mc_{args.ipt}{args.irho}.json", "w") as outfile:
                json.dump({"initial_vals":new_values.tolist()},outfile)
        else:
            break

    if fitfailed_GJ >=5:
        raise RuntimeError('Could not fit GJ after 5 tries')



    param_names = [p.name for p in tf_MCtempl.parameters.reshape(-1)]
    decoVector = rl.DecorrelatedNuisanceVector.fromRooFitResult(tf_MCtempl.name + '_deco', GJfit, param_names)
    tf_MCtempl.parameters = decoVector.correlated_params.reshape(tf_MCtempl.parameters.shape)
    tf_MCtempl_params_final = tf_MCtempl(ptscaled, rhoscaled)

    degs = tuple([int(s) for s in [args.ipt, args.irho]])
    _inits = np.ones(tuple(n + 1 for n in degs))
    log.debug(f"Initializing TF (data) with n_pt={args.ipt} and n_rho={args.irho}")
    log.debug(_inits)
    tf_dataResidual = rl.BasisPoly(
        f"tf{args.year}_dataResidual",
        degs,
        ["pt", "rho"],
        basis="Bernstein",
        init_params=_inits,
        limits=(-100, 100),
        coefficient_transform=None,
    )
    # tf_dataResidual = rl.BernsteinPoly("tf_dataResidual", poly_order, ["pt", "rho"], init_params=_inits, limits=(0, 10))
    tf_dataResidual_params = tf_dataResidual(ptscaled, rhoscaled)
    tf_params = GJeff * tf_MCtempl_params_final * tf_dataResidual_params

    # Build main model
    log.info(f"Building main model for Sigal {sig}")   
    model = rl.Model(f"{sig}_model")
    model.t2w_config = ("-P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=ptbin.*/Sig25:r[0,10]'")

    samps = ['TTBar','Sig25', 'WGamma', 'ZGamma']
    sigs = ['Sig25']
    for ptbin in range(npt):
        for region in ['pass', 'fail']:

            # drop bins outside rho validity                                                            
            mask = validbins[ptbin]

            ch = rl.Channel('ptbin%d%s' % (ptbin, region))
            log.debug(f"Initializing model region: "+'ptbin%d%s' % (ptbin, region))   
            model.addChannel(ch)

            isPass = region == 'pass'
            templates = {}

            for sName in samps:
                print("Sample "+region+" "+sName)
                templates[sName] = get_template2(sName, isPass, ptbin+2, args.year, obs=msd, syst='nominal')
                nominal = templates[sName][0]

                if(badtemp_ma(nominal)):
                    print("Sample {} is too small, skipping".format(sName))
                    continue

                # expectations
                templ = templates[sName]
                logging.info(f"Adding sample={sName} in ptbin={ptbin}, region={region}.")
                stype = rl.Sample.SIGNAL if sName in sigs else rl.Sample.BACKGROUND

                # Shape Systematics
                MORPHNOMINAL = True
                def smorph(templ):      
                    if templ is None:
                            return None                  
                            
                    if MORPHNOMINAL and sName not in ['GJ']:
                        return MorphHistW2(templ).get(shift=SF[args.year+"_ParticleNet"]['shift_SF']/smass('Wjets') * smass(sName),
                                                      smear=SF[args.year+"_ParticleNet"]['smear_SF']
                                                  )
                    else:
                        return templ
                templ = smorph(templ)

                sample = rl.TemplateSample(ch.name + '_' + sName, stype, templ)
#                print(sName+" "+region+" Expectation: "+str(sample.getExpectation(nominal=True).sum()))

                # Lumi Systematic
                sample.setParamEffect(sys_lumi, lumi[args.year[:4]]['UL'])
                sample.setParamEffect(sys_phoID, 1.05) #5% Photon ID Systematic (All Years)
                sample.setParamEffect(sys_trig, 1.05) #5% Trigger Systematic (All Years)

                # Other Systematics
                if do_systematics:
                    sample.autoMCStats(lnN=True)        # Sets MC Statistical Uncertainties
                    for sys in exp_systs:
                        syst_up = get_template(sName, isPass, ptbin+2, args.year, obs=msd, syst=sys+'Up')[0]
                        syst_do = get_template(sName, isPass, ptbin+2, args.year, obs=msd, syst=sys+'Down')[0]

                        eff_up = shape_to_num(syst_up, nominal)
                        eff_do = shape_to_num(syst_do, nominal)

                        sample.setParamEffect(sys_dict[sys], eff_up, eff_do)

                # Scale and Smear
                mtempl = AffineMorphTemplate(templ)
                if sName not in ['QCD']:
                    # shift
                    realshift = SF[args.year+"_ParticleNet"]['shift_SF_ERR']/smass('Wjets') * smass(sName)
                    print("realshift: "+str(realshift))
                    _up = mtempl.get(shift=realshift)
                    _down = mtempl.get(shift=-realshift)
                    if badtemp_ma(_up[0]) or badtemp_ma(_down[0]):
                        print("Skipping sample {}, scale systematic would be empty".format(sName))
                    else:
                        sample.setParamEffect(sys_scale, _up, _down, scale=1)
#                        ofile_morph.WriteObject(num_to_hist(templates[sName][0], sName+" Nominal ptBin "+str(ptbin)),sName+"_nom_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(templates[sName][0]*_up[0], sName+" ScaleUp ptBin "+str(ptbin)),sName+"_scaleUp_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(templates[sName][0]*_down[0], sName+" ScaleDown ptBin "+str(ptbin)),sName+"_scaleDown_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(_up[0], sName+" ScaleUp Weights ptBin "+str(ptbin)),sName+"_scaleUp_weights_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(_down[0], sName+" ScaleDown Weights ptBin "+str(ptbin)),sName+"_scaleDown_weights_"+region+str(ptbin))

                    # smear
                    _up = mtempl.get(smear=1 + SF[args.year+"_ParticleNet"]['smear_SF_ERR'])
                    _down = mtempl.get(smear=1 - SF[args.year+"_ParticleNet"]['smear_SF_ERR'])
                    if badtemp_ma(_up[0]) or badtemp_ma(_down[0]):
                        print("Skipping sample {}, scale systematic would be empty".format(sName))
                    else:
                        sample.setParamEffect(sys_smear, _up, _down)
#                        ofile_morph.WriteObject(num_to_hist(templates[sName][0]*_up[0], sName+" SmearUp ptbin "+str(ptbin)),sName+"_smearUp_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(templates[sName][0]*_down[0], sName+" SmearDown ptbin "+str(ptbin)),sName+"_smearDown_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(_up[0], sName+" SmearUp Weights ptBin "+str(ptbin)),sName+"_smearUp_weights_"+region+str(ptbin))
#                        ofile_morph.WriteObject(num_to_hist(_down[0], sName+" SmearDown Weights ptBin "+str(ptbin)),sName+"_smearDown_weights_"+region+str(ptbin))

                # Tagger SF
                sample.scale(SF[args.year+"_ParticleNet"][args.tagger+'_SF'])        # ParticleNet Scale Factor Applied Here
                if do_systematics:
                    effect = 1.0 + SF[args.year+"_ParticleNet"][args.tagger+'_SF_ERR'] / SF[args.year+"_ParticleNet"][args.tagger+'_SF'] # N2DDT Systematic Applied Here
                    sample.setParamEffect(sys_Tag_eff,effect)

                ch.addSample(sample)

            data_obs = get_template2('Data', isPass, ptbin+2, args.year, obs=msd, syst='nominal')
            ch.setObservation(data_obs, read_sumw2=True)
    

            # drop bins outside rho validity
            mask = validbins[ptbin]

            ch.mask = mask

    for ptbin in range(npt):
        failCh = model['ptbin%dfail' % ptbin]
        passCh = model['ptbin%dpass' % ptbin]
        Dataparams = np.array([rl.IndependentParameter('Dataparam_ptbin%d_msdbin%d' % (ptbin, i), 0) for i in range(msd.nbins)])
        initial_Data = failCh.getObservation()[0].astype(float)  # was integer, and numpy complained about subtracting float from it

        for sample in failCh:
            if sample.sampletype == rl.Sample.BACKGROUND:#Subtract out backgrounds from fail
                    initial_Data -= sample.getExpectation(nominal=True)
                    print("Subtract Sample: "+str(sample.name))


        if np.any(initial_Data < 0.):
#            raise ValueError('initial_Data negative for some bins..', initial_Data)
            for i in range(np.size(initial_Data)):
                if initial_Data[i] < 0:
                   initial_Data[i] = 0
            

        sigmascale = 10  # to scale the deviation from initial
        scaledparams = initial_Data * (1 + sigmascale/np.maximum(1., np.sqrt(initial_Data)))**Dataparams
        fail_NonRes = rl.ParametericSample('ptbin%dfail_NonRes' % ptbin, rl.Sample.BACKGROUND, msd, scaledparams)
        failCh.addSample(fail_NonRes)
        pass_NonRes = rl.TransferFactorSample('ptbin%dpass_NonRes' % ptbin, rl.Sample.BACKGROUND, tf_params[ptbin, :], fail_NonRes)
        passCh.addSample(pass_NonRes)

        WGpass = passCh['WGamma']
        WGfail = failCh['WGamma']
        WGpass.setParamEffect(WG_xs, 1.1)
        WGfail.setParamEffect(WG_xs, 1.1)

        ZGpass = passCh['ZGamma']
        ZGfail = failCh['ZGamma']
        ZGpass.setParamEffect(ZG_xs, 1.1)
        ZGfail.setParamEffect(ZG_xs, 1.1)

        tqqpass = passCh['TTBar']
        tqqfail = failCh['TTBar']
        tqqpass.setParamEffect(tqq_xs, 1.1)
        tqqfail.setParamEffect(tqq_xs, 1.1)

    with open(os.path.join(str(tmpdir), f"{sig}_model.pkl"), "wb") as fout:
        pickle.dump(model, fout)

    model.renderCombine(os.path.join(str(tmpdir), f"{sig}_model"))
    
    conf_dict = vars(args)
    conf_dict["nbins"] = float(np.sum(validbins))
    pprint(conf_dict)
    import json

    # Serialize data into file:
    json.dump(
        conf_dict,
        open(
            "{}/config.json".format(
                f"{tmpdir}/{sig}_model",
            ),
            "w",
        ),
        sort_keys=True,
        indent=4,
        separators=(",", ": "),
    )



if __name__ == "__main__":
    import time
    start_time = time.time()
    global opath
    startopath = f"{args.opath}"
#    os.system(f"cp rhalphalib_zprime.py {startopath}/rhalphalib_zprime.py")
    for sig in signals:
        opath = f"{startopath}/{sig}/"
        if os.path.exists(opath):
            q_overwrite = Confirm.ask(f"Path: '{opath}' already exists. Overwrite?")
            if not q_overwrite:
                pprint(f"Remove with \nrm -rf {opath}")
                sys.exit()
            else:
                os.system(f"rm -rf {opath}")
        os.makedirs(opath)
        test_rhalphabet(opath, sig, args.throwPoisson)

    elapsed = time.time() - start_time
    pprint(f"Walltime: {time.strftime('%H:%M:%S', time.gmtime(elapsed))}")
