import tensorflow as tf
import pandas as pd
import requests
import json
import base64
import random

df = pd.read_csv("data/diabetes_prediction.csv")
df.pop("diabetes")

columns = df.columns.values
rand = random.randint(0, len(columns))

features = df.values[rand]

inputs = {key: value for key, value in zip(columns, features)}
inputs

def string_feature(value):
    return tf.train.Feature(
        bytes_list=tf.train.BytesList(
            value=[bytes(value, "utf-8")]
        ),
    )
    
def float_feature(value):
    return tf.train.Feature(
        float_list=tf.train.FloatList(
            value=[value]
        ),
    )
    
def int_feature(value):
    return tf.train.Feature(
        int64_list=tf.train.Int64List(
            value=[value]
        ),
    )

def prepare_json(inputs: dict):
    feature_spec = dict()
    
    for keys, values in inputs.items():
        if isinstance(values, float):
            feature_spec[keys] = float_feature(values)
        elif isinstance(values, int):
            feature_spec[keys] = int_feature(values)
        elif isinstance(values, str):
            feature_spec[keys] = string_feature(values)
            
    example = tf.train.Example(
        features=tf.train.Features(feature=feature_spec)
    ).SerializeToString()
        
    result = [
        {
            "examples": {
                "b64": base64.b64encode(example).decode()
            }
        }
    ]
    
    return json.dumps({
        "signature_name": "serving_default",
        "instances": result,
    })

def make_predictions(inputs):
    json_data = prepare_json(inputs)
    
    endpoint = "https://model-diabetes-production.up.railway.app/v1/models/diabetes-model:predict"
    response = requests.post(endpoint, data=json_data)

    prediction = response.json()["predictions"][0][0]
    
    if prediction < 0.6:
        return "Normal"
    else:
        return "Diabetes"
    

print(make_predictions(inputs))