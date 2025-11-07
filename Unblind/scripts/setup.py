#import fileinput
import os
import subprocess
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', default="/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/FTests/2017")
    parser.add_argument('--opath', required=True,type=str,)
    parser.add_argument('--outplots', default="/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/plots")
    parser.add_argument('--root_file', required=True, type=str, help="Path to ROOT files containing templates")

    parser.add_argument('--year', type=str, choices=["2016", "2017", "2018", "Run2"], required=True, help="Year to display.")
    parser.add_argument('--is_blinded', action='store_true', help='')
    parser.add_argument('--param', type=str, choices=['bern', 'cheby', 'exp'], default='bern')

    parser.add_argument('--tagger',type=str, choices=['N2DDT','ParticleNet'],required=True)
    parser.add_argument('--make', action='store_true', help='')
    parser.add_argument('--build', action='store_true', help='')

    parser.add_argument('--run', action="store_true")
    parser.add_argument('--toys', '-t', default="10")
    parser.add_argument('--seed', '-s', default="1")
    parser.add_argument('--base', action="store_true")
    parser.add_argument('--gen', action="store_true")
    parser.add_argument('--fits', action="store_true")

    args = parser.parse_args()

    rng_pt = 4
    rng_rho = 4

    mass = 25


    if args.run:
        run_cfg = (" --base " if args.base else "") + (" --gen " if args.gen else "") + (" --fits " if args.fits else "")
        name_cfg = ("base" if args.base else "") + ("gen" if args.gen else "") + ("fits" if args.fits else "")
        toy_cfg = " -t {} -s {} ".format(args.toys, args.seed)
        

        for i in range(0,rng_pt):
            for j in range(0,rng_pt):
                base_cmd = "python3 /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/custom.py --debug False -d {}/{} --data --year {} ".format(args.opath, args.tagger, args.year)
                ws_base = " -w {base}/{tagger}/{i}{j}/Sig{mass}/Sig{mass}_model/model_combined.root "
                ws_alt = " -a {base}/{tagger}/{i}{j}/Sig{mass}/Sig{mass}_model/model_combined.root "

                logfile = " > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/CondorFiles/logfiles_{year}_{tagger}_{name_cfg}_data_{ibase}{jbase}_{ialt}{jalt}_$1_$2.log"

                cmd1 = base_cmd + ws_base.format(base=args.opath, tagger=args.tagger, mass=mass, i=i, j=j) + ws_alt.format(base=args.opath,tagger=args.tagger, mass=mass, i=i + 1, j=j) + toy_cfg + run_cfg + logfile.format(year=args.year, tagger=args.tagger, name_cfg=name_cfg, ibase=i, jbase=j, ialt=i+1, jalt=j)
#                commands.append(cmd)
                newFile1 = open(name_cfg+"_"+str(args.year)+"_"+str(args.tagger)+"_"+str(i)+str(j)+"_"+str(i+1)+str(j)+".sh", mode='a+')
                cmd2 = base_cmd + ws_base.format(base=args.opath, tagger=args.tagger, mass=mass, i=i, j=j) + ws_alt.format(base=args.opath,tagger=args.tagger, mass=mass, i=i, j=j + 1) + toy_cfg + run_cfg + logfile.format(year=args.year, tagger=args.tagger, name_cfg=name_cfg, ibase=i, jbase=j, ialt=i, jalt=j+1)
#                commands.append(cmd)
                newFile2 = open(name_cfg+"_"+str(args.year)+"_"+str(args.tagger)+"_"+str(i)+str(j)+"_"+str(i)+str(j+1)+".sh", mode='a+')
                cmd3 = base_cmd + ws_base.format(base=args.opath, tagger=args.tagger, mass=mass, i=i, j=j) + ws_alt.format(base=args.opath,tagger=args.tagger, mass=mass, i=i + 1, j=j + 1) + toy_cfg + run_cfg + logfile.format(year=args.year, tagger=args.tagger, name_cfg=name_cfg, ibase=i, jbase=j, ialt=i+1, jalt=j+1)
#                commands.append(cmd)
                newFile3 = open(name_cfg+"_"+str(args.year)+"_"+str(args.tagger)+"_"+str(i)+str(j)+"_"+str(i+1)+str(j+1)+".sh", mode='a+')

                oldline = "python3 submit_ftests.py > /home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/CondorFiles/logfiles_2017_fits_data_$1_$2.log"
                template1 = open("/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/scripts/template_run.sh", mode='r')
                for line in template1:
                    newFile1.write(line.replace(oldline, cmd1))
                template1.close()
                template2 = open("/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/scripts/template_run.sh", mode='r')
                for line in template2:
                    newFile2.write(line.replace(oldline, cmd2))
                template2.close()
                template3 = open("/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/scripts/template_run.sh", mode='r')
                for line in template3:
                    newFile3.write(line.replace(oldline, cmd3))
                template3.close()
                
                newFile1.close()
                newFile2.close()
                newFile3.close()

#    for process in range(47):
#    	template = open("/home/akobert/CMSSW_11_1_0_pre7/src/RData/NanoTool_UL_corr_btag_percentage_barrel/nano_Sample_10.py", "r")
#        newFile = open("M10_" + str(process) + "_10.py", "a+")
#       	readLine = allFiles.readline()
#	oldline1 = "files = [\"/cms/xaastorage/NanoAOD/2018/JUNE19/UL/EGamma_RunA/branch_present/jetToolbox_dataA2018_0.root\", str(1.0), 1]"
#	newline1 = "files = [\""+str(readLine[:-1])+"\", str(59.82 * 25390.0/501525.0), 1, \"mc\"]"
	
#	oldline2 = "fname = \"DataA_present_UL_0\""
#	newline2 = "fname = \"M10_UL_nano_"+str(process)+"_10\""

#	for line in template:
#		newFile.write(line.replace(oldline1, newline1).replace(oldline2, newline2))
 
#	newFile.close()
#	template.close()
