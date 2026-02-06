from fastapi import FastAPI, Depends
import httpx, time, asyncio
from app.schemas import ApiResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

async def get_http_client():
    async with httpx.AsyncClient(timeout=10.0) as client:
        yield client

async def fetch_api(client: httpx.AsyncClient, url: str) -> ApiResponse:
    try:
        start_time = time.perf_counter()
        response = await client.get(url)
        end_time = time.perf_counter()
        response.raise_for_status()
        return ApiResponse(
            ok= True,
            time_taken= round(end_time - start_time, 3),
            data= response.json()
        )
    except httpx.TimeoutException:
        return ApiResponse(
            ok= False,
            error= "Request timed out"
        )
    except httpx.HTTPStatusError as e:
        return ApiResponse(
            ok= False,
            error= f"HTTP Error: {e.response.status_code}"
        )
    except httpx.RequestError as e:
        return ApiResponse(
            ok= False,
            error= f"Request failed: {str(e)}"
        )
    except Exception as e:
        return ApiResponse(
            ok= False,
            error= f"Unexpected error: {str(e)}"
        )
    
async def fetch_cat_fact(client: httpx.AsyncClient) -> ApiResponse:
    return await fetch_api(client, "https://catfact.ninja/fact")

@app.get("/cat-fact", response_model = ApiResponse)
async def get_cat_fact(client: httpx.AsyncClient = Depends(get_http_client)):
    return await fetch_cat_fact(client)

async def fetch_advice(client: httpx.AsyncClient) -> ApiResponse:
    return await fetch_api(client, "https://api.adviceslip.com/advice")
    
@app.get("/advice", response_model = ApiResponse)
async def get_advice(client: httpx.AsyncClient = Depends(get_http_client)):
    return await fetch_advice(client)

async def fetch_joke(client: httpx.AsyncClient) -> ApiResponse:
    return await fetch_api(client, "https://official-joke-api.appspot.com/random_joke")
    
@app.get("/joke", response_model = ApiResponse)
async def get_joke(client: httpx.AsyncClient = Depends(get_http_client)):
    return await fetch_joke(client)

@app.get("/home")
async def home(client: httpx.AsyncClient = Depends(get_http_client)):
    start_time = time.perf_counter()
    results = await asyncio.gather(fetch_cat_fact(client), fetch_advice(client), fetch_joke(client))
    end_time = time.perf_counter()
    response = {
        "cat_fact": results[0],
        "advice": results[1],
        "joke": results[2],
        "total_time": round(end_time - start_time, 3)
    }
    return response
