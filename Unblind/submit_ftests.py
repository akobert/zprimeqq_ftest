# from distutils import command
import os
import subprocess
import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', default="/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/FTests/2017")
    parser.add_argument('--opath', required=True,type=str,)
    parser.add_argument('--outplots', default="/home/akobert/CMSSW_11_3_4/src/zprimeqq_ftest/Unblind/plots")
    parser.add_argument('--root_file', required=True, type=str, help="Path to ROOT files containing templates")

    parser_mc = parser.add_mutually_exclusive_group(required=True)
    parser_mc.add_argument('--data', action='store_false', dest='mc')
    parser_mc.add_argument('--mc', action='store_true', dest='mc')
    parser.add_argument('--tworeg',action='store_true', dest='tworeg')
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
    parser.add_argument('--all', action="store_true")
    parser.add_argument('--condor', action="store_true")

    parser.add_argument('--plot', action="store_true")
    parser.add_argument('-p', action="store_true", help="parallel")
    parser.add_argument('--debug', action="store_true", help="Just print")

    args = parser.parse_args()

    print("Making Directory: "+f"{args.opath}")
    os.system(f"mkdir -p {args.opath}")
    start = time.time()
    commands = []

    rng_pt = 4
    rng_rho = 4

    if args.param == 'cheby':
        basis = ' --basis Bernstein,Chebyshev'
    elif args.param == 'exp':
        basis = ' --basis Bernstein,Bernstein --transform '
    else:
        basis = " "
    if args.make:
        # Made workspaces
        for pt in range(0, rng_pt + 1):
            for rho in range(0, rng_rho + 1):
                ###I don't need just MC templates?
                if args.year == "Run2":
                    cmd = f"python3 rhalphalib_zprime_Run2.py --year {args.year} --root_file {args.root_file} --o {args.opath}/{args.tagger}/{pt}{rho} --ipt {pt} --irho {rho} --do_systematics --tagger {args.tagger} --MCTF --ftest --sigmass 25"
                else:
                    cmd = f"python3 rhalphalib_zprime.py --year {args.year} --root_file {args.root_file} --o {args.opath}/{args.tagger}/{pt}{rho} --ipt {pt} --irho {rho} --do_systematics --tagger {args.tagger} --MCTF --ftest --sigmass 25"
                commands.append(cmd)

    mass = 25
    if args.build:
        for pt in range(0, rng_pt + 1):
            for rho in range(0, rng_rho + 1):
                _refdir = os.path.realpath(os.getcwd())
                #00/pnmd2prong_0p05/ipt0_irho0/m150/m150_model
#                path = "{}/{}{}/{}/ipt{}_irho{}/m150/m150_model".format(args.opath, str(pt), str(rho), args.tagger, str(pt), str(rho))
                path = "{}/{}/{}{}/Sig{}/Sig{}_model".format(args.opath, args.tagger, str(pt), str(rho), str(mass), str(mass))
                print("XXXXXXXXXXXXXXXX")
                print("Working in:")
                print("    ", path)
                print("XXXXXXXXXXXXXXXX")
                os.chdir(path)

                os.system("bash build.sh")
                os.chdir(_refdir)


    if args.all:
        args.base = True
        args.gen = True
        args.fits = True

    
    if args.run:
        run_cfg = (" --base " if args.base else "") + (" --gen " if args.gen else "") + (" --fits " if args.fits else "")
        if args.condor:
            run_cfg += " --condor "
            toy_cfg = " -t 500 -s 1:10:1 "
        else:
            toy_cfg = " -t {} -s {} ".format(args.toys, args.seed)
        for i in range(1,rng_pt):
            for j in range(1,rng_pt):
                base_cmd = "python3 custom.py  --debug False -d {}/{} {} --year {} ".format(args.opath, args.tagger, "--mc" if args.mc else "--data", args.year)

#                ws_base = " -w {base}/{i}{j}/{tagger}/ipt{i}_irho{j}/m150/m150_model/model_combined.root "
#                ws_alt = " -a {base}/{i}{j}/{tagger}/ipt{i}_irho{j}/m150/m150_model/model_combined.root "
                ws_base = " -w {base}/{tagger}/{i}{j}/Sig{mass}/Sig{mass}_model/model_combined.root "
                ws_alt = " -a {base}/{tagger}/{i}{j}/Sig{mass}/Sig{mass}_model/model_combined.root "

                cmd = base_cmd + ws_base.format(base=args.opath, tagger=args.tagger, mass=mass, i=i, j=j) + ws_alt.format(base=args.opath,tagger=args.tagger, mass=mass, i=i + 1, j=j) + toy_cfg + run_cfg
                commands.append(cmd)
                cmd = base_cmd + ws_base.format(base=args.opath, tagger=args.tagger, mass=mass, i=i, j=j) + ws_alt.format(base=args.opath,tagger=args.tagger, mass=mass, i=i, j=j + 1) + toy_cfg + run_cfg
                commands.append(cmd)
                cmd = base_cmd + ws_base.format(base=args.opath, tagger=args.tagger, mass=mass, i=i, j=j) + ws_alt.format(base=args.opath,tagger=args.tagger, mass=mass, i=i + 1, j=j + 1) + toy_cfg + run_cfg
                commands.append(cmd)


    if args.plot:
        base_cmd = "python3 new_plot_ftests.py -o {} --year {} {}".format(args.outplots, args.year, "--mc" if args.mc else "")
        if args.mc:
            base_cmd += " --qplots "
#        for i in range(rng_pt+1):
#            for j in range(rng_pt+1):
        for i in range(1, rng_pt):
            for j in range(1, rng_pt):
                print("Plotting for pT: "+str(i)+" rho: "+str(j))
                cmd = base_cmd + " --degs {},{} ".format(i, j) + " --degsalt {},{} ".format(i, j + 1)
                cmd += " -d {}/{}/ftest_{}{}_{}{}".format(args.opath, args.tagger, i, j, i, j + 1)
                commands.append(cmd)
                cmd = base_cmd + " --degs {},{} ".format(i, j) + " --degsalt {},{} ".format(i + 1, j)
                cmd += " -d {}/{}/ftest_{}{}_{}{}".format(args.opath, args.tagger, i, j, i + 1, j)
                commands.append(cmd)
                cmd = base_cmd + " --degs {},{} ".format(i, j) + " --degsalt {},{} ".format(i + 1, j + 1)
                cmd += " -d {}/{}/ftest_{}{}_{}{}".format(args.opath, args.tagger, i, j, i + 1, j + 1)
                commands.append(cmd)

    if args.debug:
        for cmd in commands:
            print(cmd)
        import sys
        sys.exit()
    processes = []
    for cmd in commands:
        if args.p:
            processes.append(subprocess.Popen(cmd, shell=True))
        else:
            processes.append(subprocess.Popen(cmd, shell=True).wait())

#    while sum([p.wait() is not None for p in processes]) < len(processes):
#        try:
#            time.sleep(1)
#            print([p.poll() is not None for p in processes])
#            print([p.wait() for p in processes])
#        except KeyboardInterrupt:
#            term = [p.terminate() for p in processes]

    print("TIME:", time.strftime("%H:%M:%S", time.gmtime(time.time()-start)))

# python submit_ftests.py -d FTests/mconly16 -o Ftests/Fouts



