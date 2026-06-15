import streamlit as st
import matplotlib.pyplot as plt
from generatedDF import generate
st.title("Interactive HR Data Generator")
st.dataframe(df1.head(20))
st.download_button(...)
st.pyplot(...)
n=st.slider("Number",50,5000,200)
a=st.slider("strength of the influence of the EF on the HR", 0.6, 1.0,0.01)
df1=generate(n,a)
st.dataframe(df1) # ?
st.write("Correlation EF-HR:", df1["EF"].corr(df1["HR"])) # ?
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
plt.scatter(df1["EF"], df1["HR"], alpha=0.6)
plt.xlabel("Ejection fraction (%)")
plt.ylabel("Heart rate")
plt.title("EF versus simulated heart rate")
plt.savefig("output/plots/ef_vs_hr.png", dpi=300, bbox_inches="tight")
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
