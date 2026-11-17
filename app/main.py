from fastapi import FastAPI 
 
app = FastAPI(title="Support Engineer Demo") 
 
@app.get("/") 
def root(): 
    return {"service": "jenkins-demo-api"} 
 
@app.get("/health") 
def health(): 
    return {"status": "error"}