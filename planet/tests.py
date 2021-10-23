from django.test import TestCase

class PlanetViewTest(TestCase):
    def test_index_template(self):
        response = self.client.get("/planet/")
        self.assertTemplateUsed(response, "planet/index.html")
