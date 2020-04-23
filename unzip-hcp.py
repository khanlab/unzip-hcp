#!/usr/bin/env python

import pandas as pd
import yaml
import subprocess
import argparse


parser = argparse.ArgumentParser()


parser.add_argument('-c','--config', type=argparse.FileType('r'), default='config.yml',
                     help='config file to use (default: %(default)s)')
parser.add_argument('-n','--dry-run',action='store_true',
                     help='perform dry run instead of extracting')
parser.add_argument('-x','--extract',action='store_true',
                     help='perform extraction of files')

args = parser.parse_args()


config = yaml.load(args.config, Loader=yaml.FullLoader)
in_hcp_dir = config["in_hcp_dir"]
out_dir = config["out_scratch"]

#read hcp csv to get list of subjects
df = pd.read_csv(config['hcp_csv'])

#get subset of subjects with complete 7T session 
#  other useful variables in CSV: 7T_dMRI_Compl, 7T_Full_Task_fMRI, fMRI_Movie_Compl
subset = df.loc[df['7T_Full_MR_Compl']==True,'Subject']
subjects = subset.to_list()



#go through each type of zip file
for zip in config["zipfiles"]:
    print(zip)
    download_files = config["zipfiles"][zip]["download"]
    exclude_files = config["zipfiles"][zip]["exclude"]
  
    if download_files == None:
        print(f"skipping {zip}, no files selected to download...")
        continue
    
    for subject in subjects:
        unzip_cmd = f"unzip '{in_hcp_dir}/{subject}_{zip}.zip'"
        for dl in download_files:
            unzip_cmd += f" '{dl}'".format(subject=subject)
        if not exclude_files == None:
            unzip_cmd += f" -x"
            for excl in exclude_files:
                unzip_cmd += f" '{excl}'"
        unzip_cmd += f" -d '{out_dir}'"

        if args.dry_run:
            print(unzip_cmd)
        if args.extract:
            process = subprocess.run(unzip_cmd,shell=True)

