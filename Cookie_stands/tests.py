from django.test import TestCase
from .models import Cookie_stand
# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class Cookie_standTest(APITestCase):
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



        test_Cookie_stand = Cookie_stand.objects.create(
            location="amman",
            owner=testuser1,
            description="delicious treats for Cookie_standing",
            hourly_sales=50,
            minimum_customers_per_hour=10,
            maximum_customers_per_hour=30,
            average_cookies_per_sale=2,
        )
        test_Cookie_stand.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")


    def test_Cookie_stands_model(self):
        Cookie_stand = Cookie_stand.objects.get(id=1)
        actual_owner = str(Cookie_stand.owner)
        actual_location = str(Cookie_stand.location)
        actual_hourly_sales = str(Cookie_stand.hourly_sales)
        actual_minimum_customers_per_hour = str(Cookie_stand.minimum_customers_per_hour)
        actual_maximum_customers_per_hour = str(Cookie_stand.maximum_customers_per_hour)
        actual_average_cookies_per_sale = str(Cookie_stand.average_cookies_per_sale)

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



