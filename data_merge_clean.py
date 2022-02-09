import pandas as pd
import numpy as np

#
# Merges all relevant data, deletes the rest, stores the results in water.data.merged.csv
#

# The csv file with as a data frame
df = pd.read_csv('water_data_notevenclosetoclean.csv')
# Suppress numpy float sci form
np.set_printoptions(suppress=True)

def main():
    # resulting merged & cleaned data frame
    dest_df = {}

    # Dimension data
    dimensions = np.array(['state_name', 'county_nm', 'year', 'Total Population'])
    dest_df.update({dimensions[i]:df[dimensions[i]] for i in range(3)})
    dest_df.update({dimensions[3]:conv_col_to_float(df[dimensions[3]])})
    # Waste Treatment data
    wt_keep = np.array(['WT reclaimed wastewater released by wastewater facilities','WT number of wastewater facilities','WT number of public wastewater facilities',
                        'WT returns by public wastewater facilities', 'WT reclaimed wastewater released by public wastewater facilities'])
    wt_map = {}
    dest_df.update(merge(wt_keep, wt_map))
    # Hydroelectric Power data
    hp_keep = np.array(['HP instream use'])
    hp_map = {'HP total number of facilities':['HP number of offstream facilities','HP number of instream facilities'],
                'HP total power generated':['HP power generated by offstream use','HP power generated by instream use'],
                    'HP total offstream surface-water withdrawals':['HP surface s-s offstream withdrawals','HP offstream surface-water withdrawals']}
    dest_df.update(merge(hp_keep, hp_map))
    # Irrigation data
    irr_keep = np.array(['Ir Total reclaimed wastewater', 'Ir Total conveyance loss'])
    irr_map = {'Ir Total total irrigation':['Ir Total surface irrigation', 'Ir Total microirrigation', 'Ir Total sprinkler irrigation'],
                    'Ir Total total consumptive use':['Ir Total consumptive use.1', 'Ir Total consumptive use'],
                        'Ir Total total s-s withdrawals':['Ir Total s-s surface-water withdrawals.1', 'Ir Total s-s surface-water withdrawals',
                                                            'Ir Total s-s groundwater withdrawals.1', 'Ir Total s-s groundwater withdrawals']}
    dest_df.update(merge(irr_keep, irr_map))
    # Aquaculture data
    a_keep = np.array([])
    a_map = {'A total consumptive use':['A consumptive use.1','A consumptive use'],
                'A total s-s withdrawals':['A s-s surface-water withdrawals.1', 'A s-s surface-water withdrawals',
                                            'A s-s groundwater withdrawals.1', 'A s-s groundwater withdrawals']}
    dest_df.update(merge(a_keep, a_map))
    # Livestock data
    l_keep = np.array([])
    l_map = {'L consumptive use': ['L (Animal Specialties) consumptive use.1', 'L (Animal Specialties) consumptive use',
                                    'L (Stock) consumptive use.1', 'L (Stock) consumptive use'],
                'L total s-s withdrawals': ['L (Animal Specialties) s-s surface-water withdrawals.1', 'L (Animal Specialties) s-s surface-water withdrawals',
                                             'L (Animal Specialties) s-s groundwater withdrawals.1', 'L (Animal Specialties) s-s groundwater withdrawals',
                                              'L (Stock) s-s surface-water withdrawals.1', 'L (Stock) s-s surface-water withdrawals',
                                               'L (Stock) s-s groundwater withdrawals.1', 'L (Stock) s-s groundwater withdrawals']}
    dest_df.update(merge(l_keep, l_map))
    # Mining data
    m_keep = np.array(['M reclaimed wastewater'])
    m_map = {'M total consumptive use':['M consumptive use.1', 'M consumptive use'],
                'M total s-s withdrawals':['M s-s surface-water withdrawals.1', 'M s-s surface-water withdrawals',
                                            'M s-s groundwater withdrawals.1', 'M s-s groundwater withdrawals']}
    dest_df.update(merge(m_keep, m_map))
    # Thermoelectric Power data
    tp_keep = np.array([])
    tp_map = {'TP total number of facilities':['TP (CL-C) number of facilities', 'TP (OT-C) number of facilities'],
                'TP total reclaimed wastewater':['TP (CL-C) reclaimed wastewater', 'TP (OT-C) reclaimed wastewater'],
                  'TP total power generated':['TP (CL-C) power generated', 'TP (OT-C) power generated'],
                    'TP total consumptive use':['TP (CL-C) consumptive use.1', 'TP (CL-C) consumptive use',
                                                    'TP (OT-C) consumptive use.1', 'TP (OT-C) consumptive use'],
                      'TP total s-s withdrawls':['TP (CL-C) s-s surface-water withdrawals.1', 'TP (CL-C) s-s surface-water withdrawals',
                                                    'TP (CL-C) s-s groundwater withdrawals.1', 'TP (CL-C) s-s groundwater withdrawals',
                                                        'TP (OT-C) s-s surface-water withdrawals.1', 'TP (OT-C) s-s surface-water withdrawals',
                                                            'TP (OT-C) s-s groundwater withdrawals.1', 'TP (OT-C) s-s groundwater withdrawals'],
                        'TP total s-s withdrawls plus deliveries':['TP (CL-C) s-s surface-water withdrawals.1', 'TP (CL-C) s-s surface-water withdrawals',
                                                    'TP (CL-C) s-s groundwater withdrawals.1', 'TP (CL-C) s-s groundwater withdrawals',
                                                        'TP (OT-C) s-s surface-water withdrawals.1', 'TP (OT-C) s-s surface-water withdrawals',
                                                            'TP (OT-C) s-s groundwater withdrawals.1', 'TP (OT-C) s-s groundwater withdrawals',
                                                                'TP (CL-C) deliveries from public supply', 'TP (OT-C) deliveries from public supply']}
    dest_df.update(merge(tp_keep, tp_map))
    # Nuclear Thermoelectric Power data
    ntp_keep = np.array(['NTP number of facilities', 'NTP reclaimed wastewater', 'NTP power generation'])
    ntp_map = {'NTP total consumptive use':['NTP consumptive use.1', 'NTP consumptive use'],
                'NTP total s-s withdrawals':['NTP s-s surface-water withdrawals.1', 'NTP s-s surface-water withdrawals',
                                                'NTP s-s groundwater withdrawals.1', 'NTP s-s groundwater withdrawals'],
                 'NTP total s-s withdrawals plus deliveries':['NTP s-s surface-water withdrawals.1', 'NTP s-s surface-water withdrawals',
                                                                'NTP s-s groundwater withdrawals.1', 'NTP s-s groundwater withdrawals',
                                                                    'NTP deliveries from public supply']}
    dest_df.update(merge(ntp_keep, ntp_map))
    # Geothermal Thermoeletric Power data
    gtp_keep = np.array(['GTP number of facilities', 'GTP reclaimed wastewater', 'GTP power generation'])
    gtp_map = {'GTP total consumptive use':['GTP consumptive use.1', 'GTP consumptive use'],
                'GTP total s-s withdrawals':['GTP s-s surface-water withdrawals.1', 'GTP s-s surface-water withdrawals',
                                                'GTP s-s groundwater withdrawals.1', 'GTP s-s groundwater withdrawals'],
                 'GTP total s-s withdrawals plus deliveries':['GTP s-s surface-water withdrawals.1', 'GTP s-s surface-water withdrawals',
                                                                'GTP s-s groundwater withdrawals.1', 'GTP s-s groundwater withdrawals',
                                                                    'GTP deliveries from public supply']}
    dest_df.update(merge(gtp_keep, gtp_map))
    # Fossil-fuel Thermoelectric Power data
    ftp_keep = np.array(['FTP number of facilities', 'FTP reclaimed wastewater', 'FTP power generation'])
    ftp_map = {'FTP total consumptive use':['FTP consumptive use.1', 'FTP consumptive use'],
                'FTP total s-s withdrawals':['FTP s-s surface-water withdrawals.1', 'FTP s-s surface-water withdrawals',
                                                'FTP s-s groundwater withdrawals.1', 'FTP s-s groundwater withdrawals'],
                 'FTP total s-s withdrawals plus deliveries':['FTP s-s surface-water withdrawals.1', 'FTP s-s surface-water withdrawals',
                                                                'FTP s-s groundwater withdrawals.1', 'FTP s-s groundwater withdrawals',
                                                                    'FTP deliveries from public supply']}
    dest_df.update(merge(ftp_keep, ftp_map))
    # Total Thermoelectric Power data
    ttp_keep = np.array(['TTP number of facilities', 'TTP reclaimed wastewater', 'TTP power generated', 'TTP total s-s withdrawals plus deliveries'])
    ttp_map = {'TTP total consumptive use':['TTP consumptive use.1', 'TTP consumptive use'],
                'TTP total s-s withdrawals':['TTP s-s surface-water withdrawals.1', 'TTP s-s surface-water withdrawals',
                                                'TTP s-s groundwater withdrawals.1', 'TTP s-s groundwater withdrawals']}
    dest_df.update(merge(ttp_keep, ttp_map))
    # Industrial data
    i_keep = np.array(['I number of facilities', 'I reclaimed wastewater'])
    i_map = {'I total consumptive use':['I consumptive use.1', 'I consumptive use'],
                'I total s-s withdrawals':['I s-s surface-water withdrawals.1', 'I s-s surface-water withdrawals',
                                                'I s-s groundwater withdrawals.1', 'I s-s groundwater withdrawals'],
                 'I total s-s withdrawals plus deliveries':['I s-s surface-water withdrawals.1', 'I s-s surface-water withdrawals',
                                                                'I s-s groundwater withdrawals.1', 'I s-s groundwater withdrawals',
                                                                    'I deliveries from public supply']}
    dest_df.update(merge(i_keep, i_map))
    # Commerical data
    c_keep = np.array(['C reclaimed wastewater'])
    c_map = {'C total consumptive use':['C consumptive use.1', 'C consumptive use'],
                'C total s-s withdrawals':['C s-s surface-water withdrawals.1', 'C s-s surface-water withdrawals',
                                                'C s-s groundwater withdrawals.1', 'C s-s groundwater withdrawals'],
                 'C total s-s withdrawals plus deliveries':['C s-s surface-water withdrawals.1', 'C s-s surface-water withdrawals',
                                                                'C s-s groundwater withdrawals.1', 'C s-s groundwater withdrawals',
                                                                    'C deliveries from public supply']}
    dest_df.update(merge(c_keep, c_map))
    # Domestic data
    d_keep = np.array(['D reclaimed wastewater','D s-s population','D per capita use s-s',
                        'D per capita use public-supplied'])
    d_map = {'D total consumptive use': ['D consumptive use.1','D consumptive use'],
                'D total s-s withdrawals total':['D s-s surface-water withdrawals.1','D s-s surface-water withdrawals',
                                'D s-s groundwater withdrawals.1','D s-s groundwater withdrawals'],
                    'D total s-s withdrawals plus deliveries':['D s-s surface-water withdrawals.1','D s-s surface-water withdrawals',
                                'D s-s groundwater withdrawals.1','D s-s groundwater withdrawals', 'D deliveries from public supply']}
    dest_df.update(merge(d_keep, d_map))
    # Public Supply data
    ps_keep = np.array(['PS number of facilities','PS reclaimed wastewater','PS per capita use',
                        'PS public use and losses'])
    ps_map = {'PS total deliveries':['PS deliveries to thermoelectric','PS deliveries to industrial',
                                        'PS deliveries to commercial', 'PS deliveries to domestic'],
                'PS total s-s withdrawals total':['PS s-s surface-water withdrawals.1','PS s-s surface-water withdrawals',
                                                    'PS s-s groundwater withdrawals.1','PS s-s groundwater withdrawals']}
    dest_df.update(merge(ps_keep, ps_map))
    
    # Output merged & cleaned dataframe to csv file
    print(pd.DataFrame.from_dict(dest_df))
    pd.DataFrame.from_dict(dest_df).to_csv('water_data_merged_cleaned.csv', float_format='%.3f', index=False)


