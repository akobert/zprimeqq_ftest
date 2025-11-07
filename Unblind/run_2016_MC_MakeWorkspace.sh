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

#python3 submit_ftests.py --base --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016 --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016 --year 2016 -t 1000 --tagger N2DDT > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_base_mc_$1_$2.log
#python3 submit_ftests.py --gen --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016 --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016 --year 2016 -t 1000 --tagger N2DDT > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_gen_mc_$1_$2.log
#python3 submit_ftests.py --fits --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016 --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016 --year 2016 -t 1000 --tagger N2DDT > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_fits_mc_$1_$2.log

python3 submit_ftests.py --make --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --year 2016 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_make_mc_$1_$2.log
python3 submit_ftests.py --build --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --year 2016 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_build_mc_$1_$2.log


#python3 submit_ftests.py --base --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --year 2016 -t 1000 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_base_mc_$1_$2.log
#python3 submit_ftests.py --gen --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --year 2016 -t 1000 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_gen_mc_$1_$2.log
#python3 submit_ftests.py --fits --run --mc -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/MC --year 2016 -t 1000 --tagger ParticleNet > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_fits_mc_$1_$2.log

