from dependency_injector import containers, providers

from apps.app_2.src.services.hello import HelloService
from apps.app_2.src.settings import Settings


class MainContainer(containers.DeclarativeContainer):
    settings = providers.Configuration(pydantic_settings=[Settings()])
    wiring_config = containers.WiringConfiguration(
        modules=["apps.app_2.src.main"],
    )
    hello_service = providers.Factory(
        HelloService,
        hello=settings.hello,
    )
