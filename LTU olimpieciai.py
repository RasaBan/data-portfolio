import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df= pd.read_csv("Olimpines_pagal_atstova.tsv", sep="\t")
df.info()
print(df.head())
print("-------Tik LT duomenys---------")
#Tik LTU duomenys:
df_LT=df[df["Trigram"]== "LTU"]
# df_LT.to_csv("LTUolimp.csv")
# print(df_LT.info())
# print(df_LT.Year.head())
# print(df_LT.Year.tail())
# print("------------")
# # kiek viso medaliu laimeta, + pasiskirstymas
# print("====kiek viso medaliu laimeta=======")
# print(df_LT[["Gold", "Silver", "Bronze", "Total"]].sum(axis=0, skipna=True))
# print("======pasiskirstymas=======")
# Gold = df_LT["Gold"].sum()
# Silver = df_LT["Silver"].sum()
# Bronze = df_LT["Bronze"].sum()
# proportions = [Gold, Silver, Bronze]
# plt.pie(proportions, labels = ['Gold', 'Silver', 'Bronze'], autopct = '%1.2f%%')
# plt.show()
# # print(df_LT[ "Total"].sum(axis=0, skipna=True))
# print(df_LT[["Gold", "Silver", "Bronze"]].sum(axis=0, skipna=True).to_frame()*100/df_LT[ "Total"].sum(axis=0, skipna=True))
#
# # metai kada laimeti medaliai
# print("===metai kada laimeta========")
# df_LT_pagal_metus = df_LT.groupby("Year").sum().drop("Rank", axis=1)
# print(df_LT_pagal_metus[df_LT_pagal_metus["Total"] > 0])
# df_LT_pagal_metus[df_LT_pagal_metus["Total"] > 0].plot(kind="bar")
# plt.show()
# # kokiuose sezonuose("Event") kokie medaliai laimeti
# print("======= medaliai pagal sezona ===========")
# df_LT_pagal_sezona = df_LT.groupby("Event").sum().drop(df_LT[["Rank", "Year"]], axis=1)
# print(df_LT_pagal_sezona)
# # kokiose rungtyse laimeti medaliai ir kiek (kokia sporto saka sekmingiausia)
# print("---------Sporto sakos kuriose laimeta------")
# df_LT_pagal_rungti = df_LT.groupby(["Sport"]).sum().drop(df_LT[["Rank", "Year"]], axis=1)
# print(df_LT_pagal_rungti[df_LT_pagal_rungti["Total"] > 0])
# print("------Sporto saku TOP 5----")
# print(df_LT_pagal_rungti.nlargest(5, ['Gold','Total']))
# # medaliu pasiskirstymas pagal lyti
# print("---------- Medaliai pagal lyti ----------")
# df_LT_pagal_lyti = df_LT.groupby("Gender").sum().drop(df_LT[["Rank", "Year"]], axis=1)
# print(df_LT_pagal_lyti[df_LT_pagal_lyti["Total"] > 0])
# # vidutinis amzius laimetu medaliu
# print("===amziaus vidurkiai========")
# df_LT2 = df_LT[df_LT.Age != "None"]
# df_LT2.Age = pd.to_numeric(df_LT2.Age)
# print(df_LT2.groupby("Gold").mean().Age)
# print(df_LT2.groupby("Silver").mean().Age)
# print(df_LT2.groupby("Bronze").mean().Age)
# print(df_LT2.groupby("Total").mean().Age)
#
# print("--------Atletai laimeje daugiausiai medaliu--------")
# df_LT_pagal_atstova = df_LT.groupby(["Athlete","Sport"]).sum().drop(df_LT[["Rank", "Year"]], axis=1)
# print(df_LT_pagal_atstova[df_LT_pagal_atstova["Total"] > 0])
# df_LT_pagal_atstova.info()
# print("--- LT Olimpieciu TOP 5----")
# print(df_LT_pagal_atstova.nlargest(5, ["Gold",'Total']))
# # Visos salys
# # sukurti nauja isfiltruota lentele, kuria sudaro:
# # # atskiros salys susumavus ju duomenis
# print("--------Salys-------------")
# df_salys2=df.groupby("Country").sum()
# print(len(df_salys2.index))
# print("-------palyginimas su visomis salimis --------")
# print("-------visu saliu medaliu suma---------")
# print(df[["Gold","Silver", "Bronze", "Total"]].sum())
# print("-------- LT tarp kitu saliu per paskutinius 20 metu-------")
# df_metai = df[df.Year >= 1992]
# df_group_sal= df_metai.groupby("Country").sum().drop(df_metai[["Rank", "Year"]], axis=1)
# print(len(df_group_sal.index))
# # print(df_group_sal)
# print("------Pagal auksa----")
# auksas= df_group_sal.nlargest(55,["Gold"]).drop(df_group_sal[["Silver", "Bronze", "Total"]], axis=1)
# auksas = auksas.reset_index(level="Country")
# print(auksas.tail(3))
# print("------Pagal sidabra----")
# sidabras = df_group_sal.nlargest(60,["Silver"]).drop(df_group_sal[["Gold", "Bronze", "Total"]], axis=1)
# sidabras = sidabras.reset_index(level="Country")
# print(sidabras.tail(3))
# print("------Pagal bronza----")
# bronza = df_group_sal.nlargest(30,["Bronze"]).drop(df_group_sal[["Silver", "Gold", "Total"]], axis=1)
# bronza = bronza.reset_index(level="Country")
# print(bronza.tail(3))
# print("------Pagal bendra medaliu kieki----")
# visi = df_group_sal.nlargest(40,["Total"]).drop(df_group_sal[["Silver", "Bronze", "Gold"]], axis=1)
# visi = visi.reset_index(level="Country")
# print(visi.tail(3))
# print("===== log regresija ==========")
# print("======= tikimybe laimeti auksa=====")
# df_LT92= df_LT[df_LT.Year >= 1992][["Year", "Rank", "Gold", "Silver", "Bronze", "Total"]]
# xTrain, xTest, yTrain, yTest = train_test_split(df_LT92.drop(["Gold"], axis=1), df_LT92["Gold"], test_size = 0.2)
# logReg = LogisticRegression()
# logReg.fit(xTrain, yTrain)
# print(logReg.score(xTest, yTest))
# print("===== tikimybe laimeti sidabra======")
# xTrain, xTest, yTrain, yTest = train_test_split(df_LT92.drop(["Silver"], axis=1), df_LT92["Silver"], test_size = 0.2)
# logReg = LogisticRegression()
# logReg.fit(xTrain, yTrain)
# print(logReg.score(xTest, yTest))
# print("====== tikimybe laimeti bronza========")
# xTrain, xTest, yTrain, yTest = train_test_split(df_LT92.drop(["Bronze"], axis=1), df_LT92["Bronze"], test_size = 0.2)
# logReg = LogisticRegression()
# logReg.fit(xTrain, yTrain)
# print(logReg.score(xTest, yTest))

print(df.loc[df["Athlete"]== "Jasikevicius,Sarunas"])
print(df.loc[df["Athlete"]== "Zadneprovskis,Andrejus"])
print(df.loc[df["Athlete"]== "Gudzineviciute,Daina"])
print(df.loc[df["Athlete"]== "Krupeckaite,Simona"])

