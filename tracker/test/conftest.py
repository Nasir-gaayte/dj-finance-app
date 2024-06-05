import pytest
from tracker.factory import TransactionFactory


@pytest.fixture
def transaction():
    return TransactionFactory.create_batch(20)