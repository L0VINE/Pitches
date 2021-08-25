import unittest
from app.models import User,Comments, Pitches


class CommentsModelTest(unittest.TestCase):

    def setUp(self):
       self.new_comment = Comments(id=1, user_id = 2, comment = 'cross buns',pitches_id = '5',date_posted='2018-09-09')

    def test_comment_variables(self):

       # self.assertEquals(self.new_comment.id, 2)
       self.assertEquals(self.new_comment.comment,'cross buns')
       self.assertEquals(self.new_comment.date_posted,'2018-09-09')
       self.assertEquals(self.new_comment.user_id, 2)
       # self.assertEquals(self.new_comment.pitches_id, 4)

    def test_save_comment(self):

        self.assertTrue(len(Comments.query.all())>0)