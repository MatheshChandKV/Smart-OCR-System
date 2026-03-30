import numpy as np
import joblib
from torchvision import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
emnist=datasets.EMNIST(root='./data',split='balanced',train=True,download=True)
x=emnist.data.numpy()
y=emnist.targets.numpy()
print("Original shape:",x.shape,y.shape)
x=np.transpose(x,(0,2,1))
x=np.flip(x,axis=2)
print("After orientation fix:",x.shape,y.shape)
x=x / 255.0
x=x.reshape(x.shape[0],-1)
x,_,y,_=train_test_split(x,y,train_size=40000,stratify=y,random_state=42)
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=42)
model=SVC(kernel='rbf')
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("\nClassification Report:\n")
print(classification_report(y_test,y_pred))
joblib.dump(model, "emnist_model.pkl")