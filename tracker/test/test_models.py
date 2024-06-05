import pytest
from tracker.models import User, Transaction, Category


@pytest.mark.django_db
def test_qu_get_income_method(transaction):
    income = Transaction.objects.get_income()
    assert income.count() > 0
    assert all(
            [
                    transaction.type == 'income' for transaction in income
            ]
    )
    
    
@pytest.mark.django_db
def test_qu_get_expenses_method(transaction):
    qs = Transaction.objects.get_expenses()
    assert qs.count() > 0
    assert all(
            [
                    transaction.type == 'expense' for transaction in qs
            ]
    )
@pytest.mark.django_db
def test_qu_get_total_expenses_method(transaction):
    qs = Transaction.objects.get_total_expanses()
    assert qs == sum(t.amount for t in Transaction.objects.get_expenses() if t.type =='expense')
     

    
@pytest.mark.django_db
def test_qu_get_total_incomes_method(transaction):
    qs = Transaction.objects.get_total_incomes()
    assert qs == sum(t.amount for t in Transaction.objects.get_income() if t.type =='income')
     

    