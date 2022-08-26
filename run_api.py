import os

from backend.api_entitys import DocApi

import uvicorn

if __name__ == "__main__":
    uvicorn.run(DocApi, host=os.getenv('SERVER_IP'), port=int(os.getenv('API_PORT')))
