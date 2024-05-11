from django.urls import path
from .views import BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list_view'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail_view'),
    path('add/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete')

]
