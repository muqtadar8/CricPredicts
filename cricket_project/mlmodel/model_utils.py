import joblib
import pickle
import numpy as np
import sklearn
# Load the trained model and scaler
# lin = joblib.load(r'C:\Users\Shaji\cricpro\cricket_project\model.pkl')
# sc = joblib.load(r'C:\Users\Shaji\cricpro\cricket_project\sc.pkl')


def prediction_model(f1,f2,f3,f4,f5):
    x = np.array([[f1,f2,f3,f4,f5]])
    model = pickle.load(open('model.sav', 'rb'))
    sc = pickle.load(open('sc.sav', 'rb'))
    x = sc.transform(x)

    result = model.predict(x)
    return result 
