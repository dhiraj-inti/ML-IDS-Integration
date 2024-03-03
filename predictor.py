import pickle
import sys

def preprocess(X_New):
    X_New_ret = []
    for row in X_New:
        
        row = [0 if x=='Inactive' else x for x in row]
        row = [1 if x=='Active' else x for x in row]

        X_New_ret.append(row)
    
    return X_New_ret


with open('swat_2019.pkl','rb') as f:
    nn = pickle.load(f)

data = sys.argv[2:]
print(len(data))
data = [float(x) if x!='Active' and x!='Inactive' else x for x in data]

data = [data]
data = preprocess(data)

print(nn.predict(data))