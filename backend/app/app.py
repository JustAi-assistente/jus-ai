from fastapi import FastAPI
import uuid
import uvicorn
from openai import OpenAI
import json
from fastapi.middleware.cors import CORSMiddleware
from app.core.middlewares.logging_middleware import LoggingMiddleware
from app.core.monitoring import logging_config
from app.routes.v1 import just_ai_router

###############################################################################
#   Application object                                                        #
###############################################################################

app = FastAPI(
    title="Just Ai",
    description="Chatbot destinado a fornecer orientações jurídicas para problemas específicos.",
    version="1.0",
    docs_url='/just-ai/docs',
    openapi_url='/just-ai/openapi.json',
    redoc_url=None
)

###############################################################################
#   Logging configuration                                                     #
###############################################################################

logging_config.configure_logging(
    level='DEBUG', service='just-ai', instance=str(uuid.uuid4()))

###############################################################################
#   Middlewares configuration                                                 #
###############################################################################

# app.add_middleware(LoggingMiddleware)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

###############################################################################
#   Routers configuration                                                     #
###############################################################################

app.include_router(just_ai_router.router, prefix='/just-ai')

@app.get("/just-ai/health")
def main():
    msg = "Api is up and running!!"
    return {'message': json.dumps(msg)}

###############################################################################
#   Run the self contained application                                        #
###############################################################################

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)