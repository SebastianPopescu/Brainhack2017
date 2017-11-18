from __future__ import print_function
import numpy as np
from collections import defaultdict
import subprocess
import math
import time
import nibabel as nib
import random
import os
import argparse


def data_factory(realpath_gm_data,matter_involved,username):

		if matter_involved=='gm':

			### this part is for gray matter data
			### get the mask
			gm_mask_object = nib.load('/home/'+str(username)+'/masks/gm_mask.nii')
			gm_mask_data = gm_mask_object.get_data()

			gm_mask_data_reshaped = gm_mask_data.reshape(np.prod(gm_mask_data.shape),)
			gm_mask_data_full_bool = gm_mask_data_reshaped.astype(bool)
			f=open(realpath_gm_data)
			lista_imagini_gm = []
			lista_ids = []
			for line in f.readlines():

				temporar_object = nib.load(line.rstrip('\n'))
				lista_ids.append(line.rstrip('\n').rsplit('/')[-1].rsplit('sub-')[1].rsplit('_T1.nii')[0])
				temporar_data = temporar_object.get_data()
				temporar_data_reshaped = temporar_data.reshape(np.prod(temporar_data.shape),)
				### this is parsing just over the gm_mask
				lista_imagini_gm.append(temporar_data_reshaped[gm_mask_data_full_bool])
				### this is taking the whole MRI image
				#lista_imagini_gm.append(temporar_data_reshaped)
			imagini_gm = np.stack(lista_imagini_gm)
			ids = lista_ids
			print('here we print the dimensions of the testing data')
			print(imagini_gm.shape)
			f.close
			return imagini_gm,ids


		if matter_involved=='wm':

			### this part is for gray matter data
			### get the mask
			gm_mask_object = nib.load('/home/'+str(username)+'/masks/wm_mask.nii')
			gm_mask_data = gm_mask_object.get_data()

			gm_mask_data_reshaped = gm_mask_data.reshape(np.prod(gm_mask_data.shape),)
			gm_mask_data_full_bool = gm_mask_data_reshaped.astype(bool)
			f=open(realpath_gm_data)
			lista_imagini_gm = []
			lista_ids=[]
			for line in f.readlines():

				temporar_object = nib.load(line.rstrip('\n'))
				lista_ids.append(line.rstrip('\n').rsplit('/')[-1].rsplit('sub-')[1].rsplit('_T1.nii')[0])
				temporar_data = temporar_object.get_data()
				temporar_data_reshaped = temporar_data.reshape(np.prod(temporar_data.shape),)
				### this is parsing just over the gm_mask
				lista_imagini_gm.append(temporar_data_reshaped[gm_mask_data_full_bool])
				### this is taking the whole MRI image
				#lista_imagini_gm.append(temporar_data_reshaped)
			imagini_gm = np.stack(lista_imagini_gm)
			ids = lista_ids
			print('here we print the dimensions of the testing data')
			print(imagini_gm.shape)
			f.close
			return imagini_gm,ids		
		else:
			print('the file permits just gray matter data now')
			sys.exit();


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--username',type=str,help='your name')
	parser.add_argument('--matter',type=str,help='the type of matter---choose between gm and wm')
	args = parser.parse_args()

	bashCommand='realpath /home/'+str(args.username)+'/CamCan/gm_data/* > /home/'+str(args.username)+'/realpath_camcan_gm.txt'
	os.system(bashCommand)
	X,lista_ids = data_factory(realpath_gm_data='/home/'+str(args.username)+'/realpath_camcan_gm.txt',matter_involved=args.matter,username=args.username)
	#### now let's save it into a text file
	np.savetxt('/home/'+str(args.username)+'/CamCan/X_camcan_'+str(args.matter)+'.txt',X,delimiter=',')

	### let's parse the age of the subjects

	lista_age = []
	with open('/home/'+str(args.username)+'/CamCan/original_participant_data.tsv') as f:
		for line in f.readlines():

			temporar = line.rsplit('\t')[1]
			id_current = line.rsplit('\t')[0]
			if id_current in lista_ids:
				
				lista_age.append([np.float(temporar)])

	age_camcan = np.stack(lista_age)
	

	np.savetxt('/home/'+str(args.username)+'/CamCan/Y_camcan.txt',age_camcan,delimiter=',')