# takes in an np arr of column names
# returns an np arr of float converted columns
def cols_to_conv_np(cols):
    return np.array([conv_col_to_float(df[cols[i]]) for i in range(len(cols))])

# Takes in a column, converts column values to float, zeroes out missing values
# col - the input column 
# returns an np array of the col
def conv_col_to_float(col):
    # print([ord(c) for c in c1[i]])
    c_arr = col.to_numpy()
    return np.array([0.00 if (str(c_arr[i])[0] == str(chr(45))) else float(c_arr[i]) for i in range(len(col))])

# keeps select columns, merges select columns
# keepCols - an np array of column names to keep
# mergeCols - a map of new col names to an array of column names to merge
# Returns a map of new columns to names
def merge(keepCols, mergeCols):
    # sorry
    colMap = {{} if (len(keepCols) == 0) else keepCols[i]:conv_col_to_float(df[keepCols[i]]) for i in range(len(keepCols))}
    if (mergeCols):
        colMap.update({k:merge_cols(cols_to_conv_np(mergeCols[k])) for k in mergeCols.keys()})
    return colMap

# Takes in columns as np arrays and merges 
# --column data values must be of type float--
# cols - np array of columns being merged
# returns a map of name to col
def merge_cols(cols):
    return np.sum(cols, axis = 0)

