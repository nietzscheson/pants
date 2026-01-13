from dependency_injector.wiring import Provide, inject
from fastapi import Depends, FastAPI

from apps.app_1.src.container import MainContainer
from apps.app_1.src.services.hello import HelloService

app = FastAPI()


@app.get("/")
@inject
def read_root(
    hello_service: HelloService = Depends(Provide[MainContainer.hello_service]),
):
    return {"Hello": "World", "Message": hello_service.hello()}


@app.get("/health")
def health():
    return {"data": "OK"}


main_container = MainContainer()
app.container = main_container  # type: ignore
