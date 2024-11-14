from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Community, Membership, Post, Like, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar', 'read_day', 'post_reads', 'comment_reads', 'followers']

class CommunitySerializer(serializers.ModelSerializer):
    admin = UserSerializer()

    class Meta:
        model = Community
        fields = ['id', 'name', 'description', 'created_at', 'admin', 'post_reads', 'comment_reads', 'rules']

class MembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    community = CommunitySerializer()

    class Meta:
        model = Membership
        fields = ['id', 'user', 'community', 'joined_at']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'description', 'post_reads', 'created', 'discussions']

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'parent', 'comment', 'comment_reads', 'created_at']

    def create(self, validated_data):
        parent = validated_data.get('parent', None)
        if parent:
            validated_data['parent'] = parent
        return super().create(validated_data)
