from fastapi import FastAPI
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
patch_all()

app = FastAPI()

xray_recorder.begin_segment('FastAPITest')
@app.get("/")
def read_root():
    return{"Hello":"World"}

xray_recorder.end_segment()