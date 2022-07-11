from rest_framework.test import APIClient, APITestCase


class TestPlaylists(APITestCase):
    fixtures = ['/playlists/tests/fixtures.json']

    def setUp(self) -> None:
        self.client = APIClient()
        self.root_endpoint_path = '/playlists/'

    def test_get_request(self):
        response = self.client.get(self.root_endpoint_path)
        self.assertEqual(response.status_code, 200)
