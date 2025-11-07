#!/bin/bash

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc820"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/

eval `scramv1 runtime -sh`


python3 submit_ftests.py --base --run --data -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/Data --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/Data --year 2016 -t 500 --tagger ParticleNet --condor > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_base_data_manual_test.log &
python3 submit_ftests.py --gen --run --data -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/Data --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/Data --year 2016 -t 500 --tagger ParticleNet --condor > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_gen_data_manual_test.log &
python3 submit_ftests.py --fits --run --data -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/Data --root_file /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/InputHists/FitHist_2016_ParticleNet.root --opath /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2016/Data --year 2016 -t 500 --tagger ParticleNet --condor > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/CondorFiles/logfiles_2016_ParticleNet_fits_data_manual_test.log &

