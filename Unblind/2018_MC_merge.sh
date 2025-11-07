#!/bin/bash

# CMSSW setup etc
export SCRAM_ARCH="slc7_amd64_gcc820"
export VO_CMS_SW_DIR="/cms/base/cmssoft"
export COIN_FULL_INDIRECT_RENDERING=1
source $VO_CMS_SW_DIR/cmsset_default.sh

cd /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/

eval `scramv1 runtime -sh`

cd FTests/2018/MC/ParticleNet/

for pt in 1 2 3
	do
	for rho in 1 2 3
		do
		printf "merging toy files in ftest_%d%d_%d%d\n" "$pt" "$rho" "$((pt+1))" "$((rho+0))"
		cd ftest_${pt}${rho}_$((pt+1))$((rho+0))
		hadd -f higgsCombine.BaseToys.GoodnessOfFit.mH120.root higgsCombine.BaseToys.GoodnessOfFit.mH120.*.root
		hadd -f higgsCombine.AltToys.GoodnessOfFit.mH120.root higgsCombine.AltToys.GoodnessOfFit.mH120.*.root
		cd ../
		printf "merging toy files in ftest_%d%d_%d%d\n" "$pt" "$rho" "$((pt+0))" "$((rho+1))"
		cd ftest_${pt}${rho}_$((pt+0))$((rho+1))
		hadd -f higgsCombine.BaseToys.GoodnessOfFit.mH120.root higgsCombine.BaseToys.GoodnessOfFit.mH120.*.root
		hadd -f higgsCombine.AltToys.GoodnessOfFit.mH120.root higgsCombine.AltToys.GoodnessOfFit.mH120.*.root
		cd ../
		printf "merging toy files in ftest_%d%d_%d%d\n" "$pt" "$rho" "$((pt+1))" "$((rho+1))"
		cd ftest_${pt}${rho}_$((pt+1))$((rho+1))
		hadd -f higgsCombine.BaseToys.GoodnessOfFit.mH120.root higgsCombine.BaseToys.GoodnessOfFit.mH120.*.root
		hadd -f higgsCombine.AltToys.GoodnessOfFit.mH120.root higgsCombine.AltToys.GoodnessOfFit.mH120.*.root
		cd ../
		done
	done
echo "Merging Done"
cd /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/
