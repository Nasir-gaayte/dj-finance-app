from datetime import datetime
import factory
from tracker.models import User , Transaction, Category


class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = User
                django_get_or_create = ("username",)
        
        first_name = factory.Faker('first_name')
        last_name = factory.Faker('last_name')        
        username = factory.Sequence(lambda n: 'user%d' % n)
class CategoryFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Category
                django_get_or_create = ("name",)
        name = factory.Iterator(['Food', 'Bills', 'Housing', 'Salary', 'Social'])
class TransactionFactory(factory.django.DjangoModelFactory):
        class Meta:
                model = Transaction
                django_get_or_create = ("user", "category", "type", "amount", "date")
        user = factory.SubFactory(UserFactory)
        category = factory.SubFactory(CategoryFactory)
        type = factory.Iterator(['income', 'expense'])
        amount = factory.Faker('pydecimal', left_digits=10, right_digits=2, positive=True, min_value=1000, max_value=100000)
        date = factory.Faker('date_between', start_date='-1y', end_date='today')
        
        # date = factory.Faker('date_between', start_date=datetime(year=2022,month=1,day=1).date(), end_date=datetime().now().date())
        
        # typy = factory.Faker(
        #         'random_element',
        #         elements=[
        #                 x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES
        #         ]
        # )