import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from initializer import IncludeAPIRouter
from dsc_labs.libs.logger import DSCLabsLogger
from dsc_labs.common import read_yaml

dsc_labs_logger = DSCLabsLogger()
logger = dsc_labs_logger.get_logger()
config = read_yaml('config/default.yaml')
api_config = config.get('api')


def get_application():
    # _app = FastAPI(title=api_config.get('name'),
    #                description=api_config.get('description'),
    #                version=api_config.get('version'),
    #                debug=api_config.get('debug_mode'))
    _app = FastAPI()
    _app.include_router(IncludeAPIRouter())
    _app.add_middleware(
        CORSMiddleware,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return _app


app = get_application()

@app.get("/")
async def home():
    return {"message": "OKE"}

@app.on_event("shutdown")
async def app_shutdown():
    # on app shutdown do something probably close some connections or trigger some event
    logger.info('event={} message="{}"'.format('app-shutdown', 'All connections are closed.'))


if __name__ == '__main__':
    uvicorn.run("main:app",
                host=api_config.get('host'),
                port=api_config.get('port'),
                reload=True)
