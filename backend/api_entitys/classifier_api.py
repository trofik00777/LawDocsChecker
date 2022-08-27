import os
import io

from loguru import logger
from fastapi import Depends, FastAPI, HTTPException, status, File, UploadFile, Form
from fastapi.security import HTTPBearer
import docx

from .api_models import ResponseModel
from ml.model_manager import DocManager
from ml.models import BaseModel

DocApi = FastAPI()
token_auth_scheme = HTTPBearer()
manager = DocManager()
model = BaseModel()


@DocApi.post("/post_file")
async def process_the_document(item: UploadFile = File(...),
                               token: str = Depends(token_auth_scheme)
                               ) -> ResponseModel:
    check_authorization(token)

    try:
        contents = await item.read()
        doc = docx.Document(io.BytesIO(contents))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
            detail="File is invalid",
        )
    finally:
        await item.close()

    logger.info('Parsing file')
    result_parsing = manager.parsing_with_brackets(doc)
    # logger.debug(f'{"".join(result_parsing)}')
    info = ResponseModel()
    info.parts = result_parsing

    answer = {"classes": []}
    # print(info.parts)

    for text, flag in info.parts:
        answer["classes"].append({"text": text, "label": model(text) + 1 if flag else -1})

    print(answer)

    return info


def check_authorization(token: str) -> None:
    if token.credentials != os.getenv('AUTHORIZATION_TOKEN'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
