import os
import ROOT
from ROOT import *
from array import array
import math
from math import *
import sys
import numpy as np

TF = "/eos/uscms/store/user/anovak/QCD/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_234704/0000/"

QCD = ["/eos/uscms/store/user/anovak/QCD/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_234704/0000/", "/eos/uscms/store/user/anovak/QCD/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_234825/0000/", "/eos/uscms/store/user/anovak/QCD/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_234946/0000/", "/eos/uscms/store/user/anovak/QCD/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/160806_235108/0000/","/eos/uscms/store/user/anovak/QCD/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v3/160806_235229/0000/", "/eos/uscms/store/user/anovak/QCD/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_235350/0000/"]

W = ["/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/160806_235511/0000/", "/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_235632/0000/", "/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_235755/0000/", "/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160806_235917/0000/" ,"/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/160807_000038/0000/", "/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/160807_000159/0000/" , "/eos/uscms/store/user/anovak/Wjets/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160807_000322/0000/",  "/eos/uscms/store/user/anovak/Wjets/WJetsToQQ_HT180_13TeV-madgraphMLM-pythia8/B2GAnaFW_80X_V2p0_PR53_Aug06_RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/160807_000443/0000/"]


def Fill(TreeName): # Loop through events and fill them. Actual Fill step is done at the end, allowing us to make a few quality control cuts.
	total = 0
	for i in files:
		print i
		File = TFile("root://cmsxrootd.fnal.gov/"+TF  + "/" +i)
		Tree = File.Get(TreeName)
		n = Tree.GetEntries()
		total += n
	return total

def count(TF, end=".root"):
	files =[]
	for file in os.listdir(TF):
		if file.endswith(end): # select files, allows you to select a subset of files for running on very large directories
			files.append(file)

	#TreeName = "B2GTTreeMaker/B2GTree"
	TreeName = "tree_T1"
	total = 0
	for i in files:
		print i
		File = TFile("root://cmsxrootd.fnal.gov/"+TF  + "/" +i)
		Tree = File.Get(TreeName)
		n = Tree.GetEntries()
		total += n
	return total

direc = "/home/storage/andrzejnovak/T"

M = np.zeros((15,9))
for n, i in enumerate([2,3,4,5,6,7,9,10,11]):
	M[0,n] = i



qcd = [10272017, 19005761, 15338355, 4976814, 3475786, 1959055]
w = [1585119, 2047224, 1899917, 3654847, 1539154, 6811765, 253402, 4938577]
trigs = [231792, 227647,196935]

for i, t in enumerate([2,3,4,5,6,7,9,10,11]):
	TF = direc+str(t)
	for j, n in enumerate(["QCD_HT300to500", "QCD_HT500to700", "QCD_HT700to1000", "QCD_HT1000to1500", "QCD_HT1500to2000", "QCD_HT2000toInf"]):
		try:
			c = count(TF, n+".root")
			M[j+1,i] = c/float(qcd[j])*100
		except:
			print n

for i, t in enumerate([2,3,4,5,6,7,9,10,11]):
	TF = direc+str(t)
	for j, n in enumerate(["WJetsToLNu_HT-100To200","WJetsToLNu_HT-200To400", "WJetsToLNu_HT-400To600","WJetsToLNu_HT-600To800","WJetsToLNu_HT-800To1200", "WJetsToLNu_HT-1200To2500", "WJetsToLNu_HT-2500ToInf", "WJetsToQQ"]):
		try:		
			c = count(TF, n+".root")
			print c
			M[j+7,i] = c/float(w[j])*100
		except:
			print n

for i, t in enumerate([2,3,4,5,6,7,9,10,11]):
	TF = "/home/storage/andrzejnovak/signal"
	for j, n in enumerate(["ZprimeToTprimeT_TprimeToWB_MZp-1500Nar_MTp-900Nar_LH_Tune_T", "ZprimeToTprimeT_TprimeToWB_MZp-2000Nar_MTp-1200Nar_LH_Tune_T", "ZprimeToTprimeT_TprimeToWB_MZp-2500Nar_MTp-1500Nar_LH_Tune_T"]):
	
		try:		
			c = count(TF, n+str(t)+".root")
			print c/float(trigs[j])
			#M[j+7,i] = c/float(w[j])*100
		except:
			print n

np.set_printoptions(precision=3, threshold=None, edgeitems=None, linewidth=None, suppress=True, nanstr=None, infstr=None, formatter=None)
print M

	


	
