from django.test import TestCase
from .models import Profile,Reviews,Rates,Project_Post

class ProfileTestClass(TestCase):

    def setup(self):
        self.profile = Profile(user = 'dan',profile_pic = 'd.jpg',bio ='my bio',updated_on = '12/7/1019')
        self.profile.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile_by_user(self):
        profile = Profile.get_profile_by_name(dan)
        self.assertTrue(profile == self.profile)

class ReviewTestClass(TestCase):
    def setUp(self):
        self.review = Review(review = 'i am a comment',posted_by = 'dan',posted_on = '12/23/2017',Project_id='1')
        self.comment.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.review,Reviews))
    # def test_get_all_(self):
    #     self.comment.save()
    #     comments = Comment.get_all_comments()
    #     self.assertTrue(len(comments)==1)
    def test_get_review_by_project_id(1):
        self.review.save()
        review = Reviews.get_review_by_project_id(1)
        self.assertTrue(len(review)==1)
class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project_Post(project_url = "http://dan.com",description="happy now",img_project = 's.jpg',posted_on= "4/12/2019", posted_by = 'dan')
        self.project.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project_Post))

    def test_get_all_Projects():
        self.project.save()
        projects = Project_Post.get_all_images()
        self.assertTrue(len(projects)==1)
    def test_get_project_by_id(id):
        self.project.save()
        image = Project_Post.get_project_by_id(id)
        self.assertTrue(project.description == 'i am codding now')
# Create your tests here.
