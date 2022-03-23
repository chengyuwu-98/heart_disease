from fastapi import FastAPI
import uvicorn
import mlflow
import pandas as pd
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class Story(BaseModel):
    BMI: float
    Smoking: str
    AlcoholDrinking: str
    Stroke : str
    PhysicalHealth: float
    MentalHealth:float
    DiffWalking: str
    Sex:str
    AgeCategory: str
    Race: str
    Diabetic: str
    PhysicalActivity: str
    GenHealth: str
    SleepTime:float
    Asthma:str
    KidneyDisease: str
    SkinCancer: str

def predict(Story):
    print(f"Accepted payload: { Story.BMI,Story.Smoking,Story.Stroke,Story.PhysicalHealth,Story.DiffWalking,Story.Sex,Story.AgeCategory,Story.Race,Story.Diabetic,Story.GenHealth,Story.SleepTime,Story.Asthma,Story.KidneyDisease,Story.SkinCancer,Story.AlcoholDrinking,Story.PhysicalActivity}")
    my_data = {
        "BMI": {0: Story.BMI},
        "Smoking": {0: Story.Smoking},
        "Stroke": {0: Story.Stroke},
        "AlcoholDrinking" :{0:Story.AlcoholDrinking},
        "PhysicalActivity" :{0:Story.PhysicalActivity},
        "PhysicalHealth": {0: Story.PhysicalHealth},
        "MentalHealth": {0: Story.MentalHealth},
        "DiffWalking": {0: Story.DiffWalking},
        "Sex": {0: Story.Sex},
        "AgeCategory": {0: Story.AgeCategory},
        "Race": {0: Story.Race},
        "Diabetic": {0: Story.Diabetic},
        "GenHealth": {0: Story.GenHealth},
        "SleepTime": {0: Story.SleepTime},
         "Asthma": {0: Story.Asthma},
        "KidneyDisease": {0: Story.KidneyDisease},
        "SkinCancer": {0: Story.SkinCancer},
    }
    data = pd.DataFrame(data=my_data)
    result = loaded_model.predict(pd.DataFrame(data))
    return result


# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')
app = FastAPI()

@app.post("/predict")
async def predict_story(story: Story):
    print(f"predict_story accepted json payload: {story}")
    result = predict(story)
    print(f"The result is the following payload: {result}")
    payload = {"Prediect has heart disease or not": result.tolist()[0]}
    json_compatible_item_data = jsonable_encoder(payload)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def root():
    return {"message": "Welcome to use the heart dosease Detection application"}




if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')