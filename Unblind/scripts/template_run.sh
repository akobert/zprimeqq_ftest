#!/bin/bash

#cluster=$1
#process=$2

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc820"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/

eval `scramv1 runtime -sh`

python3 submit_ftests.py > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/CondorFiles/logfiles_2017_fits_data_$1_$2.log
