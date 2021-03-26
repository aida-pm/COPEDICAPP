#!/usr/bin/env python
# coding: utf-8

# In[96]:


import streamlit as st
import numpy as np
import pandas as pd
import datetime


# In[97]:


st.set_page_config('COPEDICAPP','https://pbs.twimg.com/profile_images/1309527192381067270/6zbTWN-M.jpg','wide')


# In[98]:


st.title('Projecte La Marató - COPEDICAT') # TITOL API


# In[99]:


#dades = pd.read_csv('COPEDICATClinicSympt_DATA_2021-03-15_1112.csv') # LLEGIM LES DADES DE L'EXCEL
#vec_part = dades.participant_id # ID PARTICIPANT


# In[100]:


# st.write("Pacient:"+str(vec_part[0])) # ESCRIC ID PARTICIPANT 1 - AIXÒ ÉS USELESS PERÒ EM FEIA ILU


# In[101]:


# CALENDARIS DATES
data = st.sidebar.date_input("Data d'avui")
born = st.sidebar.date_input("Data naixement pacient")


# In[102]:


id_pacient = st.text_input('ID del/la pacient', 'ID XXXXXX')


# In[103]:


# SOCIAL
st.header("Paràmetres socials")
left_column, right_column = st.beta_columns(2)
sport = left_column.radio("Practica esport?",['Si','No'])
sympt_epi = left_column.radio("A casa hi ha algú amb símptomes?",['Si','No'])
housemembers_symp = left_column.radio("Qui té símptomes a casa?",['Pare','Mare','Germà/na','Avi/a','Altres'])
home_confirmed = right_column.radio("COVID confimat a casa?",['Si','No'])
school_sympt = right_column.radio("A l'escola hi ha algú amb símptomes?",['Si','No'])
school_confirmed = right_column.radio("COVID confirmat a l'escola?",['Si','No'])


# In[104]:


# SIMPTOMES
st.header("Símptomes")
left_column, right_column = st.beta_columns(2)
fever = left_column.radio("Té febre?",['Si','No'])
highest_fever = left_column.radio("Valor màxim de febre",['37ºC a < 38ºC','Entre 38ºC i 39ºC','> 39ºC'])
ini_fever = right_column.date_input("Data inici febre")
end_fever = right_column.date_input("Data final febre")

tos = left_column.radio("Té tos?",['Si','No'])
cough_first = left_column.radio("Va presentar tos durant les primeres 24h?",['Si','No'])

crup = right_column.radio("Té diftèria?",['Si','No','No Consta'])
crup_first = right_column.radio("Va presentar diftèria durant les primeres 24h?",['Si','No'])

disfonia = left_column.radio("Té disfonia?",['Si','No','No Consta'])
disfonia_first = left_column.radio("Va presentar disfonia durant les primeres 24h?",['Si','No'])

resp = right_column.radio("Té dispnea?",['Si','No','No Consta'])
resp_first = right_column.radio("Va presentar dispnea durant les primeres 24h?",['Si','No'])

tachypnea = left_column.radio("Té taquipnea?",['Si','No','No Consta'])
tachypnea_first = left_column.radio("Va presentar taquipnea durant les primeres 24h?",['Si','No'])

ausc = right_column.radio("És l'auscultació patològica?",['Si','No'])
ausc_first = right_column.radio("Va presentar auscultació patològica durant les primeres 24h?",['Si','No'])

wheezing = left_column.radio("És l'auscultació sibilant?",['Si','No'])
crackles = left_column.radio("És l'auscultació crepitant?",['Si','No'])

odyno = right_column.radio("Té odinofàgia?",['Si','No','No Consta'])
odyno_first = right_column.radio("Va presentar odinofàgia durant les primeres 24h?",['Si','No'])

nasal = left_column.radio("Té congestió nasal?",['Si','No','No Consta'])
nasal_first = left_column.radio("Va presentar congestió nasal durant les primeres 24h?",['Si','No'])

fatiga = left_column.radio("Té fatiga?",['Si','No','No Consta'])
fatiga_first = right_column.radio("Va presentar fatiga durant les primeres 24h?",['Si','No'])

headache = right_column.radio("Té mal de cap?",['Si','No','No Consta'])
headache_first = right_column.radio("Va presentar mal de cap durant les primeres 24h?",['Si','No'])

conj = left_column.radio("Té conjuntivitis?",['Si','No','No Consta'])
conj_first = left_column.radio("Va presentar conjuntivitis durant les primeres 24h?",['Si','No'])

ocular = right_column.radio("Té dolor ocular?",['Si','No','No Consta'])
ocular_first = right_column.radio("Va presentar dolor ocular durant les primeres 24h?",['Si','No'])

gi_symp = left_column.radio("Té símptomes gastrointestinals?",['Si','No'])
gi_first = left_column.radio("Va presentar símptomes gastrointestinals durant les primeres 24h?",['Si','No'])

