import streamlit as st
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 


st.write('''
# Application  pour la prediction de prix des maisons
cette application va nous permettre de prédire le prix des differentes maisons publiées sur maMaison.sn
''')

st.sidebar.header("les parametres d'entrees")

def user_input():
    LotFrontage=st.sidebar.slider('LotFrontage',4.3,7.9,5.3)
    OverallQual=st.sidebar.slider(' OverallQual',2.0,4.4,3.3)
    YearBuilt=st.sidebar.slider(' YearBuilt',1.0,6.9,2.3)
    YearRemodAdd=st.sidebar.slider(' YearRemodAdd',0.1,2.5,5.3)
    data={'LotFrontage':LotFrontage,
          'OverallQual':OverallQual,
          'YearBuil':YearBuil,
          'YearRemodAdd':YearRemodAdd
         }
       
        

        
         
df=user_input() 


st.subheader('on veut trouver les categories de cette prediction')
st.write(df)
            
            
            
            
            
            
            
            
            
            
            
            
        
    
          
    



    
