from pydantic import BaseModel,Field,EmailStr

class PostSchema(BaseModel):
    id:int = Field(default=None)
    title:str = Field(default=None)
    content:str = Field(default=None)
    class Config:
        schema_extra={
            "post_demo":{
                "title":"some title about animals",
                "content":"some content"
            }
        }

class UserSchema(BaseModel):
    fullname:str = Field(default=None)
    email:str = Field(default=None)
    password:str = Field(default=None)
    class Config:
        schema_extra={
            "user_demo":{
                "fullname":"some title about animals",
                "email":"some@gmail.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    email:str = Field(default=None)
    password:str = Field(default=None)
    class Config:
        schema_extra={
            "login_demo":{
                "email":"some@gmail.com",
                "password":"123"
            }
        }