abd = right_column.radio("Té dolor abdominal?",['Si','No','No Consta'])
vomit = right_column.radio("Té vòmits?",['Si','No','No Consta'])
diarrea = right_column.radio("Té diarrea?",['Si','No','No Consta'])

skin = left_column.radio("Té símptomes dermatològics?",['Si','No'])
skin_first = left_column.radio("Va presentar símptomes dermatològics durant les primeres 24h?",['Si','No'])
rash = left_column.radio("Té erupcions cutànies?",['Si','No'])

infla_peri = right_column.radio("Té signes d'inflamació perifèrica?",['Si','No'])
infla_oral = right_column.radio("Té signes d'inflamació oral?",['Si','No'])

adeno = right_column.radio("Té limfadenopaties > 1cm?",['Si','No','No Consta'])
adeno_first = right_column.radio("Va presentar limfadenopaties > 1cm durant les primeres 24h?",['Si','No'])

hepato = left_column.radio("Té hepatomegalia?",['Si','No','No Consta'])
hepato_first = left_column.radio("Va presentar hepatomegalia durant les primeres 24h?",['Si','No'])

spleno = left_column.radio("Té esplenomegalia?",['Si','No','No Consta'])
spleno_first = left_column.radio("Va presentar esplenomegalia durant les primeres 24h?",['Si','No'])

hemo = right_column.radio("Té hemorràgies?",['Si','No','No Consta'])
hemo_first = right_column.radio("Va presentar hemorràgies durant les primeres 24h?",['Si','No'])

irriti = left_column.radio("Està irritable?",['Si','No','No Consta'])
irriti_first = left_column.radio("Va presentar irritabilitat durant les primeres 24h?",['Si','No'])

neuro = right_column.radio("Té símptomes neurològics?",['Si','No'])
neuro_first = right_column.radio("Va presentar símptomes neurològics durant les primeres 24h?",['Si','No'])
confu = right_column.radio("Presenta confusió?",['Si','No'])
seizures = right_column.radio("Té convulsions?",['Si','No'])

nuch = left_column.radio("Té rigidesa nucal?",['Si','No'])
hypotonia = left_column.radio("Té hipotònia?",['Si','No'])

paral = right_column.radio("Presenta paràlisi perifèrica?",['Si','No'])
shock = right_column.radio("Té símptomes de shock?",['Si','No'])
shock_first = right_column.radio("Va presentar símptomes de shock durant les primeres 24h?",['Si','No'])

taste = left_column.radio("Té alteració en el gust?",['Si','No'])
taste_first = left_column.radio("Va presentar símptomes d'alteració en el gust durant les primeres 24h?",['Si','No'])
smell = left_column.radio("Té alteració en l'olfacte?",['Si','No'])
smell_first = left_column.radio("Va presentar símptomes d'alteració en l'olfacte durant les primeres 24h?",['Si','No'])


# In[105]:


# Comorbiditats
st.header("Comorbiditats")
comorb = 'No'
cardio = 'No'
hipert = 'No'
com_resp = 'No'
asma = 'No'
if st.checkbox('Presenta comorbiditat'):
    comorb = 'Si'
    left_column, right_column = st.beta_columns(2)
    cardio = left_column.radio("Té alguna cardiopatia?",['Si','No'])
    hipert = left_column.radio("Té hipertensió?",['Si','No'])
    com_resp = right_column.radio("Té alguna malaltia pulmonar crònica?",['Si','No'])
    asma = right_column.radio("Té asma?",['Si','No'])


# In[106]:



dades_pacient = [data,born,sport,sympt_epi,housemembers_symp,home_confirmed,school_sympt,school_confirmed,fever,highest_fever,ini_fever,end_fever,tos,cough_first,disfonia,disfonia_first,resp,resp_first,tachypnea,tachypnea_first,ausc,ausc_first,wheezing,crackles,odyno,odyno_first,nasal,nasal_first,fatiga,fatiga_first,headache,headache_first,conj,conj_first,ocular,ocular_first,gi_symp,gi_first,abd,vomit,diarrea,skin,skin_first,rash,infla_peri,infla_oral,adeno,adeno_first,hepato,hepato_first,spleno,spleno_first,hemo,hemo_first,irriti,irriti_first,neuro,neuro_first,confu,seizures,nuch,hypotonia,paral,shock,shock_first,taste,taste_first,smell,smell_first,comorb,cardio,hipert,com_resp,asma]


# In[107]:


print(dades_pacient)


# In[108]:


for ss in range(len(dades_pacient)):
    if dades_pacient[ss] == 'Si':
        dades_pacient[ss] = 1
    if dades_pacient[ss] == 'No':
        dades_pacient[ss] = 0


# In[109]:


print(dades_pacient)


# In[112]:


st.header("Resultat")
# SOM-HI
button = st.button('COVID?')
if not button:
    st.stop()


# In[111]:


st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">'+ str(id_pacient)+' té un 90% de probabilitat de tenir COVID </p>', unsafe_allow_html=True)
st.write("Aquí va la gràfica maca dels bitsbitsbits!")


# In[ ]:





# In[ ]:




