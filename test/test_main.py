from yucky_context.src import main, open_context, write_context
from unittest.mock import MagicMock, Mock, patch

def get_mock_context_manager(context) -> Mock:
    """
    simple mock context manager
    """
    mock = Mock(spec_set=['__enter__', '__exit__'])
    mock.__exit__ = Mock()
    mock.__enter__ = Mock(return_value=context)
    return mock


@patch('yucky_context.src.open_context')
@patch('yucky_context.src.ContextManager1', new_callable=Mock)
def test_main(
    cm: Mock,
    open_context: MagicMock,
):
    context_1 = Mock()
    cm.return_value = get_mock_context_manager(context_1)
    main()
    open_context.assert_called_with(context_1)


@patch('yucky_context.src.write_context')
def test_open_context(
    write_context: MagicMock,
):
    context_2 = Mock()
    context = Mock(spec_set=['open'])
    context.open.return_value = get_mock_context_manager(context_2)
    open_context(context)
    write_context.assert_called_with(context_2)


def test_write_context():
    context = Mock(spec_set=['write'])
    write_context(context)
    context.write.assert_called_with(1234)

