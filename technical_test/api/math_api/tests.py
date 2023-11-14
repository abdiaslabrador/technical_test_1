from rest_framework import status
from rest_framework.test import APITestCase


class MathTest(APITestCase):
    def test_get_math_mcm(self):
        """
        comprueba el endpoint para obtener el mcm de una lista dada pasada por parámetros
        """
        numbers = "2, 3"
        url = f"/math/?numbers={numbers}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(6, response.data["result"])

    def test_get_math_plus_number(self):
        """
        comprueba el endpoint para sumarle 1 al número dado
        """
        number = "4"
        url = f"/math/?number={number}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(5, response.data["result"])
