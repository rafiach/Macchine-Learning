import streamlit as st
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def prediksi(gender, age, ht, hd, sh, bmi, HbA1c, bg):

    if gender == 'Perempuan':
        gender = 0
    elif gender == 'Laki Laki':
        gender = 1
    elif gender == 'Lainnya':
        gender = 2
    else:
        gender = 3

    if sh == 'no info':
        sh = 0
    elif sh == 'current':
        sh = 1
    elif sh == 'ever':
        sh = 2
    elif sh == 'former':
        sh = 3
    elif sh == 'never':
        sh = 4
    elif sh == 'not current':
        sh = 5
    else:
        sh = 6
    
    if ht == 'Ya':
        ht = 1
    else:
        ht = 0
    
    if hd == 'Ya':
        hd = 1
    else:
        hd = 0

    X = np.array([[gender, age, ht, hd, sh, bmi, HbA1c, bg]])

    model = pickle.load(open('UAS/ID3_model.pkl', 'rb'))
    predict = model.predict(X)

    return predict

