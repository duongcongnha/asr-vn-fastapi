class IncludeAPIRouter(object):
    def __new__(cls):
        from handlers.health_check import router as router_health_check
        from handlers.ASR import router as ASR
        from fastapi.routing import APIRouter
        router = APIRouter()
        router.include_router(router_health_check, tags=['Health Check'])
        router.include_router(ASR, prefix='/api/v1', tags=['asr service'])
        return router