# prints out the column headers in reversed order
# header - np array of the column headers
def print_col_reversed(header):
    for i in reversed(range(len(header))):
        print(header[i])

# prints out the column headers in reversed order with a
# data value paired from select row
# header - np array of the column headers
def print_col_reversed_c(header, row):
    fRow = df.iloc[row].to_numpy()
    for i in reversed(range(len(header))):
        print(header[i] + ' ' + str(fRow[i]))

if __name__ == "__main__":
    main()

##################################################### Data Format #####################################################
#                                                                                                                     #
#######################################################################################################################

#
# Child data of parent data denoted by tabs
# parent data is the sum of the child data
#

# WT reclaimed wastewater released by wastewater facilities -
# WT number of wastewater facilities -
# WT number of public wastewater facilities 7
# WT returns by public wastewater facilities 142.32
# WT reclaimed wastewater released by public wastewater facilities -

# HP total number of facilities -
    # HP number of offstream facilities -
    # HP number of instream facilities -
# HP total power generated -
    # HP power generated by offstream use -
    # HP power generated by instream use 0.00
# HP total offstream surface-water withdrawals -
    # HP surface s-s offstream withdrawals -
    # HP offstream surface-water withdrawals -
# HP instream use 0.00

# Ir Golf Courses reclaimed wastewater for golf courses -
# Ir Golf Courses total irrigation for golf courses -
    # Ir Golf Courses surface irrigation for golf courses -
    # Ir Golf Courses microirrigation for golf courses -
    # Ir Golf Courses sprinkler irrigation for golf courses -
