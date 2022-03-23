# heart_disease

## Project description

This project uses AutoML in databricks to generate machine learning models to predict whether a candidate will have a heart disease using features such as BMI, Smoking, Stroke, Asthma, PhysicalHealth etc. 


## MLFLOW API
`export MLFLOW_TRACKING_URI=databricks`

`export DATABRICKS_TOKEN=<token>`

see all the registed models in databricks
`python model_list.py`

download models from databricks
`python model_download.py`

## Result show

<img width="711" alt="1648063716(1)" src="https://user-images.githubusercontent.com/76429734/159788525-4b419065-6567-4785-a458-8de7da7eb0c5.png">

<img width="698" alt="1648063745(1)" src="https://user-images.githubusercontent.com/76429734/159788556-b4216839-f299-4cbd-8afa-cfa166b352f1.png">
