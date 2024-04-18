import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import altair as alt

st.set_page_config(
    page_title="Job Salary Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


st.title('Analisa Hasil Pendapatan Pekerjaan di Bidang Data Science dan Identifikasi Faktor - Faktor yang Mempengaruhi Nilainya')

df = pd.read_csv('data/jobs_in_data.csv')

year = df.groupby('work_year').median(numeric_only=True)
year = year.rename_axis('work_year').reset_index()

st.subheader('Gaji Pekerjaan Data Science')
st.bar_chart(year, x='work_year', y='salary_in_usd')
st.caption('Tampilan di atas merupakan rata - rata gaji tiap tahunnya untuk pekerjaan di bidang Data Science mulai dari tahun 2020 hingga tahun 2023.')

# first plot with X and Y data
plt.plot(year['work_year'], year['salary'])
# second plot with x1 and y1 data
plt.plot(year['work_year'], year['salary_in_usd'])

plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
st.pyplot(plt)
st.caption('Dari sini kita bisa melihat, bahwa baik dari salary maupun salary_in_usd, keduanya mengalami peningkatan nilai untuk tiap tahunnya, dengan peningkatan paling besar ada diantara tahun 2021 - 2022.')

job_title = df[['job_title', 'salary_in_usd']]
job_title = job_title.groupby('job_title').median()
job_title = job_title.rename_axis('job_title').reset_index()
job_title = job_title.sort_values(by=['salary_in_usd'], ascending=False).head(10)
job_title

# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(job_title['job_title'], job_title['salary_in_usd'])

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

# Add x, y gridlines

# Show top values
ax.invert_yaxis()
st.pyplot(plt)
st.caption('Lalu dari tabel dan grafik diatas kita bisa menyimpulkan bahwa "Analytics Engineering Manager" merupakan pekerjaan dengan salary atau gaji tertinggi. Diikuti oleh "Data Science Tech Lead", "Managing Director Data Science", dst.')
