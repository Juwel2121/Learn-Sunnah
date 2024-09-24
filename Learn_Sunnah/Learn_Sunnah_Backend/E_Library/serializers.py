from rest_framework import serializers
from .models import (Book, BookCategory, Review, User, UserProfile, Rating, STATUS_CHOICES, Question, QuestionCategory, Rank, Comment, Reply, QUESTION_CHOICES, QUESTION_TYPE_CHOICES)
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
        

class RatingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    book_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Rating
        fields = ['id', 'user_id', 'book_id', 'rating', 'date_time']
    
    def create(self, validated_data):
        book_id = self.context['book_id']
        user_id = self.context['request'].user.id
        return Rating.objects.create(book_id=book_id, user_id=user_id, **validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    book_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'book_id', 'review', 'date_time']
    
    def create(self, validated_data):
        book_id = self.context['book_id']
        user_id = self.context['request'].user.id
        return Review.objects.create(book_id=book_id, user_id=user_id, **validated_data)


class BookCategorySerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = BookCategory
        fields = ['id', 'name', 'books']



class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    book_status = serializers.ChoiceField(choices=STATUS_CHOICES, read_only=True)
    views = serializers.IntegerField(read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField(method_name='get_rating')
    added_by = UserSerializer(read_only=True)
    category = BookCategorySerializer()

    def get_rating(self, book):
        qs = Rating.objects.all().filter(book_id=book.id)
        total_rating = 0
        count_user = 0
        for rating in qs:
            total_rating += rating.rating
            count_user += 1

        if count_user == 0:
            return 0.0
        return total_rating / count_user
        
    def create(self, validated_data):
        added_by = self.context['request'].user
        category_data = validated_data.pop('category', None)
        category_instance, created = BookCategory.objects.get_or_create(**category_data)
        return Book.objects.create(added_by=added_by, category=category_instance, **validated_data)
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'added_by', 'description', 'isbn', 'views', 'publisher', 'publish_date', 'language', 'page_number', 'cover_photo', 'pdf', 'book_status', 'ratings', 'rating', 'reviews', 'category']
        # fields = ('id', 'field1', 'field2')
        # exclude = ('field3',)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'user_id', 'profile_picture', 'phone', 'birth_date']


class QuestionCategorySerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = QuestionCategory
        fields = ['id', 'name', 'questions']


class RankSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Rank
        fields = '__all__'
    
    def create(self, validated_data):
        question_id = self.context['question_id']
        user_id = self.context['request'].user.id
        return Rank.objects.create(question_id=question_id, user_id=user_id, **validated_data)


class ReplySerializer(serializers.ModelSerializer):
    comment = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Reply
        fields = '__all__'
    
    def create(self, validated_data):
        comment_id = self.context['comment_id']
        author_id = self.context['request'].user.id
        return Reply.objects.create(comment_id=comment_id, author_id=author_id, **validated_data)

        

class CommentSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = ReplySerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'author', 'question', 'replies']
    
    def create(self, validated_data):
        question_id = self.context['question_id']
        author_id = self.context['request'].user.id
        return Comment.objects.create(question_id=question_id, author_id=author_id, **validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    question_status = serializers.ChoiceField(choices=QUESTION_CHOICES, read_only=True)
    views = serializers.IntegerField(read_only=True)
    ranks = RankSerializer(many=True, read_only=True)
    rank = serializers.SerializerMethodField(method_name='get_rank')
    author = UserSerializer(read_only=True)
    category = QuestionCategorySerializer()

    answer = serializers.CharField(read_only=True)
    answer_photo = serializers.ImageField(read_only=True)
    answer_video = serializers.FileField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def get_rank(self, question):
        qs = Rank.objects.all().filter(question_id=question.id)
        total_rank = 0
        for rank in qs:
            total_rank += rank.value

        return total_rank
        
    def create(self, validated_data):
        author = self.context['request'].user
        
        category_data = validated_data.pop('category', None)
        category_instance, created = QuestionCategory.objects.get_or_create(**category_data)
        return Question.objects.create(author=author, category=category_instance, **validated_data)
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'author', 'views', 'created_at', 'language', 'answer', 'answer_photo', 'answer_video', 'question_status', 'question_type', 'ranks', 'rank', 'comments', 'category']

