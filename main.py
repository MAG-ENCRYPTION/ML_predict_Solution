from fastapi import FastAPI
from pandas import *
from numpy import *
from unipath import Path
from production import *
import sklearn

app = FastAPI()
BASE_DIR = Path(__file__).parent.replace("\\", "/")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/xlsx")
async def excel():
    dico = {}
    df = read_excel(f"{BASE_DIR}/SSC.xlsx")
    DF = df.columns.tolist()
    retour = predict_KPI_with_date(df, 1, 12, 2023)
    dico[f'{DF[0]}'] = ExcelConvertDate(retour[0])
    for i in range(1, len(retour)):
        dico[f'{DF[i]}'] = retour[i]
    return dico


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
