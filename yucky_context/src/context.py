class ContextManager:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        return None


class Context2():
    def write(self, num):
        print('writing', num)


class ContextManager2(ContextManager):
    def __enter__(self):
        return Context2()


class Context1():
    def open(self):
        return ContextManager2()


class ContextManager1(ContextManager):
    def __enter__(self):
        return Context1()


