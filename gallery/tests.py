from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime


class GalleryViewTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image = Image.objects.create(
            title='Test Image',
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=datetime.date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'gallery.html')

    def test_gallery_view_content(self):
        response = self.client.get(reverse('main'))
        self.assertContains(response, 'Test Category')
        self.assertContains(response, 'Test Image')


class ImageDetailViewTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.image = Image.objects.create(
            title='Test Image',
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=datetime.date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_image_detail_view_status_code(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)

    def test_image_detail_view_template(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertTemplateUsed(response, 'image_detail.html')

    def test_image_detail_view_content(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertContains(response, 'Test Image')
