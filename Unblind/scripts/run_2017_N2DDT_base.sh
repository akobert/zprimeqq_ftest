#!/bin/bash

cluster=$1
process=$2

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc820"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/scripts/

eval `scramv1 runtime -sh`

base_pt=$(($2 / 12))
base_rho=$((($2 % 12) / 3))

if [[ $(($2 % 3)) -eq 0 ]]
then
	alt_pt=$base_pt
else
	alt_pt=$(($base_pt + 1))
fi

if [[ $((($2 - 1) % 3)) -eq 0 ]]
then
	alt_rho=$base_rho
else
	alt_rho=$(($base_rho + 1))
fi

echo "Base pT="$base_pt
echo "Base Rho="$base_rho
echo "Alt pT="$alt_pt
echo "Alt Rho="$alt_rho

under="_"

run_name=base_2017_N2DDT_$base_pt$base_rho$under$alt_pt$alt_rho.sh
echo $run_name

source $run_name "$1" "$2"
