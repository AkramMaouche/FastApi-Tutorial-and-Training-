import uvicorn 
from fastapi import FastAPI 


app =  FastAPI()

@app.get('/')
def index(): 
    return {
        'message': 'Hello world'
    }

@app.get('/Welcome')
def welcome(name :str): 
    return f'Hello {name}, nice to meet you'



if __name__ =='__main__': 
    uvicorn.run(app, host ='127.0.0.1',port=8000 )

