from yucky_context.src.context import ContextManager1


def write_context(context):
    context.write(1234)


def open_context(writer, context):
    with context.open() as opened_context:
        writer(opened_context)


def main(opener):
    with ContextManager1() as context:
        opener(context)
