from fastapi import FastAPI
from pandas import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/xlsx")
async def excel():
    df = read_excel('C:/Users/MBO/PycharmProjects/NewFastAPI/data.xlsx')
    a2_value = df.loc[1, 'ID FILIERE']
    r = str(a2_value)
    ID = []
    TAILLE = int(df.size / df.columns.size)
    for i in range(TAILLE):
        ID.append(df.loc[i, 'ID FILIERE'])
    return 


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