# Ir Golf Courses conveyance loss for golf courses -
# Ir Golf Courses consumptive use for golf courses -
# Ir Golf Courses total s-s withdrawals for golf courses -
    # Ir Golf Courses s-s surface-water withdrawals for golf courses -
    # Ir Golf Courses s-s groundwater withdrawals for golf courses -
# Ir Crop reclaimed wastewater for crops -
# Ir Crop total irrigation for crops -
    # Ir Crop surface irrigation for crops -
    # Ir Crop microirrigation for crops -
    # Ir Crop sprinkler irrigation for crops -
# Ir Crop conveyance loss for crops -
# Ir Crop consumptive use for crops -
# Ir Crop total s-s withdrawals for crops -
    # Ir Crop s-s surface-water withdrawals for crops -
    # Ir Crop s-s groundwater withdrawals for crops -
# Ir Total reclaimed wastewater 0.33
# Ir Total total irrigation -
    # Ir Total surface irrigation 9.01
    # Ir Total microirrigation -
    # Ir Total sprinkler irrigation 3.29
# Ir Total conveyance loss 0.28
# Ir Total total consumptive use -
    # Ir Total consumptive use.1 -
    # Ir Total consumptive use 16.11
# Ir Total total s-s withdrawals.2 -
    # Ir Total total s-s withdrawals.1 -
    # Ir Total total s-s withdrawals 23.44
        # Ir Total total s-s withdrawals surface -
            # Ir Total s-s surface-water withdrawals.1 -
            # Ir Total s-s surface-water withdrawals 15.61
        # Ir Total total s-s withdrawals groundwater -
            # Ir Total s-s groundwater withdrawals.1 -
            # Ir Total s-s groundwater withdrawals 7.83

