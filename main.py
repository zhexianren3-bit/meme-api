from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "表情包API"}
@app.get("/random")
def random_meme():
    return {"success": True, "meme": "https://example.com/meme.jpg"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
