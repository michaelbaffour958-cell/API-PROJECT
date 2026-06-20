from fastapi import FastAPI
from activities.activities import router as activities_router
from registers.register import router as register_router
from fastapi import FastAPI,Depends,HTTPException,status
from sqlmodel import SQLModel,Session,Field,select,create_engine
from typing  import Annotated
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None

class Student(SQLModel,table=True):
    # name: str = Field(index=True, primary_key=True)
    # age: int  = Field(index=True)
    # price:int = Field()
    Student_id: str = Field(index =True, primary_key=True)
    name: str = Field()
    age: int = Field() 
    contact: str |None = Field(default = None)
    Email: str | None = Field(default = None)
    fees: int | None = Field(default = None)


    

sqlite_filename = "database.db"
sqlite_db_url = f"sqlite:///{sqlite_filename}"

connect_arg =  {"check_same_thread": False}
# connect our database to the app 
engine =create_engine(sqlite_db_url, connect_args=connect_arg)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def create_db():
     return SQLModel.metadata.create_all(engine)


app = FastAPI()

app.include_router(activities_router, prefix ="/activities")
app.include_router(register_router, prefix ='/registers')

@app.on_event("startup")
def main():
    create_db()

@app.get("/")
def main():
    return "home page"

@app.get('/')
async def root():
    return {'message': "Welcome to home"}

@app.post('/Student')
def create_post(product: Student,session:SessionDep):
    session.add(Student)
    session.commit()
    session.refresh(Student)
    return Student

@app.post('/product/{product_name}')
def get_product(product_name:str,session:SessionDep):
    data = session.get(Product,product_name)
    session.commit()
    session.refresh(data)
    return data





