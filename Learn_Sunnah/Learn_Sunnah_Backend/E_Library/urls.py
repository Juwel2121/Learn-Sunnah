from django.urls import path, include 
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'books_categorys', views.BookCategoryViewSet)
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'questions_categorys', views.QuestionCategoryViewSet)
# router.register(r'reviews', views.ReviewViewSet)

book_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_router.register('reviews', views.ReviewViewSet, basename='book-reviews')
book_router.register('ratings', views.RatingViewSet, basename='book-ratings')

question_router = routers.NestedDefaultRouter(router, 'questions', lookup='question')
question_router.register('ranks', views.RankViewSet, basename='question-ranks')
question_router.register('comments', views.CommentViewSet, basename='question-comments')

comment_router = routers.NestedDefaultRouter(question_router, 'comments', lookup='comment')
comment_router.register('replies', views.ReplyViewSet, basename='comment-reply')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
    path('', include(question_router.urls)),
    path('', include(comment_router.urls))
]
