from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Branch Created and Merged Successfully"}