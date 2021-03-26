#!/usr/bin/env python
# coding: utf-8

# In[21]:


import streamlit as st
import numpy as np
import pandas as pd
import datetime


# In[22]:


st.set_page_config('COPEDICAPP','https://pbs.twimg.com/profile_images/1309527192381067270/6zbTWN-M.jpg','wide')


# In[23]:


st.title('Projecte La Marató - COPEDICAT') # TITOL API


# In[24]:


# CALENDARIS DATES
data = st.sidebar.date_input("Data d'avui")
born = st.sidebar.date_input("Data naixement pacient")


# In[25]:


id_pacient = st.text_input('ID del/la pacient', 'ID XXXXXX')


# In[26]:


# SOCIAL
st.header("Paràmetres socials")
left_column, right_column = st.beta_columns(2)
sport = left_column.radio("Practica esport?",['Si','No'])
sympt_epi = left_column.radio("A casa hi ha algú amb símptomes?",['Si','No'])
housemembers_symp = left_column.radio("Qui té símptomes a casa?",['Pare','Mare','Germà/na','Avi/a','Altres'])
home_confirmed = right_column.radio("COVID confimat a casa?",['Si','No'])
school_sympt = right_column.radio("A l'escola hi ha algú amb símptomes?",['Si','No'])
school_confirmed = right_column.radio("COVID confirmat a l'escola?",['Si','No'])


# In[27]:


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


# In[28]:


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


# In[29]:



dades_pacient = [data,born,sport,sympt_epi,housemembers_symp,home_confirmed,school_sympt,school_confirmed,fever,highest_fever,ini_fever,end_fever,tos,cough_first,crup,crup_first,disfonia,disfonia_first,resp,resp_first,tachypnea,tachypnea_first,ausc,ausc_first,wheezing,crackles,odyno,odyno_first,nasal,nasal_first,fatiga,fatiga_first,headache,headache_first,conj,conj_first,ocular,ocular_first,gi_symp,gi_first,abd,vomit,diarrea,skin,skin_first,rash,infla_peri,infla_oral,adeno,adeno_first,hepato,hepato_first,spleno,spleno_first,hemo,hemo_first,irriti,irriti_first,neuro,neuro_first,confu,seizures,nuch,hypotonia,paral,shock,shock_first,taste,taste_first,smell,smell_first,comorb,cardio,hipert,com_resp,asma]


# In[30]:


print(dades_pacient)


# In[31]:


for ss in range(len(dades_pacient)):
    if dades_pacient[ss] == 'Si':
        dades_pacient[ss] = 1
    if dades_pacient[ss] == 'No':
        dades_pacient[ss] = 0


# In[32]:


print(dades_pacient)


# In[33]:


st.header("Resultat")
# SOM-HI
button = st.button('COVID?')
if not button:
    st.stop()


# In[34]:


st.markdown("""
<style>
.big-font {
    font-size:40px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">'+ str(id_pacient)+' té un 90% de probabilitat de tenir COVID </p>', unsafe_allow_html=True)
st.write("Aquí va la gràfica maca dels bitsbitsbits!")


# In[37]:


# dictionary of lists 
dict = {'id': [id_pacient],'recruit_date':[dades_pacient[0]],'date_of_birth':[dades_pacient[1]],'sports':[dades_pacient[2]],'sympt_epi':[dades_pacient[3]],'housemember_symptoms':[dades_pacient[4]],'home_confirmed':[dades_pacient[5]],'school_symptoms':[dades_pacient[6]],'school_confirmed':[dades_pacient[7]],'fever':[dades_pacient[8]],'highest_fever':[dades_pacient[9]],'date_fever':[dades_pacient[10]],'end_fever':[dades_pacient[11]],'tos':[dades_pacient[12]],'cough_first':[dades_pacient[13]],'crup':[dades_pacient[14]],'crup_first':[dades_pacient[15]],'dysphonia':[dades_pacient[16]],'disfonia_first':[dades_pacient[17]],'resp':[dades_pacient[18]],'dyspnea_first':[dades_pacient[19]],'tachypnea':[dades_pacient[20]],'tachypnea_first':[dades_pacient[21]],'ausc_resp':[dades_pacient[22]],'auscult_first':[dades_pacient[23]],'wheezing':[dades_pacient[24]],'crackles':[dades_pacient[25]],'odynophagia':[dades_pacient[26]],'odynophagia_first':[dades_pacient[27]],'nasal_congestion':[dades_pacient[28]],'nasal_first':[dades_pacient[29]],'fatiga':[dades_pacient[30]],'fatigue_first':[dades_pacient[31]],'headache':[dades_pacient[32]],'headache_first':[dades_pacient[33]],'conjuntivitis':[dades_pacient[34]],'conj_first':[dades_pacient[35]],'ocular_pain':[dades_pacient[36]],'ocular_first':[dades_pacient[37]],'gi_symptoms':[dades_pacient[38]],'gi_first':[dades_pacient[39]],'abdominal_pain':[dades_pacient[40]],'vomiting':[dades_pacient[41]],'dyarrea':[dades_pacient[42]],'dermatologic':[dades_pacient[43]],'skin_first':[dades_pacient[44]],'rash':[dades_pacient[45]],'inflam_periferic':[dades_pacient[46]],'inflam_oral':[dades_pacient[47]],'adenopathies':[dades_pacient[48]],'lymph_first':[dades_pacient[49]],'hepato':[dades_pacient[50]],'hepato_first':[dades_pacient[51]],'splenomegaly':[dades_pacient[52]],'spleno_first':[dades_pacient[53]],'hemorrhagies':[dades_pacient[54]],'hemorr_first':[dades_pacient[55]],'irritability':[dades_pacient[56]],'irritability_first':[dades_pacient[57]],'neuro':[dades_pacient[58]],'neuro_first':[dades_pacient[59]],'confusion':[dades_pacient[60]],'seizures':[dades_pacient[61]],'nuchal_stiffness':[dades_pacient[62]],'hypotonia':[dades_pacient[63]],'peripheral_paralysis':[dades_pacient[64]],'shock':[dades_pacient[65]],'shock_first':[dades_pacient[66]],'taste_smell':[dades_pacient[67]],'taste_first':[dades_pacient[68]],'smell':[dades_pacient[69]],'smell_first':[dades_pacient[70]],'comorbi_binary':[dades_pacient[71]],'cardiopathy':[dades_pacient[72]],'hypertension':[dades_pacient[73]],'pulmonar_disease':[dades_pacient[74]],'asma':[dades_pacient[75]]} 
     
df = pd.DataFrame(dict)
import base64 
# saving the dataframe
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="new_data.csv">Descarrega fitxer csv</a>'
    return href
st.markdown(get_table_download_link(df), unsafe_allow_html=True)


# In[ ]:




