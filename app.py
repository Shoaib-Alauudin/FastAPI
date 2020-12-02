import uvicorn
from fastapi import FastAPI
from Bank_Note_Model import BankNote
import pickle

app = FastAPI()
load_file = open("classifier.pkl", "rb")
model_file = pickle.load(load_file)

@app.get("/")
def index():
    return {"message": 'Hello, Bank Note Authentication'}

@app.post("/predict")
def note_classifier(data:BankNote):
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]
    prediction = model_file.predict([[variance, skewness, curtosis, entropy]])

    if prediction[0]>0.5:
        prediction = "Fake Note"
    else:
        prediction = "Authentic Bank Note"
    return {"Prediction :":prediction}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)