# A total consumptive use -
    # A consumptive use.1 -
    # A consumptive use -
# A total s-s withdrawals.2 -
    # A total s-s withdrawals.1 -
    # A total s-s withdrawals -
        # A total s-s withdrawals surface -
            # A s-s surface-water withdrawals.1 -
            # A s-s surface-water withdrawals -
        # A total s-s withdrawals groundwater -
            # A s-s groundwater withdrawals.1 -
            # A s-s groundwater withdrawals -

# L (Animal Specialties) total consumptive use -
    # L (Animal Specialties) consumptive use.1 -
    # L (Animal Specialties) consumptive use -
# L (Animal Specialties) total s-s withdrawals.2 -
    # L (Animal Specialties) total s-s withdrawals.1 -
    # L (Animal Specialties) total s-s withdrawals -
        # L (Animal Specialties) total s-s withdrawals surface -
            # L (Animal Specialties) s-s surface-water withdrawals.1 -
            # L (Animal Specialties) s-s surface-water withdrawals -
        # L (Animal Specialties) total s-s withdrawals groundwater -
            # L (Animal Specialties) s-s groundwater withdrawals.1 -
            # L (Animal Specialties) s-s groundwater withdrawals -
# L (Stock) total consumptive use -
    # L (Stock) consumptive use.1 -
    # L (Stock) consumptive use 0.67
# L (Stock) total s-s withdrawals.2 -
    # L (Stock) total s-s withdrawals.1 -
    # L (Stock) total s-s withdrawals 0.73
        # L (Stock) total s-s withdrawals surface -
            # L (Stock) s-s surface-water withdrawals.1 -
            # L (Stock) s-s surface-water withdrawals 0.60
        # L (Stock) total s-s withdrawals groundwater -
            # L (Stock) s-s groundwater withdrawals.1 -
            # L (Stock) s-s groundwater withdrawals 0.13
# L consumptive use -
# L total s-s withdrawals -
    # L s-s surface-water withdrawals -
    # L s-s groundwater withdrawals -

# M reclaimed wastewater -
# M total consumptive use 0.30
    # M consumptive use.1 0.19
    # M consumptive use 0.11
# M total s-s withdrawals.2 1.13
    # M total s-s withdrawals.1 0.73
    # M total s-s withdrawals 0.4
        # M total s-s withdrawals surface 0.2
            # M s-s surface-water withdrawals.1 0.06
            # M s-s surface-water withdrawals 0.14
        # M total s-s withdrawals groundwater 0.93
            # M s-s groundwater withdrawals.1 0.67
            # M s-s groundwater withdrawals 0.26

