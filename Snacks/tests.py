from django.test import TestCase
from .models import Snack
# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class SnackTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save()



        test_snack = Snack.objects.create(
            location="amman",
            owner=testuser1,
            description="delicious treats for snacking",
            hourly_sales=50,
            minimum_customers_per_hour=10,
            maximum_customers_per_hour=30,
            average_cookies_per_sale=2,
        )
        test_snack.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")


    def test_snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_owner = str(snack.owner)
        actual_location = str(snack.location)
        actual_hourly_sales = str(snack.hourly_sales)
        actual_minimum_customers_per_hour = str(snack.minimum_customers_per_hour)
        actual_maximum_customers_per_hour = str(snack.maximum_customers_per_hour)
        actual_average_cookies_per_sale = str(snack.average_cookies_per_sale)

        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_hourly_sales, '50')
        self.assertEqual(actual_location, "amman")
        self.assertEqual(
            actual_minimum_customers_per_hour, '10'
        )
        self.assertEqual(
            actual_maximum_customers_per_hour, '30'
        )
        self.assertEqual(
            actual_average_cookies_per_sale, '2.0'
        )



