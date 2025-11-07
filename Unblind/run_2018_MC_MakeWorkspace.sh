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

python3 submit_ftests.py --make --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2018/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2018_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2018/MC --year 2018 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2018_ParticleNet_make_mc_$1_$2.log
python3 submit_ftests.py --build --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2018/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2018_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2018/MC --year 2018 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2018_ParticleNet_build_mc_$1_$2.log

