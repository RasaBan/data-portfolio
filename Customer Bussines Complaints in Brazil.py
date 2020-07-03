import os, glob

import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\rasav\PycharmProjects\mokslai\Portfolio'
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)
all_df = pd.concat(df_from_each_file, ignore_index=True, sort=True)

all_df.rename(columns={'AnoCalendario': 'RefYear', 'DataArquivamento': 'ComplClosingDate', 'DataAbertura': 'ComplOpeningDate',
'CodigoRegiao':'RegionCode ', 'Regiao': 'RegionName', 'UF': 'State', 'strRazaoSocial': 'BLegalName',
'strNomeFantasia': 'BTradeName', 'Tipo': 'Type', 'NumeroCNPJ': 'BRegistrationNr',
'RadicalCNPJ': '8DigitsRegistrNr', 'RazaoSocialRFB':'BLegalName(FederalDB)',
'NomeFantasiaRFB': 'BTradeName(FederalDB)', 'CNAEPrincipal': 'BActivityCode',
'DescCNAEPrincipal': 'BActivityDescr', 'Atendida': 'IfComplResolved', 'CodigoAssunto':'ComplSubjectCode',
'DescricaoAssunto': 'ComplSubjectDescr', 'CodigoProblema': 'IssueCode', 'DescricaoProblema': 'IssueDescr',
'SexoConsumidor': 'ConsGender', 'FaixaEtariaConsumidor': 'ConsAgeRange', 'CEPConsumidor': 'ConsZipCode'},
inplace=True)
#
# all_df.info()
all_df[["ComplClosingDate", 'ComplOpeningDate']]= all_df[["ComplClosingDate", 'ComplOpeningDate']].apply(pd.to_datetime)
# #df[cols] = df[cols].applymap(np.int64)
all_df[['BRegistrationNr', '8DigitsRegistrNr', 'BActivityCode', 'IssueCode']]= all_df[['BRegistrationNr',
'8DigitsRegistrNr', 'BActivityCode', 'IssueCode']].astype("Int64")
#all_df.info()

print('---Complaints by year---')
print(all_df.groupby(['RefYear']).count()[['ComplSubjectCode']]. sort_values (by=['ComplSubjectCode'], ascending=False))
comp_by_year= all_df.groupby(['RefYear']).count()[['ComplSubjectCode']].plot(kind="bar")
plt.tight_layout()
plt.show()
print('------ About Business ------')
print('== Business legal names =======')
print(all_df.BLegalName.nunique())
print ('Business trade names ========')
print(all_df.BTradeName.nunique())
print('====== Business Legal names (FederalDB) ======')
print(all_df['BLegalName(FederalDB)'].nunique())
print('======= Business trade names (Federal DB) =====')
print(all_df['BTradeName(FederalDB)'].nunique())
#print(all_df.BActivityCode.nunique())

print('====== About consumers =======')
print('Gender: '+ str(all_df.ConsGender.value_counts()))
# Female = 637319
# Male = 559967
# NaN = 7815
# proportions = [Female, Male, NaN]
# plt.pie( proportions, labels=["Female", 'Male', 'NaN'], colors=['orange', 'blue', 'grey'],autopct = '%1.2f%%')
# plt.show()
all_df["ConsAgeRange"].replace({"entre 31 a 40 anos": "31 - 40 y", "entre 41 a 50 anos": "41 - 50 y", 'entre 21 a 30 anos':
 '21 - 30 y', 'entre 51 a 60 anos': '51 - 60 y', 'entre 61 a 70 anos': '61 - 70 y', 'mais de 70 anos': '> 70 y', 'até 20 anos':
 '< 20 y', 'Nao Informada': 'NaN', 'Nao se aplica': 'NaN' }, inplace=True)
