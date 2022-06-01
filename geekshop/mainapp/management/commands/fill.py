import json

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import Category, Product

from authapp.models import ShopUser


class Command(BaseCommand):

    def _load_data_from_file(self, file_name):
        with open(f'{settings.BASE_DIR}/mainapp/json/{file_name}.json') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):
        Category.objects.all().delete()

        categories_list = self._load_data_from_file('categories')

        categories_batch = []
        for cat in categories_list:
            categories_batch.append(
                Category(
                    name=cat.get('name'),
                    description=cat.get('description')
                )
            )

        Category.objects.bulk_create(categories_batch)

        Product.objects.all().delete()

        products_list = self._load_data_from_file('products')

        for prod in products_list:
            _cat = Category.objects.filter(name=prod.get('category')).first()
            prod['category'] = _cat

            Product.objects.create(**prod)

        shop_user = ShopUser.objects.create_superuser(username='django', password='geekbrains', age=32)
        # shop_user.set_password('geekbrains')
        # shop_user.save()