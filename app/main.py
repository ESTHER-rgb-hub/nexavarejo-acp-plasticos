from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, EmailStr

app = FastAPI(title="NexaVarejo API", version="1.0.0")

# Disponibiliza todas as telas HTML da pasta static
app.mount("/static", StaticFiles(directory="static"), name="static")

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

@app.get("/")
def read_root():
    return FileResponse("static/login.html")

@app.get("/api/health")
def health_check():
    return {"status": "online", "sistema": "NexaVarejo - ACP Plásticos"}

@app.post("/login")
def login(user: UserLogin):
    if user.email == "operador.fabbri@acpplasticos.com.br" and user.senha == "12345678":
        return {"access_token": "token_jwt_ficticio_sucesso", "token_type": "bearer", "perfil": "producao"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
