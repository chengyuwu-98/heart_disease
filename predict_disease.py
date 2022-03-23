import os
import requests
import numpy as np
import pandas as pd

my_data = {
        "BMI": {0: 28.87},
        "Smoking": {0: "Yes"},
        "AlcoholDrinking": {0: "No" },
        "Stroke": {0: "Yes"},
        "PhysicalHealth": {0: 6.0},
        "MentalHealth": {0: 0.0},
        "DiffWalking" : {0: "Yes"},
        "Sex":{0:"Female"},
        "AgeCategory": {0:"75-79"},
        "Race":{0: "Black"},
        "Diabetic":{0: "No"},
        "PhysicalActivity":{0:"No"},
        "GenHealth":{0: "Fair"},
        "SleepTime":{0:12.0},
        "Asthma":{0:"Yes"},
        "KidneyDisease":{0:"Yes"},
        "SkinCancer":{0:"Yes"},

    }
df = pd.DataFrame(data=my_data)


def create_tf_serving_json(data):
  return {'inputs': {name: data[name].tolist() for name in data.keys()} if isinstance(data, dict) else data.tolist()}

def score_model(dataset):
  url = 'https://adb-8196151818591343.3.azuredatabricks.net/model/heart_disease/1/invocations'
  headers = {'Authorization': f'Bearer {os.environ.get("DATABRICKS_TOKEN")}'}
  data_json = dataset.to_dict(orient='split') if isinstance(dataset, pd.DataFrame) else create_tf_serving_json(dataset)
  response = requests.request(method='POST', headers=headers, url=url, json=data_json)
  if response.status_code != 200:
    raise Exception(f'Request failed with status {response.status_code}, {response.text}')
  return response.json()




if __name__ == "__main__":
    print(score_model(df))
