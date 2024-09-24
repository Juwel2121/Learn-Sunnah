from django.shortcuts import render
from django.core.files.storage import default_storage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from .models import Book, BookCategory, Review, Rating, UserProfile, STATUS_PUBLISHED, Rank, Question, QuestionCategory, Comment, Reply, QUESTION_ANSWERED, QUESTION_TYPE_PUBLIC
from .serializers import BookSerializer, BookCategorySerializer, ReviewSerializer, RatingSerializer, UserProfileSerializer, QuestionCategorySerializer, QuestionSerializer, RankSerializer, CommentSerializer, ReplySerializer
from .permissions import IsOwnerOrAdmin, IsOwner, BookIsOwner, QuestionIsOwner
from .admin import GROUP_MODERATOR

UNSAFE_METHODS = ('PATCH', 'PUT', 'DELETE')

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.prefetch_related('reviews').prefetch_related('ratings').all().filter(book_status=STATUS_PUBLISHED).order_by('-created_at')
    serializer_class = BookSerializer

    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [BookIsOwner()]
        

    @action(detail=False, methods=['get'], permission_classes=[BookIsOwner])
    def my_books(self, request):
        books = Book.objects.filter(added_by=request.user.id)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.cover_photo:
            file_path = instance.cover_photo.path
            if default_storage.exists(file_path):
                default_storage.delete(file_path)
        
        if instance.pdf:
            file_path = instance.pdf.path
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [IsOwner()]

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk']).order_by('-date_time')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        context.update({'book_id': self.kwargs['book_pk']})
        return context
    

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(book_id=self.kwargs['book_pk']).order_by('-date_time')
    
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in UNSAFE_METHODS:
            return [IsOwner()]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        context.update({'book_id': self.kwargs['book_pk']})
        return context
    

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer 
    
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [IsOwner()]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.profile_picture:
            file_path = instance.profile_picture.path
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['GET', 'PATCH', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (profile, created) = UserProfile.objects.get_or_create(user_id=request.user.id)

        if request.method in permissions.SAFE_METHODS:
            serializer = UserProfileSerializer(profile)
        else:
            serializer = UserProfileSerializer(profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data)
    

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().filter(question_type=QUESTION_TYPE_PUBLIC).filter(question_status=QUESTION_ANSWERED).order_by('-created_at')
    serializer_class = QuestionSerializer

    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [QuestionIsOwner()]
    

    @action(detail=False, methods=['get'], permission_classes=[QuestionIsOwner])
    def my_questions(self, request):
        questions = Question.objects.filter(author_id=request.user.id)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
        

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.answer_photo:
            file_path = instance.answer_photo.path
            if default_storage.exists(file_path):
                default_storage.delete(file_path)
        
        if instance.answer_video:
            file_path = instance.answer_video.path
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

        return super().destroy(request, *args, **kwargs)


class QuestionCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuestionCategory.objects.all()
    serializer_class = QuestionCategorySerializer

    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class RankViewSet(viewsets.ModelViewSet):
    serializer_class = RankSerializer
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [IsOwner()]

    def get_queryset(self):
        return Rank.objects.filter(question_id=self.kwargs['question_pk']).order_by('value')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        context.update({'question_id': self.kwargs['question_pk']})
        return context


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [QuestionIsOwner()]

    def get_queryset(self):
        return Comment.objects.filter(question_id=self.kwargs['question_pk']).order_by('-created_at')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        context.update({'question_id': self.kwargs['question_pk']})
        return context


class ReplyViewSet(viewsets.ModelViewSet):
    serializer_class = ReplySerializer

    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            return [AllowAny()]
        elif method == 'POST':
            return [IsAuthenticated()]
        elif method in ('PATCH', 'PUT', 'DELETE'):
            return [QuestionIsOwner()]

    def get_queryset(self):
        return Reply.objects.filter(comment_id=self.kwargs['comment_pk']).order_by('-created_at')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        context.update({'comment_id': self.kwargs['comment_pk']})
        return context