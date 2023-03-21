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


def write_context(context):
    context.write(1234)


def open_context(context):
        with context.open() as opened_context:
            write_context(opened_context)

def main():
    with ContextManager1() as context:
        open_context(context)
