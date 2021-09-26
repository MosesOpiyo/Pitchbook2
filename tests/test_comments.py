import unittest
from app.models import Pitch, Comment,User
from app import db

class TestPitch(unittest.TestCase):
    '''
    A test case that tests the behaviours of the Pitch model
    '''

    def setUp(self):
        '''
        Method that will run before each test is ran
        '''
        self.new_pitch = Pitch(pitch_content = "pitch-1", pitch_category = 'category-1')
        self.new_comment = Comment(comment_content = "commment-1", pitch=self.new_pitch)


    def tearDown(self):
        db.session.delete(self)
        User.query.commit()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment, Comment, "comment-1")
        self.assertEquals(self.new_comment.pitch, self.new_pitch, "pitch-1")
