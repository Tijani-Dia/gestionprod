from django.test import TestCase, Client
from django.urls import reverse

from suiviqualite.models import ParametresPhysicoChimiques
from suiviproduction.models import FormulaireProduction, FormulaireCasse
from home.models import User


class CasseFormTest(TestCase):
    """ Test module for Casse form. """

    def setUp(self):
        self.user = User.objects.create(username="User1", user_role='P', password="azerty50")
        new  = FormulaireCasse(
                        controleur = self.user,
                        casse_reelle = 20,
                        observation = "Some text"
                    )
        new.save()

    def test_fill_form(self):
        self.assertEqual(FormulaireCasse.objects.all().count(), 1)
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("suiviproduction:submit", kwargs={"parametre": "casses_recues"}),
            data = {
                'casses_recues' : '10'
            }
        )

        self.assertEqual(FormulaireCasse.objects.all().count(), 2)

    def test_updates_form(self):
        form = FormulaireCasse.objects.get(id=1)
        self.assertEqual(form.casse_reelle, 20)
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("suiviproduction:submit", kwargs={"parametre": "casse_reelle"}),
            data={
                'casse_reelle': '4',
                'element_id': "{}".format(form.id)
            })

        self.assertEqual(FormulaireCasse.objects.get(id=form.id).casse_reelle, 24)


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

    def test_fill_form(self):
        self.assertEqual(ParametresPhysicoChimiques.objects.all().count(), 1)
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("suiviqualite:submit", kwargs={"parametre": "physicochimique"}),
            data = {
                'chlore_libre' : 0,
                'chlore_total' : 0,
                'turbidite' : 0,
                'ph' : 7,
                'durete' : 15,
                'nitrate' : 0,
                'observation' : "Some text"
            }
        )

        self.assertEqual(ParametresPhysicoChimiques.objects.all().count(), 2)

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



class ProductionTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="User1", user_role='P', password="azerty50")

    def test_fill_form(self):
        self.assertEqual(FormulaireProduction.objects.all().count(), 0)
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("suiviproduction:submit", kwargs={"parametre": "production"}),
            data={
                'quart': 'Q1',
                'tickets' : 10,
                'sacs' : 32,
                'observation' : "Some text"
            })

        self.assertEqual(FormulaireProduction.objects.all().count(), 1)
