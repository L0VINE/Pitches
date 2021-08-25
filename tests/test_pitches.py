import unittest
from app.models import User,Comments, Pitches


class PitchesModelTest(unittest.TestCase):


    def test_save_pitch(self):
        self.assertTrue(len(Pitches.query.all())>0)