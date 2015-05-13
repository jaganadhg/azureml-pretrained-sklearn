#!/usr/bin/env python
import pickle
import sys
import numpy as np

sys.path.append(r".\\Script Bundle\\")

model = pickle.load(open(r".\\Script Bundle\\boston_lm.py","rb"))

def predict_hp(data):
	"""
	Predict house price
	"""
	price = model.predict(np.array(data))
	return price

if __name__ == "__main__":
	data = [0.00632,18,2.31,0,0.538,6.575,65.2,4.0900,1,296,15.3,396.90,4.98]
        p = predict_hp(data)
	print p
