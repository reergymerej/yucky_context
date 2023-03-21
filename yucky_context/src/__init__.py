class ContextManager:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        return None


class Context2():
    def write(self, num):
        print('writing', num)
        return None


class ContextManager2(ContextManager):
    def __enter__(self):
        return Context2()


class Context1():
    def open(self):
        return ContextManager2()


class ContextManager1(ContextManager):
    def __enter__(self):
        return Context1()


def main():
    with ContextManager1() as context_1:
        with context_1.open() as context_2:
            context_2.write(1234)