print('=== Consumers by age range ======')
print('Age Range: '+ str(all_df.ConsAgeRange.value_counts()))
# all_df.ConsAgeRange.value_counts().plot(kind= "barh")
# plt.show()
print('==== General info about complaints =======')
print('==== Complaints by Age Range =========')
print(all_df.groupby(['ConsAgeRange']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'], ascending=False))
print('======= Complaints by Gender ============')
print(all_df.groupby(['ConsGender']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'], ascending=False))
print('==== TOP 10 States with Business complaints ======')
print(all_df.groupby(['State']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'], ascending=False).head(10))

print('==== Business ======')
print('==== TOP 10 Business with complaints ========')
print(all_df.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],\
                                                                                           ascending=False).head(10))
print('------- If complaint resolved------')
print(all_df.IfComplResolved.value_counts())
# Yes = 750698
# No = 45537
# proportions= [Yes, No]
# plt.pie(proportions, labels=['Yes', 'No'],autopct = '%1.2f%%' )
# plt.show()
print('==== Complaints per ref year and business (TOP 5) =====')

df2012= all_df.loc[all_df['RefYear'] == 2012]
#print(df2012)
print ('\033[1m'+'RefYear: 2012'+ '\033[0m')
print(df2012.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5))
df2012.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5).plot(kind='bar')
plt.title("Business complaints TOP5 2012")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()

df2013= all_df.loc[all_df['RefYear'] == 2013]
print ('\033[1m'+'RefYear: 2013'+'\033[0m' )
print(df2013.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5))
df2013.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5).plot(kind='bar')
plt.title("Business complaints TOP5 2013")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()

df2014= all_df.loc[all_df['RefYear'] == 2014]
print ('\033[1m'+'RefYear: 2014'+'\033[0m' )
print(df2014.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5))
df2014.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],\
                                                                                           ascending=False).head(5).plot(kind='bar')
plt.title("Business complaints TOP5 2014")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
df2015= all_df.loc[all_df['RefYear'] == 2015]
print ('\033[1m'+'RefYear: 2015'+'\033[0m' )
print(df2015.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],\
                                                                                           ascending=False).head(5))
df2015.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],\
                                                                                           ascending=False).head(5).plot(kind='bar')
plt.title("Business complaints TOP5 2015")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
df2016= all_df.loc[all_df['RefYear'] == 2016]
print ('\033[1m'+'RefYear: 2016'+ '\033[0m')
print(df2016.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5))
df2016.groupby(['BTradeName(FederalDB)']).count()[['ComplSubjectCode']].sort_values (by=['ComplSubjectCode'],
                                                                                           ascending=False).head(5).plot(kind='bar')
plt.title("Business complaints TOP5 2016")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
# sugruouota top5 stulpeline diagrama

