#/generation of the DF, using pandas, with HF as a main parameter. 
#//in each observation (obsID). THe Hf is dependent or not dependent from ater parameter
#// such as age (no dependence), sex (no dependence), EF (slightly increasing with a slope 2 revers direction)
#// NYHA dependent of EF with noise
#//HF (HFpEF (EF>55, HYHA 1), HFmrEF(EF=<55,>40), HFrEF (EF=<40)
#HR dependend of HF
#//othe parameter, that will be consedered: mean, SD, assymmetry
#%%         
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs("output/plots",exist_ok=True)
# %%
def generate(n,a,b,c,d,e,f):   #//number of observations n=50 .. 5000, korrelation strangth with EF
    # a= 0.6 ..1 (nominal 0.8), 
    # b korrelation with Hb
    #c korrelation wich SV (stroke volume)
    #d korr wich BMI
    #e korrelation with BB
    #f korellation with Rhthmus
    Age=np.clip(np.random.normal(50,10,n),18,90).astype(int)#//generate age of n patients from 18 to 90 years, normal distribution
    Sex=np.random.choice(["M","F"],n)
    EF=70-Age*0.4+np.random.normal(0,5,n)#//correlation with age, empiric, with noise
    NYHA_score=(5-EF/15+np.random.normal(0,0.5,n))
    NYHA=np.clip(np.round(NYHA_score),1,4).astype(int)
    HF=np.where((EF>55)&(NYHA==1), "no HF",
                  np.where ((EF>55), "HFpEF",
                  np.where ((EF>40), "HFmrEF", "HFrEF")))
    HF = pd.Categorical(
    HF,
    categories=["no HF", "HFpEF", "HFmrEF", "HFrEF"],
    ordered=True
    )
    Hb=np.random.normal(7,0.6,n)
    EDV= np.random.normal (120, 20, n) # end diastolic volume
    SV=EDV*EF/100
    BMI=np.random.normal(22,1.5,n) 
    BB=np.random.choice(["mit BB", "ohne BB"],n)
    Rhythm=np.random.choice(["SR", "AF"], n)
    HR=75+(60-EF)*a+(70-EF)*c+d*(BMI-22)+(b*(7-Hb))-e*(np.where(BB=="mit BB",5,0).astype(float))+f*(np.where(Rhythm=="AF",10,0).astype(float))+np.random.normal(0,5,n) # HF empirisch, depending from EF, SV, Hb,
    df1 = pd.DataFrame({
"ObservID":range(1, n+1),#//n+1 besouse the py built to n-1
"Age":Age,
"Sex":Sex,
"EF":EF,
"NYHA":NYHA,
"HF":HF,
"Hb":Hb,
"HR":HR,
"SV":SV,
"BMI":BMI,
"BB":BB,
"Rhythm":Rhythm
})

    return df1
# df1=generate()
# print(df1)

