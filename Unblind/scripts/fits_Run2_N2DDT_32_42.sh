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

python3 /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/custom.py --debug False -d /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/FTests/Run2/N2DDT --data --year Run2  -w /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/FTests/Run2/N2DDT/32/Sig25/Sig25_model/model_combined.root  -a /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/FTests/Run2/N2DDT/42/Sig25/Sig25_model/model_combined.root  -t 500 -s 1  --fits  > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/CondorFiles/logfiles_Run2_N2DDT_fits_data_32_42_$1_$2.log
