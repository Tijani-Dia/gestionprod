from django.test import TestCase, Client
from django.urls import reverse

from suiviqualite.models import ParametresPhysicoChimiques
from home.models import User


class UpdateFormTest(TestCase):
    """ Test module for updating a form. """

    def setUp(self):
        self.user = User.objects.create(username="User1", user_role='Q', password="azerty50")
        self.form  = ParametresPhysicoChimiques(
                        controleur = self.user,
                        chlore_libre = 0,
                        chlore_total = 0,
                        turbidite = 0,
                        ph = 7,
                        durete = 15,
                        nitrate = 0,
                        observation = "Some text"
                    )
        self.form.save()

    def test_updates_form(self):
        self.assertEqual(self.form.chlore_libre, 0)
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("suiviqualite:submit", kwargs={"parametre": "physicochimique"}),
            data={
                'chlore_libre': 1,
                'chlore_total' : 1,
                'turbidite' : 0,
                'ph' : 7,
                'durete' : 15,
                'nitrate' : 0,
                'observation' : "Some text",
                'element_id': "{}".format(self.form.id)
            })

        self.assertEqual(ParametresPhysicoChimiques.objects.get(id=self.form.id).chlore_libre, 1)