#!/bin/bash

cluster=$1
process=$2

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc820"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/

eval `scramv1 runtime -sh`


python3 submit_ftests.py --base --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2017_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017/MC --year 2017 -t 500 --tagger ParticleNet --condor > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2017_ParticleNet_base_mc_manual.log &
python3 submit_ftests.py --gen --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2017_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017/MC --year 2017 -t 500 --tagger ParticleNet --condor > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2017_ParticleNet_gen_mc_manual.log &
python3 submit_ftests.py --fits --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2017_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017/MC --year 2017 -t 500 --tagger ParticleNet --condor > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2017_ParticleNet_fits_mc_manual.log &

