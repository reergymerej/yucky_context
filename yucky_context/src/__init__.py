from yucky_context.src.context import ContextManager1


def write_context(context):
    context.write(1234)


def open_context(context):
    with context.open() as opened_context:
        write_context(opened_context)


def main():
    with ContextManager1() as context:
        open_context(context)