# TP (CL-C) number of facilities -
# TP (CL-C) reclaimed wastewater -
# TP (CL-C) power generated -
# TP (CL-C) total consumptive use -
    # TP (CL-C) consumptive use.1 -
    # TP (CL-C) consumptive use -
# TP (CL-C) total s-s withdrawals plus deliveries -
    # TP (CL-C) deliveries from public supply -
    # TP (CL-C) total s-s withdrawals total -
        # TP (CL-C) total s-s withdrawals.1 -
        # TP (CL-C) total s-s withdrawals -
        # TP (CL-C) total s-s withdrawals surface -
            # TP (CL-C) s-s surface-water withdrawals.1 -
            # TP (CL-C) s-s surface-water withdrawals -
        # TP (CL-C) total s-s withdrawals groundwater -
            # TP (CL-C) s-s groundwater withdrawals.1 -
            # TP (CL-C) s-s groundwater withdrawals -
# TP (OT-C) number of facilities -
# TP (OT-C) reclaimed wastewater -
# TP (OT-C) power generated -
# TP (OT-C) total consumptive use -
    # TP (OT-C) consumptive use.1 -
    # TP (OT-C) consumptive use -
# TP (OT-C) total s-s withdrawals plus deliveries -
    # TP (OT-C) deliveries from public supply -
    # TP (OT-C) total s-s withdrawals total -
        # TP (OT-C) total s-s withdrawals.1 -
        # TP (OT-C) total s-s withdrawals -
            # TP (OT-C) total s-s withdrawals surface -
                # TP (OT-C) s-s surface-water withdrawals.1 -
                # TP (OT-C) s-s surface-water withdrawals -
            # TP (OT-C) total s-s withdrawals groundwater -
                # TP (OT-C) s-s groundwater withdrawals.1 -
                # TP (OT-C) s-s groundwater withdrawals -

# NTP number of facilities -
# NTP reclaimed wastewater -
# NTP power generation 0.00
# NTP total consumptive use 0.00
    # NTP consumptive use.1 0.00
    # NTP consumptive use 0.00
# NTP total s-s withdrawals plus deliveries -
    # NTP deliveries from public supply 0.00
    # NTP total s-s withdrawals.2 -
        # NTP total s-s withdrawals.1 -
        # NTP total s-s withdrawals 0.00
            # NTP total s-s withdrawals surface 0.00
                # NTP s-s surface-water withdrawals.1 0.00
                # NTP s-s surface-water withdrawals 0.00
            # NTP total s-s withdrawals groundwater -
                # NTP s-s groundwater withdrawals.1 -
                # NTP s-s groundwater withdrawals 0.00

# GTP number of facilities -
# GTP reclaimed wastewater -
# GTP power generation 0.00
# GTP total consumptive use 0.00
    # GTP consumptive use.1 0.00
    # GTP consumptive use 0.00
# GTP total s-s withdrawals plus deliveries -
    # GTP deliveries from public supply 0.00
    # GTP total s-s withdrawals.2 -
        # GTP total s-s withdrawals.1 -
        # GTP total s-s withdrawals -
            # GTP total s-s withdrawals surface -
                # GTP s-s surface-water withdrawals.1 -
                # GTP s-s surface-water withdrawals -
            # GTP total s-s withdrawals groundwater 0.00
                # GTP s-s groundwater withdrawals.1 0.00
                # GTP s-s groundwater withdrawals 0.00

# FTP number of facilities -
# FTP reclaimed wastewater -
# FTP power generation 7.72
# FTP total consumptive use 0.00
    # FTP consumptive use.1 0.00
    # FTP consumptive use 0.00
# FTP total s-s withdrawals plus deliveries -
    # FTP deliveries from public supply 0.00
    # FTP total s-s withdrawals.2 -
        # FTP total s-s withdrawals.1 -
        # FTP total s-s withdrawals 0.00
            # FTP total s-s withdrawals surface 0.00
                # FTP s-s surface-water withdrawals.1 0.00
                # FTP s-s surface-water withdrawals 0.00
            # FTP total s-s withdrawals groundwater -
                # FTP s-s groundwater withdrawals.1 -
                # FTP s-s groundwater withdrawals 0.00