# """gautusi viename viskas bet nelabai graziai stulpeliai isidelioja
# OI= [6510, 10049, 15269, 15381, 11216]
# CLARO= [4264, 4694, 3805, 6773, 4991]
# ITAUCARD_FINANCEIRA=[2135, 2121]
# RICARDO_ELETRO= [1891]
# SKY= [1745, 2715, 3285, 6440,3632]
# UNIDADE_DE_ELETRODOMESTICOS= [ 0,2351, 2269]
# SAMSUNG_DA_AMAZONIA= [0,0, 2029, 0, 2091]
# CEF_MATRIZ= [0, 0, 0, 3528, 2301]
# EST_UNIF= [0, 0, 0,3324]
# x= numpy.arange(len(OI))
# bar_width=0.15
# plt.bar(x,OI, width=bar_width, color="green", zorder=2)
# plt.bar(x+bar_width, CLARO, width=bar_width, color="red", zorder=2)
# plt.bar(x+bar_width*2, ITAUCARD_FINANCEIRA, width=bar_width, color="orange", zorder=2)
# plt.bar(x+bar_width*3, RICARDO_ELETRO, width=bar_width, color="purple", zorder=2)
# plt.bar(x+bar_width*4, SKY, width=bar_width, color="blue", zorder=2)
# plt.bar(x+bar_width*5, UNIDADE_DE_ELETRODOMESTICOS, width=bar_width, color="yellow", zorder=2)
# plt.bar(x+bar_width*6, SAMSUNG_DA_AMAZONIA, width=bar_width, color="black", zorder=2)
# plt.bar(x+bar_width*7, CEF_MATRIZ, width=bar_width, color="grey", zorder=2)
# plt.bar(x+bar_width*8, EST_UNIF, width=bar_width, color="pink", zorder=2)
# plt.xticks(x+bar_width*2, [2012,2013,2014,2015,2016])
# plt.title("Most complained businesses")
# plt.ylabel("Business")
# import matplotlib.patches as mpatches
# green_patch= mpatches.Patch(color="green", label = "OI")
# red_patch= mpatches.Patch(color="red", label = "CLARO")
# orange_patch= mpatches.Patch(color="orange", label = "ITAUCARD_FINANCEIRA")
# purple_patch= mpatches.Patch(color="purple", label = "RICARDO_ELETRO")
# blue_patch= mpatches.Patch(color="blue", label = "SKY")
# yellow_patch= mpatches.Patch(color="yellow", label = "UNIDADE_DE_ELETRODOMESTICOS")
# black_patch= mpatches.Patch(color="black", label = "SAMSUNG_DA_AMAZONIA")
# grey_patch= mpatches.Patch(color="grey", label = "CEF_MATRIZ")
# pink_patch= mpatches.Patch(color="pink", label = "EST_UNIF")
# plt.grid(axis="y")
# plt.show()"""


# ax = plt.subplot(111)
# def bar_plot(ax, data, total_width=0.8, legend=True):
#     n_bars = len(data)
#     bar_width = total_width / n_bars
#     bars = [2012, 2013, 2014, 2015, 2016]
#     if legend:
#         ax.legend(bars, data.keys())
#     fig, ax = plt.subplots()
# bar_plot(ax, data, total_width=.8, single_width=1)
# plt.show()
print('=== Resolved complaints by Business in 2012 (TOP5) ====') #TODO procentaliai
print(df2012[df2012.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().sort_values(ascending=False).head(5))

df2012[df2012.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().\
    sort_values(ascending=False).head(5).plot(kind="bar", color="green", zorder=2)
plt.grid()
plt.title("Resolved complaints 2012")
plt.xlabel("Business trade name")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
print('=== Resolved complaints by Business in 2013 (TOP5) ====')
print(df2013[df2013.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().sort_values(ascending=False).head(5))

df2013[df2013.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().\
    sort_values(ascending=False).head(5).plot(kind="bar", color="green", zorder=2)
plt.grid()
plt.title("Resolved complaints 2013")
plt.xlabel("Business trade name")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
print('=== Resolved complaints by Business in 2014 (TOP5) ====')
print(df2014[df2014.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().sort_values(ascending=False).head(5))
df2014[df2014.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().\
    sort_values(ascending=False).head(5).plot(kind="bar", color="green", zorder=2)
plt.grid()
plt.title("Resolved complaints 2014")
plt.xlabel("Business trade name")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
print('=== Resolved complaints by Business in 2015 (TOP5) ====')
print(df2015[df2015.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().sort_values(ascending=False).head(5))
df2015[df2015.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().\
    sort_values(ascending=False).head(5).plot(kind="bar", color="green", zorder=2)
plt.grid()
plt.title("Resolved complaints 2015")
plt.xlabel("Business trade name")
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()
print('=== Resolved complaints by Business in 2016 (TOP5) ====')
print(df2016[df2016.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().sort_values(ascending=False).head(5))
df2016[df2016.IfComplResolved== 'S'].groupby(['BTradeName(FederalDB)'])['IfComplResolved'].count().\
    sort_values(ascending=False).head(5).plot(kind="bar", color="green", zorder=2)
plt.grid()
plt.title("Resolved complaints 2016")
plt.xlabel("Business trade name", )
plt.ylabel("Complaints")
plt.tight_layout()
plt.show()