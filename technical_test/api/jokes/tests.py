from rest_framework import status
from rest_framework.test import APITransactionTestCase
from api.jokes.models import JokeModel


class JokesTest(APITransactionTestCase):
    reset_sequences = True

    def test_get_joke(self):
        """
        comprueba el endpoint para obtener un chiste aleatorio
        """
        url = "/jokes/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = "/jokes/Chuck"
        response = self.client.get(url)
        self.assertTrue(response.status_code == 200 or response.status_code == 301)

        url = "/jokes/Dad"
        response = self.client.get(url)
        self.assertTrue(response.status_code == 200 or response.status_code == 301)

    def test_post_joke(self):
        """
        comprueba el endpoint para crear un chiste, y si fue creado
        """

        joke = "this is a joke"
        url = f"/jokes/?joke={joke}"

        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, JokeModel.objects.all().count())

    def test_update_joke(self):
        """
        comprueba el endpoint para actualizar un chiste
        """

        joke = JokeModel.objects.create(joke="this is the first joke")
        joke.save()
        joke = JokeModel.objects.create(joke="this is the second joke")
        joke.save()

        number = 2
        joke_data = "the joke updated"
        url = f"/jokes/?number={number}&joke={joke_data}"

        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, JokeModel.objects.filter(joke="the joke updated").count())

    def test_delete_joke(self):
        """
        comprueba el endpoint para eliminar un chiste
        """

        joke = JokeModel.objects.create(joke="this is the first joke")
        joke.save()
        joke = JokeModel.objects.create(joke="this is the second joke")
        joke.save()

        number = 1
        url = f"/jokes/?number={number}"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        number = 2
        url = f"/jokes/?number={number}"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, JokeModel.objects.all().count())
