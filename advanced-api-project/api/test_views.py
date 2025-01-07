from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from rest_framework.authtoken.models import Token

class BookApiTests(APITestCase):

    def setUp(self):
        # Create an author for the books
        self.author = Author.objects.create(name="John Doe")
        
        # Create a book
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)
        
        # Create a user and authenticate
        self.client.login(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_book(self):
        """Test creating a book."""
        url = reverse('book-list')  # URL for the Book list endpoint
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_update_book(self):
        """Test updating a book."""
        url = reverse('book-detail', args=[self.book.id])  # URL for the Book detail endpoint
        
        data = {'title': 'Updated Book Title', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse('book-detail', args=[self.book.id])  # URL for the Book detail endpoint
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_search_books(self):
        """Test search functionality."""
        url = reverse('book-list')  # URL for the Book list endpoint
        
        # Test searching by title
        response = self.client.get(url, {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books(self):
        """Test filtering by author."""
        url = reverse('book-list')  # URL for the Book list endpoint
        
        response = self.client.get(url, {'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering by title."""
        url = reverse('book-list')  # URL for the Book list endpoint
        
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['title'] < response.data[1]['title'])
