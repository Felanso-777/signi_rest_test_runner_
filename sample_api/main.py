from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

# Simulated user
mock_user = {
    "email": "test@example.com",
    "password": "secret",
    "token": "mocked-access-token"
}

# Login request schema
class LoginRequest(BaseModel):
    email: str
    password: str

# GET /hello (client requirement)
@app.get("/hello")
def say_hello():
    return {"message": "Hello from my minimal REST API!"}

# POST /login (used in your YAML)
@app.post("/login")
def login(data: LoginRequest):
    if data.email == mock_user["email"] and data.password == mock_user["password"]:
        return {"access_token": mock_user["token"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# GET /profile (used in your YAML)
@app.get("/profile")
def get_profile(Authorization: str = Header(default=None)):
    if Authorization != f"Bearer {mock_user['token']}":
        raise HTTPException(status_code=403, detail="Unauthorized")

    return {
        "email": mock_user["email"],
        "name": "John Doe",
        "age": 30
    }
