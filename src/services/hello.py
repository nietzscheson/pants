class HelloService:
    def __init__(self, hello: str) -> None:
        self.hello = hello
        
    def __call__(self) -> str:
        return self.hello