# TTP number of facilities -
# TTP reclaimed wastewater -
# TTP power generated 7.72
# TTP total consumptive use 0.00
    # TTP consumptive use.1 0.00
    # TTP consumptive use 0.00
# TTP total s-s withdrawals plus deliveries -
    # TTP total s-s withdrawals total -
            # TTP total s-s withdrawals.1 -
            # TTP total s-s withdrawals -
            # TTP total s-s withdrawals surface -
                # TTP s-s surface-water withdrawals.1 -
                # TTP s-s surface-water withdrawals -
            # TTP total s-s withdrawals groundwater -
                # TTP s-s groundwater withdrawals.1 -
                # TTP s-s groundwater withdrawals 0.0

# I number of facilities -
# I reclaimed wastewater 0.00
# I total consumptive use 2.53
    # I consumptive use.1 0.14
    # I consumptive use 2.39
# I total s-s withdrawals plus deliveries 10.12
    # I deliveries from public supply 6.24
    # I total s-s withdrawals.2 3.88
        # I total s-s withdrawals.1 0.61
        # I total s-s withdrawals 3.27
            # I total s-s withdrawals surface 0.62
                # I s-s surface-water withdrawals.1 0.61
                # I s-s surface-water withdrawals 0.01
            # I total s-s withdrawals groundwater 3.26
                # I s-s groundwater withdrawals.1 0.0
                # I s-s groundwater withdrawals 3.26

# C reclaimed wastewater -
# C total consumptive use -
    # C consumptive use.1 -
    # C consumptive use 11.67
# C total s-s withdrawals plus deliveries -
    # C deliveries from public supply 44.87
    # C total s-s withdrawals.2 -
        # C total s-s withdrawals.1 -
        # C total s-s withdrawals 1.19
            # C total s-s withdrawals surface -
                # C s-s surface-water withdrawals.1 -
                # C s-s surface-water withdrawals 0.10
            # C total s-s withdrawals groundwater -
                # C s-s groundwater withdrawals.1 -
                # C s-s groundwater withdrawals 1.09

# D reclaimed wastewater -
# D s-s population 42.05
# D per capita use s-s 75
# D total consumptive use -
# D per capita use public-supplied 103
    # D consumptive use.1 -
    # D consumptive use 31.76
# D total s-s withdrawals plus deliveries 122.16
    # D deliveries from public supply 119.010
    # D total s-s withdrawals.2 -
        # D total s-s withdrawals.1 -
        # D total s-s withdrawals 3.15
            # D total s-s withdrawals surface -
                # D s-s surface-water withdrawals.1 -
                # D s-s surface-water withdrawals 0.25
            # D total s-s withdrawals groundwater -
                # D s-s groundwater withdrawals.1 -
                # D s-s groundwater withdrawals 2.9

# PS number of facilities -
# PS reclaimed wastewater -
# PS per capita use -
# PS public use and losses -
# PS total deliveries 170.12
    # PS deliveries to thermoelectric 0.00
    # PS deliveries to industrial 6.24
    # PS deliveries to commercial 44.87
    # PS deliveries to domestic 119.01
# PS total s-s withdrawals total -
    # PS total s-s withdrawals.1 -
    # PS total s-s withdrawals 195.1
        # PS total s-s withdrawals surface -
            # PS s-s surface-water withdrawals.1 -
            # PS s-s surface-water withdrawals 163.52
        # PS total s-s withdrawals groundwater -
            # PS s-s groundwater withdrawals.1 -
            # PS s-s groundwater withdrawals 31.58
# PS total population served 1153.11
    # PS population served by surface 967.160
    # PS population served by groundwater 185.950

# Total Population 1195.16
# year 1985
# county_nm Alameda
# county_cd 1
# state_name California
# state_cd 6