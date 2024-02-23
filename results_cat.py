import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
import os
import pandas as pd


def results_table(catalogue_path, data_path, output_path):
        
        id_list = []
        hlya_1216_wave_list = []
        hlya_1216_flux_list = []
        hlya_1216_flux_err_list = []
        hlya_1216_flux_mc_err_list = []
        hlya_1216_flux_upper_list = []
        hlya_1216_ew_rest_list = []
        hlya_1216_ew_rest_err_list = []
        hlya_1216_flux_flag_list = []
        hlya_1216_vel_list = []
        hlya_1216_vel_err_list = []
        hlya_1216_sig_list = []
        hlya_1216_sig_err_list = []
        hlya_1216_comp_list = []

        lyA_drop_wave_list = []
        lyA_drop_flux_list = []
        lyA_drop_flux_err_list = []
        lyA_drop_flux_mc_err_list = []
        lyA_drop_flux_upper_list = []
        lyA_drop_ew_rest_list = []
        lyA_drop_ew_rest_err_list = []
        lyA_drop_flux_flag_list = []
        lyA_drop_vel_list = []
        lyA_drop_vel_err_list = []
        lyA_drop_sig_list = []
        lyA_drop_sig_err_list = []
        lyA_drop_comp_list = []

        n4_1486_wave_list = []
        n4_1486_flux_list = []
        n4_1486_flux_err_list = []
        n4_1486_flux_mc_err_list = []
        n4_1486_flux_upper_list = []
        n4_1486_ew_rest_list = []
        n4_1486_ew_rest_err_list = []
        n4_1486_flux_flag_list = []
        n4_1486_vel_list = []
        n4_1486_vel_err_list = []
        n4_1486_sig_list = []
        n4_1486_sig_err_list = []
        n4_1486_comp_list = []

        c4_1549_wave_list = []
        c4_1549_flux_list = []
        c4_1549_flux_err_list = []
        c4_1549_flux_mc_err_list = []
        c4_1549_flux_upper_list = []
        c4_1549_ew_rest_list = []
        c4_1549_ew_rest_err_list = []
        c4_1549_flux_flag_list = []
        c4_1549_vel_list = []
        c4_1549_vel_err_list = []
        c4_1549_sig_list = []
        c4_1549_sig_err_list = []
        c4_1549_comp_list = []

        he2_1640_wave_list = []
        he2_1640_flux_list = []
        he2_1640_flux_err_list = []
        he2_1640_flux_mc_err_list = []
        he2_1640_flux_upper_list = []
        he2_1640_ew_rest_list = []
        he2_1640_ew_rest_err_list = []
        he2_1640_flux_flag_list = []
        he2_1640_vel_list = []
        he2_1640_vel_err_list = []
        he2_1640_sig_list = []
        he2_1640_sig_err_list = []
        he2_1640_comp_list = []

        o3_1666_wave_list = []
        o3_1666_flux_list = []
        o3_1666_flux_err_list = []
        o3_1666_flux_mc_err_list = []
        o3_1666_flux_upper_list = []
        o3_1666_ew_rest_list = []
        o3_1666_ew_rest_err_list = []
        o3_1666_flux_flag_list = []
        o3_1666_vel_list = []
        o3_1666_vel_err_list = []
        o3_1666_sig_list = []
        o3_1666_sig_err_list = []
        o3_1666_comp_list = []

        n3_1750_wave_list = []
        n3_1750_flux_list = []
        n3_1750_flux_err_list = []
        n3_1750_flux_mc_err_list = []
        n3_1750_flux_upper_list = []
        n3_1750_ew_rest_list = []
        n3_1750_ew_rest_err_list = []
        n3_1750_flux_flag_list = []
        n3_1750_vel_list = []
        n3_1750_vel_err_list = []
        n3_1750_sig_list = []
        n3_1750_sig_err_list = []
        n3_1750_comp_list = []

        c3_1907_wave_list = []
        c3_1907_flux_list = []
        c3_1907_flux_err_list = []
        c3_1907_flux_mc_err_list = []
        c3_1907_flux_upper_list = []
        c3_1907_ew_rest_list = []
        c3_1907_ew_rest_err_list = []
        c3_1907_flux_flag_list = []
        c3_1907_vel_list = []
        c3_1907_vel_err_list = []
        c3_1907_sig_list = []
        c3_1907_sig_err_list = []
        c3_1907_comp_list = []

        ne4_2424_wave_list = []
        ne4_2424_flux_list = []
        ne4_2424_flux_err_list = []
        ne4_2424_flux_mc_err_list = []
        ne4_2424_flux_upper_list = []
        ne4_2424_ew_rest_list = []
        ne4_2424_ew_rest_err_list = []
        ne4_2424_flux_flag_list = []
        ne4_2424_vel_list = []
        ne4_2424_vel_err_list = []
        ne4_2424_sig_list = []
        ne4_2424_sig_err_list = []
        ne4_2424_comp_list = []

        mg2_2796_wave_list = []
        mg2_2796_flux_list = []
        mg2_2796_flux_err_list = []
        mg2_2796_flux_mc_err_list = []
        mg2_2796_flux_upper_list = []
        mg2_2796_ew_rest_list = []
        mg2_2796_ew_rest_err_list = []
        mg2_2796_flux_flag_list = []
        mg2_2796_vel_list = []
        mg2_2796_vel_err_list = []
        mg2_2796_sig_list = []
        mg2_2796_sig_err_list = []
        mg2_2796_comp_list = []

        ne5_3426_wave_list = []
        ne5_3426_flux_list = []
        ne5_3426_flux_err_list = []
        ne5_3426_flux_mc_err_list = []
        ne5_3426_flux_upper_list = []
        ne5_3426_ew_rest_list = []
        ne5_3426_ew_rest_err_list = []
        ne5_3426_flux_flag_list = []
        ne5_3426_vel_list = []
        ne5_3426_vel_err_list = []
        ne5_3426_sig_list = []
        ne5_3426_sig_err_list = []
        ne5_3426_comp_list = []
        
        o2_3727_wave_list = []
        o2_3727_flux_list = []
        o2_3727_flux_err_list = []
        o2_3727_flux_mc_err_list = []
        o2_3727_flux_upper_list = []
        o2_3727_ew_rest_list = []
        o2_3727_ew_rest_err_list = []
        o2_3727_flux_flag_list = []
        o2_3727_vel_list = []
        o2_3727_vel_err_list = []
        o2_3727_sig_list = []
        o2_3727_sig_err_list = []
        o2_3727_comp_list = []

        ne3_3869_wave_list = []
        ne3_3869_flux_list = []
        ne3_3869_flux_err_list = []
        ne3_3869_flux_mc_err_list = []
        ne3_3869_flux_upper_list = []
        ne3_3869_ew_rest_list = []
        ne3_3869_ew_rest_err_list = []
        ne3_3869_flux_flag_list = []
        ne3_3869_vel_list = []
        ne3_3869_vel_err_list = []
        ne3_3869_sig_list = []
        ne3_3869_sig_err_list = []
        ne3_3869_comp_list = []

        hbad_4102_wave_list = []
        hbad_4102_flux_list = []
        hbad_4102_flux_err_list = []
        hbad_4102_flux_mc_err_list = []
        hbad_4102_flux_upper_list = []
        hbad_4102_ew_rest_list = []
        hbad_4102_ew_rest_err_list = []
        hbad_4102_flux_flag_list = []
        hbad_4102_vel_list = []
        hbad_4102_vel_err_list = []
        hbad_4102_sig_list = []
        hbad_4102_sig_err_list = []
        hbad_4102_comp_list = []

        hbag_4340_wave_list = []
        hbag_4340_flux_list = []
        hbag_4340_flux_err_list = []
        hbag_4340_flux_mc_err_list = []
        hbag_4340_flux_upper_list = []
        hbag_4340_ew_rest_list = []
        hbag_4340_ew_rest_err_list = []
        hbag_4340_flux_flag_list = []
        hbag_4340_vel_list = []
        hbag_4340_vel_err_list = []
        hbag_4340_sig_list = []
        hbag_4340_sig_err_list = []
        hbag_4340_comp_list = []

        blnd_hbag_o3_4340_wave_list = []
        blnd_hbag_o3_4340_flux_list = []
        blnd_hbag_o3_4340_flux_err_list = []
        blnd_hbag_o3_4340_flux_mc_err_list = []
        blnd_hbag_o3_4340_flux_upper_list = []
        blnd_hbag_o3_4340_ew_rest_list = []
        blnd_hbag_o3_4340_ew_rest_err_list = []
        blnd_hbag_o3_4340_flux_flag_list = []
        blnd_hbag_o3_4340_vel_list = []
        blnd_hbag_o3_4340_vel_err_list = []
        blnd_hbag_o3_4340_sig_list = []
        blnd_hbag_o3_4340_sig_err_list = []
        blnd_hbag_o3_4340_comp_list = []

        o3_4363_wave_list = []
        o3_4363_flux_list = []
        o3_4363_flux_err_list = []
        o3_4363_flux_mc_err_list = []
        o3_4363_flux_upper_list = []
        o3_4363_ew_rest_list = []
        o3_4363_ew_rest_err_list = []
        o3_4363_flux_flag_list = []
        o3_4363_vel_list = []
        o3_4363_vel_err_list = []
        o3_4363_sig_list = []
        o3_4363_sig_err_list = []
        o3_4363_comp_list = []

        heii_4686_wave_list = []
        heii_4686_flux_list = []
        heii_4686_flux_err_list = []
        heii_4686_flux_mc_err_list = []
        heii_4686_flux_upper_list = []
        heii_4686_ew_rest_list = []
        heii_4686_ew_rest_err_list = []
        heii_4686_flux_flag_list = []
        heii_4686_vel_list = []
        heii_4686_vel_err_list = []
        heii_4686_sig_list = []
        heii_4686_sig_err_list = []
        heii_4686_comp_list = []

        hbab_4861_wave_list = []
        hbab_4861_flux_list = []
        hbab_4861_flux_err_list = []
        hbab_4861_flux_mc_err_list = []
        hbab_4861_flux_upper_list = []
        hbab_4861_ew_rest_list = []
        hbab_4861_ew_rest_err_list = []
        hbab_4861_flux_flag_list = []
        hbab_4861_vel_list = []
        hbab_4861_vel_err_list = []
        hbab_4861_sig_list = []
        hbab_4861_sig_err_list = []
        hbab_4861_comp_list = []

        o3_4959_wave_list = []
        o3_4959_flux_list = []
        o3_4959_flux_err_list = []
        o3_4959_flux_mc_err_list = []
        o3_4959_flux_upper_list = []
        o3_4959_ew_rest_list = []
        o3_4959_ew_rest_err_list = []
        o3_4959_flux_flag_list = []
        o3_4959_vel_list = []
        o3_4959_vel_err_list = []
        o3_4959_sig_list = []
        o3_4959_sig_err_list = []
        o3_4959_comp_list = []

        o3_5007d_wave_list = []
        o3_5007d_flux_list = []
        o3_5007d_flux_err_list = []
        o3_5007d_flux_mc_err_list = []
        o3_5007d_flux_upper_list = []
        o3_5007d_ew_rest_list = []
        o3_5007d_ew_rest_err_list = []
        o3_5007d_flux_flag_list = []
        o3_5007d_vel_list = []
        o3_5007d_vel_err_list = []
        o3_5007d_sig_list = []
        o3_5007d_sig_err_list = []
        o3_5007d_comp_list = []

        o3_5007_wave_list = []
        o3_5007_flux_list = []
        o3_5007_flux_err_list = []
        o3_5007_flux_mc_err_list = []
        o3_5007_flux_upper_list = []
        o3_5007_ew_rest_list = []
        o3_5007_ew_rest_err_list = []
        o3_5007_flux_flag_list = []
        o3_5007_vel_list = []
        o3_5007_vel_err_list = []
        o3_5007_sig_list = []
        o3_5007_sig_err_list = []
        o3_5007_comp_list = []

        he1_5875_wave_list = []
        he1_5875_flux_list = []
        he1_5875_flux_err_list = []
        he1_5875_flux_mc_err_list = []
        he1_5875_flux_upper_list = []
        he1_5875_ew_rest_list = []
        he1_5875_ew_rest_err_list = []
        he1_5875_flux_flag_list = []
        he1_5875_vel_list = []
        he1_5875_vel_err_list = []
        he1_5875_sig_list = []
        he1_5875_sig_err_list = []
        he1_5875_comp_list = []

        o1_6300_wave_list = []
        o1_6300_flux_list = []
        o1_6300_flux_err_list = []
        o1_6300_flux_mc_err_list = []
        o1_6300_flux_upper_list = []
        o1_6300_ew_rest_list = []
        o1_6300_ew_rest_err_list = []
        o1_6300_flux_flag_list = []
        o1_6300_vel_list = []
        o1_6300_vel_err_list = []
        o1_6300_sig_list = []
        o1_6300_sig_err_list = []
        o1_6300_comp_list = []

        blnd_hbaa_n2_wave_list = []
        blnd_hbaa_n2_flux_list = []
        blnd_hbaa_n2_flux_err_list = []
        blnd_hbaa_n2_flux_mc_err_list = []
        blnd_hbaa_n2_flux_upper_list = []
        blnd_hbaa_n2_ew_rest_list = []
        blnd_hbaa_n2_ew_rest_err_list = []
        blnd_hbaa_n2_flux_flag_list = []
        blnd_hbaa_n2_vel_list = []
        blnd_hbaa_n2_vel_err_list = []
        blnd_hbaa_n2_sig_list = []
        blnd_hbaa_n2_sig_err_list = []
        blnd_hbaa_n2_comp_list = []
        
    
        catalogue = Table.read(catalogue_path, format='fits')

        lines = ["HLyA_1216", "LyA_drop", "N4_1486", "C4_1549", "He2_1640", "O3_1666", "N3_1750", "C3_1907", "Ne4_2424", "Mg2_2796", "Ne5_3426", "O2_3727", "Ne3_3869", "HBaD_4102", "HBaG_4340", "Blnd_HBaG_O3_4340", "O3_4363", "HeII_4686", "HBaB_4861", "O3_4959", "O3_5007d", "O3_5007", "He1_5875", "O1_6300", "Blnd_HBaA_N2"]

        # data_types = ["wave_list", "flux_list", "flux_err_list", "flux_mc_err_list", "flux_upper_list", "ew_rest_list", "ew_rest_err_list", "flux_flag_list", "vel_list", "vel_err_list", "sig_list", "sig_err_list", "comp_list"]

        data_types = ["wave", "flux", "flux_err", "flux_mc_err", "flux_upper", "ew_rest", "ew_rest_err", "flux_flag", "vel", "vel_err", "sig", "sig_err", "comp"]

        for row in catalogue:
            ID = row['NIRSpec ID']
            id_list.append(ID)
            ID = str(int(ID)).zfill(6)

            em_lines_path = f"{data_path}/{ID}_R100_em_lines.fits"

            em_table = Table.read(em_lines_path, format='fits') # table of emission lines for the current galaxy 


            try:
                hyla_wave = em_table['wave'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_wave_list.append(hyla_wave)
            except:
                hlya_1216_wave_list.append(np.nan)
            
            try:
                hyla_flux = em_table['flux'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_flux_list.append(hyla_flux)
            except:
                hlya_1216_flux_list.append(np.nan)
            
            try:
                hyla_flux_err = em_table['flux_err'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_flux_err_list.append(hyla_flux_err)
            except:
                hlya_1216_flux_err_list.append(np.nan)
            
            try:
                hyla_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_flux_mc_err_list.append(hyla_flux_mc_err)
            except:
                hlya_1216_flux_mc_err_list.append(np.nan)
            
            try:
                hyla_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_flux_upper_list.append(hyla_flux_upper)
            except:
                hlya_1216_flux_upper_list.append(np.nan)

            try:
                hyla_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_ew_rest_list.append(hyla_ew_rest)
            except:
                hlya_1216_ew_rest_list.append(np.nan)

            try:    
                hyla_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_ew_rest_err_list.append(hyla_ew_rest_err)
            except:
                hlya_1216_ew_rest_err_list.append(np.nan)
            
            try:
                hyla_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_flux_flag_list.append(hyla_flux_flag)
            except:
                hlya_1216_flux_flag_list.append(np.nan)

            try:
                hyla_vel = em_table['vel'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_vel_list.append(hyla_vel)
            except:
                hlya_1216_vel_list.append(np.nan)

            try:
                hyla_vel_err = em_table['vel_err'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_vel_err_list.append(hyla_vel_err)
            except:
                hlya_1216_vel_err_list.append(np.nan)

            try:
                hyla_sig = em_table['sig'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_sig_list.append(hyla_sig)
            except:
                hlya_1216_sig_list.append(np.nan)

            try:
                hyla_sig_err = em_table['sig_err'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_sig_err_list.append(hyla_sig_err)
            except:
                hlya_1216_sig_err_list.append(np.nan)
            
            try:
                hyla_comp = em_table['comp'][(em_table['line_name'] == "HLyA_1216").nonzero()[0][0]]
                hlya_1216_comp_list.append(hyla_comp)
            except:
                hlya_1216_comp_list.append(np.nan)

            try:
                lyA_drop_wave = em_table['wave'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_wave = -999999

            try:
                lyA_drop_flux = em_table['flux'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_flux = -999999

            try:
                lyA_drop_flux_err = em_table['flux_err'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_flux_err = -999999

            try:
                lyA_drop_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_flux_mc_err = -999999

            try:
                lyA_drop_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_flux_upper = -999999

            try:
                lyA_drop_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_ew_rest = -999999

            try:
                lyA_drop_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_ew_rest_err = -999999

            try:
                lyA_drop_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_flux_flag = -999999

            try:
                lyA_drop_vel = em_table['vel'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_vel = -999999

            try:
                lyA_drop_vel_err = em_table['vel_err'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_vel_err = -999999

            try:
                lyA_drop_sig = em_table['sig'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_sig = -999999

            try:
                lyA_drop_sig_err = em_table['sig_err'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_sig_err = -999999

            try:
                lyA_drop_comp = em_table['comp'][(em_table['line_name'] == "LyA_drop").nonzero()[0][0]]
            except:
                lyA_drop_comp = -999999

            lyA_drop_wave_list.append(lyA_drop_wave)
            lyA_drop_flux_list.append(lyA_drop_flux)
            lyA_drop_flux_err_list.append(lyA_drop_flux_err)
            lyA_drop_flux_mc_err_list.append(lyA_drop_flux_mc_err)
            lyA_drop_flux_upper_list.append(lyA_drop_flux_upper)
            lyA_drop_ew_rest_list.append(lyA_drop_ew_rest)
            lyA_drop_ew_rest_err_list.append(lyA_drop_ew_rest_err)
            lyA_drop_flux_flag_list.append(lyA_drop_flux_flag)
            lyA_drop_vel_list.append(lyA_drop_vel)
            lyA_drop_vel_err_list.append(lyA_drop_vel_err)
            lyA_drop_sig_list.append(lyA_drop_sig)
            lyA_drop_sig_err_list.append(lyA_drop_sig_err)
            lyA_drop_comp_list.append(lyA_drop_comp)


            try:
                N4_1648_wave = em_table['wave'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_wave = -999999

            try:
                N4_1648_flux = em_table['flux'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_flux = -999999

            try:
                N4_1648_flux_err = em_table['flux_err'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_flux_err = -999999

            try:
                N4_1648_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_flux_mc_err = -999999

            try:
                N4_1648_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_flux_upper = -999999

            try:
                N4_1648_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_ew_rest = -999999

            try:
                N4_1648_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_ew_rest_err = -999999

            try:
                N4_1648_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_flux_flag = -999999

            try:
                N4_1648_vel = em_table['vel'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_vel = -999999

            try:
                N4_1648_vel_err = em_table['vel_err'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_vel_err = -999999

            try:
                N4_1648_sig = em_table['sig'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_sig = -999999

            try:
                N4_1648_sig_err = em_table['sig_err'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_sig_err = -999999

            try:
                N4_1648_comp = em_table['comp'][(em_table['line_name'] == "N4_1486").nonzero()[0][0]]
            except:
                N4_1648_comp = -999999

            n4_1486_wave_list.append(N4_1648_wave)
            n4_1486_flux_list.append(N4_1648_flux)
            n4_1486_flux_err_list.append(N4_1648_flux_err)
            n4_1486_flux_mc_err_list.append(N4_1648_flux_mc_err)
            n4_1486_flux_upper_list.append(N4_1648_flux_upper)
            n4_1486_ew_rest_list.append(N4_1648_ew_rest)
            n4_1486_ew_rest_err_list.append(N4_1648_ew_rest_err)
            n4_1486_flux_flag_list.append(N4_1648_flux_flag)
            n4_1486_vel_list.append(N4_1648_vel)
            n4_1486_vel_err_list.append(N4_1648_vel_err)
            n4_1486_sig_list.append(N4_1648_sig)
            n4_1486_sig_err_list.append(N4_1648_sig_err)
            n4_1486_comp_list.append(N4_1648_comp)


            try:
                C4_1551_wave = em_table['wave'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_wave = -999999

            try:
                C4_1551_flux = em_table['flux'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_flux = -999999

            try:
                C4_1551_flux_err = em_table['flux_err'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_flux_err = -999999

            try:
                C4_1551_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_flux_mc_err = -999999

            try:
                C4_1551_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_flux_upper = -999999

            try:
                C4_1551_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_ew_rest = -999999

            try:
                C4_1551_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_ew_rest_err = -999999

            try:
                C4_1551_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_flux_flag = -999999

            try:
                C4_1551_vel = em_table['vel'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_vel = -999999

            try:
                C4_1551_vel_err = em_table['vel_err'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_vel_err = -999999

            try:
                C4_1551_sig = em_table['sig'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_sig = -999999

            try:
                C4_1551_sig_err = em_table['sig_err'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_sig_err = -999999

            try:
                C4_1551_comp = em_table['comp'][(em_table['line_name'] == "C4_1549").nonzero()[0][0]]
            except:
                C4_1551_comp = -999999

            c4_1549_wave_list.append(C4_1551_wave)
            c4_1549_flux_list.append(C4_1551_flux)
            c4_1549_flux_err_list.append(C4_1551_flux_err)
            c4_1549_flux_mc_err_list.append(C4_1551_flux_mc_err)
            c4_1549_flux_upper_list.append(C4_1551_flux_upper)
            c4_1549_ew_rest_list.append(C4_1551_ew_rest)
            c4_1549_ew_rest_err_list.append(C4_1551_ew_rest_err)
            c4_1549_flux_flag_list.append(C4_1551_flux_flag)
            c4_1549_vel_list.append(C4_1551_vel)
            c4_1549_vel_err_list.append(C4_1551_vel_err)
            c4_1549_sig_list.append(C4_1551_sig)
            c4_1549_sig_err_list.append(C4_1551_sig_err)
            c4_1549_comp_list.append(C4_1551_comp)

            try:
                He2_1640_wave = em_table['wave'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_wave = -999999

            try:
                He2_1640_flux = em_table['flux'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_flux = -999999

            try:
                He2_1640_flux_err = em_table['flux_err'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_flux_err = -999999

            try:
                He2_1640_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_flux_mc_err = -999999

            try:
                He2_1640_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_flux_upper = -999999

            try:
                He2_1640_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_ew_rest = -999999

            try:
                He2_1640_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_ew_rest_err = -999999

            try:
                He2_1640_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_flux_flag = -999999

            try:
                He2_1640_vel = em_table['vel'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_vel = -999999

            try:
                He2_1640_vel_err = em_table['vel_err'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_vel_err = -999999

            try:
                He2_1640_sig = em_table['sig'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_sig = -999999

            try:
                He2_1640_sig_err = em_table['sig_err'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_sig_err = -999999

            try:
                He2_1640_comp = em_table['comp'][(em_table['line_name'] == "He2_1640").nonzero()[0][0]]
            except:
                He2_1640_comp = -999999

            he2_1640_wave_list.append(He2_1640_wave)
            he2_1640_flux_list.append(He2_1640_flux)
            he2_1640_flux_err_list.append(He2_1640_flux_err)
            he2_1640_flux_mc_err_list.append(He2_1640_flux_mc_err)
            he2_1640_flux_upper_list.append(He2_1640_flux_upper)
            he2_1640_ew_rest_list.append(He2_1640_ew_rest)
            he2_1640_ew_rest_err_list.append(He2_1640_ew_rest_err)
            he2_1640_flux_flag_list.append(He2_1640_flux_flag)
            he2_1640_vel_list.append(He2_1640_vel)
            he2_1640_vel_err_list.append(He2_1640_vel_err)
            he2_1640_sig_list.append(He2_1640_sig)
            he2_1640_sig_err_list.append(He2_1640_sig_err)
            he2_1640_comp_list.append(He2_1640_comp)

            try:
                O3_1666_wave = em_table['wave'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_wave = -999999

            try:
                O3_1666_flux = em_table['flux'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_flux = -999999

            try:
                O3_1666_flux_err = em_table['flux_err'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_flux_err = -999999

            try:
                O3_1666_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_flux_mc_err = -999999

            try:
                O3_1666_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_flux_upper = -999999

            try:
                O3_1666_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_ew_rest = -999999

            try:
                O3_1666_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_ew_rest_err = -999999

            try:
                O3_1666_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_flux_flag = -999999

            try:
                O3_1666_vel = em_table['vel'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_vel = -999999

            try:
                O3_1666_vel_err = em_table['vel_err'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_vel_err = -999999

            try:
                O3_1666_sig = em_table['sig'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_sig = -999999

            try:
                O3_1666_sig_err = em_table['sig_err'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_sig_err = -999999

            try:
                O3_1666_comp = em_table['comp'][(em_table['line_name'] == "O3_1666").nonzero()[0][0]]
            except:
                O3_1666_comp = -999999

            o3_1666_wave_list.append(O3_1666_wave)
            o3_1666_flux_list.append(O3_1666_flux)
            o3_1666_flux_err_list.append(O3_1666_flux_err)
            o3_1666_flux_mc_err_list.append(O3_1666_flux_mc_err)
            o3_1666_flux_upper_list.append(O3_1666_flux_upper)
            o3_1666_ew_rest_list.append(O3_1666_ew_rest)
            o3_1666_ew_rest_err_list.append(O3_1666_ew_rest_err)
            o3_1666_flux_flag_list.append(O3_1666_flux_flag)
            o3_1666_vel_list.append(O3_1666_vel)
            o3_1666_vel_err_list.append(O3_1666_vel_err)
            o3_1666_sig_list.append(O3_1666_sig)
            o3_1666_sig_err_list.append(O3_1666_sig_err)
            o3_1666_comp_list.append(O3_1666_comp)

            try:
                N3_1750_wave = em_table['wave'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_wave = -999999

            try:
                N3_1750_flux = em_table['flux'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_flux = -999999

            try:
                N3_1750_flux_err = em_table['flux_err'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_flux_err = -999999

            try:
                N3_1750_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_flux_mc_err = -999999

            try:
                N3_1750_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_flux_upper = -999999

            try:
                N3_1750_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_ew_rest = -999999

            try:
                N3_1750_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_ew_rest_err = -999999

            try:
                N3_1750_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_flux_flag = -999999

            try:
                N3_1750_vel = em_table['vel'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_vel = -999999

            try:
                N3_1750_vel_err = em_table['vel_err'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_vel_err = -999999

            try:
                N3_1750_sig = em_table['sig'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_sig = -999999

            try:
                N3_1750_sig_err = em_table['sig_err'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_sig_err = -999999

            try:
                N3_1750_comp = em_table['comp'][(em_table['line_name'] == "N3_1750").nonzero()[0][0]]
            except:
                N3_1750_comp = -999999

            n3_1750_wave_list.append(N3_1750_wave)
            n3_1750_flux_list.append(N3_1750_flux)
            n3_1750_flux_err_list.append(N3_1750_flux_err)
            n3_1750_flux_mc_err_list.append(N3_1750_flux_mc_err)
            n3_1750_flux_upper_list.append(N3_1750_flux_upper)
            n3_1750_ew_rest_list.append(N3_1750_ew_rest)
            n3_1750_ew_rest_err_list.append(N3_1750_ew_rest_err)
            n3_1750_flux_flag_list.append(N3_1750_flux_flag)
            n3_1750_vel_list.append(N3_1750_vel)
            n3_1750_vel_err_list.append(N3_1750_vel_err)
            n3_1750_sig_list.append(N3_1750_sig)
            n3_1750_sig_err_list.append(N3_1750_sig_err)
            n3_1750_comp_list.append(N3_1750_comp)

            try:
                C3_1907_wave = em_table['wave'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_wave = -999999

            try:
                C3_1907_flux = em_table['flux'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_flux = -999999

            try:
                C3_1907_flux_err = em_table['flux_err'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_flux_err = -999999

            try:
                C3_1907_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_flux_mc_err = -999999

            try:
                C3_1907_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_flux_upper = -999999

            try:
                C3_1907_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_ew_rest = -999999

            try:
                C3_1907_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_ew_rest_err = -999999

            try:
                C3_1907_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_flux_flag = -999999

            try:
                C3_1907_vel = em_table['vel'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_vel = -999999

            try:
                C3_1907_vel_err = em_table['vel_err'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_vel_err = -999999

            try:
                C3_1907_sig = em_table['sig'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_sig = -999999

            try:
                C3_1907_sig_err = em_table['sig_err'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_sig_err = -999999

            try:
                C3_1907_comp = em_table['comp'][(em_table['line_name'] == "C3_1907").nonzero()[0][0]]
            except:
                C3_1907_comp = -999999

            c3_1907_wave_list.append(C3_1907_wave)
            c3_1907_flux_list.append(C3_1907_flux)
            c3_1907_flux_err_list.append(C3_1907_flux_err)
            c3_1907_flux_mc_err_list.append(C3_1907_flux_mc_err)
            c3_1907_flux_upper_list.append(C3_1907_flux_upper)
            c3_1907_ew_rest_list.append(C3_1907_ew_rest)
            c3_1907_ew_rest_err_list.append(C3_1907_ew_rest_err)
            c3_1907_flux_flag_list.append(C3_1907_flux_flag)
            c3_1907_vel_list.append(C3_1907_vel)
            c3_1907_vel_err_list.append(C3_1907_vel_err)
            c3_1907_sig_list.append(C3_1907_sig)
            c3_1907_sig_err_list.append(C3_1907_sig_err)
            c3_1907_comp_list.append(C3_1907_comp)

            try:
              Ne4_2424_wave = em_table['wave'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_wave = -999999
            
            try:
                Ne4_2424_flux = em_table['flux'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_flux = -999999
            
            try:
                Ne4_2424_flux_err = em_table['flux_err'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_flux_err = -999999

            try:
                Ne4_2424_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_flux_mc_err = -999999

            try:
                Ne4_2424_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_flux_upper = -999999
            
            try:
                Ne4_2424_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_ew_rest = -999999

            try:
                Ne4_2424_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_ew_rest_err = -999999

            try:
                Ne4_2424_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_flux_flag = -999999
            
            try:
                Ne4_2424_vel = em_table['vel'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_vel = -999999
            
            try:
                Ne4_2424_vel_err = em_table['vel_err'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_vel_err = -999999

            try:
                Ne4_2424_sig = em_table['sig'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_sig = -999999

            try:
                Ne4_2424_sig_err = em_table['sig_err'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_sig_err = -999999

            try:
                Ne4_2424_comp = em_table['comp'][(em_table['line_name'] == "Ne4_2424").nonzero()[0][0]]
            except:
                Ne4_2424_comp = -999999
            
            ne4_2424_wave_list.append(Ne4_2424_wave)
            ne4_2424_flux_list.append(Ne4_2424_flux)
            ne4_2424_flux_err_list.append(Ne4_2424_flux_err)
            ne4_2424_flux_mc_err_list.append(Ne4_2424_flux_mc_err)
            ne4_2424_flux_upper_list.append(Ne4_2424_flux_upper)
            ne4_2424_ew_rest_list.append(Ne4_2424_ew_rest)
            ne4_2424_ew_rest_err_list.append(Ne4_2424_ew_rest_err)
            ne4_2424_flux_flag_list.append(Ne4_2424_flux_flag)
            ne4_2424_vel_list.append(Ne4_2424_vel)
            ne4_2424_vel_err_list.append(Ne4_2424_vel_err)
            ne4_2424_sig_list.append(Ne4_2424_sig)
            ne4_2424_sig_err_list.append(Ne4_2424_sig_err)
            ne4_2424_comp_list.append(Ne4_2424_comp)

            try:
                mg2_2796_wave = em_table['wave'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_wave = -999999

            try:
                mg2_2796_flux = em_table['flux'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_flux = -999999

            try:
                mg2_2796_flux_err = em_table['flux_err'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_flux_err = -999999

            try:
                mg2_2796_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_flux_mc_err = -999999

            try:
                mg2_2796_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_flux_upper = -999999

            try:
                mg2_2796_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_ew_rest = -999999

            try:
                mg2_2796_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_ew_rest_err = -999999

            try:
                mg2_2796_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_flux_flag = -999999

            try:
                mg2_2796_vel = em_table['vel'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_vel = -999999

            try:
                mg2_2796_vel_err = em_table['vel_err'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_vel_err = -999999

            try:
                mg2_2796_sig = em_table['sig'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_sig = -999999

            try:
                mg2_2796_sig_err = em_table['sig_err'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_sig_err = -999999

            try:
                mg2_2796_comp = em_table['comp'][(em_table['line_name'] == "Mg2_2796").nonzero()[0][0]]
            except:
                mg2_2796_comp = -999999

            mg2_2796_wave_list.append(mg2_2796_wave)
            mg2_2796_flux_list.append(mg2_2796_flux)
            mg2_2796_flux_err_list.append(mg2_2796_flux_err)
            mg2_2796_flux_mc_err_list.append(mg2_2796_flux_mc_err)
            mg2_2796_flux_upper_list.append(mg2_2796_flux_upper)
            mg2_2796_ew_rest_list.append(mg2_2796_ew_rest)
            mg2_2796_ew_rest_err_list.append(mg2_2796_ew_rest_err)
            mg2_2796_flux_flag_list.append(mg2_2796_flux_flag)
            mg2_2796_vel_list.append(mg2_2796_vel)
            mg2_2796_vel_err_list.append(mg2_2796_vel_err)
            mg2_2796_sig_list.append(mg2_2796_sig)
            mg2_2796_sig_err_list.append(mg2_2796_sig_err)
            mg2_2796_comp_list.append(mg2_2796_comp)

            try:
                ne5_3426_wave = em_table['wave'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_wave = -999999

            try:
                ne5_3426_flux = em_table['flux'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_flux = -999999

            try:
                ne5_3426_flux_err = em_table['flux_err'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_flux_err = -999999

            try:
                ne5_3426_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_flux_mc_err = -999999

            try:
                ne5_3426_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_flux_upper = -999999

            try:
                ne5_3426_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_ew_rest = -999999

            try:
                ne5_3426_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_ew_rest_err = -999999

            try:
                ne5_3426_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_flux_flag = -999999

            try:
                ne5_3426_vel = em_table['vel'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_vel = -999999

            try:
                ne5_3426_vel_err = em_table['vel_err'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_vel_err = -999999

            try:
                ne5_3426_sig = em_table['sig'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_sig = -999999

            try:
                ne5_3426_sig_err = em_table['sig_err'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_sig_err = -999999

            try:
                ne5_3426_comp = em_table['comp'][(em_table['line_name'] == "Ne5_3426").nonzero()[0][0]]
            except:
                ne5_3426_comp = -999999

            ne5_3426_wave_list.append(ne5_3426_wave)
            ne5_3426_flux_list.append(ne5_3426_flux)
            ne5_3426_flux_err_list.append(ne5_3426_flux_err)
            ne5_3426_flux_mc_err_list.append(ne5_3426_flux_mc_err)
            ne5_3426_flux_upper_list.append(ne5_3426_flux_upper)
            ne5_3426_ew_rest_list.append(ne5_3426_ew_rest)
            ne5_3426_ew_rest_err_list.append(ne5_3426_ew_rest_err)
            ne5_3426_flux_flag_list.append(ne5_3426_flux_flag)
            ne5_3426_vel_list.append(ne5_3426_vel)
            ne5_3426_vel_err_list.append(ne5_3426_vel_err)
            ne5_3426_sig_list.append(ne5_3426_sig)
            ne5_3426_sig_err_list.append(ne5_3426_sig_err)
            ne5_3426_comp_list.append(ne5_3426_comp)

            try:
                o2_3727_wave = em_table['wave'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_wave = -999999

            try:
                o2_3727_flux = em_table['flux'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_flux = -999999

            try:
                o2_3727_flux_err = em_table['flux_err'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_flux_err = -999999

            try:
                o2_3727_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_flux_mc_err = -999999

            try:
                o2_3727_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_flux_upper = -999999

            try:
                o2_3727_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_ew_rest = -999999

            try:
                o2_3727_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_ew_rest_err = -999999

            try:
                o2_3727_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_flux_flag = -999999

            try:
                o2_3727_vel = em_table['vel'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_vel = -999999

            try:
                o2_3727_vel_err = em_table['vel_err'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_vel_err = -999999

            try:
                o2_3727_sig = em_table['sig'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_sig = -999999

            try:
                o2_3727_sig_err = em_table['sig_err'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_sig_err = -999999

            try:
                o2_3727_comp = em_table['comp'][(em_table['line_name'] == "O2_3727").nonzero()[0][0]]
            except:
                o2_3727_comp = -999999

            o2_3727_wave_list.append(o2_3727_wave)
            o2_3727_flux_list.append(o2_3727_flux)
            o2_3727_flux_err_list.append(o2_3727_flux_err)
            o2_3727_flux_mc_err_list.append(o2_3727_flux_mc_err)
            o2_3727_flux_upper_list.append(o2_3727_flux_upper)
            o2_3727_ew_rest_list.append(o2_3727_ew_rest)
            o2_3727_ew_rest_err_list.append(o2_3727_ew_rest_err)
            o2_3727_flux_flag_list.append(o2_3727_flux_flag)
            o2_3727_vel_list.append(o2_3727_vel)
            o2_3727_vel_err_list.append(o2_3727_vel_err)
            o2_3727_sig_list.append(o2_3727_sig)
            o2_3727_sig_err_list.append(o2_3727_sig_err)
            o2_3727_comp_list.append(o2_3727_comp)

            try:
                ne3_3869_wave = em_table['wave'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_wave = -999999

            try:
                ne3_3869_flux = em_table['flux'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_flux = -999999

            try:
                ne3_3869_flux_err = em_table['flux_err'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_flux_err = -999999

            try:
                ne3_3869_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_flux_mc_err = -999999

            try:
                ne3_3869_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_flux_upper = -999999

            try:
                ne3_3869_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_ew_rest = -999999

            try:
                ne3_3869_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_ew_rest_err = -999999

            try:
                ne3_3869_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_flux_flag = -999999

            try:
                ne3_3869_vel = em_table['vel'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_vel = -999999

            try:
                ne3_3869_vel_err = em_table['vel_err'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_vel_err = -999999

            try:
                ne3_3869_sig = em_table['sig'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_sig = -999999

            try:
                ne3_3869_sig_err = em_table['sig_err'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_sig_err = -999999

            try:
                ne3_3869_comp = em_table['comp'][(em_table['line_name'] == "Ne3_3869").nonzero()[0][0]]
            except:
                ne3_3869_comp = -999999

            ne3_3869_wave_list.append(ne3_3869_wave)
            ne3_3869_flux_list.append(ne3_3869_flux)
            ne3_3869_flux_err_list.append(ne3_3869_flux_err)
            ne3_3869_flux_mc_err_list.append(ne3_3869_flux_mc_err)
            ne3_3869_flux_upper_list.append(ne3_3869_flux_upper)
            ne3_3869_ew_rest_list.append(ne3_3869_ew_rest)
            ne3_3869_ew_rest_err_list.append(ne3_3869_ew_rest_err)
            ne3_3869_flux_flag_list.append(ne3_3869_flux_flag)
            ne3_3869_vel_list.append(ne3_3869_vel)
            ne3_3869_vel_err_list.append(ne3_3869_vel_err)
            ne3_3869_sig_list.append(ne3_3869_sig)
            ne3_3869_sig_err_list.append(ne3_3869_sig_err)
            ne3_3869_comp_list.append(ne3_3869_comp)

            try:
                hbad_4102_wave = em_table['wave'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_wave = -999999

            try:
                hbad_4102_flux = em_table['flux'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_flux = -999999

            try:
                hbad_4102_flux_err = em_table['flux_err'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_flux_err = -999999

            try:
                hbad_4102_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_flux_mc_err = -999999

            try:
                hbad_4102_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_flux_upper = -999999

            try:
                hbad_4102_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_ew_rest = -999999

            try:
                hbad_4102_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_ew_rest_err = -999999

            try:
                hbad_4102_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_flux_flag = -999999

            try:
                hbad_4102_vel = em_table['vel'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_vel = -999999

            try:
                hbad_4102_vel_err = em_table['vel_err'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_vel_err = -999999

            try:
                hbad_4102_sig = em_table['sig'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_sig = -999999

            try:
                hbad_4102_sig_err = em_table['sig_err'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_sig_err = -999999

            try:
                hbad_4102_comp = em_table['comp'][(em_table['line_name'] == "HBaD_4102").nonzero()[0][0]]
            except:
                hbad_4102_comp = -999999

            hbad_4102_wave_list.append(hbad_4102_wave)
            hbad_4102_flux_list.append(hbad_4102_flux)
            hbad_4102_flux_err_list.append(hbad_4102_flux_err)
            hbad_4102_flux_mc_err_list.append(hbad_4102_flux_mc_err)
            hbad_4102_flux_upper_list.append(hbad_4102_flux_upper)
            hbad_4102_ew_rest_list.append(hbad_4102_ew_rest)
            hbad_4102_ew_rest_err_list.append(hbad_4102_ew_rest_err)
            hbad_4102_flux_flag_list.append(hbad_4102_flux_flag)
            hbad_4102_vel_list.append(hbad_4102_vel)
            hbad_4102_vel_err_list.append(hbad_4102_vel_err)
            hbad_4102_sig_list.append(hbad_4102_sig)
            hbad_4102_sig_err_list.append(hbad_4102_sig_err)
            hbad_4102_comp_list.append(hbad_4102_comp)

            try:
                hbag_4340_wave = em_table['wave'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_wave = -999999

            try:
                hbag_4340_flux = em_table['flux'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_flux = -999999

            try:
                hbag_4340_flux_err = em_table['flux_err'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_flux_err = -999999

            try:
                hbag_4340_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_flux_mc_err = -999999

            try:
                hbag_4340_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_flux_upper = -999999

            try:
                hbag_4340_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_ew_rest = -999999

            try:
                hbag_4340_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_ew_rest_err = -999999

            try:
                hbag_4340_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_flux_flag = -999999

            try:
                hbag_4340_vel = em_table['vel'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_vel = -999999

            try:
                hbag_4340_vel_err = em_table['vel_err'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_vel_err = -999999

            try:
                hbag_4340_sig = em_table['sig'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_sig = -999999

            try:
                hbag_4340_sig_err = em_table['sig_err'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_sig_err = -999999

            try:
                hbag_4340_comp = em_table['comp'][(em_table['line_name'] == "HBaG_4340").nonzero()[0][0]]
            except:
                hbag_4340_comp = -999999

            hbag_4340_wave_list.append(hbag_4340_wave)
            hbag_4340_flux_list.append(hbag_4340_flux)
            hbag_4340_flux_err_list.append(hbag_4340_flux_err)
            hbag_4340_flux_mc_err_list.append(hbag_4340_flux_mc_err)
            hbag_4340_flux_upper_list.append(hbag_4340_flux_upper)
            hbag_4340_ew_rest_list.append(hbag_4340_ew_rest)
            hbag_4340_ew_rest_err_list.append(hbag_4340_ew_rest_err)
            hbag_4340_flux_flag_list.append(hbag_4340_flux_flag)
            hbag_4340_vel_list.append(hbag_4340_vel)
            hbag_4340_vel_err_list.append(hbag_4340_vel_err)
            hbag_4340_sig_list.append(hbag_4340_sig)
            hbag_4340_sig_err_list.append(hbag_4340_sig_err)
            hbag_4340_comp_list.append(hbag_4340_comp)

            try:
                blnd_hbag_o3_4340_wave = em_table['wave'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_wave = -999999

            try:
                blnd_hbag_o3_4340_flux = em_table['flux'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_flux = -999999

            try:
                blnd_hbag_o3_4340_flux_err = em_table['flux_err'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_flux_err = -999999

            try:
                blnd_hbag_o3_4340_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_flux_mc_err = -999999

            try:
                blnd_hbag_o3_4340_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_flux_upper = -999999

            try:
                blnd_hbag_o3_4340_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_ew_rest = -999999

            try:
                blnd_hbag_o3_4340_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_ew_rest_err = -999999

            try:
                blnd_hbag_o3_4340_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_flux_flag = -999999

            try:
                blnd_hbag_o3_4340_vel = em_table['vel'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_vel = -999999

            try:
                blnd_hbag_o3_4340_vel_err = em_table['vel_err'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_vel_err = -999999

            try:
                blnd_hbag_o3_4340_sig = em_table['sig'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_sig = -999999

            try:
                blnd_hbag_o3_4340_sig_err = em_table['sig_err'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_sig_err = -999999

            try:
                blnd_hbag_o3_4340_comp = em_table['comp'][(em_table['line_name'] == "Blnd_HBaG_O3_4340").nonzero()[0][0]]
            except:
                blnd_hbag_o3_4340_comp = -999999

            blnd_hbag_o3_4340_wave_list.append(blnd_hbag_o3_4340_wave)
            blnd_hbag_o3_4340_flux_list.append(blnd_hbag_o3_4340_flux)
            blnd_hbag_o3_4340_flux_err_list.append(blnd_hbag_o3_4340_flux_err)
            blnd_hbag_o3_4340_flux_mc_err_list.append(blnd_hbag_o3_4340_flux_mc_err)
            blnd_hbag_o3_4340_flux_upper_list.append(blnd_hbag_o3_4340_flux_upper)
            blnd_hbag_o3_4340_ew_rest_list.append(blnd_hbag_o3_4340_ew_rest)
            blnd_hbag_o3_4340_ew_rest_err_list.append(blnd_hbag_o3_4340_ew_rest_err)
            blnd_hbag_o3_4340_flux_flag_list.append(blnd_hbag_o3_4340_flux_flag)
            blnd_hbag_o3_4340_vel_list.append(blnd_hbag_o3_4340_vel)
            blnd_hbag_o3_4340_vel_err_list.append(blnd_hbag_o3_4340_vel_err)
            blnd_hbag_o3_4340_sig_list.append(blnd_hbag_o3_4340_sig)
            blnd_hbag_o3_4340_sig_err_list.append(blnd_hbag_o3_4340_sig_err)
            blnd_hbag_o3_4340_comp_list.append(blnd_hbag_o3_4340_comp)

            try:
                o3_4363_wave = em_table['wave'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_wave = -999999

            try:
                o3_4363_flux = em_table['flux'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_flux = -999999

            try:
                o3_4363_flux_err = em_table['flux_err'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_flux_err = -999999

            try:
                o3_4363_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_flux_mc_err = -999999

            try:
                o3_4363_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_flux_upper = -999999

            try:
                o3_4363_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_ew_rest = -999999

            try:
                o3_4363_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_ew_rest_err = -999999

            try:
                o3_4363_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_flux_flag = -999999

            try:
                o3_4363_vel = em_table['vel'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_vel = -999999

            try:
                o3_4363_vel_err = em_table['vel_err'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_vel_err = -999999

            try:
                o3_4363_sig = em_table['sig'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_sig = -999999

            try:
                o3_4363_sig_err = em_table['sig_err'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_sig_err = -999999

            try:
                o3_4363_comp = em_table['comp'][(em_table['line_name'] == "O3_4363").nonzero()[0][0]]
            except:
                o3_4363_comp = -999999

            o3_4363_wave_list.append(o3_4363_wave)
            o3_4363_flux_list.append(o3_4363_flux)
            o3_4363_flux_err_list.append(o3_4363_flux_err)
            o3_4363_flux_mc_err_list.append(o3_4363_flux_mc_err)
            o3_4363_flux_upper_list.append(o3_4363_flux_upper)
            o3_4363_ew_rest_list.append(o3_4363_ew_rest)
            o3_4363_ew_rest_err_list.append(o3_4363_ew_rest_err)
            o3_4363_flux_flag_list.append(o3_4363_flux_flag)
            o3_4363_vel_list.append(o3_4363_vel)
            o3_4363_vel_err_list.append(o3_4363_vel_err)
            o3_4363_sig_list.append(o3_4363_sig)
            o3_4363_sig_err_list.append(o3_4363_sig_err)
            o3_4363_comp_list.append(o3_4363_comp)

            try:
                heii_4686_wave = em_table['wave'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_wave = -999999

            try:
                heii_4686_flux = em_table['flux'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_flux = -999999

            try:
                heii_4686_flux_err = em_table['flux_err'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_flux_err = -999999

            try:
                heii_4686_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_flux_mc_err = -999999

            try:
                heii_4686_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_flux_upper = -999999

            try:
                heii_4686_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_ew_rest = -999999

            try:
                heii_4686_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_ew_rest_err = -999999

            try:
                heii_4686_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_flux_flag = -999999

            try:
                heii_4686_vel = em_table['vel'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_vel = -999999

            try:
                heii_4686_vel_err = em_table['vel_err'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_vel_err = -999999

            try:
                heii_4686_sig = em_table['sig'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_sig = -999999

            try:
                heii_4686_sig_err = em_table['sig_err'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_sig_err = -999999

            try:
                heii_4686_comp = em_table['comp'][(em_table['line_name'] == "HeII_4686").nonzero()[0][0]]
            except:
                heii_4686_comp = -999999

            heii_4686_wave_list.append(heii_4686_wave)
            heii_4686_flux_list.append(heii_4686_flux)
            heii_4686_flux_err_list.append(heii_4686_flux_err)
            heii_4686_flux_mc_err_list.append(heii_4686_flux_mc_err)
            heii_4686_flux_upper_list.append(heii_4686_flux_upper)
            heii_4686_ew_rest_list.append(heii_4686_ew_rest)
            heii_4686_ew_rest_err_list.append(heii_4686_ew_rest_err)
            heii_4686_flux_flag_list.append(heii_4686_flux_flag)
            heii_4686_vel_list.append(heii_4686_vel)
            heii_4686_vel_err_list.append(heii_4686_vel_err)
            heii_4686_sig_list.append(heii_4686_sig)
            heii_4686_sig_err_list.append(heii_4686_sig_err)
            heii_4686_comp_list.append(heii_4686_comp)

            try:
                hbab_4861_wave = em_table['wave'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_wave = -999999

            try:
                hbab_4861_flux = em_table['flux'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_flux = -999999

            try:
                hbab_4861_flux_err = em_table['flux_err'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_flux_err = -999999

            try:
                hbab_4861_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_flux_mc_err = -999999

            try:
                hbab_4861_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_flux_upper = -999999

            try:
                hbab_4861_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_ew_rest = -999999

            try:
                hbab_4861_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_ew_rest_err = -999999

            try:
                hbab_4861_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_flux_flag = -999999

            try:
                hbab_4861_vel = em_table['vel'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_vel = -999999

            try:
                hbab_4861_vel_err = em_table['vel_err'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_vel_err = -999999

            try:
                hbab_4861_sig = em_table['sig'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_sig = -999999

            try:
                hbab_4861_sig_err = em_table['sig_err'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_sig_err = -999999

            try:
                hbab_4861_comp = em_table['comp'][(em_table['line_name'] == "HBaB_4861").nonzero()[0][0]]
            except:
                hbab_4861_comp = -999999

            hbab_4861_wave_list.append(hbab_4861_wave)
            hbab_4861_flux_list.append(hbab_4861_flux)
            hbab_4861_flux_err_list.append(hbab_4861_flux_err)
            hbab_4861_flux_mc_err_list.append(hbab_4861_flux_mc_err)
            hbab_4861_flux_upper_list.append(hbab_4861_flux_upper)
            hbab_4861_ew_rest_list.append(hbab_4861_ew_rest)
            hbab_4861_ew_rest_err_list.append(hbab_4861_ew_rest_err)
            hbab_4861_flux_flag_list.append(hbab_4861_flux_flag)
            hbab_4861_vel_list.append(hbab_4861_vel)
            hbab_4861_vel_err_list.append(hbab_4861_vel_err)
            hbab_4861_sig_list.append(hbab_4861_sig)
            hbab_4861_sig_err_list.append(hbab_4861_sig_err)
            hbab_4861_comp_list.append(hbab_4861_comp)

            try:
                o3_4959_wave = em_table['wave'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_wave = -999999

            try:
                o3_4959_flux = em_table['flux'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_flux = -999999

            try:
                o3_4959_flux_err = em_table['flux_err'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_flux_err = -999999

            try:
                o3_4959_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_flux_mc_err = -999999

            try:
                o3_4959_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_flux_upper = -999999

            try:
                o3_4959_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_ew_rest = -999999

            try:
                o3_4959_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_ew_rest_err = -999999

            try:
                o3_4959_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_flux_flag = -999999

            try:
                o3_4959_vel = em_table['vel'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_vel = -999999

            try:
                o3_4959_vel_err = em_table['vel_err'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_vel_err = -999999

            try:
                o3_4959_sig = em_table['sig'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_sig = -999999

            try:
                o3_4959_sig_err = em_table['sig_err'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_sig_err = -999999

            try:
                o3_4959_comp = em_table['comp'][(em_table['line_name'] == "O3_4959").nonzero()[0][0]]
            except:
                o3_4959_comp = -999999

            o3_4959_wave_list.append(o3_4959_wave)
            o3_4959_flux_list.append(o3_4959_flux)
            o3_4959_flux_err_list.append(o3_4959_flux_err)
            o3_4959_flux_mc_err_list.append(o3_4959_flux_mc_err)
            o3_4959_flux_upper_list.append(o3_4959_flux_upper)
            o3_4959_ew_rest_list.append(o3_4959_ew_rest)
            o3_4959_ew_rest_err_list.append(o3_4959_ew_rest_err)
            o3_4959_flux_flag_list.append(o3_4959_flux_flag)
            o3_4959_vel_list.append(o3_4959_vel)
            o3_4959_vel_err_list.append(o3_4959_vel_err)
            o3_4959_sig_list.append(o3_4959_sig)
            o3_4959_sig_err_list.append(o3_4959_sig_err)
            o3_4959_comp_list.append(o3_4959_comp)

            try:
                o3_5007_wave = em_table['wave'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_wave = -999999

            try:
                o3_5007_flux = em_table['flux'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_flux = -999999

            try:
                o3_5007_flux_err = em_table['flux_err'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_flux_err = -999999

            try:
                o3_5007_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_flux_mc_err = -999999

            try:
                o3_5007_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_flux_upper = -999999

            try:
                o3_5007_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_ew_rest = -999999

            try:
                o3_5007_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_ew_rest_err = -999999

            try:
                o3_5007_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_flux_flag = -999999

            try:
                o3_5007_vel = em_table['vel'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_vel = -999999

            try:
                o3_5007_vel_err = em_table['vel_err'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_vel_err = -999999

            try:
                o3_5007_sig = em_table['sig'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_sig = -999999

            try:
                o3_5007_sig_err = em_table['sig_err'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_sig_err = -999999

            try:
                o3_5007_comp = em_table['comp'][(em_table['line_name'] == "O3_5007").nonzero()[0][0]]
            except:
                o3_5007_comp = -999999

            o3_5007_wave_list.append(o3_5007_wave)
            o3_5007_flux_list.append(o3_5007_flux)
            o3_5007_flux_err_list.append(o3_5007_flux_err)
            o3_5007_flux_mc_err_list.append(o3_5007_flux_mc_err)
            o3_5007_flux_upper_list.append(o3_5007_flux_upper)
            o3_5007_ew_rest_list.append(o3_5007_ew_rest)
            o3_5007_ew_rest_err_list.append(o3_5007_ew_rest_err)
            o3_5007_flux_flag_list.append(o3_5007_flux_flag)
            o3_5007_vel_list.append(o3_5007_vel)
            o3_5007_vel_err_list.append(o3_5007_vel_err)
            o3_5007_sig_list.append(o3_5007_sig)
            o3_5007_sig_err_list.append(o3_5007_sig_err)
            o3_5007_comp_list.append(o3_5007_comp)

            try:
                o3_5007d_wave = em_table['wave'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_wave = -999999

            try:
                o3_5007d_flux = em_table['flux'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_flux = -999999

            try:
                o3_5007d_flux_err = em_table['flux_err'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_flux_err = -999999

            try:
                o3_5007d_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_flux_mc_err = -999999

            try:
                o3_5007d_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_flux_upper = -999999

            try:
                o3_5007d_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_ew_rest = -999999

            try:
                o3_5007d_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_ew_rest_err = -999999

            try:
                o3_5007d_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_flux_flag = -999999

            try:
                o3_5007d_vel = em_table['vel'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_vel = -999999

            try:
                o3_5007d_vel_err = em_table['vel_err'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_vel_err = -999999

            try:
                o3_5007d_sig = em_table['sig'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_sig = -999999

            try:
                o3_5007d_sig_err = em_table['sig_err'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_sig_err = -999999

            try:
                o3_5007d_comp = em_table['comp'][(em_table['line_name'] == "O3_5007d").nonzero()[0][0]]
            except:
                o3_5007d_comp = -999999

            o3_5007d_wave_list.append(o3_5007d_wave)
            o3_5007d_flux_list.append(o3_5007d_flux)
            o3_5007d_flux_err_list.append(o3_5007d_flux_err)
            o3_5007d_flux_mc_err_list.append(o3_5007d_flux_mc_err)
            o3_5007d_flux_upper_list.append(o3_5007d_flux_upper)
            o3_5007d_ew_rest_list.append(o3_5007d_ew_rest)
            o3_5007d_ew_rest_err_list.append(o3_5007d_ew_rest_err)
            o3_5007d_flux_flag_list.append(o3_5007d_flux_flag)
            o3_5007d_vel_list.append(o3_5007d_vel)
            o3_5007d_vel_err_list.append(o3_5007d_vel_err)
            o3_5007d_sig_list.append(o3_5007d_sig)
            o3_5007d_sig_err_list.append(o3_5007d_sig_err)
            o3_5007d_comp_list.append(o3_5007d_comp)

            try:
                he1_5875_wave = em_table['wave'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_wave = -999999

            try:
                he1_5875_flux = em_table['flux'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_flux = -999999

            try:
                he1_5875_flux_err = em_table['flux_err'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_flux_err = -999999

            try:
                he1_5875_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_flux_mc_err = -999999

            try:
                he1_5875_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_flux_upper = -999999

            try:
                he1_5875_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_ew_rest = -999999

            try:
                he1_5875_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_ew_rest_err = -999999

            try:
                he1_5875_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_flux_flag = -999999

            try:
                he1_5875_vel = em_table['vel'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_vel = -999999

            try:
                he1_5875_vel_err = em_table['vel_err'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_vel_err = -999999

            try:
                he1_5875_sig = em_table['sig'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_sig = -999999

            try:
                he1_5875_sig_err = em_table['sig_err'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_sig_err = -999999

            try:
                he1_5875_comp = em_table['comp'][(em_table['line_name'] == "He1_5875").nonzero()[0][0]]
            except:
                he1_5875_comp = -999999

            he1_5875_wave_list.append(he1_5875_wave)
            he1_5875_flux_list.append(he1_5875_flux)
            he1_5875_flux_err_list.append(he1_5875_flux_err)
            he1_5875_flux_mc_err_list.append(he1_5875_flux_mc_err)
            he1_5875_flux_upper_list.append(he1_5875_flux_upper)
            he1_5875_ew_rest_list.append(he1_5875_ew_rest)
            he1_5875_ew_rest_err_list.append(he1_5875_ew_rest_err)
            he1_5875_flux_flag_list.append(he1_5875_flux_flag)
            he1_5875_vel_list.append(he1_5875_vel)
            he1_5875_vel_err_list.append(he1_5875_vel_err)
            he1_5875_sig_list.append(he1_5875_sig)
            he1_5875_sig_err_list.append(he1_5875_sig_err)
            he1_5875_comp_list.append(he1_5875_comp)

            try:
                o1_6300_wave = em_table['wave'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_wave = -999999
            
            try:
                o1_6300_flux = em_table['flux'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_flux = -999999

            try:
                o1_6300_flux_err = em_table['flux_err'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_flux_err = -999999

            try:
                o1_6300_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_flux_mc_err = -999999

            try:
                o1_6300_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_flux_upper = -999999

            try:
                o1_6300_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_ew_rest = -999999

            try:
                o1_6300_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_ew_rest_err = -999999

            try:
                o1_6300_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_flux_flag = -999999

            try:
                o1_6300_vel = em_table['vel'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_vel = -999999

            try:
                o1_6300_vel_err = em_table['vel_err'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_vel_err = -999999

            try:
                o1_6300_sig = em_table['sig'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_sig = -999999

            try:
                o1_6300_sig_err = em_table['sig_err'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_sig_err = -999999

            try:
                o1_6300_comp = em_table['comp'][(em_table['line_name'] == "O1_6300").nonzero()[0][0]]
            except:
                o1_6300_comp = -999999

            o1_6300_wave_list.append(o1_6300_wave)
            o1_6300_flux_list.append(o1_6300_flux)
            o1_6300_flux_err_list.append(o1_6300_flux_err)
            o1_6300_flux_mc_err_list.append(o1_6300_flux_mc_err)
            o1_6300_flux_upper_list.append(o1_6300_flux_upper)
            o1_6300_ew_rest_list.append(o1_6300_ew_rest)
            o1_6300_ew_rest_err_list.append(o1_6300_ew_rest_err)
            o1_6300_flux_flag_list.append(o1_6300_flux_flag)
            o1_6300_vel_list.append(o1_6300_vel)
            o1_6300_vel_err_list.append(o1_6300_vel_err)
            o1_6300_sig_list.append(o1_6300_sig)
            o1_6300_sig_err_list.append(o1_6300_sig_err)
            o1_6300_comp_list.append(o1_6300_comp)

            try:
                blnd_hbaa_n2_wave = em_table['wave'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_wave = -999999

            try:
                blnd_hbaa_n2_flux = em_table['flux'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_flux = -999999

            try:
                blnd_hbaa_n2_flux_err = em_table['flux_err'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_flux_err = -999999

            try:
                blnd_hbaa_n2_flux_mc_err = em_table['flux_mc_err'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_flux_mc_err = -999999

            try:
                blnd_hbaa_n2_flux_upper = em_table['flux_upper'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_flux_upper = -999999

            try:
                blnd_hbaa_n2_ew_rest = em_table['ew_rest'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_ew_rest = -999999

            try:
                blnd_hbaa_n2_ew_rest_err = em_table['ew_rest_err'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_ew_rest_err = -999999

            try:
                blnd_hbaa_n2_flux_flag = em_table['flux_flag'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_flux_flag = -999999

            try:
                blnd_hbaa_n2_vel = em_table['vel'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_vel = -999999

            try:
                blnd_hbaa_n2_vel_err = em_table['vel_err'][(em_table['line_name'] == "Blnd_HBaa_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_vel_err = -999999

            try:
                blnd_hbaa_n2_sig = em_table['sig'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_sig = -999999

            try:
                blnd_hbaa_n2_sig_err = em_table['sig_err'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_sig_err = -999999

            try:
                blnd_hbaa_n2_comp = em_table['comp'][(em_table['line_name'] == "Blnd_HBaA_N2").nonzero()[0][0]]
            except:
                blnd_hbaa_n2_comp = -999999

            blnd_hbaa_n2_wave_list.append(blnd_hbaa_n2_wave)
            blnd_hbaa_n2_flux_list.append(blnd_hbaa_n2_flux)
            blnd_hbaa_n2_flux_err_list.append(blnd_hbaa_n2_flux_err)
            blnd_hbaa_n2_flux_mc_err_list.append(blnd_hbaa_n2_flux_mc_err)
            blnd_hbaa_n2_flux_upper_list.append(blnd_hbaa_n2_flux_upper)
            blnd_hbaa_n2_ew_rest_list.append(blnd_hbaa_n2_ew_rest)
            blnd_hbaa_n2_ew_rest_err_list.append(blnd_hbaa_n2_ew_rest_err)
            blnd_hbaa_n2_flux_flag_list.append(blnd_hbaa_n2_flux_flag)
            blnd_hbaa_n2_vel_list.append(blnd_hbaa_n2_vel)
            blnd_hbaa_n2_vel_err_list.append(blnd_hbaa_n2_vel_err)
            blnd_hbaa_n2_sig_list.append(blnd_hbaa_n2_sig)
            blnd_hbaa_n2_sig_err_list.append(blnd_hbaa_n2_sig_err)
            blnd_hbaa_n2_comp_list.append(blnd_hbaa_n2_comp)


        # use the lists to create a df 
            
        data = {
                "NIRSpec_ID": id_list,
                "HLyA_1216_wave": hlya_1216_wave_list,
                "HLyA_1216_flux": hlya_1216_flux_list,
                "HLyA_1216_flux_err": hlya_1216_flux_err_list,
                "HLyA_1216_flux_mc_err": hlya_1216_flux_mc_err_list,
                "HLyA_1216_flux_upper": hlya_1216_flux_upper_list,
                "HLyA_1216_ew_rest": hlya_1216_ew_rest_list,
                "HLyA_1216_ew_rest_err": hlya_1216_ew_rest_err_list,
                "HLyA_1216_flux_flag": hlya_1216_flux_flag_list,
                "HLyA_1216_vel": hlya_1216_vel_list,
                "HLyA_1216_vel_err": hlya_1216_vel_err_list,
                "HLyA_1216_sig": hlya_1216_sig_list,
                "HLyA_1216_sig_err": hlya_1216_sig_err_list,
                "HLyA_1216_comp": hlya_1216_comp_list,
                "LyA_drop_wave": lyA_drop_wave_list,
                "LyA_drop_flux": lyA_drop_flux_list,
                "LyA_drop_flux_err": lyA_drop_flux_err_list,
                "LyA_drop_flux_mc_err": lyA_drop_flux_mc_err_list,
                "LyA_drop_flux_upper": lyA_drop_flux_upper_list,
                "LyA_drop_ew_rest": lyA_drop_ew_rest_list,
                "LyA_drop_ew_rest_err": lyA_drop_ew_rest_err_list,
                "LyA_drop_flux_flag": lyA_drop_flux_flag_list,
                "LyA_drop_vel": lyA_drop_vel_list,
                "LyA_drop_vel_err": lyA_drop_vel_err_list,
                "LyA_drop_sig": lyA_drop_sig_list,
                "LyA_drop_sig_err": lyA_drop_sig_err_list,
                "LyA_drop_comp": lyA_drop_comp_list,
                "N4_1486_wave": n4_1486_wave_list,
                "N4_1486_flux": n4_1486_flux_list,
                "N4_1486_flux_err": n4_1486_flux_err_list,
                "N4_1486_flux_mc_err": n4_1486_flux_mc_err_list,
                "N4_1486_flux_upper": n4_1486_flux_upper_list,
                "N4_1486_ew_rest": n4_1486_ew_rest_list,
                "N4_1486_ew_rest_err": n4_1486_ew_rest_err_list,
                "N4_1486_flux_flag": n4_1486_flux_flag_list,
                "N4_1486_vel": n4_1486_vel_list,
                "N4_1486_vel_err": n4_1486_vel_err_list,
                "N4_1486_sig": n4_1486_sig_list,
                "N4_1486_sig_err": n4_1486_sig_err_list,
                "N4_1486_comp": n4_1486_comp_list,
                "C4_1549_wave": c4_1549_wave_list,
                "C4_1549_flux": c4_1549_flux_list,
                "C4_1549_flux_err": c4_1549_flux_err_list,
                "C4_1549_flux_mc_err": c4_1549_flux_mc_err_list,
                "C4_1549_flux_upper": c4_1549_flux_upper_list,
                "C4_1549_ew_rest": c4_1549_ew_rest_list,
                "C4_1549_ew_rest_err": c4_1549_ew_rest_err_list,
                "C4_1549_flux_flag": c4_1549_flux_flag_list,
                "C4_1549_vel": c4_1549_vel_list,
                "C4_1549_vel_err": c4_1549_vel_err_list,
                "C4_1549_sig": c4_1549_sig_list,
                "C4_1549_sig_err": c4_1549_sig_err_list,
                "C4_1549_comp": c4_1549_comp_list,
                "He2_1640_wave": he2_1640_wave_list,
                "He2_1640_flux": he2_1640_flux_list,
                "He2_1640_flux_err": he2_1640_flux_err_list,
                "He2_1640_flux_mc_err": he2_1640_flux_mc_err_list,
                "He2_1640_flux_upper": he2_1640_flux_upper_list,
                "He2_1640_ew_rest": he2_1640_ew_rest_list,
                "He2_1640_ew_rest_err": he2_1640_ew_rest_err_list,
                "He2_1640_flux_flag": he2_1640_flux_flag_list,
                "He2_1640_vel": he2_1640_vel_list,
                "He2_1640_vel_err": he2_1640_vel_err_list,
                "He2_1640_sig": he2_1640_sig_list,
                "He2_1640_sig_err": he2_1640_sig_err_list,
                "He2_1640_comp": he2_1640_comp_list,
                "O3_1666_wave": o3_1666_wave_list,
                "O3_1666_flux": o3_1666_flux_list,
                "O3_1666_flux_err": o3_1666_flux_err_list,
                "O3_1666_flux_mc_err": o3_1666_flux_mc_err_list,
                "O3_1666_flux_upper": o3_1666_flux_upper_list,
                "O3_1666_ew_rest": o3_1666_ew_rest_list,
                "O3_1666_ew_rest_err": o3_1666_ew_rest_err_list,
                "O3_1666_flux_flag": o3_1666_flux_flag_list,
                "O3_1666_vel": o3_1666_vel_list,
                "O3_1666_vel_err": o3_1666_vel_err_list,
                "O3_1666_sig": o3_1666_sig_list,
                "O3_1666_sig_err": o3_1666_sig_err_list,
                "O3_1666_comp": o3_1666_comp_list,
                "N3_1750_wave": n3_1750_wave_list,
                "N3_1750_flux": n3_1750_flux_list,
                "N3_1750_flux_err": n3_1750_flux_err_list,
                "N3_1750_flux_mc_err": n3_1750_flux_mc_err_list,
                "N3_1750_flux_upper": n3_1750_flux_upper_list,
                "N3_1750_ew_rest": n3_1750_ew_rest_list,
                "N3_1750_ew_rest_err": n3_1750_ew_rest_err_list,
                "N3_1750_flux_flag": n3_1750_flux_flag_list,
                "N3_1750_vel": n3_1750_vel_list,
                "N3_1750_vel_err": n3_1750_vel_err_list,
                "N3_1750_sig": n3_1750_sig_list,
                "N3_1750_sig_err": n3_1750_sig_err_list,
                "N3_1750_comp": n3_1750_comp_list,
                "C3_1907_wave": c3_1907_wave_list,
                "C3_1907_flux": c3_1907_flux_list,
                "C3_1907_flux_err": c3_1907_flux_err_list,
                "C3_1907_flux_mc_err": c3_1907_flux_mc_err_list,
                "C3_1907_flux_upper": c3_1907_flux_upper_list,
                "C3_1907_ew_rest": c3_1907_ew_rest_list,
                "C3_1907_ew_rest_err": c3_1907_ew_rest_err_list,
                "C3_1907_flux_flag": c3_1907_flux_flag_list,
                "C3_1907_vel": c3_1907_vel_list,
                "C3_1907_vel_err": c3_1907_vel_err_list,
                "C3_1907_sig": c3_1907_sig_list,
                "C3_1907_sig_err": c3_1907_sig_err_list,
                "C3_1907_comp": c3_1907_comp_list,
                "Mg2_2796_wave": mg2_2796_wave_list,
                "Mg2_2796_flux": mg2_2796_flux_list,
                "Mg2_2796_flux_err": mg2_2796_flux_err_list,
                "Mg2_2796_flux_mc_err": mg2_2796_flux_mc_err_list,
                "Mg2_2796_flux_upper": mg2_2796_flux_upper_list,
                "Mg2_2796_ew_rest": mg2_2796_ew_rest_list,
                "Mg2_2796_ew_rest_err": mg2_2796_ew_rest_err_list,
                "Mg2_2796_flux_flag": mg2_2796_flux_flag_list,
                "Mg2_2796_vel": mg2_2796_vel_list,
                "Mg2_2796_vel_err": mg2_2796_vel_err_list,
                "Mg2_2796_sig": mg2_2796_sig_list,
                "Mg2_2796_sig_err": mg2_2796_sig_err_list,
                "Mg2_2796_comp": mg2_2796_comp_list,
                "Ne5_3426_wave": ne5_3426_wave_list,
                "Ne5_3426_flux": ne5_3426_flux_list,
                "Ne5_3426_flux_err": ne5_3426_flux_err_list,
                "Ne5_3426_flux_mc_err": ne5_3426_flux_mc_err_list,
                "Ne5_3426_flux_upper": ne5_3426_flux_upper_list,
                "Ne5_3426_ew_rest": ne5_3426_ew_rest_list,
                "Ne5_3426_ew_rest_err": ne5_3426_ew_rest_err_list,
                "Ne5_3426_flux_flag": ne5_3426_flux_flag_list,
                "Ne5_3426_vel": ne5_3426_vel_list,
                "Ne5_3426_vel_err": ne5_3426_vel_err_list,
                "Ne5_3426_sig": ne5_3426_sig_list,
                "Ne5_3426_sig_err": ne5_3426_sig_err_list,
                "Ne5_3426_comp": ne5_3426_comp_list,
                "O2_3727_wave": o2_3727_wave_list,
                "O2_3727_flux": o2_3727_flux_list,
                "O2_3727_flux_err": o2_3727_flux_err_list,
                "O2_3727_flux_mc_err": o2_3727_flux_mc_err_list,
                "O2_3727_flux_upper": o2_3727_flux_upper_list,
                "O2_3727_ew_rest": o2_3727_ew_rest_list,
                "O2_3727_ew_rest_err": o2_3727_ew_rest_err_list,
                "O2_3727_flux_flag": o2_3727_flux_flag_list,
                "O2_3727_vel": o2_3727_vel_list,
                "O2_3727_vel_err": o2_3727_vel_err_list,
                "O2_3727_sig": o2_3727_sig_list,
                "O2_3727_sig_err": o2_3727_sig_err_list,
                "O2_3727_comp": o2_3727_comp_list,
                "Ne3_3869_wave": ne3_3869_wave_list,
                "Ne3_3869_flux": ne3_3869_flux_list,
                "Ne3_3869_flux_err": ne3_3869_flux_err_list,
                "Ne3_3869_flux_mc_err": ne3_3869_flux_mc_err_list,
                "Ne3_3869_flux_upper": ne3_3869_flux_upper_list,
                "Ne3_3869_ew_rest": ne3_3869_ew_rest_list,
                "Ne3_3869_ew_rest_err": ne3_3869_ew_rest_err_list,
                "Ne3_3869_flux_flag": ne3_3869_flux_flag_list,
                "Ne3_3869_vel": ne3_3869_vel_list,
                "Ne3_3869_vel_err": ne3_3869_vel_err_list,
                "Ne3_3869_sig": ne3_3869_sig_list,
                "Ne3_3869_sig_err": ne3_3869_sig_err_list,
                "Ne3_3869_comp": ne3_3869_comp_list,
                "HBaD_4102_wave": hbad_4102_wave_list,
                "HBaD_4102_flux": hbad_4102_flux_list,
                "HBaD_4102_flux_err": hbad_4102_flux_err_list,
                "HBaD_4102_flux_mc_err": hbad_4102_flux_mc_err_list,
                "HBaD_4102_flux_upper": hbad_4102_flux_upper_list,
                "HBaD_4102_ew_rest": hbad_4102_ew_rest_list,
                "HBaD_4102_ew_rest_err": hbad_4102_ew_rest_err_list,
                "HBaD_4102_flux_flag": hbad_4102_flux_flag_list,
                "HBaD_4102_vel": hbad_4102_vel_list,
                "HBaD_4102_vel_err": hbad_4102_vel_err_list,
                "HBaD_4102_sig": hbad_4102_sig_list,
                "HBaD_4102_sig_err": hbad_4102_sig_err_list,
                "HBaD_4102_comp": hbad_4102_comp_list,
                "HBaG_4340_wave": hbag_4340_wave_list,
                "HBaG_4340_flux": hbag_4340_flux_list,
                "HBaG_4340_flux_err": hbag_4340_flux_err_list,
                "HBaG_4340_flux_mc_err": hbag_4340_flux_mc_err_list,
                "HBaG_4340_flux_upper": hbag_4340_flux_upper_list,
                "HBaG_4340_ew_rest": hbag_4340_ew_rest_list,
                "HBaG_4340_ew_rest_err": hbag_4340_ew_rest_err_list,
                "HBaG_4340_flux_flag": hbag_4340_flux_flag_list,
                "HBaG_4340_vel": hbag_4340_vel_list,
                "HBaG_4340_vel_err": hbag_4340_vel_err_list,
                "HBaG_4340_sig": hbag_4340_sig_list,
                "HBaG_4340_sig_err": hbag_4340_sig_err_list,
                "HBaG_4340_comp": hbag_4340_comp_list,
                "Blnd_HBaG_O3_4340_wave": blnd_hbag_o3_4340_wave_list,
                "Blnd_HBaG_O3_4340_flux": blnd_hbag_o3_4340_flux_list,
                "Blnd_HBaG_O3_4340_flux_err": blnd_hbag_o3_4340_flux_err_list,
                "Blnd_HBaG_O3_4340_flux_mc_err": blnd_hbag_o3_4340_flux_mc_err_list,
                "Blnd_HBaG_O3_4340_flux_upper": blnd_hbag_o3_4340_flux_upper_list,
                "Blnd_HBaG_O3_4340_ew_rest": blnd_hbag_o3_4340_ew_rest_list,
                "Blnd_HBaG_O3_4340_ew_rest_err": blnd_hbag_o3_4340_ew_rest_err_list,
                "Blnd_HBaG_O3_4340_flux_flag": blnd_hbag_o3_4340_flux_flag_list,
                "Blnd_HBaG_O3_4340_vel": blnd_hbag_o3_4340_vel_list,
                "Blnd_HBaG_O3_4340_vel_err": blnd_hbag_o3_4340_vel_err_list,
                "Blnd_HBaG_O3_4340_sig": blnd_hbag_o3_4340_sig_list,
                "Blnd_HBaG_O3_4340_sig_err": blnd_hbag_o3_4340_sig_err_list,
                "Blnd_HBaG_O3_4340_comp": blnd_hbag_o3_4340_comp_list,
                "O3_4363_wave": o3_4363_wave_list,
                "O3_4363_flux": o3_4363_flux_list,
                "O3_4363_flux_err": o3_4363_flux_err_list,
                "O3_4363_flux_mc_err": o3_4363_flux_mc_err_list,
                "O3_4363_flux_upper": o3_4363_flux_upper_list,
                "O3_4363_ew_rest": o3_4363_ew_rest_list,
                "O3_4363_ew_rest_err": o3_4363_ew_rest_err_list,
                "O3_4363_flux_flag": o3_4363_flux_flag_list,
                "O3_4363_vel": o3_4363_vel_list,
                "O3_4363_vel_err": o3_4363_vel_err_list,
                "O3_4363_sig": o3_4363_sig_list,
                "O3_4363_sig_err": o3_4363_sig_err_list,
                "O3_4363_comp": o3_4363_comp_list,
                "HeII_4686_wave": heii_4686_wave_list,
                "HeII_4686_flux": heii_4686_flux_list,
                "HeII_4686_flux_err": heii_4686_flux_err_list,
                "HeII_4686_flux_mc_err": heii_4686_flux_mc_err_list,
                "HeII_4686_flux_upper": heii_4686_flux_upper_list,
                "HeII_4686_ew_rest": heii_4686_ew_rest_list,
                "HeII_4686_ew_rest_err": heii_4686_ew_rest_err_list,
                "HeII_4686_flux_flag": heii_4686_flux_flag_list,
                "HeII_4686_vel": heii_4686_vel_list,
                "HeII_4686_vel_err": heii_4686_vel_err_list,
                "HeII_4686_sig": heii_4686_sig_list,
                "HeII_4686_sig_err": heii_4686_sig_err_list,
                "HeII_4686_comp": heii_4686_comp_list,
                "HBaB_4861_wave": hbab_4861_wave_list,
                "HBaB_4861_flux": hbab_4861_flux_list,
                "HBaB_4861_flux_err": hbab_4861_flux_err_list,
                "HBaB_4861_flux_mc_err": hbab_4861_flux_mc_err_list,
                "HBaB_4861_flux_upper": hbab_4861_flux_upper_list,
                "HBaB_4861_ew_rest": hbab_4861_ew_rest_list,
                "HBaB_4861_ew_rest_err": hbab_4861_ew_rest_err_list,
                "HBaB_4861_flux_flag": hbab_4861_flux_flag_list,
                "HBaB_4861_vel": hbab_4861_vel_list,
                "HBaB_4861_vel_err": hbab_4861_vel_err_list,
                "HBaB_4861_sig": hbab_4861_sig_list,
                "HBaB_4861_sig_err": hbab_4861_sig_err_list,
                "HBaB_4861_comp": hbab_4861_comp_list,
                "O3_4959_wave": o3_4959_wave_list,
                "O3_4959_flux": o3_4959_flux_list,
                "O3_4959_flux_err": o3_4959_flux_err_list,
                "O3_4959_flux_mc_err": o3_4959_flux_mc_err_list,
                "O3_4959_flux_upper": o3_4959_flux_upper_list,
                "O3_4959_ew_rest": o3_4959_ew_rest_list,
                "O3_4959_ew_rest_err": o3_4959_ew_rest_err_list,
                "O3_4959_flux_flag": o3_4959_flux_flag_list,
                "O3_4959_vel": o3_4959_vel_list,
                "O3_4959_vel_err": o3_4959_vel_err_list,
                "O3_4959_sig": o3_4959_sig_list,
                "O3_4959_sig_err": o3_4959_sig_err_list,
                "O3_4959_comp": o3_4959_comp_list,
                "O3_5007_wave": o3_5007_wave_list,
                "O3_5007_flux": o3_5007_flux_list,
                "O3_5007_flux_err": o3_5007_flux_err_list,
                "O3_5007_flux_mc_err": o3_5007_flux_mc_err_list,
                "O3_5007_flux_upper": o3_5007_flux_upper_list,
                "O3_5007_ew_rest": o3_5007_ew_rest_list,
                "O3_5007_ew_rest_err": o3_5007_ew_rest_err_list,
                "O3_5007_flux_flag": o3_5007_flux_flag_list,
                "O3_5007_vel": o3_5007_vel_list,
                "O3_5007_vel_err": o3_5007_vel_err_list,
                "O3_5007_sig": o3_5007_sig_list,
                "O3_5007_sig_err": o3_5007_sig_err_list,
                "O3_5007_comp": o3_5007_comp_list,
                "O3_5007d_wave": o3_5007d_wave_list,
                "O3_5007d_flux": o3_5007d_flux_list,
                "O3_5007d_flux_err": o3_5007d_flux_err_list,
                "O3_5007d_flux_mc_err": o3_5007d_flux_mc_err_list,
                "O3_5007d_flux_upper": o3_5007d_flux_upper_list,
                "O3_5007d_ew_rest": o3_5007d_ew_rest_list,
                "O3_5007d_ew_rest_err": o3_5007d_ew_rest_err_list,
                "O3_5007d_flux_flag": o3_5007d_flux_flag_list,
                "O3_5007d_vel": o3_5007d_vel_list,
                "O3_5007d_vel_err": o3_5007d_vel_err_list,
                "O3_5007d_sig": o3_5007d_sig_list,
                "O3_5007d_sig_err": o3_5007d_sig_err_list,
                "O3_5007d_comp": o3_5007d_comp_list,
                "He1_5875_wave": he1_5875_wave_list,
                "He1_5875_flux": he1_5875_flux_list,
                "He1_5875_flux_err": he1_5875_flux_err_list,
                "He1_5875_flux_mc_err": he1_5875_flux_mc_err_list,
                "He1_5875_flux_upper": he1_5875_flux_upper_list,
                "He1_5875_ew_rest": he1_5875_ew_rest_list,
                "He1_5875_ew_rest_err": he1_5875_ew_rest_err_list,
                "He1_5875_flux_flag": he1_5875_flux_flag_list,
                "He1_5875_vel": he1_5875_vel_list,
                "He1_5875_vel_err": he1_5875_vel_err_list,
                "He1_5875_sig": he1_5875_sig_list,
                "He1_5875_sig_err": he1_5875_sig_err_list,
                "He1_5875_comp": he1_5875_comp_list,
                "O1_6300_wave": o1_6300_wave_list,
                "O1_6300_flux": o1_6300_flux_list,
                "O1_6300_flux_err": o1_6300_flux_err_list,
                "O1_6300_flux_mc_err": o1_6300_flux_mc_err_list,
                "O1_6300_flux_upper": o1_6300_flux_upper_list,
                "O1_6300_ew_rest": o1_6300_ew_rest_list,
                "O1_6300_ew_rest_err": o1_6300_ew_rest_err_list,
                "O1_6300_flux_flag": o1_6300_flux_flag_list,
                "O1_6300_vel": o1_6300_vel_list,
                "O1_6300_vel_err": o1_6300_vel_err_list,
                "O1_6300_sig": o1_6300_sig_list,
                "O1_6300_sig_err": o1_6300_sig_err_list,
                "O1_6300_comp": o1_6300_comp_list,
                "Blnd_HBaa_N2_wave": blnd_hbaa_n2_wave_list,
                "Blnd_HBaa_N2_flux": blnd_hbaa_n2_flux_list,
                "Blnd_HBaa_N2_flux_err": blnd_hbaa_n2_flux_err_list,
                "Blnd_HBaa_N2_flux_mc_err": blnd_hbaa_n2_flux_mc_err_list,
                "Blnd_HBaa_N2_flux_upper": blnd_hbaa_n2_flux_upper_list,
                "Blnd_HBaa_N2_ew_rest": blnd_hbaa_n2_ew_rest_list,
                "Blnd_HBaa_N2_ew_rest_err": blnd_hbaa_n2_ew_rest_err_list,
                "Blnd_HBaa_N2_flux_flag": blnd_hbaa_n2_flux_flag_list,
                "Blnd_HBaa_N2_vel": blnd_hbaa_n2_vel_list,
                "Blnd_HBaa_N2_vel_err": blnd_hbaa_n2_vel_err_list,
                "Blnd_HBaa_N2_sig": blnd_hbaa_n2_sig_list,
                "Blnd_HBaa_N2_sig_err": blnd_hbaa_n2_sig_err_list,
                "Blnd_HBaa_N2_comp": blnd_hbaa_n2_comp_list}

            # Convert the dictionary to a DataFrame
        df = pd.DataFrame(data)
        #replace nan/blank values with -9999

        df = df.replace('--', -9999)



        df.to_csv(output_path.replace(".fits", ".csv"), index=False)

        # fits_table = Table.from_pandas(df)
        # fits_table.write(output_path, format="fits", overwrite=True)

        return df


