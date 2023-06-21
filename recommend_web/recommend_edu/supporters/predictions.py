import pickle
import imblearn
import numpy as np

with open('model_preffered.pkl', 'rb') as f:
    model_preferred = pickle.load(f)

with open('model_responsibilities.pkl', 'rb') as f:
    model_responsibilities = pickle.load(f)

models = {"Model Preferred Skills": model_preferred,
          "Model trained on responsibilities": model_responsibilities
          }

skills = ['speak fluently idiomatically write communicate create english']

for key, model in models.items():
    print(key, model.predict(skills))
