from yucky_context.src import main
from unittest.mock import Mock, patch

def get_mock_context_manager(context) -> Mock:
    """
    simple mock context manager
    """
    mock = Mock(spec_set=['__enter__', '__exit__'])
    mock.__exit__ = Mock()
    mock.__enter__ = Mock(return_value=context)
    return mock


@patch(
    'yucky_context.src.ContextManager1',
    # no magic
    new_callable=Mock,
)
def test_main(
    ContextManagerCallable: Mock,
):
    context_2 = Mock(spec_set=['write'])
    ContextManager2 = get_mock_context_manager(context_2)
    context_1 = Mock(spec_set=['open'])
    context_1.open.return_value = ContextManager2
    ContextManager1 = get_mock_context_manager(context_1)
    ContextManagerCallable.return_value = ContextManager1

    main()
    context_2.write.assert_called_with(1234)
