import os
import nirspecxf
from astropy.table import Table
from multiprocessing import freeze_support
from datetime import datetime
import results_cat
import plotting

run_analysis = False
create_cat = False
sort_plots = True

catalogue_path = "/Users/katherineormerod/Documents/LJMU/WIDE/catalogues/EGS_GOODSN_UDS_combined.fits"
data_path = "/Users/katherineormerod/Documents/LJMU/WIDE/nirspecxf_heii/"
output_path = "/Users/katherineormerod/Documents/LJMU/WIDE/catalogues/EGS_GOODSN_UDS_combined_nirspecxf_heii_3sig.fits"


if run_analysis:
    # ensure each process only uses one thread 

    os.environ["NUMEXPR_NUM_THREADS"] = "1"
    os.environ["OMP_NUM_THREADS"] = "1"
    os.environ["MKL_NUM_THREADS"] = "1"


    if __name__ == '__main__': 

        starttime = datetime.now()

        freeze_support()  

        z_table_path = "/Users/katherineormerod/Documents/LJMU/WIDE/nirspecxf_heii/wide_z_table.fits"
        config_path = "/Users/katherineormerod/Documents/LJMU/WIDE/nirspecxf_heii/r100_all.yaml"
        cores = 6

        ids = Table.read(z_table_path)['ID']
        config = nirspecxf.nirspec_spec.NIRSpecConfig(config_path)

        nirspecxf.process_multi(cores, ids, dict(config))

        endtime = datetime.now()

        print(f"Time taken to run nirspecxf for {len(ids)} galaxies: {endtime - starttime}")

if create_cat:
    df = results_cat.results_table(catalogue_path, data_path, output_path)
    # res_cat.results_table(catalogue_path, data_path, output_path)

if sort_plots:
    plotting.sort(data_path)



