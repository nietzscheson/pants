from dependency_injector import containers, providers
from src.settings import Settings
from src.services.hello import HelloService

class MainContainer(containers.DeclarativeContainer):

    settings = providers.Configuration(pydantic_settings=[Settings()])
    
    hello_service = providers.Factory(
        HelloService,
        hello="hello"
    )