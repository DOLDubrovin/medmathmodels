import streamlit as st
import matplotlib.pyplot as plt
from generatedDF import generate
st.title("Interactive HR Data Generator")
st.write(
    """
    This simulator generates synthetic patient datasets based on an assumed relationship 
    between heart rate and clinical variables. We hypothesize that heart rate can be 
    described by a multivariable regression model, 
    **HR = β₀ + β₁X₁ + β₂X₂ + ⋯ + βₙXₙ + ε**, 
    whose coefficients can be estimated and validated in future clinical studies. 
    The current implementation is intended for education, hypothesis generation, 
    and methodological development.
    """
)
n=st.slider("Number",50,5000,200)
a=st.slider("strength of the influence of the EF on the HR", 0.1, 0.5, 0.3, 0.1)#mi,max, startvalue,schritt
b=st.slider("strength of the influence of the Hb on the HR", 2.5, 10.0, 5.0, 0.1)
c=st.slider("strength of the influence of the SV on the HR", 0.3, 0.7, 0.5, 0.1)
d=st.slider("strength of the influence of the BMI/Gewicht on the HR",0.2, 0.6,0.4,0.1)
e=st.slider("strength of the influence of the BB THerapie",0.7,1.3,1.0,0.1)
f=st.slider("strength of the influence of the presence of AF", 0.7,1.3,0.1,0.1)
df1=generate(n,a,b,c,d,e,f)
# st.dataframe(df1.head(20))
st.dataframe(df1) # ?
st.write("Correlation EF-HR:", df1["EF"].corr(df1["HR"])) # ?
st.write("Correlation SV-HR:", df1["SV"].corr(df1["HR"]))
st.write("Correlation Hb-HR:", df1["Hb"].corr(df1["HR"]))
st.write("Correlation BMI-HR:", df1["BMI"].corr(df1["HR"]))
st.write("Correlation AGe-HR:", df1["Age"].corr(df1["HR"]))
# print(df1)
csv=df1.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download csv",
    data=csv,
    file_name="df1.csv",
    mime="text/csv"
)

plt.figure()
df1["Age"].hist(bins=10)
plt.xlabel("Age")
plt.ylabel("Number of observations")
plt.title("Distribution of the age")
plt.savefig("output/plots/age_hist.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()


plt.figure()
df1["Sex"].hist()
plt.xlabel("Sex")
plt.ylabel("Number of observations")
plt.title("Distribution of the sex")
plt.savefig("output/plots/sex_hist.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()


plt.figure()
df1["NYHA"].hist()
plt.xlabel("HYHA")
plt.ylabel("Number of observations")
plt.title("Distribution of the Patients by NYHA class")
plt.savefig("output/plots/NYHA_hist.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
order = ["no HF", "HFpEF", "HFmrEF", "HFrEF"]
counts = (
    df1["HF"]
    .value_counts()
    .reindex(order)
)
plt.bar(
    counts.index,
    counts.values,
    color="blue",
    width=0.5
)
plt.xlabel("heart failure Category")
plt.ylabel("Patients")
plt.title("Distribution of heart failure category")
plt.savefig("output/plots/HF_bar.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()




plt.figure()
df1.boxplot(column="HR", by="NYHA")
plt.xlabel("NYHA classes")
plt.ylabel("heart rate")
plt.title ("heart rate by NYHA classes")
plt.savefig("output/plots/hr_by_HYHA.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()


plt.figure()
df1.boxplot(column="HR", by="HF")
plt.xlabel("HF kind")
plt.ylabel("heart rate")
plt.title ("heart rate by HF kind")
plt.savefig("output/plots/hr_by_HF.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()



plt.figure()
df1.boxplot(column="HR", by="BB")
plt.xlabel("BB Therapie")
plt.ylabel("heart rate")
plt.title ("BB Therapie by HF kind")
plt.savefig("output/plots/bb_by_HF.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
df1.boxplot(column="HR", by="Rhythm")
plt.xlabel("Rhythm")
plt.ylabel("heart rate")
plt.title ("Rhythm by HF kind")
plt.savefig("output/plots/rhythm_by_HF.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
plt.scatter(df1["EF"], df1["HR"], alpha=0.6)
plt.xlabel("Ejection fraction (%)")
plt.ylabel("Heart rate")
plt.title("EF versus simulated heart rate")
plt.savefig("output/plots/ef_vs_hr.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
plt.scatter(df1["SV"], df1["HR"], alpha=0.6)
plt.xlabel("Stroke Volume")
plt.ylabel("Heart rate")
plt.title("SV versus simulated heart rate")
plt.savefig("output/plots/sv_vs_hr.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
plt.scatter(df1["BMI"], df1["HR"], alpha=0.6)
plt.xlabel("BMI")
plt.ylabel("Heart rate")
plt.title("BMI versus simulated heart rate")
plt.savefig("output/plots/bmi_vs_hr.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
plt.scatter(df1["Hb"], df1["HR"], alpha=0.6)
plt.xlabel("Hb, mg/dl")
plt.ylabel("Heart rate")
plt.title("Hb versus simulated heart rate")
plt.savefig("output/plots/hb_vs_hr.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()

plt.figure()
plt.scatter(df1["Age"], df1["HR"], alpha=0.6)
plt.xlabel("Age")
plt.ylabel("Heart rate")
plt.title("Age versus simulated heart rate")
plt.savefig("output/plots/Age_vs_hr.png", dpi=300, bbox_inches="tight")
st.pyplot(plt)
plt.close()
