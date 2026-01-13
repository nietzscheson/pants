class HelloService:
    def __init__(self, hello: str) -> None:
        self._hello = hello

    def hello(self) -> str:
        return self._hello
