from fastapi import FastAPI, Form, Depends
from fastapi.responses import JSONResponse
from database import session
from models import User
import sqhem
from typing import Annotated
from sqlalchemy.orm import Session



app = FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get('/users', tags=['users'])
async def users(user: sqhem.User, db: Session = Depends(get_db)) -> list[sqhem.User]:
    lst = db.query(User).all()
    return 

@app.get('/user/{id}', tags=['users'])
async def get_user(db: Session = Depends(get_db)):
    usr = db.query(User).get(id)
    print(usr, end='\n\n\n\n\n')
    if not usr:
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})
    return usr

@app.post('/user', tags=['users'])
async def create_user(user: sqhem.User, db: Session = Depends(get_db)):
    db.add(
        User(
            name=user.name,
            password=user.password
        )
    )
    db.flush()
    db.commit()
    return {'status': 'ok'}

